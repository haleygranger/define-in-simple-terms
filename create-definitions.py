import os
import string

fancy_words = []
filename = "saved_definitions.txt"
symbols = symbols = string.punctuation
bad_symbols = []
# Load 1000 words into a set from outside txt file
def create_top_words():
    with open("top-words.txt", 'r') as file:
        return set(word.strip().lower() for word in file.readlines())
    
def remove_punctuation(definition):
    return ''.join([char for char in definition if char not in symbols])

# Split definition
def filter_words(definition, top_words):
    words = definition.split()
    fancy_words.clear()

    for word in words:
        if word.lower() not in top_words:
            fancy_words.append(word)
    # Keep track if a "fancy" word is used
    if len(fancy_words) > 0:
        return False
    else:
        return True
    
def save_to_file(term, definition):
    with open(filename, 'a') as file: # Opening in append
        file.write(term + " - " + definition + "\n")
        return True
    
def validate_not_empty(text):
    return not text.strip()

def validate_word_count(definition, min_words=3, max_words=100):
    word_count = len(definition.split())
    if word_count < min_words:
        return False
    if word_count > max_words:
        return False
    else:
        return True

def validate_duplicates(term):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            if term in file.read():
                return True
    return False

def main():
    # Create words
    top_words = create_top_words()

    # Clear screen to give clean interface
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print("\nEnter term (or type 'exit' to quit).")
        term = input(">>> ")

        if term.lower() == 'exit':
            break
        
        print("Enter definition for " + term + ".")
        definition = input(">>> ")

        # VALIDATION
        if validate_not_empty(definition):
            print("Definition cannot be empty.")
            continue

        if not validate_word_count(definition):
            print("Definition cannot be greater than 100 words and less than 3.")
            continue
        
        # Remove punctuation
        definition = remove_punctuation(definition)
        ##for word in definition:
            ##print(word)

        # Filter words
        if filter_words(definition, top_words) is False:
            print("\nThe following words should not be used:")
            for word in fancy_words:
                print(word)
        else:
            print("\nThis is your definition:\n" + term + ": " + definition)
            print("Save? (y/n)")
            ans = input(">>> ")

            # if the definition is a good one you can save it
            if ans is 'y':
                save_to_file(term, definition)
                # Check if term already exists
                if validate_duplicates(term):
                    print("Term already exists.")
                    continue

if __name__ == "__main__":
    main()