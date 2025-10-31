def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def get_sorted_char_list(char_count):
    sorted_list = []
    for char in char_count:
        sorted_list.append({"char": char, "num": char_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list