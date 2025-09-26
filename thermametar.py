import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        # Read the value entered by the user
        temp = float(entry_value.get())
        scale = selected_scale.get()

        if scale == "Celsius":
            c = temp
            f = (c * 9/5) + 32
            k = c + 273.15
        elif scale == "Fahrenheit":
            f = temp
            c = (f - 32) * 5/9
            k = c + 273.15
        elif scale == "Kelvin":
            k = temp
            c = k - 273.15
            f = (c * 9/5) + 32
        else:
            messagebox.showerror("Error", "Select a valid scale.")
            return

        # Update results
        result_celsius.config(text=f"{c:.2f} °C")
        result_fahrenheit.config(text=f"{f:.2f} °F")
        result_kelvin.config(text=f"{k:.2f} K")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.state("zoomed")
#root.resizable(False, False)

# Title
title = tk.Label(root, text="Temperature Converter", font=("Arial", 25, "bold"))
title.pack(pady=10)

# Entry field
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Enter Value:", font=("Arial", 20)).grid(row=0, column=0, padx=5)
entry_value = tk.Entry(frame_input, width=10, font=("Arial", 20))
entry_value.grid(row=0, column=1, padx=5)

# Dropdown for scale selection
selected_scale = tk.StringVar(value="Celsius")
tk.OptionMenu(frame_input, selected_scale, "Celsius", "Fahrenheit", "Kelvin").grid(row=0, column=2, padx=5)

# Convert button
btn_convert = tk.Button(root, text="Convert", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white",
                        command=convert_temperature)
btn_convert.pack(pady=10)

# Result labels
frame_results = tk.Frame(root)
frame_results.pack(pady=10)

tk.Label(frame_results, text="Celsius:", font=("Arial", 20)).grid(row=0, column=0, sticky="e", padx=5)
result_celsius = tk.Label(frame_results, text="-- °C", font=("Arial", 20, "bold"))
result_celsius.grid(row=0, column=1, sticky="w", padx=5)

tk.Label(frame_results, text="Fahrenheit:", font=("Arial", 20)).grid(row=1, column=0, sticky="e", padx=5)
result_fahrenheit = tk.Label(frame_results, text="-- °F", font=("Arial", 20, "bold"))
result_fahrenheit.grid(row=1, column=1, sticky="w", padx=5)

tk.Label(frame_results, text="Kelvin:", font=("Arial", 20)).grid(row=2, column=0, sticky="e", padx=5)
result_kelvin = tk.Label(frame_results, text="-- K", font=("Arial", 20, "bold"))
result_kelvin.grid(row=2, column=1, sticky="w", padx=5)

root.mainloop()
