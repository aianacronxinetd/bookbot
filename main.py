from stats import *
import sys

def get_book_text(file_path):

    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    str = sys.argv[1]
    word_count = num_of_words(get_book_text(str))
    dct = order_dct(num_of_characters(get_book_text(str)))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in dct:
        for key, value in item.items():
            if key.isalpha():
                print(f"{key}: {value}")
    print("============= END ===============")
