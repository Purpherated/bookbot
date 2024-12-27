def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    char_list = get_char_list(chars_dict)
    ordered_list = sort_list(char_list)
   
    print("calculating...")
    print(f"{num_words} words found")
    for dict_item in ordered_list:
        character = dict_item["char"]
        number = dict_item["count"]
        print(f"the character '{character}' appears '{number}' times")

    print("report complete")


    



def sort_list(char_list):
    char_list.sort(reverse=True,key=sort_on)
    return char_list

def sort_on(dict):
    return dict["count"]

def get_char_list(chars_dict):
    char_listed = []
    for char , count in chars_dict.items():
        char_listed.append({"char": char, "count": count})
    return char_listed


def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else: 
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
