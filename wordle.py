import random
import os

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

    Args:
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

print(get_feedback("aabbcc", "ababbc"))


def main():
    # Load the list of valid words
    word_list = load_words()

    # Choose a random target word
    target_word = random.choice(word_list)


if __name__ == "__main__":
    main()
