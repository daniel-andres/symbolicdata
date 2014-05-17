import unittest
import SDTable
import os
import XMLRessources

class TestSDTable(unittest.TestCase):
    """
    Tests for the class SDTable

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def setUp(self):
        """
        General Assumptions:
           - Tests run on top of Symbolic Data base, i.e. in the folder structure
             as given in the repository.
             Otherwise the user will be asked to either enter the path to the XMLResources folder
             or to skip the related tests (empty string entering).
        """
        self.xr = None
        try:
            tempPathToXMLRessources = str(os.path.realpath(os.path.dirname(__file__))).split(os.sep)[0:-3]
            self.xr = XMLRessources.XMLRessources(os.path.join(str(os.sep).join(tempPathToXMLRessources),"XMLResources"))
        except:
            tempPathToXMLRessources = raw_input("Path to XMLRessources not at the usual location. Please enter Path\
 to it or press Enter to skip tests related to the Symbolic Data source: ")
            if tempPathToXMLRessources != '':
                self.xr = XMLRessources.XMLRessources(os.path.join(str(os.sep).join(tempPathToXMLRessources),"XMLResources"))
        if self.xr ==None:
            print "WARNING: As the path to the XMLResources is not provided, some tests will be ignored"

    def testInitialization(self):
        """
        Tests the initialization routine of the SD-Table.
        The tests that are covered are the following:

        1) Call with None everywhere.
        2) Constructed via a full path to the SD-Table
           2.1) valid path
           2.2) invalid path
        3) Constructed via an XMLRessources instance and a table name
           3.1) non existing table name
           3.2) existing table name
        4) Correct name saved
        5) Empiric tests of entries.
        Note:
        - If there is no path to the XMLRessources provided in the setUp,
          some tests will be ignored.
        """
        #1)
        try:
            SDTable.SDTable()
            self.fail("Initializing SDTable with no arguments should raise an exception")
        except:
            pass
        #2.1)
        try:
            SDTable.SDTable(".")
        except:
            self.fail("Initializing SDTable with valid path fails.")
        #2.2)
        try:
            SDTable.SDTable(os.path.join(".","SillyNameThatWouldNeverAppearInOurProgram"))
            self.fail("Initializing SDTable with invalid path was possible")
        except:
            pass
        #3.1)
        if self.xr != None:
            try:
                SDTable.SDTable(None, (self.xr,"SillyTableNameWouldNeverEnterSData"))
                self.fail("Could initialize SDTable that is not existent")
            except:
                pass
        #3.2)
        if self.xr != None:
            try:
                SDTable.SDTable(None, (self.xr,"IntPS"))
            except:
                self.fail("There should be at least the table IntPS in the XMLResources")
        #4)
        if self.xr != None:
            sdt = SDTable.SDTable(None, (self.xr,"IntPS"))
            self.assertEqual(sdt.getName(), "IntPS")
            #5)
            tempList = sdt.listEntries()
            if "Amrhein" not in tempList or\
                "Becker-Niermann" not in tempList or\
                "Fee_1" not in tempList or\
                "FourBodyProblem" not in tempList or\
                "Wu-90" not in tempList:
                self.fail("Some expected entries were not to be found in IntPS.")


    def testLoadEntry(self):
        """
        This test makes sure that entries in the given table can be loaded.

        The tests in detail:
        1) We load an entry that does not exist.
        2) We load an entry that does exist (Amrhein)
           2.1) Check the XML-String for validity and correctness.
           2.2) With .xml ending and without
        Note:
        - If there is no path to the XMLRessources provided in the setUp,
          this test will be completely ignored.

        GENERAL ASSUMPTION:
        - In the XMLResources, there is a table called IntPS
        - Inside IntPS, there is an entry called 'Becker-Niermann'
        """
        #1)
        if self.xr != None:
            sdt = SDTable.SDTable(None, (self.xr,"IntPS"))
            try:
                sdt.loadEntry("SillyEntryWouldNeverBeInThereBooyah")
                self.fail("Could load an entry that clearly did not exist.")
            except:
                pass
            #2)
            try:
                sdt.loadEntry("Becker-Niermann")
            except:
                self.fail("Could not load existing entry (without .xml at the end of the argument)")
            try:
                sdt.loadEntry("Becker-Niermann.xml")
            except:
                self.fail("Could not load existing entry (with .xml at the end of the argument)")
            bn = sdt.loadEntry("Becker-Niermann.xml")
            expectedString = "<?xml version=\"1.0\"?>\n\
<INTPS createdAt=\"2010-05-11\" createdBy=\"graebe\">\n\
<!-- $Id: Becker-Niermann.xml,v 1.1 2010/05/14 09:05:07 graebe Exp $ -->\n\
  <vars>x,y,z</vars>\n\
  <basis>\n\
    <poly>x^2+x*y^2*z-2*x*y+y^4+y^2+z^2</poly>\n\
    <poly>-x^3*y^2+x*y^2*z+x*y*z^3-2*x*y+y^4</poly>\n\
    <poly>-2*x^2*y+x*y^4+y*z^4-3</poly>\n\
  </basis>\n\
  <Comment>\n\
    Contributed by Stefan Steidel (Uni KL)\n\
\n\
    cf. Decker, W.; Greuel, G.-M.; Pfister, G.: Primary Decomposition:\n\
    Algorithms and Comparisons. In: Algorithmic Algebra and Number Theory,\n\
    Springer, 187--220 (1998).\n\
  </Comment>\n\
</INTPS>"
            if bn.strip() != expectedString.strip():
                # print bn.strip()
                # print "-------"
                # print expectedString.strip()
                self.fail("Not the correct entry loaded")