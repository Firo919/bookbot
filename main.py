from stats import get_book_text
from stats import get_book_words
from stats import get_num_char

def main():
    print(f"{get_book_words("books/frankenstein.txt")} words found in the document")
    print(get_num_char("books/frankenstein.txt"))

main()