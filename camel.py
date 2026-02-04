# Enter your code here""


uinputcamel = str(input("Enter the name of a variable in camelCase: "))
for letter in uinputcamel:
    if letter.isupper():
        uinputcamel = uinputcamel.replace(letter, "_" + letter.lower())


snakecase = uinputcamel.lower()  

print(snakecase)

## ** Part Six **

# When a number is inputed alongside the regular camelcase input, the output will still contain the number and not throw an error.
# This is because the numbers are recognized as a string and cannot be upper or lower case. Therefore remain unaffected.
# A 'safety critical' version would ensure that the input is checked before any conversion, this check will make sure that there are only letters.
# if there are any numbers and the program would then remove them and only after that will carry on and convert the rest of the input.

## **Edge Case**

# The program may not wok if the input is in another format, or if there are no letters and only numbers.
