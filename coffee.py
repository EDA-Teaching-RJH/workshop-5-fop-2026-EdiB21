#Your code goes here

total_inserted = 0



def main():
    print("Welcome to the Coffee Machine, Coins accepted: 50p, 20p, 10p, 5p")
    print("-------------------------------------")
    print("Price of a coffee is : 75p")
    print("-------------------------------------")

    customer_input()



def customer_input():
    global total_inserted

    while total_inserted < 75:
        coins = int(input("Insert Coins: "))

        if coins in [50, 20, 10, 5]:
            total_inserted += coins
            print(f"Total inserted: {total_inserted}p")
            print("-------------------------------------")
            if total_inserted >= 75:
                change_calculator()
        else:
            print("Invalid coin. Please insert from the above.")

    
def change_calculator():
    global total_inserted

    if total_inserted > 75:
        change  = total_inserted - 75
        print("-------------------------------------")
        print(f"Your change is : {change}p")
        print("Enjoy your coffee!")
        print("-------------------------------------")

    else:
        print("-------------------------------------")
        print("No change to return.")
        print("Enjoy your coffee!")
        print("-------------------------------------")


main()




