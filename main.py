import os

def main():
    base_path = "github.com/adammikolaj/bookbot/books/"
    book_filename = "frankenstein.txt"
    book_path = os.path.join(os.getcwd(), base_path, book_filename)
    text = get_book_text(book_path)
    words = len(text.split())
    l_words = str(text).lower()   
    word_count(l_words)
    print(words)
    

def get_book_text(path):
    """
    Read the content of the file located at the specified path and return it as a string.
    """
    with open(path) as f:
        return f.read()

def word_count(l_words):
    wc = {}
    for w in l_words:  
        if w in wc:
            wc[w] += 1
        else:
            wc[w] = 1
    print(wc)


main()