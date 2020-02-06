import colorama
from colorama import Fore, Back, Style

if __name__ == "__main__":
    start()
    colorama.init()

sold = []


def start(items):
    db_items = items

    exit = False
    while not exit:
        print("+++++++++++++++SalesManadger+++++++++++++++++++++++++++++")
        choise = int(input(
            " 1. add item\n 2. delete item\n 3. sort by price\n 4. sell item\n 5. sell statictics\n 6. show items\n 0. exit\n"))
        print("User choise", choise)
        if choise == 1:
            add_items(db_items)

        elif choise == 2:
            delete_items(db_items)
            show_items(db_items)
        elif choise == 3:
            sort_items(db_items)
            db_items = sort_items(items)
            show_items(db_items)
        elif choise == 4:
            sell_items(db_items)
           # sold.append(sell_items(items))
        elif choise == 5:
            sell_stat(sold)
        elif choise == 6:
            show_items(db_items)
        elif choise == 0:
            exit = True
        else:
            print("read manual")


def add_items(items):
    name = input("Enter vendor phone\n")
    model = input("Enter model phone\n")
    price = input("Enter price phone\n")
    items.append({"name": name, "model": model, "price": price})


def delete_items(items):
    counter = 1
    for item in items:
        print("------#", counter, "--------", "\n|| Vendor- ",
              item["name"], "\n|| Model - ", item["model"], "\n|| Price - ", item["price"], "\n-----------------")
        counter += 1
    choise_del = input("Enter number for delete")
    try:
        choise_del = int(choise_del)
        return items.pop(choise_del-1)
    except:
        print("Make your choice. Enter number integer")


def sort_items(items):
    item_sort = sorted(items, key=lambda x: x['price'])
    return item_sort


def sell_items(items):
    counter = 1
    for item in items:
        print("------#", counter, "--------", "\n|| Vendor- ",
              item["name"], "\n|| Model - ", item["model"], "\n|| Price - ", item["price"], "\n-----------------")
        counter += 1
    choise_sell = input("Enter number sell phone")
    try:
        choise_sell = int(choise_sell)
        sel = items.pop(choise_sell-1)
        return sold.append(sel)
    except:
        print("Make your choice. Enter number integer")
    


def sell_stat(sold):
    print("----Sold phone----")
    for item in sold:
        print("-----------------", "\n|| Vendor- ",
              item["name"], "\n|| Model - ", item["model"], "\n|| Price - ", item["price"], "\n-----------------")
        sum = item["price"]
        print(sum)
    # sum1 = sum(item["price"] for item in sold)
    # print("Daily revenue: ", sum1, "UA grn")


def show_items(items):

    for item in items:
        print("-----------------", "\n|| Vendor- ",
              item["name"], "\n|| Model - ", item["model"], "\n|| Price - ", item["price"], "\n-----------------")
    # sum1 = sum(item["price"] for item in items)
    # print(Fore.RED + "Total cost: ", sum1, "UA grn")
    # print(Style.RESET_ALL)
