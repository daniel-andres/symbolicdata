"""
This is the template for the computation problem of computing a Groebner basis of an ideal
generated by a finite set of polynomials with integer coefficients (commutative). It creates
code for the computer algebra system Singular.

.. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
"""

#--------------------------------------------------
#---------------The template-----------------------
#--------------------------------------------------

def generateCode(vars, basis):
    """
    The main function generating the Singular code for the computation of
    the Groebner basis given the input variables.

    :param         vars: A list of variables used in the IntPS-System
    :type          vars: list
    :param        basis: The polynomials forming a basis of the IntPS-System. This input will not be checked whether
                         there are polynomials using variables not in the list of variables.
    :type         basis: list
    """
    """
    gbasis({x*y+z, ...},{x,y,z});
    """
    result = "gbasis({%s},{%s});" % (",".join(basis), ",".join(vars))
    return result

#--------------------------------------------------
#----------------Help Functions--------------------
#--------------------------------------------------