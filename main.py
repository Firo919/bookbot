from stats import get_book_text
from stats import get_book_words
from stats import get_num_char
from stats import sorted_list_char


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python 3 main.py <path_to_book>")
        sys.exit(1) 
    func, path = sys.argv
    print(f"= Bookbot = \nAnalyzing book found at {path}")
    print("= Word Count =")
    print(f"Found {get_book_words(path)} total words")
    print("= Character Count =")
    list = sorted_list_char(path)
    for elem in list:
        print(f"{elem["char"]}: {elem["num"]}")
    print("= End =")

main()