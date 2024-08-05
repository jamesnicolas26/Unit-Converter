import tkinter as tk
from tkinter import ttk

# Conversion rates
conversion_factors = {
    'Kilometers to Miles': 0.621371,
    'Miles to Kilometers': 1.60934,
    'Centimeters to Inches': 0.393701,
    'Inches to Centimeters': 2.54,
    'Kilograms to Pounds': 2.20462,
    'Pounds to Kilograms': 0.453592,
}

def convert_units():
    """Convert units based on the selected conversion type."""
    try:
        value = float(entry_value.get())
        conversion_type = combo_conversion.get()
        factor = conversion_factors[conversion_type]
        converted_value = value * factor
        label_result.config(text=f"Result: {converted_value:.2f}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")

def create_unit_converter():
    """Create a simple unit converter GUI."""
    root = tk.Tk()
    root.title("Unit Converter")

    global entry_value, combo_conversion, label_result

    # Entry for the value to be converted
    tk.Label(root, text="Value:").pack(pady=5)
    entry_value = tk.Entry(root, width=20)
    entry_value.pack(pady=5)

    # Dropdown for conversion types
    tk.Label(root, text="Conversion:").pack(pady=5)
    combo_conversion = ttk.Combobox(root, values=list(conversion_factors.keys()), width=25)
    combo_conversion.set("Kilometers to Miles")
    combo_conversion.pack(pady=5)

    # Convert button
    tk.Button(root, text="Convert", command=convert_units).pack(pady=10)

    # Result label
    label_result = tk.Label(root, text="Result:")
    label_result.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_unit_converter()
