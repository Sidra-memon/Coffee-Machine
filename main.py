import tkinter
from tkinter import *

# Create the main window
window = tkinter.Tk()
window.geometry("700x600")
# set maximum window size value
window.maxsize(700, 600)
window.configure(bg="beige")


# Load the images
splash_image = PhotoImage(file='splash.png')
espresso_image = PhotoImage(file='espresso.png')
latte_image = PhotoImage(file='latte.png')
cappucino_image = PhotoImage(file='cappucino.png')

# Create and place the labels with images
# main title
label8 = Label(window, text="COFFEE SHOP",font="times 28 bold",bg="beige")
label8.place(x=350, y=20, anchor="center")
# my_label = tkinter.Label(text = "COFFEE SHOP", font=("Arial", 35, "bold"),bg="beige")
# my_label.grid(column=1, row= 0)
restruant_name = tkinter.Label(image=splash_image, bg="beige")
restruant_name.grid(column =, row= 0)
# restruant_info= Label(text="COFFEE SHOP",font=("Times New Roman",70,"bold italic"),bg="beige",compound='top')
# restruant_info.place(x=5, y=10)

# Functions to increase and decrease quantity
def increase_quantity(label):
    current_quantity = int(label['text'])
    label.config(text=str(current_quantity + 1))

def decrease_quantity(label):
    current_quantity = int(label['text'])
    if current_quantity > 0:
        label.config(text=str(current_quantity - 1))

# Espresso
espresso_label = Label(image=espresso_image, bg="beige")
espresso_label.place(x=200, y=150)
espresso_info = Label(text="Espresso\n$1.5", font=("Times New Roman",30,"bold"), bg="beige")
espresso_info.place(x=5, y=150)
# my_button = Button(window, state=ACTIVE, text="Espresso", font=("Times New Roman",30,"bold"), borderwidth=5, padx=5, pady=5)
# my_button.place(x=200, y=530)

# Quantity controls for Espresso
espresso_minus_button = Button(window, text="-", command=lambda: decrease_quantity(espresso_quantity_label), width=2, height=1)
espresso_minus_button.place(x=200, y=580)
espresso_quantity_label = Label(window, text="0", width=2, height=1, bg="white")
espresso_quantity_label.place(x=240, y=580)
espresso_plus_button = Button(window, text="+", command=lambda: increase_quantity(espresso_quantity_label), width=2, height=1)
espresso_plus_button.place(x=280, y=580)

# Latte
latte_label = Label(image=latte_image, bg="beige")
latte_label.place(x=535, y=300)
latte_info = Label(text="Latte\n$2.5", font=("Times New Roman",30,"bold"), bg="beige")
latte_info.place(x=600, y=530)
# my_button = Button(window, state=ACTIVE, text="Order now", font=("Times New Roman",20,"bold"), borderwidth=5, width=10, height=1)
# my_button.place(x=500, y=610)

# Quantity controls for Latte
latte_minus_button = Button(window, text="-", command=lambda: decrease_quantity(latte_quantity_label), width=2, height=1)
latte_minus_button.place(x=535, y=580)
latte_quantity_label = Label(window, text="0", width=2, height=1, bg="white")
latte_quantity_label.place(x=575, y=580)
latte_plus_button = Button(window, text="+", command=lambda: increase_quantity(latte_quantity_label), width=2, height=1)
latte_plus_button.place(x=615, y=580)

# Cappucino
cappucino_label = Label(image=cappucino_image, bg="beige")
cappucino_label.place(x=900, y=300)
# my_button = Button(window, state=ACTIVE, text="Cappucino", font=("Times New Roman",30,"bold"), borderwidth=5, padx=5, pady=5)
# my_button.place(x=900, y=530)

# Quantity controls for Cappucino
cappucino_minus_button = Button(window, text="-", command=lambda: decrease_quantity(cappucino_quantity_label), width=2, height=1)
cappucino_minus_button.place(x=900, y=580)
cappucino_quantity_label = Label(window, text="0", width=2, height=1, bg="white")
cappucino_quantity_label.place(x=940, y=580)
cappucino_plus_button = Button(window, text="+", command=lambda: increase_quantity(cappucino_quantity_label), width=2, height=1)
cappucino_plus_button.place(x=980, y=580)

# Start the main event loop
window.mainloop()