"""
This is the template for extracting the solution for the computation problem of computing
a Groebner basis of an indeal in a free algebra over QQ from the output of the computer
algebra system Singular.

.. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
"""

import xml.dom.minidom as dom
import re

#--------------------------------------------------
#---------------The template-----------------------
#--------------------------------------------------

def extractSolution(outpString):
    """
    This function extracts the solution of a free algebra Groebner basis
    computation performed in Singular, using the executable code that was
    generated by the template in the same folder on a certain instance.

    If there is no solution given, or something is wrong with the given string,
    a ValueError is raised.

    :param outpString: The String that was returned by the Singular-execution
    :type  outpString: str
    :returns: XML-Representation of the solution.
    :rtype: str
    :raises: ValueError
    """
    solBeginStr = "=====Solution Begin====="
    solEndStr   = "=====Solution End====="
    solBeginPos = outpString.index(solBeginStr) + len(solBeginStr)
    solEndStrPos   = outpString.index(solEndStr)
    solStr = outpString[solBeginPos:solEndStrPos]
    if (solStr.strip()==""):
        raise ValueError("There is no solution to be found in the output-file")
    #From here on, we can assume that we are dealing with a valid string.
    result = solStr.split(',')
    result = map(lambda x: convertFromLetterplace(x.strip()),result)
    return result
    
    

#--------------------------------------------------
#----------------Help Functions--------------------
#--------------------------------------------------

def convertFromLetterplace(inpPoly):
    """
    This function converts a string representing a polynomial in Letterplace form
    into a polynomial without the position indicators. For example::

      2*x(1)*y(2) + z(1)

    will be converted into::

      2*x*y + z

    :param inpPoly: The polynomial in letterplace form
    :type  inpPoly: str
    """
    result = ""
    plusSplit = inpPoly.split("+")
    for p in plusSplit:
        minusSplit = p.split("-")
        for ms in minusSplit:
            monomials = ms.split("*")
            monomials = map(lambda x: re.sub(r"\([0-9]+\)","",x),monomials)
            result += ("*".join(monomials)) + "-"
        result = result[:-1]
        result += "+"
    result = result[:-1]
    return result
        
