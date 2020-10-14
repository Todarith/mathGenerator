import random

# || Generator class

class Generator:
    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func

    def __str__(self):
        return str(self.id) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self):
        return self.func()


# || Functions

def additionFunc(maxSum = 99, maxAddend = 50):
    a = random.randint(0, maxAddend)
    b = random.randint(0, min((maxSum-a), maxAddend)) #The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    c = a+b
    problem = str(a) + "+" + str(b) + "="
    solution = str(c)
    return problem, solution

def subtractionFunc(maxMinuend = 99, maxDiff = 99):
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a-maxDiff)), a)
    c = a-b
    problem = str(a) + "-" + str(b) + "="
    solution = str(c)
    return problem, solution

def multiplicationFunc(maxRes = 99, maxMulti = 99):
    a = random.randint(0, maxMulti)
    b = random.randint(0, min(maxRes, maxMulti))
    c = a*b
    problem = str(a) + "*" + str(b) + "="
    solution = str(c)
    return problem, solution

def divisionFunc(maxRes = 99, maxDivid = 99):
    a = random.randint(0, maxDivid)
    b = random.randint(0, min(maxRes, maxDivid))
    c = a/b
    problem = str(a) + "/" + str(b) + "="
    solution = str(c)
    return problem, solution

def binaryComplement1sFunc(maxDigits = 10):
    question = ''
    answer = ''    
    for i in range(random.randint(1,maxDigits)): 
        temp = str(random.randint(0, 1)) 
        question += temp
        answer += "0" if temp == "1" else "1" 
   
    problem = question    
    solution = answer
    return problem, solution

def moduloFunc(maxRes = 99, maxModulo= 99):
    a = random.randint(0, maxModulo)
    b = random.randint(0, min(maxRes, maxModulo))
    c = a%b
    problem = str(a) + "%" + str(b) + "="
    solution = str(c)
    return problem, solution

def squareRootFunction(minNo = 1, maxNo = 12):
    b = random.randint(minNo, maxNo)
    a = b*b
    problem = "sqrt(" + str(a) + ")="
    solution = str(b)
    return problem, solution

def powerRuleDifferentiationFunc(maxCoef = 10, maxExp = 10, maxTerms = 5):
    numTerms = random.randint(1, maxTerms)
    problem = ""
    solution = ""
    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, maxCoef)
        exponent = random.randint(1, maxExp)
        problem += str(coefficient) + "x^" + str(exponent)
        solution += str(coefficient * exponent) + "x^" + str(exponent - 1)
    return problem, solution

def basicAlgebraFunc(maxVariable = 10):
    a = random.randint(1, maxVariable)
    b = random.randint(1, maxVariable)
    c = random.randint(b, maxVariable)
    # calculate gcd
    def calculate_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    i = calculate_gcd((c - b), a)
    x = f"{(c - b)//i}/{a//i}"
    if (c - b == 0):
        x = "0"
    problem = f"{a}x + {b} = {c}"
    solution = x
    return problem, solution



# || Class Instances

#Format is:
#<title> = Generator("<Title>", <id>, <generalized problem>, <generalized solution>, <function name>)
addition = Generator("Addition", 2, "a+b=", "c", additionFunc)
subtraction = Generator("Subtraction", 3, "a-b=", "c", subtractionFunc)
multiplication = Generator("Multiplication", 4, "a*b=", "c", multiplicationFunc)
division = Generator("Division", 5, "a/b=", "c", divisionFunc)
binaryComplement1s = Generator("binary_complement_1s", 6, "1010=", "0101", binaryComplement1sFunc)
moduloDivision = Generator("Modulo_Division", 7, "a%b=", "c", moduloFunc)
squareRoot = Generator("Square _Root", 8, "sqrt(a)=", "b", squareRootFunction)
powerRuleDifferentiation = Generator("Power_Rule_Differentiation", 9, "nx^m=", "(n*m)x^(m-1)", powerRuleDifferentiationFunc)
basicAlgebra = Generator("Basic_Algebra", 13, "ax + b = c", "d", basicAlgebraFunc)




