def main():
    path = './book/frankenstein.txt'
    content = get_book_content(path)
    count_of_words = get_count_of_words(content)
    count_of_each_letter = get_count_of_letters(content)

    print_report(count_of_words, count_of_each_letter)

def get_book_content(path):
    with open(path) as f:
        return f.read()

def get_count_of_words(content):
    return len(content.split())

def get_count_of_letters(content):
    letters_count = {}

    content = content.split()
    for word in content:
        for letter in list(word):
            if letter.isalpha() is False:
                continue

            letter = letter.lower()
            if letter in letters_count:
                letters_count[letter] = letters_count[letter] + 1
                continue

            letters_count[letter] = 1

    return letters_count

def dict_to_list_and_sort_by_quantity(the_dict):
    final_list = []
    for key, value in the_dict.items():
        final_list.append([key, value])
        
    final_list.sort(key=lambda letter: letter[1], reverse=True)
    return final_list

def print_report(count_of_words, count_of_letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_of_words} words found in the document")
    print()
    for letter, quantity in dict_to_list_and_sort_by_quantity(count_of_letters):
        print(f"The '{letter}' character was found {quantity} times")
    print("--- End report ---")

main()