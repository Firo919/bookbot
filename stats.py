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

def sort_on(item):
    return item["num"]

def sorted_list_char(file_path):
    dict = get_num_char(file_path)
    list = []
    for entry in dict:
        if entry.isalpha():
            list_dict = {"char": entry, "num": dict[entry]}
            list.append(list_dict)
    list.sort(key = sort_on, reverse = True)
    return list
