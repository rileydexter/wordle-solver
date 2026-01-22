import random
import os
import math
import time
start_time = time.time()

def load_words(filename="valid-wordle-words.txt"):
    """
    Load the list of valid Wordle words from a text file.
    Each line in the file should contain one word.
    """
    # Ensure the file path works regardless of working directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    # Return list of words from file
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

    # Add words which match the given feedback to list
    for word in possible_words:
        if get_feedback(guess, word) == feedback:
            filtered.append(word)

    return filtered
    
# Create dictionary storing the feedback produced by all necessary guess-target pairs
feedback_cache = {}

def cached_feedback(guess, target):
    """
    Takes guess word and target word as input, and returns the feedback produced, and 
    adds it to global dictionary if not already there
    """
    key = (guess, target)
    if key not in feedback_cache:
        feedback_cache[key] = tuple(get_feedback(guess, target))
    return feedback_cache[key]


def choose_guess_uniform(possible_words, all_words):
    """
    Uniformly choose guess from list of possible target words
    """
    return random.choice(possible_words)


def choose_guess_entropy(possible_words, all_words):
    """
    Choose guess that maximises expected entropy of remaining candidates.
    """

    # If there is only one possible word remaining, choose that word as guess
    if len(possible_words) == 1:
        return possible_words[0]

    # Initialise optimal guess and optimal entropy
    best_guess = None
    best_entropy = -float("inf")

    for guess in all_words:
        feedback_counts = {}

        for target in possible_words:
            fb = cached_feedback(guess, target)
            feedback_counts[fb] = feedback_counts.get(fb, 0) + 1

        entropy = 0
        total = len(possible_words)
        for count in feedback_counts.values():
            p = count / total
            entropy -= p * math.log2(p)
         
        if entropy > best_entropy:
            best_entropy = entropy
            best_guess = guess

    return best_guess

def choose_guess_entropy_hard(possible_words, all_words):
    """
    Choose guess that maximises expected entropy of remaining candidates.
    """

    # If there is only one possible word remaining, choose that word as guess
    if len(possible_words) == 1:
        return possible_words[0]

    best_guess = None
    best_entropy = -1

    
    for guess in possible_words:
        feedback_counts = {}

        for target in possible_words:
            fb = cached_feedback(guess, target)
            feedback_counts[fb] = feedback_counts.get(fb, 0) + 1

        entropy = 0
        total = len(possible_words)
        for count in feedback_counts.values():
            p = count / total
            entropy -= p * math.log2(p)
         

        if entropy > best_entropy:
            best_entropy = entropy
            best_guess = guess

    return best_guess

def run_game(strategy, num_words):
    # Initialise list of valid words, random target, and list of possibletargets
    start_words = load_words()
    all_words = random.sample(start_words, num_words)
    target = random.choice(all_words)
    possible_words = all_words.copy()
    print(time.time() - start_time)

    max_guesses = 20
    for turn in range(1, max_guesses + 1):
        guess = strategy(possible_words, all_words)
        feedback = get_feedback(guess, target)


        possible_words = filter_words(possible_words, guess, feedback)

        print(f"Turn {turn}: {guess} → {feedback}")

        if guess == target:
            print("Solved!")
            return

    print(f"Failed. Target was {target}")

def main():
    run_game(choose_guess_entropy, 2000)
    print(f"Time: {time.time() - start_time}")


if __name__ == "__main__":
    main()

