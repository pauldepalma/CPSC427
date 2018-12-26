'''
Demonstrates:
    list comprehension
    dictionary
    use of dictionary as frequency counter
'''


import re

'''
pre: string is a string
post: returns a string containing all characters in string_in that are also
    in good_chars, namely lower case alphabetic characters and spaces
'''
def tokenize(string_in):

    string = re.sub('\n',' ', string_in)
     #create a list containing all lower case characters
    good_chars = [chr(value) for value in range(ord('a'),ord('z') + 1,1)]
    good_chars.append(' ')
    string = string.lower()
    new_str = ''
    for ch in string:
        if ch in good_chars:
            new_str = new_str + ch
    return new_str

'''
pre: string_in is a string
post: returns a dictionary where the key is an element of string_in and the
    value is the number of times it appears in string_in
'''
def freq_table(string_in):
    count_dict = {}
    word_lst = string_in.split()
    for word in word_lst:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
    return count_dict
'''
pre: count_dict is the dictionary created in the function freq_table
post: writes the the key/value pairs of count_dict to a file
'''
def display_freq(count_dict,fout):
    word_lst = list(count_dict.keys())
    word_lst.sort()
    fout.write("CHARACTER  FREQUENCY\n")
    for word in word_lst:
        fout.write(word + '\t\t' + str(count_dict[word]) + '\n')
'''
pre: none
post: input and output files are opened and references returned
'''
def my_open():
    while(True):
        file_in = raw_input('Enter an input file name\n')
        try:
            fin = open(file_in, 'r')
            break
        except:
            print("Invalid file name, Try again")
    file_out = raw_input('Enter an output file name\n')
    fout = open(file_out, 'w')
    return fin, fout

def main():
    fin, fout = my_open()
    contents_raw = fin.read()
    contents_cooked = tokenize(contents_raw)
    count_dict = freq_table(contents_cooked)
    display_freq(count_dict, fout)
    
    fin.close()
    fout.close()
    
    
main()
    
