import re

try:
    # 1. Accept a paragraph from the user
    paragraph = input("Enter a paragraph to analyze:\n").strip()

    if not paragraph:
        print("The input was empty. Please provide some text.")
    else:
        lowercase_text = paragraph.lower()

        clean_text = re.sub(r"[^\w\s]", "", lowercase_text)

        words = clean_text.split()

        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        sorted_words = sorted(
            word_counts.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        print("\n--- Top 10 Most Common Words ---")
        for word, count in sorted_words[:10]:
            print(f"'{word}': {count} times")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
