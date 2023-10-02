

import tkinter as tk
from product_details_window import ProductDetailsWindow
from contact_window import ContactWindow
from validation import validate_product_index

class ProductCatalogWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Twisted Tooth Fairy Jewelry Shop")
        
        # Loading images
        self.load_images()

        # Displaying product buttons
        self.display_product_buttons()

        # Contact button to open ContactWindow
        self.contact_button = tk.Button(self, text="Contact Us", command=self.open_contact_window)
        self.contact_button.grid(row=0, column=5)  # Adjust the position as needed

        # Exit button to close the application
        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.grid(row=1, column=5)  # Adjust the position as needed

    def load_images(self):
        """Load product images and use a label to display alternate text if an image cannot be loaded."""
        self.images = []
        for i in range(1, 11):
            try:
                self.images.append(tk.PhotoImage(file=f'images/{i}.png'))
            except tk.TclError:
                alt_text = tk.Label(self, text=f"Image {i} not found")
                alt_text.grid(row=(i-1)//5, column=(i-1)%5)
        
    def display_product_buttons(self):
        """Display buttons for each product."""
        for i, image in enumerate(self.images, 1):
            button = tk.Button(self, image=image, command=lambda i=i: self.show_details(i))
            button.grid(row=(i-1)//5, column=(i-1)%5)  # 5 columns of images

    def show_details(self, index):
        """Open ProductDetailsWindow to show product details."""
        ProductDetailsWindow(self, index, self.images[index - 1])

    def open_contact_window(self):
        """Open ContactWindow to show contact information."""
        ContactWindow(self)
