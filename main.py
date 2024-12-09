def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    if text == "":
        return


    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    sorted_chars = [{'char' : c, 'num' : n} for c, n in chars_dict.items() if c.isalpha()]
    sorted_chars.sort(key=sort_on, reverse=True)

    for entry in sorted_chars:
        character = entry['char']
        count = entry['num']
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")


    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
           if lowered in chars:
            chars[lowered] += 1
           else:
            chars[lowered] = 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)





def get_book_text(book_path):
    try:
        with open(book_path) as f:
            return f.read()
    except FileNotFoundError: 
        print("Error: File not found")
        return ""
    
def sort_on(dict):
    return dict["num"]

   


main()
