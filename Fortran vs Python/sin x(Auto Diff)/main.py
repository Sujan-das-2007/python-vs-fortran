import torch
import time
import math

def cos_autograd(x_value):
    """
    Use PyTorch autograd to compute d/dx [sin(x)] = cos(x).
    """
    try:
        # Convert scalar to torch tensor with gradient tracking
        x = torch.tensor(x_value, dtype=torch.float64, requires_grad=True)

        # Define f(x) = sin(x)
        f = torch.sin(x)

        # Compute derivative df/dx using autograd
        f.backward()

        # Gradient is stored in x.grad
        return x.grad.item()
    except Exception:
        return "exceeded limits"

# Test values for x
test_values = [0.1, 0.5, 1.0, 2.0, 3.14, 6.28, 10.0, 20.0, 50.0, 100.0]

# Run tests
for x in test_values:
    t0 = time.time()
    got = cos_autograd(x)
    t1 = time.time()

    expected = math.cos(x) if isinstance(got, float) else "exceeded limits"

    print(f"x={x:.2f}: {{'time_taken': {t1 - t0:.8f}, "
          f"'answer_got': {got}, 'answer_expected': {expected}}}")
