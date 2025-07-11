# main.py
import MyModule

def format_result(result):
    if isinstance(result, float):
        return f"{result:.3f}"
    return result  # For strings like division errors

def main():
    try:
        val = {}

        print("Enter inputs:")
        val["a"] = float(input("a = "))
        val["b"] = float(input("b = "))
        val["angle_deg"] = float(input("Angle (in degrees) = "))
        val["x"] = float(input("Value for inverse/hyperbolic = "))
        log_base = input("Log base (default is 10): ")
        val["log_base"] = float(log_base) if log_base else 10

        # Convert angle to radians for trig functions
        val["angle_rad"] = MyModule.degrees_to_radians(val["angle_deg"])

        print("\n--- SCIENTIFIC CALCULATOR OUTPUT ---")
        print("Add:", format_result(MyModule.add(val["a"], val["b"])))
        print("Subtract:", format_result(MyModule.subtract(val["a"], val["b"])))
        print("Multiply:", format_result(MyModule.multiply(val["a"], val["b"])))
        print("Divide:", format_result(MyModule.divide(val["a"], val["b"])))
        print("Modulus:", format_result(MyModule.modulus(val["a"], val["b"])))
        print("Power:", format_result(MyModule.power(val["a"], val["b"])))
        print("Square Root of a:", format_result(MyModule.square_root(val["a"])))
        print("Exponential (e^x):", format_result(MyModule.exponential(val["x"])))
        print("Logarithm of a (base {}):".format(val["log_base"]),
              format_result(MyModule.logarithm(val["a"], val["log_base"])))

        # Trigonometric (in radians)
        print("Sine(angle):", format_result(MyModule.sine_radians(val["angle_rad"])))
        print("Cosine(angle):", format_result(MyModule.cosine_radians(val["angle_rad"])))
        print("Tangent(angle):", format_result(MyModule.tangent_radians(val["angle_rad"])))

        # Inverse trig (result in degrees)
        print("θ = sin⁻¹(x):", format_result(MyModule.arcsin(val["x"])))
        print("θ = cos⁻¹(x):", format_result(MyModule.arccos(val["x"])))
        print("θ = tan⁻¹(x):", format_result(MyModule.arctan(val["x"])))

        # Hyperbolic functions
        print("Sinh(x):", format_result(MyModule.sinh(val["x"])))
        print("Cosh(x):", format_result(MyModule.cosh(val["x"])))
        print("Tanh(x):", format_result(MyModule.tanh(val["x"])))

    except Exception:
        print("\nSyntax Error: Please enter valid input values.")

if __name__ == "__main__":
    main()