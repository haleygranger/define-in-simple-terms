import os

fancy_words = []
# Load 1000 words into a set from outside txt file
def create_top_words():
    with open("top-words.txt", 'r') as file:
        return set(word.strip().lower() for word in file.readlines())

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
    

def main():
    # Create words
    top_words = create_top_words()

    # Clear screen to give clean interface
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print("Enter term (or type 'exit' to quit).")
        term = input(">>> ")

        if term.lower() == 'exit':
            break
        
        print("Enter definition for " + term + ".")
        definition = input(">>> ")

        # Filter words
        if filter_words(definition, top_words) is False:
            print("The following words should not be used:")
            for word in fancy_words:
                print(word)
        else:
            print("This is your definition:\n" + term + ": " + definition)

if __name__ == "__main__":
    main()