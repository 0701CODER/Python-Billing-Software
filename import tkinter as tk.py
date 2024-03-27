import tkinter as tk
from tkinter import messagebox

class PaymentApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Payment Options")

        # Payment method variable
        self.payment_method = tk.StringVar()

        # Widgets
        tk.Label(master, text="Select Payment Method:").pack()
        tk.Radiobutton(master, text="Google Pay", variable=self.payment_method, value="gpay").pack()
        tk.Radiobutton(master, text="Cash on Delivery", variable=self.payment_method, value="cod").pack()
        tk.Button(master, text="Proceed to Payment", command=self.process_payment).pack()

    def process_payment(self):
        selected_method = self.payment_method.get()

        if selected_method == "gpay":
            # Code to initiate GPay payment
            messagebox.showinfo("Payment Successful",) 