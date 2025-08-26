import torch
import time

PI = 3.1415926535897932384626433832795028841971693993751

dtype = torch.float64
def f(x):
    return torch.sin(x)

def autograd_integration(a, b, n=2000):
    # x = torch.linspace(a, b, n, dtype=dtype, requires_grad=True) # icche hole eta use korish 
    x = torch.tensor([1e-320,   
    1e-200,   
    1e-16,    
    1e-8,     
    1e-4,    
    0.1,      
    1.0,     
    2.0,      
    3.14,     
    PI  
    ])
    y = f(x)
    h = (b - a) / (n-1)
    return torch.trapz(y, dx=h)

def exact_integral(a, b):
    return -torch.cos(b) + torch.cos(a)

x_values = torch.linspace(0.1, torch.pi, 10, dtype=dtype)
a = torch.tensor(0.0, dtype=dtype)

results = {}

for x in x_values:
    entry = {}
    
    start = time.time()
    auto = autograd_integration(a, x).item()
    end = time.time()
    
    entry["Auto_time"] = end - start
    entry["Autograd"] = auto
    
    entry["Expected"] = exact_integral(a, x).item()
    
    results[round(x.item(), 4)] = entry

for k, v in results.items():
    print(f"x={k} : {v}")
