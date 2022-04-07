class Fraction:
    def __init__(self, num: int, den: int):

        if num < 0 or den <= 0:
            raise ValueError("neither the numerator nor the denominator can be < 0")
        self.num = num
        self.den = den
        self.simplify()

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction({self.num}, {self.den})"

    def __mul__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.num * other.num, self.den * other.den)

    def __add__(self, other: "Fraction") -> "Fraction":
        return Fraction((self.num * other.den + other.num * self.den), self.den * other.den)

    def simplify(self):
        gcd_var = gcd(self.num, self.den)
        self.num = self.num//gcd_var
        self.den = self.den//gcd_var
        return self


def gcd(a, b) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

