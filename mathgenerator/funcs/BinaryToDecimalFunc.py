from .__init__ import *
from ..__init__ import Generator


def BinaryToDecimalFunc(max_dig=10):
    problem = ''

    for i in range(random.randint(1, max_dig)):
        temp = str(random.randint(0, 1))
        problem += temp

    solution = int(problem, 2)
    return problem, solution


binaryToDecimal = Generator("Binary to Decimal", 15, "Decimal of a=", "b",
                            BinaryToDecimalFunc)
