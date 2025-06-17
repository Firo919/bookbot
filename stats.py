def get_book_text(file_path):
    with open(file_path) as book:
        text = book.read()
        return text

def get_book_words(file_path):
    with open(file_path) as book:
        text = book.read()
        words = text.split()
        return len(words)

def get_num_char(file_path):
    text = get_book_text(file_path)
    text = text.lower()
    dict = {}
    for char in text:
        if char not in dict:
            dict[char] = 0
        dict[char] += 1
    return dict