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
        if word not in top_words:
            fancy_words.append(word)
    # Keep track if a "fancy" word is used
    if len(fancy_words) > 0:
        return False
    else:
        return True
    

def main():
    # Create words
    top_words = create_top_words()

    term = "Programming"
    definition = "process of writing explicit instruction for a computer to follow"

    if filter_words(definition, top_words) is False:
        print("The following words should not be used:")
        for word in fancy_words:
            print(word)

main()