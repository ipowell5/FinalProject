import tkinter as tk

class ProductDetailsWindow(tk.Toplevel):
    def __init__(self, parent, index, image):
        super().__init__(parent)
        self.title(f"Product {index} Details")

        self.image_label = tk.Label(self, image=image)
        self.image_label.pack()

        self.details_label = tk.Label(self, text=f"Details: Product {index} details go here...")
        self.details_label.pack()

        self.back_button = tk.Button(self, text="Back", command=self.destroy)
        self.back_button.pack()
