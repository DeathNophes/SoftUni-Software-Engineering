from PIL import ImageTk, Image
from helpers import clean_screen
from json import load, dump
from canvas import frame, root
from tkinter import Button
import os

products_path = os.path.join('db', 'products.json')


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open(products_path, 'r') as stock:
        info = load(stock)

    x, y = 120, 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info['image']))
        images.append(item_img)
        # keeping the reference to the image so tkinter doesn't delete it after function ends

        frame.create_text(x, y, text=item_name, font=('Comic Sans MS', 13))
        frame.create_image(x, y + 80, image=item_img)

        if item_info['quantity'] > 0:
            color = 'green'
            text = f"In stock: {item_info['quantity']}"

            item_button = Button(
                root,
                text='Buy',
                bg='green',
                fg='white',
                font=('Comic Sans MS', 12),
                width=5,
                command=lambda a=item_name, b=info: buy_product(a, b)
            )

            frame.create_window(x, y + 205, window=item_button)

        else:
            color = 'red'
            text = 'Out of stock'

        frame.create_text(x, y + 170, text=text, fill=color, font=('Comic Sans MS', 8))

        x += 200

        if x >= 550:
            y += 300
            x = 150


def buy_product(product_name, info):
    info[product_name]['quantity'] -= 1

    with open(products_path, 'w') as stock:
        dump(info, stock)

    display_products()
    print(f"You bought a {product_name}")


images = []