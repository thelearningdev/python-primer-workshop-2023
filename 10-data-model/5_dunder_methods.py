class Fraction:
    def simplify(self):
        gcd = self.find_gcd(self.num, self.den)
        return Fraction(self.num // gcd, self.den // gcd)

    @staticmethod
    def find_gcd(a, b):
        if b == 0:
            return a
        return Fraction.find_gcd(b, a % b)


f = Fraction(1, 5)
assert str(f) == "1/5"
assert f.numerator == 1
assert f.denominator == 5
assert f + Fraction(2, 5) == Fraction(3, 5)
