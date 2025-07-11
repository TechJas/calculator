# MyModule.py
import math 

# Arithmetic
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"
def modulus(a, b): return a % b
def power(a, b): return a ** b

# Scientific
def square_root(x): return math.sqrt(x)
def exponential(x): return math.exp(x)
def logarithm(x, base=10): return math.log(x, base)

# Trigonometric (input in radians)
def sine_radians(x): return math.sin(x)
def cosine_radians(x): return math.cos(x)
def tangent_radians(x): return math.tan(x)

# Inverse trig (output in degrees)
def arcsin(x): return math.degrees(math.asin(x))
def arccos(x): return math.degrees(math.acos(x))
def arctan(x): return math.degrees(math.atan(x))

# Hyperbolic
def sinh(x): return math.sinh(x)
def cosh(x): return math.cosh(x)
def tanh(x): return math.tanh(x)

# Conversion
def degrees_to_radians(deg): return math.radians(deg)
def radians_to_degrees(rad): return math.degrees(rad)