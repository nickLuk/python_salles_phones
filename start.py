import colorama
from colorama import Fore, Back, Style
from salles import start
colorama.init()
phones = [
    {
    "name": "Samsung", 
    "model": "S9",
    "price":12600
    },
    {
    "name": "Meizu", 
    "model": "X8",
    "price":4800
    },
     {
    "name": "Nokia", 
    "model": "3.1",
    "price":3000
    },
    {
    "name": "Apple", 
    "model": "Iphone11",
    "price":23000
    },
    {
    "name": "Asus", 
    "model": "5z",
    "price":7999
    }
]

#for item  in tovar:
 #   print(item["name"], "-", item["model"], "-", item["price"])

start(phones)
