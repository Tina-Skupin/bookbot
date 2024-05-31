def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print ("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print ()
    Buchstabensuppe = get_grundliste(text)
    letter_counts_list1 = get_letter_counts(Buchstabensuppe)
    dictionary_list = list_of_dictionaries(letter_counts_list1)


    # Sort the list of dictionaries
    dictionary_list.sort(reverse=True, key=sort_on)

    for item in dictionary_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    #print(f"The {char} character was found {num} times in the document")
    print ("--- End report ---")
    # Print the sorted list
    #print(dictionary_list)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_grundliste(text):
    grossliste = list(text)
    grundliste = []
    for buchstabe in grossliste:
        kleinbuchstabe = buchstabe.lower()
        grundliste.append(kleinbuchstabe)
    return grundliste

def get_letter_counts(grundliste):
    letter_dict = {}
    get_grundliste
    for buchstabe in grundliste:
        if buchstabe in letter_dict:
            letter_dict[buchstabe]+= 1
        else:
            letter_dict[buchstabe] = 1
    return letter_dict


#copying the code from one_step_trash

def sort_on(item):
    return item["num"]

def list_of_dictionaries(letter_counts_list1):
    char_counts_list = []
    for char, count in letter_counts_list1.items():
            if char.isalpha():
                char_counts_list.append({"char": char, "num": count})
    return char_counts_list



main()