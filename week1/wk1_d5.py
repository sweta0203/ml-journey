"""
===============================================================================
                          REGEX (REGULAR EXPRESSIONS) CHEAT SHEET
===============================================================================

SYMBOL      MEANING
-------------------------------------------------------------------------------
.           Any character (except newline)
\d          Digit [0-9]
\D          Not a digit
\w          Word character (Letter, digit, underscore) [a-zA-Z0-9_]
\W          Not a word character
\s          Whitespace (space, tab, newline)
\S          Not whitespace
+           Quantifier: One or more
* Quantifier: Zero or more
?           Quantifier: Zero or one (optional)
^           Anchor: Start of string
$           Anchor: End of string
[abc]       Character class: Matches a, b, or c
[^abc]      Negated character class: Matches any character except a, b, or c


===============================================================================
                      CORE PYTHON 're' MODULE FUNCTIONS
===============================================================================

1. re.search(pattern, string)
   - Scans through the entire string looking for the FIRST match.
   - Returns a match object if found, or None if no match exists.
   - Best for: Checking if a pattern exists anywhere in a line.

2. re.match(pattern, string)
   - Checks for a match ONLY at the beginning of the string.
   - Returns a match object if the start matches, or None.
   - Best for: Strict validation (e.g., ensuring a line starts with a ID).

3. re.findall(pattern, string)
   - Scans the entire string and returns ALL non-overlapping matches.
   - Returns a list of strings (or a list of tuples if groups are used).
   - Best for: Extracting multiple data points (e.g., grabbing all emails).

4. re.sub(pattern, replacement, string)
   - Searches for the pattern and replaces it with the replacement string.
   - Returns the modified string.
   - Best for: Data cleaning and find-and-replace tasks.

===============================================================================
"""

import re

# Quick Examples for reference:
text = "The price is $45 dollars."

# re.search() -> Finds '45' anywhere
if re.search(r"\d+", text):
    print("Found a number!")

# re.sub() -> Replaces digits with 'X'
cleaned_text = re.sub(r"\d+", "XX", text)
print(cleaned_text)  # "The price is $XX dollars."

sample = "apple 123 banana 456 cherry"

# 1. re.match()
# Looking for digits at the START. (Fails because 'apple' is first)
print(re.match(r"\d+", sample))
# Output: None

# 2. re.findall()
# Looks everywhere and extracts all digit groups.
print(re.findall(r"\d+", sample))
# Output: ['123', '456']

# 3. re.split()
# Uses the digits as the cutting points to split the text.
print(re.split(r"\d+", sample))
# Output: ['apple ', ' banana ', ' cherry']


# The parenthesis separates the username and the domain
match = re.search(r"(.+)@(.+)", "user@example.com")
if match:
    print(match.group(1))  # Outputs: user
    print(match.group(2))  # Outputs: example.com


# --- 1. Basics & Immutability ---

name = "Alice"
city = "Kathmandu"
sentence = "Python is awesome!"

# Strings are immutable. Modifying an index directly will raise a TypeError:
# name[0] = "b"


# --- 2. Slicing & Basic Operations ---
text = "Programming"

print(text[0:7])  # Output: Program (Slices from index 0 to 6)
print(text[::-1])  # Output: gnimmargorP (Reverses the string)

# Raw strings (r"...") ignore escape characters like \u or \t
path = r"c:\Users\sweta\OneDrive\Desktop\ml\tempCodeRunnerFile.py"
print(path)

print("Hi " * 3)  # Output: Hi Hi Hi (String multiplication)


# --- 3. Case Modification ---
text2 = "PyTHon oNE Two"

print(text.upper())  # Output: PROGRAMMING
print(text2.lower())  # Output: python one two
print("hello world".title())  # Output: Hello World
print("python".capitalize())  # Output: Python
print(text2.swapcase())  # Output: pYthON One tWO (Inverts casing)


# --- 4. Stripping Whitespace ---
print(" Python ".strip())  # Output: "Python"  (Removes both sides)
print(" Python ".lstrip())  # Output: "Python " (Removes left side)
print(" Python ".rstrip())  # Output: " Python" (Removes right side)


# --- 5. Searching, Counting & Replacing ---
# Replace substrings
print(text2.replace("Two", "hi"))  # Output: PyTHon oNE hi

# .find() returns the start index if found, and -1 if not found
print(text2.find("oNE"))  # Output: 7
print(text2.find("one"))  # Output: -1 (Case-sensitive!)

# .index() behaves like .find(), but raises a ValueError if not found
# print(text2.index('two'))        # Error: substring not found

print(text2.count("a"))  # Output: 0 (Counts occurrences)
print(text2.startswith("p"))  # Output: False
print(text2.endswith("h"))  # Output: False


# --- 6. Splitting, Joining & Padding ---
sentence = "Python is fun"

# Split string into a list of words
words = sentence.split()
print(words)  # Output: ['Python', 'is', 'fun']

# Join a list of strings back into a single string
print(" ".join(words))  # Output: Python is fun

# Alignment and padding
print("Python".center(60))  # Centers "Python" in a 60-character block
print("25".zfill(5))  # Output: 00025 (Pads with zeros)


# --- 7. Character Validation (Booleans) ---
# Note: Parentheses () are required to execute these methods
print("Python".isalpha())  # Output: True  (Only letters)
print("123".isdigit())  # Output: True  (Only digits)
print("hi12".isalnum())  # Output: True  (Only alphanumeric)
print("hi12".isspace())
