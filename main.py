import os

def main():
    base_path = "github.com/adammikolaj/bookbot/books/"
    book_filename = "frankenstein.txt"
    book_path = os.path.join(os.getcwd(), base_path, book_filename)
    text = get_book_text(book_path)
    words = len(text.split())
    print(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()