import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_pixel(c, maxiter):
    """Check wether a single pixel diverges"""
    z = 0

    for n in range(maxiter):
        z = z*z + c
        if abs(z) > 2:
            return n

    return 0

def mandelbrot_image(xmin, xmax, ymin, ymax, width, height, maxiter):
    """Render an image of the Mandelbrot set"""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            c = xi + 1j*yj
            img[i, j] = mandelbrot_pixel(c, maxiter)

    return img

def benchmark(mandelbrot):
    xmin = -0.74877
    xmax = -0.74872
    ymin = 0.065053
    ymax = 0.065103
    pixels = 1000
    maxiter = 2048
    return mandelbrot(xmin, xmax, ymin, ymax, pixels, pixels, maxiter)