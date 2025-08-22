def get_num_words(text):
    words = text.split()
    count = 0
    for _ in words:
        count = count + 1
    
    return f"{count} words found in the document"