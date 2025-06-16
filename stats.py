def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_char_counts(char_dict):
    char_list = [{"char": char, "num": count} for char, count in char_dict.items() if char.isalpha()]
    
    def sort_on(item):
        return item["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list