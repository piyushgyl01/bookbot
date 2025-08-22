import sys
from stats import get_num_words, get_char_count, get_sorted_char_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_char_list = get_sorted_char_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char_list:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()