#Your code goes here

##  **Statement of Requirements**

# **FUNCTIONAL REQUIREMENTS**
# 1. The program will only accept coins of value : 50p, 20p, 10p and 5p.
# 2. The price of a coffee will be fixed to 75p.
# 3. It will follow a simple addition method for the total inputed from the user
# 4. It will caulculate the change through subtraction of inputed amount and price of coffee.

# **NON-FUNCTIONAL REQUIREMENTS**
# 1. The program will only accept integer values.
# 2. The program will display correct messages incase of ivalid entry.

# **RELIABILTY REQUIREMENTS**
# 1. The program must be able to handle invalid string inputs without crashing.







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
        coins = input("Insert Coins: ")
        try:
            coins = int(coins)
        except ValueError:
            print("Invalid input. Please insert integer values only.")
            continue


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




