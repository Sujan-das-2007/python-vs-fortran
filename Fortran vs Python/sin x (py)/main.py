import math
from time import perf_counter

# Calculating the factorial here, jeta porechis using recursion otai, python e eta 
# lambda functions diye erom bhabe one line e o lekha jai, ha flexing here
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

# ekhane question nicchi f(x) =  sin x
# d/dx sin(x) -> cos x jani toh ebr function e value bosiye dekhbo otar f'(x) e ki 
# value asbe seta r jonno estimation ache, the more accurate we want the more terms we 
# keep on adding to the taylor series polynomial , ekhane accuracy kaaj na 
# vulnerability ber korai kaaj tai first order derivative er jonnoi gelam, 

# eitai mathematics jeta sikhte holo bole hocche numerical derivation estimation using
# Taylor expansion ba series ja bolar techincality ache terms er but u get the drill
def cos_taylor_first(x):
    """
    Approximate cos(x) using only the first two terms of its Taylor series:
    cos(x) ≈ 1 - x^2 / 2! karon agei bolechi er besi jawa mane vulneribility optimize 
    kora , ami optimize korle r tahole korai kno eta in first place
    jani factorial 2 e use hocche which is 2 and hard code korar need chilo na tao for 
    technicalities dilam and to expose run time too to call functions , jeta main reason eitar.
    Ei je taylor er part ta ache eita cos function er 0 r joto kache thakbe toto near answer debe , joto 0 r edik udik joto jaabe toto faltu hbe karon lt h->0 diye amra sob solve kori mane works when things tend to 0 better, eita r kaaj e hocche thik dite dite bhul deoa 
    """
    try:
        return 1 - (x**2) / factorial(2)
    except (OverflowError, RecursionError):
        return "exceeded limits"

# eikhane test values and inferencing and taking the results as a dictionary pore ota 
# return kore parse kore nebo and kaaj done
def test_derivative():
    inputs = [0.1, 0.5, 1.0, 2.0, 3.14, 6.28, 10.0, 20.0, 50.0, 100.0]
    results = {}

    for x in inputs:
        t0 = perf_counter()
        got = cos_taylor_first(x)   
        expected = math.cos(x) if isinstance(got, float) else "exceeded limits"
        t1 = perf_counter()
        # ei tolar data structure ta is called dictionary in python, it stores key 
        # value pair ,key diye value access and vice versa kora jai , ete laage ni still
        results[x] = {
            "time_taken": t1 - t0,
            "answer_got": got,
            "answer_expected": expected
        }
    return results

# baas calling stuff and printing
if __name__ == "__main__": #eita python er main function laage na still looks good
    output = test_derivative()
    for x, vals in output.items():
        print(f"x={x}: {vals}") #eita way of printing in python , called f-strings
