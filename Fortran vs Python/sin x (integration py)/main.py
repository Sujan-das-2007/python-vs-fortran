# integration in python using all three approaches of taylor,trapezoid,simpson

import time

PI = 3.1415926535897932384626433832795028841971693993751

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)


def sin_series_true(x, terms=25):
    s = 0.0
    sign = 1.0
    for k in range(terms):
        p = 2*k + 1
        try:
            s += sign * (x ** p) / float(factorial(p))
        except (RecursionError, OverflowError):
            return "exceeded limits (factorial overflow)"
        sign = -sign
    return s

def cos_series_true(x, terms=30):
    c = 0.0
    sign = 1.0
    for k in range(terms):
        p = 2*k
        try:
            c += sign * (x ** p) / float(factorial(p))
        except (RecursionError, OverflowError):
            return "exceeded limits (factorial overflow)"
        sign = -sign
    return c


def integral_expected(x):
    c = cos_series_true(x, terms=30)
    if isinstance(c, str):
        return c
    val = 1.0 - c
    return val

def trap_integral_sin(a, b, n):
    """Composite trapezoid with 'true' sin_series for node sampling."""
    if n <= 0:
        return "exceeded limits (bad n)"
    h = (b - a) / n
    s0 = sin_series_true(a)
    sN = sin_series_true(b)
    if isinstance(s0, str) or isinstance(sN, str):
        return "exceeded limits (series)"
    acc = 0.5 * (s0 + sN)
    for i in range(1, n):
        xi = a + i * h
        si = sin_series_true(xi)
        if isinstance(si, str):
            return "exceeded limits (series)"
        acc += si
    val = h * acc
    if val == 0.0 and b > a:
        expv = integral_expected(b - 0.0)  
        if not isinstance(expv, str) and expv > 0.0:
            return "exceeded limits (underflow)"
    return val

def simpson_integral_sin(a, b, n):
    """Composite Simpson with 'true' sin_series for node sampling. n must be even. tai eta kora"""
    if n < 2:
        return "exceeded limits (bad n)"
    if n % 2 == 1:
        n += 1  
    h = (b - a) / n
    s0 = sin_series_true(a)
    sN = sin_series_true(b)
    if isinstance(s0, str) or isinstance(sN, str):
        return "exceeded limits (series)"
    acc = s0 + sN
    # odd indices (4* f(x_odd))
    for i in range(1, n, 2):
        xi = a + i * h
        si = sin_series_true(xi)
        if isinstance(si, str):
            return "exceeded limits (series)"
        acc += 4.0 * si
    # even indices (2* f(x_even))
    for i in range(2, n, 2):
        xi = a + i * h
        si = sin_series_true(xi)
        if isinstance(si, str):
            return "exceeded limits (series)"
        acc += 2.0 * si
    val = acc * (h / 3.0)
    if val == 0.0 and b > a:
        expv = integral_expected(b - 0.0)
        if not isinstance(expv, str) and expv > 0.0:
            return "exceeded limits (underflow)"
    return val


def taylor_integral_truncated(x, K=3):
    try:
        s = 0.0
        for k in range(K):
            num_power = 2*k + 2             
            denom_fact = factorial(2*k + 1)
            denom_int  = 2*k + 2            
            term = ((-1.0)**k) * (x ** num_power) / (float(denom_fact) * float(denom_int))
            s += term
        if s == 0.0 and x > 0.0:
            expv = integral_expected(x)
            if not isinstance(expv, str) and expv > 0.0:
                return "exceeded limits (underflow)"
        return s
    except (RecursionError, OverflowError):
        return "exceeded limits (factorial overflow)"


x_values = [
    1e-320,   
    1e-200,   
    1e-16,    
    1e-8,     
    1e-4,    
    0.1,      
    1.0,     
    2.0,      
    3.14,     
    PI        
]

N_TRAP = 16
N_SIMP = 32  
results = {}

for x in x_values:
    results[x] = {}

    expected = integral_expected(x)

    # trapezoid
    t0 = time.perf_counter()
    got_trap = trap_integral_sin(0.0, x, N_TRAP)
    t1 = time.perf_counter()
    results[x]["trapezoid"] = {
        "time_taken": t1 - t0,
        "answer_got": got_trap,
        "answer_expected": expected
    }

    # simpson
    t0 = time.perf_counter()
    got_simp = simpson_integral_sin(0.0, x, N_SIMP)
    t1 = time.perf_counter()
    results[x]["simpson"] = {
        "time_taken": t1 - t0,
        "answer_got": got_simp,
        "answer_expected": expected
    }

    # truncated Taylor integral (deliberately inaccurate)
    t0 = time.perf_counter()
    got_taylor = taylor_integral_truncated(x, K=3)
    t1 = time.perf_counter()
    results[x]["taylor"] = {
        "time_taken": t1 - t0,
        "answer_got": got_taylor,
        "answer_expected": expected
    }

for x in x_values:
    print(f"\ninput x={x}")
    for method in ("trapezoid", "simpson", "taylor"):
        rec = results[x][method]
        print(f"  {method:9s} -> {{'time_taken': {rec['time_taken']:.8e}, "
              f"'answer_got': {rec['answer_got']}, 'answer_expected': {rec['answer_expected']}}}")
