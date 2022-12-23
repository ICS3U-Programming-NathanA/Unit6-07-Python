#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Dec.15, 2022
# This program splits sentences into separate words


def parse_sentence(sentence):
    # Split the sentence into a list of words
    words = sentence.split()

    # Return the list of words
    return words


def main():
    # Ask the user to enter a sentence
    sentence_str = input("Enter a sentence: ")
    # try catch to change int or floats to strings
    try:
        sentence = str(sentence_str)
    except:
        print("Invalid input. Please enter a valid sentence.")

    # Call the parse_sentence()
    words = parse_sentence(sentence)

    # Print each word in the list
    for word in words:
        print(word)


if __name__ == "__main__":
    main()
