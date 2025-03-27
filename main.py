import sys

from stats import count_words
from stats import count_characters
from stats import sort_function

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

PATH = sys.argv[1]

def main():
    
    def get_block_text(file_path):

        with open(file_path) as f:
            file_content = f.read()
            return file_content
    
    text = get_block_text(PATH)
    number = count_words(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    
    char_num = count_characters(text)
    end_result = sort_function(char_num)
    
    for n in end_result:
        if str(n["name"]).isalpha():
            print(f"{n["name"]}: {n["count"]}")
   
    
if __name__ == "__main__":
    main()