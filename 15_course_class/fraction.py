class Fraction:
    def __init__(self, numberator = 0, denominator = 1):
        divisor = gcd(numberator, denominator)
        self.__numerator = numberator // divisor
        self.__denominator = denominator // divisor
    
    # Getter
    @property
    def numerator(self):
        return self.__numerator
    
    @property
    def denominator(self):
        return self.__denominator
    
    # Setters
    @numerator.setter
    def numerator(self, value):
        self.__numerator = value
    
    @denominator.setter
    def denominator(self, value):
        if value == 0:
            print("Incorrect logic: denominator cannot be zero")
        else:
            self.__denominator = value
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    # Multiplication operator
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    # Addition operator
    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)
    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)
    def __lt__(self, other):
        return self.__cmp__(other) < 0
    
    # Compare
    def __cmp__(self, other):
        temp = self.__sub__(other)


def gcd(n, d):
    gcd = 1
    k = 1
    while k <= n and k <= d:
        if n % k == 0 and d % k == 0:
            gcd = k
        k += 1
    
    return gcd

frac = Fraction(2, 3)
print(frac)
frac.numerator = 3
frac.denominator = 0
print(frac)
frac2 = Fraction(4, 5)
print(f"{frac} * {frac2} = {frac * frac2}")
print(f"{frac} + {frac2} = {frac + frac2}")
print(f"{frac} - {frac2} = {frac - frac2}")
#print(f"{frac} < {frac2} is {frac < frac2}")
