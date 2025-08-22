from stats import get_num_words, get_char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    char_count = get_char_count(book_text)

    print(book_text)
    print(num_words)
    print(char_count)

main()