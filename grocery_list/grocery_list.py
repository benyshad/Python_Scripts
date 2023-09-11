
def main():
    grocery()

def grocery():
    grocery_list = cart()
    grocery_list_keys = sorted(grocery_list)
    print_grocery(grocery_list, grocery_list_keys)

def cart():
    grocery_list = {}
    while True:
        try:
            newItem = input("Add Item to Grocery List: ").capitalize()
            if newItem in grocery_list.keys():
                grocery_list.update({newItem: grocery_list[newItem] + 1})
            else:
                grocery_list.update({newItem: 1})
        except EOFError:
            return grocery_list

def print_grocery(grocery_list, grocery_list_keys):
    print("\n")
    for item in grocery_list_keys:
        print(grocery_list[item], item)

if __name__ == "__main__":
    main()