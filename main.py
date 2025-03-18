from stats import get_num_words, character_count, sorted_dics
import sys

if len(sys.argv) < 2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path, "r") as f:
       return f.read()

def main():
    file = get_book_text(sys.argv[1])
    dictionaty_chars = character_count(file)
    # print(get_num_words(file))
    sorted_dics(dictionaty_chars)


if __name__ == "__main__":
    main()

