def get_num_words(text):
    words = text.split()
    count = 0
    for _ in words:
        count += 1
    
    return f"{count} words found in the document"

def get_char_count(book_text):
    char_count_dict = {}
    words_arr = book_text.lower().split()

    for word in words_arr:
        for char in word:
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1

    return char_count_dict
