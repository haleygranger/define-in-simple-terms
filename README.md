# Simple Definitions

This project is designed to help create simple definitions for complex words using only the most commonly used 1000 words in the English language. It provides a command-line tool that allows you to automatically check whether your created definiton only uses the most commonly used words.

## Background
Inspired by the xkcd webcomic ["Up Goer Five"](https://xkcd.com/1133/) which aims to descrive the parts of the Saturn V rocket using only the 1000 most common words (in 2015).

**This project is more a exercise rather than a work tool** since the top 1000 words in the English language are extremely limiting. For example, heres a definition of a sunflower: 

> Sunflower - A tall plant with a large yellow flower whose seeds can be eaten or used to make cooking oil.

This definiton actually uses 4 words not in the word list: plant, seeds, cooking, and oil.

## How to use
1. Navigate to the project directory and execute: ```python filter_def.py```
2. The script will prmpt you to enter a term and a definiton.
3. After inputting the term and definition, it will either:
   - Ask if you would like to save the definiton to an external file.
   - Tell you why the term or definition doesn't meet criteria (e.g. It contains a word not in 1000 word list).
4. To quit the program, enter exit when prompted.

## Saving the Output
All terms and definitons that meet guidelines can be saved to a file called ```saved_definitions.txt``` in the same directory as the script. This file is automatically created if it doesn't exist and new entries are appended if it does.

## Customization
This script is fully customizable... Here's some ideas:

### Adjust the Word List
If you don't want to use the word list provided feel free to adjust. The word list is in ```top-words.txt```

**The repo is set to update the word list once a month** So becareful if you plan to repull from the repo.
[I am using this list](https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/).

### Adjust Word Count Limits
By default, the script enforced a minimum of 3 words and a maximum of 100 words for a definition. You can change these limits in the ```validate_word_count``` function.

```def validate_word_count(definition, min_words=3, max_words=100):```

## Up Gover Five Webcomic
From https://xkcd.com/1133/

![image](https://github.com/user-attachments/assets/acfe8b85-b4f2-4643-9b89-b7c23a359a2a)
