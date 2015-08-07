import string

"""
Content Indexing Engine Capstone Project

You have a bunch of files in the file system!  How can we index these files to make them easily searchable by keyword?

Indexing is a way of moving work 'upfront' so that when the user searches, less work is needed to get them the right search results.

Tips:

Look into array .extend() method
Look into string module , and .punctuation
Look into the set() builtin data type

Example index:
index = {'cat':['filename1','filename2','filename3'],'dog':['filename2',filename3]}

"""
import os, string

#Tip: upgrade your recursive find code from a previous exercise to return a list of files 

# Finds all files within the current folder. Returns an array of filenames
def recursive_find(dirname,array):
    for content in os.listdir(dirname):
        full_path = os.path.join(dirname, content)
        if os.path.isdir(full_path) == True:
            recursive_find(full_path,array)
        else:
            array.append(full_path)
    return array

stop_words = ['a','an','and','i']

def read_data(filename):
    with open(filename,"r") as f:
        return f.read().lower()

def strip_punctuation(token):
    """strip out punctuation from a token"""
    return token.translate(None, string.punctuation)

# Takes a string, splits it into an array and removes Stop Words. Returns an array
def index_file(content):
    words = set(strip_punctuation(content).split())
    for word in words.copy():
        if word in stop_words:
            words.remove(word)
    return words
        
def add_to_index(words,filename,index):
    """takes a set of words for a filename and adds it to the index"""
    for word in words:
        if word in index:
            index[word].append(filename)
        else:
            index[word] = [filename]
    return index

def index_all_files(file_list,index):
    """go through the list of files and add a file's words to the index"""
    for filename in file_list:
        # Reads the file content, strips punctuation and stop words as an array; then sends the array to add_to_index
        add_to_index(index_file(read_data(filename)),filename,index)
    return index

def find_files_with(index,keywords):
    """takes a list of keywords, and return a list of files with those keywords"""
    not_found = []
    for word in keywords:
        if word in index:
            print "Keyword: %s\nLocation: %s" % (word, ', '.join(index[word]))
        else:
            not_found.append(word)
    if not_found:
        print "\nI could not find these words: %s" % ', '.join(not_found)
        
def ui_loop():
    print "Give me a second while I index the files..."
    index = index_all_files(recursive_find("./test",[]),{})

    keywords = raw_input("What words would you like to search for?: ").lower()
    # Calls find_files_with specifying the index and the keywords in an array without punctuation and stop words
    find_files_with(index,index_file(strip_punctuation(keywords)))

ui_loop()


