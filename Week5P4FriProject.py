# creating a shopping cart
from IPython.display import clear_output

cart = []


# create function to add items in cart
def addItem(item):
    clear_output()
    cart.append(item)
    print("{} has been added.".format(item))


# removing items
def removeItems(item):
    clear_output()
    try:
        cart.remove(item)
        print("{} has been removed.".format(item))
    except:
        print("sorry we couldn't remove that item.")


# showing the cart
def showCart():
    clear_output()
    if cart:
        print("here is your cart")
        for item in cart:
            print("- {}".format(item))
    else:
        print("your cart is empty")


# clearing the cart
def clearCart():
    clear_output()
    cart.clear()
    print("your cart is empty")


# creating main loop
def main():
    done = False
    while not done:
        ans = input("quit/add/remove/show/clear: ").lower()
        if ans == "quit":
            print("Thanks for using our program.")
            showCart()
            done = True

            # handling user input
        elif ans == "add":
            item = input("what would yiu like to add? ").title()
            addItem(item)
        elif ans == "remove":
            item = input("What item would you like to remove? ").title()
            removeItems(item)
        elif ans == "show":
            showCart()
        elif ans == "clear":
            clearCart()
        else:
            print("Sorry that was not an option.")


main()  # run the program




