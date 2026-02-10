import time # time module is used for time related functions
import random
sentences = [
    "This quick brown jumps.",
    "A journey of thousand miles begins with a single step.",
    "This is the way for us to reference the object of the class."
]

def accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence) * 100 if test_sentence else 0)
    return accuracy
    '''
    Zip function makes zip'''
def typing_test():
    test_sentence = random.choice(sentences) # pick random element from list
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter when you are ready...")
    start_time = time.time() # Measure the start time and time.time returns the time in seconds
    user_input = input("\nStart typing:\n")
    end_time = time.time() # Measure the end time
    time_taken = end_time - start_time
    word_count = len(test_sentence.split(" "))
    # White Spaces
    print("Results:")
    print(f"Time taken: {time_taken} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing speed: {word_count / (time_taken/60):.2f} words per minute")

typing_test()
