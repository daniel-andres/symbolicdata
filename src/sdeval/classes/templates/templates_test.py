import unittest

class TestTemplates(unittest.TestCase):
    """
    Tests for the different templates to generate code for different Computer algebra systems.

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def test_FA_Q_DP_GAP(self):
        """
        This test checks the template FA_Q_DP for GAP.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.FA_Q_dp.GAP.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        uptoDeg = 10;
        expectedString = """LoadPackage("GBNP","0",false);
SetInfoLevel(InfoGBNP,1);
SetInfoLevel(InfoGBNPTime,1);
F := Rationals;
A := FreeAssociativeAlgebraWithOne(F,"x4","x3","x2","x1");
g :=GeneratorsOfAlgebraWithOne(A);
x4 := g[1];
x3 := g[2];
x2 := g[3];
x1 := g[4];
weights := [1,1,1,1];
KI_gp := [x1+x2,x3*x4-x2*x1,x1*x2*x3*x4];
KI_np :=GP2NPList(KI_gp);
GB :=SGrobnerTrunc(KI_np,10,weights);
GBNP.ConfigPrint("x4","x3","x2","x1");
PrintNPList(GB);
Length(GB);
quit;"""
        output = generateCode(vars,basis,uptoDeg)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_FA_Q_DP_Singular(self):
        """
        This test checks the template FA_Q_DP for Singular.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.FA_Q_dp.Singular.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        uptoDeg = 10;
        expectedString = """LIB "freegb.lib";
ring r = 0,(x1,x2,x3,x4),dp;
int d = 10;
def R = makeLetterplaceRing(d);
 setring(R);
ideal I = x1(1)+x2(1),
x3(1)*x4(2)-x2(1)*x1(2),
x1(1)*x2(2)*x3(3)*x4(4);
option(prot);
option(redTail);
option(redSB);
ideal J = letplaceGBasis(I);
print (J, "%s");$"""
        output = generateCode(vars,basis,uptoDeg)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_FA_Q_DP_Magma(self):
        """
        This test checks the template FA_Q_DP for Magma.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.FA_Q_dp.Magma.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        uptoDeg = 10;
        expectedString = """F := RationalField();
A<x1,x2,x3,x4> := FreeAlgebra(F,4);
B := [x1+x2,
x3*x4-x2*x1,
x1*x2*x3*x4];
GroebnerBasis(B,10);
quit;"""
        output = generateCode(vars,basis,uptoDeg)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_FP_DP_GAP(self):
        """
        This test checks the template GB_Fp_dp for GAP.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.GAP.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        characteristic = 5
        expectedString = """F := GaloisField(5);
PR := PolynomialRing(F,["x1","x2","x3","x4"]);
x1:= IndeterminatesOfPolynomialRing(PR)[1];
x2:= IndeterminatesOfPolynomialRing(PR)[2];
x3:= IndeterminatesOfPolynomialRing(PR)[3];
x4:= IndeterminatesOfPolynomialRing(PR)[4];
I:= Ideal(PR,[x1+x2,x3*x4-x2*x1,x1*x2*x3*x4]);
ord := MonomialGrlexOrdering(x1,x2,x3,x4);
B := GroebnerBasis(I,ord);
B;
quit;"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_FP_DP_Singular(self):
        """
        This test checks the template GB_Fp_dp for Singular.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.Singular.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        characteristic = 5
        expectedString = """ring R = 5,(x1,x2,x3,x4),lp;
ideal I = x1+x2,
x3*x4-x2*x1,
x1*x2*x3*x4;
ideal J = std(I);
print(J);
$"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_FP_DP_Magma(self):
        """
        This test checks the template GB_Fp_dp for Magma.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.Magma.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        characteristic = 5
        expectedString = """F := FiniteField(5);
P<x1,x2,x3,x4> := PolynomialRing(F,4);
I := ideal<P | x1+x2,x3*x4-x2*x1,x1*x2*x3*x4>;
B := GroebnerBasis(I);
B;
quit;"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_FP_DP_Maple(self):
        """
        This test checks the template GB_Fp_dp for Maple.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.Maple.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        characteristic = 5
        expectedString = """with(Groebner):
Ideal := {x1+x2,x3*x4-x2*x1,x1*x2*x3*x4} mod 5:
ordering := grlex(x1,x2,x3,x4):
B := Basis(Ideal, ordering):
print(B);
quit;"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_lp_Maple(self):
        """
        This test checks the template GB_Z_lp for Maple.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.Maple.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = """with(Groebner):
Ideal := {x1+x2,x3*x4-x2*x1,x1*x2*x3*x4}:
ordering := plex(x1,x2,x3,x4):
B := Basis(Ideal, ordering):
print(B);
quit;"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_lp_Singular(self):
        """
        This test checks the template GB_Z_lp for Singular.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.Singular.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = """ring R = 0,(x1,x2,x3,x4),lp;
ideal I = x1+x2,
x3*x4-x2*x1,
x1*x2*x3*x4;
ideal J = std(I);
print(J);
$"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_lp_Magma(self):
        """
        This test checks the template GB_Z_lp for Magma.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.Magma.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = """F := RationalField();
P<x1,x2,x3,x4> := PolynomialRing(F,4);
I := ideal<P | x1+x2,x3*x4-x2*x1,x1*x2*x3*x4>;
B := GroebnerBasis(I);
B;
quit;"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_LP_GAP(self):
        """
        This test checks the template GB_Z_lp for GAP.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.GAP.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = """F := Rationals;
PR := PolynomialRing(F,["x1","x2","x3","x4"]);
x1:= IndeterminatesOfPolynomialRing(PR)[1];
x2:= IndeterminatesOfPolynomialRing(PR)[2];
x3:= IndeterminatesOfPolynomialRing(PR)[3];
x4:= IndeterminatesOfPolynomialRing(PR)[4];
I:= Ideal(PR,[x1+x2,x3*x4-x2*x1,x1*x2*x3*x4]);
ord := MonomialLexOrdering(x1,x2,x3,x4);
B := GroebnerBasis(I,ord);
B;
quit;"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_LP_REDUCE(self):
        """
        This test checks the template GB_Z_lp for REDUCE.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.REDUCE.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = """gbasis({x1+x2,x3*x4-x2*x1,x1*x2*x3*x4},{x1,x2,x3,x4});quit;"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")
        
if __name__=="__main__":
    unittest.main()
