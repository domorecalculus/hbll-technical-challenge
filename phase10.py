import collections
import random

def main():
    """
    Main game loop for taking user inputted hands or generating random hands. The number of cards 
    in a hand can be configured with hand_size.
    """

    hand_size = 10
    menu = """
    Menu:
    1. Generate a random hand
    2. Enter a hand manually
    """

    print("Welcome to phase 10!")
    print(menu)
    while (user_input := input("Please enter option number (or 'quit' to exit): ")) != "quit":
        if user_input == "1":
            hand = generate_hand(hand_size)
            print("Your hand is: " + str(hand))
            met_phases = evaluate_hand(hand)
            print("Your hand meets phases " + str(met_phases))
            print(menu)
            continue
        
        elif user_input == "2":
            hand_input = input("Enter your hand as a comma separated list (ex. 1,2,3,4...) or 'menu' to go back to the menu: ")
            if hand_input == "menu":
                print(menu)
                continue
            while not validate_hand(hand_input, hand_size):
                hand_input = input("Enter your hand as a comma separated list (ex. 1,2,3,4...) or 'menu' to go back to the menu: ")
                if hand_input == "menu":
                    print(menu)
                    continue

            hand = parse_hand(hand_input)
            met_phases = evaluate_hand(hand)
            print("Your hand meets phases " + str(met_phases))
            print(menu)
            continue
            
        else:
            print("That is not a menu option, please enter the number that correlates to the option you wish to select or enter 'quit' to exit.")
            continue

    print("Goodbye!")

def generate_hand(size: int) -> list:
    """ Generates a random hand from a standard deck. """
    deck = []
    for i in range(1, 13):
        deck += [i] * 8
    return random.sample(deck, size)
    

def parse_hand(hand_input: str) -> list:
    """ Simply splits input string into list of integers. """
    return [ int(x) for x in hand_input.split(',') ]
    
def validate_hand(hand_input: str, size: int) -> bool:
    """ 
    Validates user input to make sure there are enough numbers for the hand, all entries are 
    numbers, numbers are in the proper range, and the hand doesn't break deck composition rules.
    """

    try:
        hand = parse_hand(hand_input)
    except ValueError:
        print("Please enter valid numbers only for the hand")
        return False

    if len(hand) != size:
        print("Hand should have " + str(size) + " numbers in it")
        return False

    if True in [x > 12 or x < 1 for x in hand]:
        print("Numbers in hand should be between 1 and 12")
        return False 

    if max(collections.Counter(hand).values()) > 8:
        print("There can only be 8 cards of each number")
        return False
    
    return True
    
def evaluate_hand(hand: list) -> list:
    """
    Evaluates the provided hand, expects a list of only integers, and determines what phases it
    fulfills. It returns a list of the phase numbers. 
    The overall time complexity of this function is O(n*log(n)) where n is the hand size
    """

    phases_passed = []
    
    # Initializing counter is O(n) and most_common is O(n*log(n)) 
    sets = collections.Counter(hand).most_common()
    # Getting the largest run is O(n*log(n)) 
    largest_run = get_largest_run(hand)
    
    # Phase 1 check
    if sets[0][1] >= 3 and sets[1][1] >= 3:
        phases_passed.append(1)
        
    # Phase 2 check
    # The complexity of this check is O(n*log(n)) because len(sets) is a constant =< number of 
    # unique integers in the deck, and get_largest_run is O(n*log(n))
    for set in sets:
        if set[1] >= 3:
            # Don't use ints in the set for the run
            reduced_hand = hand.copy()
            reduced_hand.remove(set[0])
            reduced_hand.remove(set[0])
            reduced_hand.remove(set[0])
            if len(get_largest_run(reduced_hand)) >= 4:
                phases_passed.append(2)
                break
        else: 
            break

    # Phase 3 check
    # Same complexity as phase 2 check
    for set in sets:
        if set[1] >= 4:
            # Don't use ints in the set for the run
            reduced_hand = hand.copy()
            reduced_hand.remove(set[0])
            reduced_hand.remove(set[0])
            reduced_hand.remove(set[0])
            reduced_hand.remove(set[0])
            if len(get_largest_run(reduced_hand)) >= 4:
                phases_passed.append(3)
                break
        else: 
            break
    
    # Phase 4 check
    if len(largest_run) >= 7:
        phases_passed.append(4)

    # Phase 5 check
    if len(largest_run) >= 8:
        phases_passed.append(5)

    # Phase 6 check
    if len(largest_run) >= 9:
        phases_passed.append(6)

    # Phase 7 check
    if sets[0][1] >= 4 and sets[1][1] >= 4:
        phases_passed.append(7)

    # Phase 9 check
    if sets[0][1] >= 5 and sets[1][1] >= 2:
        phases_passed.append(9)

    # Phase 10 check
    if sets[0][1] >= 5 and sets[1][1] >= 3:
        phases_passed.append(10)
    
    return phases_passed

def get_largest_run(hand: list) -> list:
    """
    This function takes in a list of ints and returns the largest run of consecutive integers.
    The overall time complexity is O(n*log(n)) where n is the hand size. 
    """

    # Creating the set is O(n) and sorting it is O(n*log(n)) 
    hand_set = sorted(set(hand))
    prev_start = 0
    longest_start = 0
    longest_end = len(hand_set)
    longest_len = 0

    # Finding the largest run is O(n)
    for i in range(len(hand_set) - 1):
        if hand_set[i] + 1 != hand_set[i+1]:
            if (i - prev_start + 1) > longest_len:
                longest_start = prev_start
                longest_end = i + 1
                longest_len = i - prev_start + 1
            prev_start = i + 1
            
    if (len(hand_set) - prev_start) > longest_len:
        longest_start = prev_start
        longest_end = len(hand_set)
    
    return hand_set[longest_start:longest_end]


if __name__ == "__main__":
    main()