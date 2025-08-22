def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    return char_count

def sort_on(item):
    return item["num"]

def get_sorted_char_list(char_count):
    char_list = []
    for char in char_count:
        char_list.append({"char": char, "num": char_count[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list