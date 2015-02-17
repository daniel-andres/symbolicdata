import xml.dom.minidom as dom
from Proceedings import Proceedings
from ..Task import Task

class ProceedingsFromXMLBuilder(object):
    """
    This is a builder class that creates instance of the class Proceedings
    of a task given an XML string and a Task instance.

    .. seealso:: :mod:`Proceedings <sdeval.classes.results.Proceedings>`
    .. moduleauthor:: Albert Heinle <aheinle@uwaterloo.de>
    """

    def build(self, xmlRaw, task):
        """
        Returns an instance of Proceedings, given an xml-string and an instance of the associated task.
        The given string is assumed to have the following form::

          <proceedings>
            <timestamp>
              "The timestamp"
            </timestamp>
            <task>
              "the name of the executed task"
            </task>
            <running>
              <entry>
                <probleminstance>
                  "A problem instance"
                </probleminstance>
                <computeralgebrasystem>
                  "A computer algebra system"
                </computeralgebrasystem>
              </entry>
            </running>
            <waiting>
              "same as running"
            </waiting>
            <completed>
              "same as running"
            </completed>
            <error>
              "same as running"
            </error>
          </proceedings>

        An IOError is raised if the XML instance was not valid.
        
        :param    xmlRaw: The xml-representation of the proceedings.
        :type     xmlRaw: string
        :param    task: The task associated to the given proceedings instance.
        :type     task: Task
        :returns: An instance of the Proceedings class
        :rtype:   Proceedings
        """
        try:
            xmlTree = dom.parseString(xmlRaw)
        except:
            raise IOError("Could not parse the given string as XML-Instance")
        try:
            timeStamp = str((xmlTree.getElementsByTagName("timestamp")[0]).firstChild.data).strip()
        except:
            raise IOError("Given XML instance did not have a timestamp entry")
        result = Proceedings(task,timeStamp)
        try:
            completedCalculations = xmlTree.getElementsByTagName("completed")[0]
            erroneousCalculations   = xmlTree.getElementsByTagName("error")[0]
        except:
            raise IOError("Could not find entries for completed resp. erroneous computations")
        #First dealing with all the completed calculations
        tempEntry = completedCalculations.firstChild
        while (tempEntry != None and tempEntry.nodeType == dom.Node.TEXT_NODE):
            tempEntry = tempEntry.nextSibling
        while tempEntry != None:
            try:
                cas = str((tempEntry.getElementsByTagName("computeralgebrasystem")[0]).firstChild.data).strip()
                pi  = str((tempEntry.getElementsByTagName("probleminstance")[0]).firstChild.data).strip()
            except:
                raise IOError("The entries in the list of completed calculations are not valid")
            result.setRUNNING([pi,cas])
            result.setCOMPLETED([pi,cas])
            tempEntry = tempEntry.nextSibling
            while (tempEntry != None and tempEntry.nodeType == dom.Node.TEXT_NODE):
                tempEntry = tempEntry.nextSibling
        #Now dealing with the erroneous calculations
        tempEntry = erroneousCalculations.firstChild
        while (tempEntry != None and tempEntry.nodeType == dom.Node.TEXT_NODE):
            tempEntry = tempEntry.nextSibling
        while tempEntry != None:
            try:
                cas = str((tempEntry.getElementsByTagName("computeralgebrasystem")[0]).firstChild.data).strip()
                pi  = str((tempEntry.getElementsByTagName("probleminstance")[0]).firstChild.data).strip()
            except:
                raise IOError("The entries in the list of erroneous computations were not valid.")
            result.setRUNNING([pi,cas])
            result.setERROR([pi,cas])
            tempEntry = tempEntry.nextSibling
            while (tempEntry != None and tempEntry.nodeType == dom.Node.TEXT_NODE):
                tempEntry = tempEntry.nextSibling
        return result
