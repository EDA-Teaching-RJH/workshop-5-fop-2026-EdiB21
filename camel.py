# Enter your code here""


uinputcamel = str(input("Enter the name of a variable in camelCase: "))
for letter in uinputcamel:
    if letter.isupper():
        uinputcamel = uinputcamel.replace(letter, "_" + letter.lower())


snakecase = uinputcamel.lower()  

print(snakecase)
