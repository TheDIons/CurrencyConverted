import tkinter as tk
import requests

def convert_currency():
    # Get the current exchange rates from an API
    url = "https://api.exchangerate-api.com/v4/latest/{}"
    base = base_var.get()
    response = requests.get(url.format(base))
    data = response.json()
    rates = data["rates"]

    # Get the amount from the input field
    amount = amount_entry.get()

    # Get the selected target currency
    target = target_var.get()

    # Convert the amount to the target currency
    converted_amount = float(amount) * rates[target]

    # Display the converted amount in the output field
    converted_label.config(text=converted_amount)

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.iconbitmap("E:\Programing\Currency_Convert\img\ex.ico")
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)

# Create the input field
amount_label = tk.Label(root, text="Enter amount:")
amount_label.grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

# Create the base currency option
base_var = tk.StringVar(value='THB')
base_label = tk.Label(root, text="Select base currency:")
base_label.grid(row=1, column=0)
base_option = tk.OptionMenu(root, base_var, 'THB', 'USD', 'TRY', 'EGP')
base_option.grid(row=1, column=1)

# Create the target currency option
target_var = tk.StringVar(value='USD')
target_label = tk.Label(root, text="Select target currency:")
target_label.grid(row=2, column=0)
target_option = tk.OptionMenu(root, target_var, 'THB', 'USD', 'TRY', 'EGP')
target_option.grid(row=2, column=1)

# Create the convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create the output field
converted_label = tk.Label(root, text="")
converted_label.grid(row=4, column=0, columnspan=2)

# Start the main loop
root.mainloop()
