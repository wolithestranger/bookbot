def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} in the doc")
    num_dict = char_count_dictionary(text)
    #print(num_dict)
    print("--- Begin report of books/frankenstein.txt --- \n")
    print_report(num_dict)
    print("--- End report ---")
    
   
    
def get_num_words(text):
   words = text.split()
   return len(words)

   
    # words = file_contents.split()
    # no_of_words = len(words)
    # return no_of_words

def get_book_text(path):
   with open(path) as f:
       return f.read()

def char_count_dictionary(text):
    char_dict = {}

    for char in text.lower():
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["val"]

def print_report(char_dictionary):
    dict_list = []

    for key, val in char_dictionary.items():
        if key.isalpha():  # only include letters. Probably uses ascii to parse and check. 
            dict_list.append({'key': key, 'val' : val})

    dict_list.sort(reverse=True, key = sort_on) #key takes in a function. 
        #in this case the function returns for the value for the key
        
    for char_dict in dict_list:
        print(f"The '{char_dict['key']}' character was found {char_dict['val']} times")
        
        
    return

    


main()
#with open('books/frankenstein.txt') as f:
#    file_contents = f.read()








# if __name__ == "__main__":
#     main()

    ###conver the lext to string, have it ammend to a list