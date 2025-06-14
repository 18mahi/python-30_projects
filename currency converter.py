from tkinter import Button, Entry, Label, StringVar, Tk, messagebox, ttk

import requests


# --- Currency Converter Class ---
class CurrencyConverter:
    API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

    def __init__(self):
        self.rates = {}
        self.base = "USD"
        self.fetch_rates(self.base)

    def fetch_rates(self, base):
        try:
            response = requests.get(self.API_URL.format(base))
            data = response.json()
            self.rates = data['rates']
            self.base = base
        except Exception:
            messagebox.showerror("Error", "Failed to fetch currency rates.")

    def convert(self, amount, from_currency, to_currency):
        if from_currency != self.base:
            self.fetch_rates(from_currency)
        rate = self.rates.get(to_currency)
        if rate:
            return round(amount * rate, 4)
        else:
            messagebox.showerror("Error", "Currency not supported.")
            return None

# --- GUI Application ---
class CurrencyApp(Tk):
    def __init__(self, converter):
        super().__init__()
        self.title("💸 Aesthetic Currency Converter")
        self.geometry("400x320")
        self.configure(bg="#232946")
        self.resizable(False, False)
        self.converter = converter

        self.currencies = sorted(list(self.converter.rates.keys()))
        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('TCombobox', fieldbackground="#edb50b", background="#ecc00e")

        Label(self, text="Currency Converter", font=("Montserrat", 20, "bold"),
              bg="#232946", fg="#f1c30a").pack(pady=15)

        frame = ttk.Frame(self)
        frame.pack(pady=10)

        Label(frame, text="Amount:", font=("Montserrat", 12), background="#08175E", foreground="#ebb608").grid(row=0, column=0, padx=5, pady=5)
        self.amount_var = StringVar()
        Entry(frame, textvariable=self.amount_var, font=("Montserrat", 12), width=12).grid(row=0, column=1, padx=5, pady=5)

        Label(frame, text="From:", font=("Montserrat", 12), background="#0B1A64", foreground="#e9a40e").grid(row=1, column=0, padx=5, pady=5)
        self.from_currency = StringVar(value="USD")
        from_box = ttk.Combobox(frame, textvariable=self.from_currency, values=self.currencies, state="readonly", width=10)
        from_box.grid(row=1, column=1, padx=5, pady=5)

        Label(frame, text="To:", font=("Montserrat", 12), background="#232946", foreground="#ebb60a").grid(row=2, column=0, padx=5, pady=5)
        self.to_currency = StringVar(value="EUR")
        to_box = ttk.Combobox(frame, textvariable=self.to_currency, values=self.currencies, state="readonly", width=10)
        to_box.grid(row=2, column=1, padx=5, pady=5)

        Button(self, text="Convert", font=("Montserrat", 12, "bold"), bg="#eee30b", fg="#232946",
               command=self.perform_conversion, relief="flat", borderwidth=0, padx=10, pady=5).pack(pady=15)

        self.result_var = StringVar()
        Label(self, textvariable=self.result_var, font=("Montserrat", 16, "bold"),
              bg="#232946", fg="#eebbc3").pack(pady=10)

    def perform_conversion(self):
        try:
            amount = float(self.amount_var.get())
            from_cur = self.from_currency.get()
            to_cur = self.to_currency.get()
            result = self.converter.convert(amount, from_cur, to_cur)
            if result is not None:
                self.result_var.set(f"{amount} {from_cur} = {result} {to_cur}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

if __name__ == "__main__":
    converter = CurrencyConverter()
    app = CurrencyApp(converter)
    app.mainloop()