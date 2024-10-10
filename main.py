def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char_count = {k: v for k, v in sorted(char_count.items(), key=lambda item: item[1], reverse=True)}
    print(f"--- Begin of report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for k in sorted_char_count:
        if k.isalpha():
            print(f"The '{k}' character was found {sorted_char_count[k]} times.")
    print("-- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(string):
    return len(string.split())

def get_char_count(string):
    lowered_string = string.lower();
    char_count_dict = {}
    for char in lowered_string:
        if char not in char_count_dict:
            char_count_dict[char] = 0
        char_count_dict[char] += 1
    return char_count_dict

main()
