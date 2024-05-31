def main():
    
    #test funzt setup 
    #print ("test")
       
    char_counts = {'p': 6121, 'r': 20818, 'o': 25225, 'j': 504, 'e': 46043, 'c': 9243, 't': 30365, ' ': 74144, 'g': 5974, 'u': 10407, 'n': 24367, 'b': 5026, "'": 229, 's': 21155, 'f': 8731, 'a': 26743, 'k': 1755, 'i': 24613, ',': 5097, 'y': 7914, 'm': 10604, 'w': 7638, 'l': 12739, '(': 39, 'd': 16863, ')': 39, 'h': 19725, '\n': 7651, 'v': 3833, '.': 3124, '-': 445, ':': 68, '1': 92, '7': 23, '2': 24, '0': 21, '8': 20, '[': 4, '#': 1, '4': 17, ']': 4, '*': 28, 'z': 243, '?': 220, ';': 970, 'x': 677, 'q': 324, '!': 239, '"': 796, '3': 18, '5': 16, '9': 13, '6': 10, '_': 2, '/': 24, '%': 1, '@': 2, '$': 2}
    dictionary_list = list_of_dictionaries(char_counts)


    # Sort the list of dictionaries
    dictionary_list.sort(reverse=True, key=sort_on)

    # Print the sorted list
    print(dictionary_list)

def sort_on(item):
    return item["num"]

def list_of_dictionaries(char_counts):
    char_counts_list = []
    for char, count in char_counts.items():
            if char.isalpha():
                char_counts_list.append({"char": char, "num": count})
    return char_counts_list

#returns only letters, in right order already

main()