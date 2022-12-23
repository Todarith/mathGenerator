import random


def simple_interest(maxPrinciple=10000,
             maxRate=10,
             maxTime=10):
    """Simple Interest"""
    p = random.randint(1000, maxPrinciple)
    r = random.randint(1, maxRate)
    t = random.randint(1, maxTime)
    s = round((p * r * t) / 100, 2)

    problem = f"Simple interest for a principle amount of ${p}$ dollars, ${r}$% rate of interest and for a time period of ${t}$ years is $=$ "
    solution = f'${s}$'
    return problem, solution
