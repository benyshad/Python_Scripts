
def main():
    restaurant()

def restaurant():
    total = order("Item: ")

def order(prompt):
    total = 0

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True:
        try:
            selction = input(prompt).capitalize()
            total = total + menu[selction]
        except EOFError:
            print(f"\n")
            break
        except KeyError:
            print("Sorry that is not on the menue")
        else:
            print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()