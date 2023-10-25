import tkinter as tk
from tkinter import messagebox


class StationaryShop:
    def __init__(self):
        self.products = {}
        self.cart = {}
        self.product_file = "products.txt"
        self.username = ""

    def admin_login(self):
        admin_login_window = tk.Toplevel()
        admin_login_window.title("Admin Login")

        username_label = tk.Label(admin_login_window, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(admin_login_window)
        username_entry.pack()

        password_label = tk.Label(admin_login_window, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(admin_login_window, show="*")
        password_entry.pack()

        login_button = tk.Button(admin_login_window, text="Login",
                                 command=lambda: self.admin_menu(admin_login_window))
        login_button.pack()

    def admin_menu(self, admin_login_window):
        admin_login_window.destroy()
        admin_window = tk.Toplevel()
        admin_window.title("Admin Menu")

        # Add Product
        add_product_frame = tk.LabelFrame(admin_window, text="Add Product")
        add_product_frame.pack(padx=20, pady=10)

        product_name_label = tk.Label(add_product_frame, text="Product Name:")
        product_name_label.grid(row=0, column=0, sticky="e")
        product_name_entry = tk.Entry(add_product_frame)
        product_name_entry.grid(row=0, column=1)

        product_price_label = tk.Label(
            add_product_frame, text="Product Price:")
        product_price_label.grid(row=1, column=0, sticky="e")
        product_price_entry = tk.Entry(add_product_frame)
        product_price_entry.grid(row=1, column=1)

        add_product_button = tk.Button(add_product_frame, text="Add", command=lambda: self.add_product(
            product_name_entry.get(), product_price_entry.get()))
        add_product_button.grid(row=2, columnspan=2, pady=10)

        # Delete Product
        delete_product_frame = tk.LabelFrame(
            admin_window, text="Delete Product")
        delete_product_frame.pack(padx=20, pady=10)

        delete_product_label = tk.Label(
            delete_product_frame, text="Product Name:")
        delete_product_label.pack()
        delete_product_entry = tk.Entry(delete_product_frame)
        delete_product_entry.pack()

        delete_product_button = tk.Button(
            delete_product_frame, text="Delete", command=lambda: self.delete_product(delete_product_entry.get()))
        delete_product_button.pack(pady=10)

        # View All Products
        view_products_frame = tk.LabelFrame(
            admin_window, text="View All Products")
        view_products_frame.pack(padx=20, pady=10)

        view_products_button = tk.Button(
            view_products_frame, text="View", command=self.view_all_products)
        view_products_button.pack(pady=10)

        admin_window.mainloop()

    def add_product(self, product_name, product_price):
        if product_name and product_price:
            self.products[product_name] = float(product_price)
            self.save_products_to_file()
            messagebox.showinfo(
                "Success", f"Product '{product_name}' added successfully.")
        else:
            messagebox.showinfo(
                "Invalid Input", "Please enter valid product name and price.")

    def delete_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            self.save_products_to_file()
            messagebox.showinfo(
                "Success", f"Product '{product_name}' deleted successfully.")
        else:
            messagebox.showinfo("Product Not Found",
                                "The selected product is not available.")

    def view_all_products(self):
        if self.products:
            product_list = "\n".join(
                [f"{product}: ${price:.2f}" for product, price in self.products.items()])
            messagebox.showinfo("All Products", product_list)
        else:
            messagebox.showinfo("No Products", "No products found.")

    def user_login(self):
        user_login_window = tk.Toplevel()
        user_login_window.title("User Login")

        username_label = tk.Label(user_login_window, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(user_login_window)
        username_entry.pack()

        password_label = tk.Label(user_login_window, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(user_login_window, show="*")
        password_entry.pack()

        login_button = tk.Button(
            user_login_window, text="Login", command=lambda: self.user_menu(user_login_window, username_entry.get()))
        login_button.pack()

    def user_menu(self, user_login_window, username):
        user_login_window.destroy()
        self.username = username
        user_window = tk.Toplevel()
        user_window.title("User Menu")

        # View All Products
        view_products_frame = tk.LabelFrame(
            user_window, text="View All Products")
        view_products_frame.pack(padx=20, pady=10)

        view_products_button = tk.Button(
            view_products_frame, text="View", command=self.view_all_products)
        view_products_button.pack(pady=10)

        # Add to Cart
        add_to_cart_frame = tk.LabelFrame(user_window, text="Add to Cart")
        add_to_cart_frame.pack(padx=20, pady=10)

        product_name_label = tk.Label(add_to_cart_frame, text="Product Name:")
        product_name_label.grid(row=0, column=0, sticky="e")
        product_name_entry = tk.Entry(add_to_cart_frame)
        product_name_entry.grid(row=0, column=1)

        quantity_label = tk.Label(add_to_cart_frame, text="Quantity:")
        quantity_label.grid(row=1, column=0, sticky="e")
        quantity_entry = tk.Entry(add_to_cart_frame)
        quantity_entry.grid(row=1, column=1)

        add_to_cart_button = tk.Button(add_to_cart_frame, text="Add to Cart", command=lambda: self.add_to_cart(
            product_name_entry.get(), quantity_entry.get()))
        add_to_cart_button.grid(row=2, columnspan=2, pady=10)

        # View Cart
        view_cart_frame = tk.LabelFrame(user_window, text="View Cart")
        view_cart_frame.pack(padx=20, pady=10)

        view_cart_button = tk.Button(
            view_cart_frame, text="View Cart", command=self.view_cart)
        view_cart_button.pack(pady=10)

        # Calculate Total
        calculate_total_frame = tk.LabelFrame(
            user_window, text="Calculate Total")
        calculate_total_frame.pack(padx=20, pady=10)

        calculate_total_button = tk.Button(
            calculate_total_frame, text="Calculate Total", command=self.calculate_total)
        calculate_total_button.pack(pady=10)

        # Generate Bill
        generate_bill_frame = tk.LabelFrame(
            user_window, text="Generate Bill")
        generate_bill_frame.pack(padx=20, pady=10)

        generate_bill_button = tk.Button(
            generate_bill_frame, text="Generate Bill", command=self.generate_bill)
        generate_bill_button.pack(pady=10)

        user_window.mainloop()

    def add_to_cart(self, product_name, quantity):
        if product_name in self.products:
            if product_name in self.cart:
                self.cart[product_name] += int(quantity)
            else:
                self.cart[product_name] = int(quantity)
            messagebox.showinfo(
                "Success", f"{quantity} {product_name}(s) added to cart.")
        else:
            messagebox.showinfo(
                "Product Not Found", "The selected product is not available.")

    def view_cart(self):
        if self.cart:
            cart_items = "\n".join(
                [f"{product}: {quantity}" for product, quantity in self.cart.items()])
            messagebox.showinfo("Cart", cart_items)
        else:
            messagebox.showinfo("Empty Cart", "Your cart is empty.")

    def calculate_total(self):
        if self.cart:
            total = sum([self.products[product] *
                        quantity for product, quantity in self.cart.items()])
            messagebox.showinfo("Total", f"Total amount: ${total:.2f}")
        else:
            messagebox.showinfo("Empty Cart", "Your cart is empty.")

    def generate_bill(self):
        if self.cart:
            total = sum([self.products[product] *
                        quantity for product, quantity in self.cart.items()])

            bill = f"Username: {self.username}\n\n"
            bill += "Product\t\tQuantity\t\tPrice\n"
            bill += "----------------------------------\n"
            for product, quantity in self.cart.items():
                price = self.products[product]
                bill += f"{product}\t\t{quantity}\t\t${price:.2f}\n"

            bill += "----------------------------------\n"
            bill += f"Total:\t\t\t\t${total:.2f}\n"

            # Show bill in message box
            messagebox.showinfo("Bill", bill)

            # Save bill to file
            with open("bill.txt", "w") as file:
                file.write(bill)

            # Save bill data to separate file
            with open("bill_data.txt", "a") as data_file:
                data_file.write(
                    f"{self.username},{','.join([f'{product}:{quantity}' for product, quantity in self.cart.items()])}\n")

            # Clear cart
            self.cart = {}
        else:
            messagebox.showinfo("Empty Cart", "Your cart is empty.")

    def load_products_from_file(self):
        try:
            with open(self.product_file, "r") as file:
                for line in file:
                    product, price = line.strip().split(",")
                    self.products[product] = float(price)
        except FileNotFoundError:
            messagebox.showinfo("File Not Found",
                                "Product file not found. No products loaded.")

    def save_products_to_file(self):
        with open(self.product_file, "w") as file:
            for product, price in self.products.items():
                file.write(f"{product},{price}\n")

    def run(self):
        self.load_products_from_file()

        root = tk.Tk()
        root.title("Stationary Shop")

        admin_button = tk.Button(root, text="Admin Login",
                                 command=self.admin_login)
        admin_button.pack(pady=20)

        user_button = tk.Button(root, text="User Login",
                                command=self.user_login)
        user_button.pack(pady=20)

        root.mainloop()


if __name__ == "__main__":
    shop = StationaryShop()
    shop.run()
