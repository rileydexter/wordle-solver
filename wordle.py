import random
import os
import math

def load_words(filename="valid-wordle-words.txt"):
    """
    Load the list of valid Wordle words from a text file.
    Each line in the file should contain one word.
    """
    # Ensure the file path works regardless of working directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    with open(filepath, "r") as f:
        words = [line.strip() for line in f]
    return words

def get_feedback(guess, target):
    """
    Returns a list of feedback for each letter in the guess:
    'green'  - correct letter in correct position
    'yellow' - correct letter in wrong position
    'grey'   - letter not in target word

    guess (str): The guessed word
    target (str): The target word

    Returns:
        List[str]: Feedback for each letter
    """
 
    feedback = ['grey'] * len(guess)

    # Convert target to a list to mark letters as used
    target_letters = list(target)

    # First pass: mark greens
    for i in range(len(guess)):
        if guess[i] == target[i]:
            feedback[i] = 'green'
            target_letters[i] = None  # Remove letter so it can't be reused

    # Second pass: mark yellows
    for i in range(len(guess)):
        if feedback[i] == 'grey' and guess[i] in target_letters:
            feedback[i] = 'yellow'
            # Remove the first occurrence of this letter from target_letters
            target_letters[target_letters.index(guess[i])] = None

    return feedback

def filter_words(possible_words, guess, feedback):
    """
    Returns list of possible target words based on feedback from the
    previous guess
    
    possible_words: current list of possible targets to be filtered
    guess: the word previously guessed
    feedback: the feedback given to the previous guess

    Returns filtered list of possible words
    """

    # Initialise empty list of possible targets
    filtered = []

    for word in possible_words:
        if get_feedback(guess, word) == feedback:
            filtered.append(word)

    return filtered
    
# Strategy 1: uniformly select guess from list of possible targets
def choose_guess_uniform(possible_words):
    return random.choice(possible_words)

# Strategy 2:


def main():
    # Load the list of valid words
    word_list = load_words()

    # Choose a random target word
    target_word = random.choice(word_list)


if __name__ == "__main__":
    main()
