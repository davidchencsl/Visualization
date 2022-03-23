class Solve:
    def __init__(self):
        pass

    def derivative(self, f, x, delta=1e-6):
        return (f(x+delta) - f(x-delta))/(2*delta)

    def linspace(self, a, b, n=100):
        return [a + (b-a)/(n-1)*i for i in range(n)]

    def roots(self, f, max_iter=10, low_bound=-10, high_bound=10, sample_size=2000, delta=1e-10):
        roots = []
        samples = self.linspace(low_bound, high_bound, sample_size)
        for s in samples:
            for iter in range(max_iter):
                f_prime = self.derivative(f, s, delta)
                if (abs(f_prime) < delta):
                    f_prime = delta
                s = s - f(s)/f_prime
                if abs(f(s)) < delta:
                    roots.append(s)
                    break
        if (len(roots) == 0):
            return []
        roots = [roots[0]] + [roots[i]
                              for i in range(1, len(roots)) if abs(roots[i] - roots[i-1]) > delta]
        roots = [round(root, 6) for root in roots]
        return roots


if __name__ == '__main__':
    import math
    import matplotlib.pyplot as plt
    import numpy as np

    def f(x):
        return 0.2/(math.pi*(0.002**2)*x)-200
    print(Solve().roots(f))
    
