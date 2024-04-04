def main():
    book_path = "github.com/adammikolaj/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    words = len(text.split())
    print(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()