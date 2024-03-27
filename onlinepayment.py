import tkinter as tk

def process_payment():
    selected_method = payment_method.get()
    
    # Perform necessary validations
    # Call back-end functions based on the selected payment method
    # Update database with order and payment details
    # (In a real-world scenario, you would connect to a server for processing)

# GUI setup
root = tk.Tk()
root.title("Online Payment System")

# User details
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Order details
tk.Label(root, text="Product:").pack()
product_entry = tk.Entry(root)
product_entry.pack()

# Payment method
tk.Label(root, text="Payment Method:").pack()
payment_method = tk.StringVar()
payment_method.set("GPay")  # Default option

methods = ["GPay", "Cash on Delivery", "Debit/Credit Card"]
for method in methods:
    tk.Radiobutton(root, text=method, variable=payment_method, value=method).pack()

# Button to process payment
tk.Button(root, text="Process Payment", command=process_payment).pack()

root.mainloop()


