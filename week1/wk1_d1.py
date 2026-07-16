name = input("Please enter your name: ")
print("Hello, " + name + "! Welcome to the program.")

# formatting string
print(f"hello, {name}! This is a formatted string.")
# stripping whitespace
name = name.strip()
print(f"hello, {name}! This is a formatted string after stripping whitespace.")
# capitalize,title,upper
name = name.title()
print(f"hello, {name}! This is a formatted string after title case.")

name = input("Please enter your name again: ").strip().title()
print(
    f"hello, {name}! This is a formatted string after stripping whitespace and title case."
)
# split
fname, lname = name.split(" ")
print(f"First name: {fname}, Last name: {lname}")
# round(number[, ndigits])
# f"msdnj {z:,}"
a = 10000000
print(f"Formatted number with commas: {a:,}")


def function_example():
    print("This is an example function.")


print("Calling the function:")
function_example()


def main():
    print("This is the main function.")
    calc(10, 20)


def calc(x=5, y=1):  # default values
    print(x + y)


main()
