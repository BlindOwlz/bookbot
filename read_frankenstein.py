def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    word_count  = count_words(file_contents)
    print(f"there are {word_count} words in frankenstein.txt")

def count_words(text):
    return len(text.split())
if __name__ == "__main__":
    main()