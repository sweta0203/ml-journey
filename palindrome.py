import re

try:
    # taking input form the user
    main_text = input("Enter your string for checking palindrome").strip()
    main_text = main_text.lower()
    # removing all the unwanted punctuations
    main_text = re.sub(r"\W+", "", main_text)
    # checking if the user just provided random symbol
    if not main_text:
        print("Enter  a valid string for checking")
    checking_text = main_text[::-1]
    if checking_text == main_text:
        print(f"{main_text} is a palindrome!")
    else:
        print(f"{main_text} is NOT a palindrome.")

except Exception as e:
    # Catch any unexpected system or runtime errors
    print(f"An unexpected error occurred: {e}")
