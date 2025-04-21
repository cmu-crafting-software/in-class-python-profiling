import time

import numpy as np
import requests
import torch


def cpu_bound(n):
    if n <= 1:
        return 1
    return cpu_bound(n - 1) + cpu_bound(n - 2)


def io_bound():
    time.sleep(1)
    requests.get("https://httpbin.org/get")


def memory_hog():
    return [x**2 for x in range(10**6)]


def native_numpy():
    x = np.random.rand(1000, 1000)
    y = x @ x
    return y


def native_torch():
    a = torch.randn(1000, 1000)
    b = torch.matmul(a, a)
    return b


def main():
    for i in range(3):
        start = time.time()
        print(f"iteration {i}")
        cpu_bound(35)
        middle = time.time()
        print(f"finished `cpu_bound`: {middle - start}")
        io_bound()
        end = time.time()
        print(f"finished `io_bound`: {end - middle}")
        memory_hog()
        native_numpy()
        native_torch()


if __name__ == "__main__":
    main()
