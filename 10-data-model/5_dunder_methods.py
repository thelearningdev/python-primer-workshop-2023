class Fraction:
    def simplify(self):
        gcd = self.find_gcd(self.num, self.den)
        return Fraction(self.num // gcd, self.den // gcd)

    @staticmethod
    def find_gcd(a, b):
        if b == 0:
            return a
        return Fraction.find_gcd(b, a % b)


f = Fraction(1, 5) # 1/5  # __init__
assert str(f) == "1/5"    # __str__
assert f.numerator == 1   # __init__
assert f.denominator == 5 # __init__

assert f + Fraction(2, 5) == Fraction(3, 5) # addition __add__
assert Fraction(2, 2) - Fraction(2, 2) == 0

# Subtraction __sub__
# multiplication  __mul__
# div __divmod__
# less than __lt__
# greater than __gt__
# equal __eq__
