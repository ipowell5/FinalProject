import tkinter as tk
import webbrowser
from validation import validate_url, validate_email

class ContactWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Contact Information")

        self.email_label = tk.Label(self, text="Email: shop@example.com")
        self.email_label.pack()

        self.shop_button = tk.Button(self, text="Shop Available Pieces", command=self.open_shop)
        self.shop_button.pack()

        self.back_button = tk.Button(self, text="Back", command=self.destroy)
        self.back_button.pack()

    def open_shop(self):
        url = 'https://yourshop.com'
        if validate_url(url):
            webbrowser.open(url)
        else:
            print(f"Invalid URL: {url}")
