import random
from cs_queue import Queue
from cs_stack import Stack

"""
CSCI-603 - Homework 6
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 6 to implement program to design "What Happens in Vegas" using Stacks and Queues.
Strategy 1 - 
                a. Pick a card from the deck. 
                b. If the card picked is 1 greater than the card at the top of victory pile, push it to victory pile.
                c. If a card is pushed to the victory pile in step b, check if any number of cards from both discard 
                    piles can be pushed till no more cards from discard piles can be pushed to victory pile.
                    return to step a.
                d. If a card cannot be pushed to the victory pile, check the following in the given order - 
                    1. If both of the discard piles are empty - 
                            push it discard pile 1.
                    2. If discard pile 1 is not empty and discard pile 2 is empty - 
                            if the card is less than the card at the top of the discard pile 1, 
                            push it to discard pile 1 else push it to the discard pile 2.
                    3. If discard pile 1 is empty and discard pile 2 is not empty - 
                            if the card is less than the card at the top of the discard pile 2, 
                            push it to discard pile 2 else push it to the discard pile 1.
                    4. If both of the discard piles are not empty - 
                        (i) if the card is less than the top cards at both discard piles, 
                            push it to the discard pile which has the maximum top card among the two.
                        (ii) if the card is more than the top cards at both discard piles,
                            push it to the discard pile which has the minimum top card among the two.
                        (iii) if the card is less than discard pile 1 but greater than discard pile 2 -
                            push it to discard pile 1.
                        (iv) if the card is less than discard pile 2 but greater than discard pile 1 -
                            push it to discard pile 2.
                    return to step a
                e. check if any more cards from discard piles can be moved in repetitive manner.
                f. exit if no more card can be moved from discard piles or no more card exists in discard piles.
                    

Strategy 2 - 
                a. Pick a card from the deck. 
                b. If the card picked is 1 greater than the card at the top of victory pile, push it to victory pile.
                c. If a card is pushed to the victory pile in step b, check if any number of cards from both discard 
                    piles can be pushed till no more cards from discard piles can be pushed to victory pile.
                    return to step a.
                d. If a card cannot be pushed to the victory pile, check the following in the given order - 
                    (i) if discard pile 2 is empty, push the card.
                    (ii) if the discard pile 2 is not empty - 
                            if the card is less than the card at the top of the discard pile 2, push to discard pile 2
                            else push to discard pile 1.
                e. check if any more cards from discard piles can be moved in repetitive manner.
                f. exit if no more card can be moved from discard piles or no more card exists in discard piles.
"""


def convert_input_str_to_integer(input_value):
    """
    Function to check if the input string is numeric and convert if the input string is integer.
    :param input_value: Input value entered by the user on standard input.
    :return: Integer value of the string. -1 if the input string in not numeric.
    """
    if not input_value.isnumeric():
        print("Value must be an int. You entered '{}'".format(input_value))
        return -1
    else:
        return int(input_value)


def get_number_of_cards_to_use():
    """
    Function to get the number of the card to use in the game
    :return: Number of cards to use for the game. Loops till valid number of cards are provided
    """
    input_msg = "Enter number of cards to use:"
    input_value = input(input_msg).strip()
    number_of_cards = convert_input_str_to_integer(input_value)
    while number_of_cards < 0:
        input_value = input(input_msg)
        number_of_cards = convert_input_str_to_integer(input_value)
    return number_of_cards


def get_number_of_simulation():
    """
    Function to get the number of simulation during the game.
    :return: Number of simulation during the game. Loops till valid number of simulations are provided.
    """
    input_msg = "Enter number of games to simulate:"
    input_value = input(input_msg).strip()
    number_of_simulation = convert_input_str_to_integer(input_value)
    while number_of_simulation < 1:
        input_value = input(input_msg)
        number_of_simulation = convert_input_str_to_integer(input_value)
    return number_of_simulation


def display_simulation_statistics(average_victory_pile, max_victory_pile_size, min_victory_pile_size):
    """
    Function to display the Simulation statistics.
    :param average_victory_pile: Average size of victory pile over n simulations.
    :param max_victory_pile_size: maximum size of the victory pile achieved over n simulations.
    :param min_victory_pile_size: minimum size of the victory pile achieved over n simulations.
    :return: None.
    """
    print("Average victory pile size: {}".format(average_victory_pile))
    print("Max victory pile size: {}".format(max_victory_pile_size))
    print("Min victory pile size: {}".format(min_victory_pile_size))


def shuffle_cards(card_deck):
    """
    Function to shuffle the deck of cards. Does not do anything if the card deck is empty.
    :return: None
    """
    if card_deck is None:
        return

    shuffle_count = random.randint(1, card_deck.get_length())
    for _ in range(shuffle_count):
        temp_card = card_deck.peek()
        card_deck.dequeue()
        card_deck.enqueue(temp_card)


def issue_card(card_deck):
    """
    Function to issue card from card deck. Shuffles random number of times before issuing the card.
    :param card_deck: deck of cards to issue card from .
    :return: card value.
    """
    shuffle_cards(card_deck)
    if card_deck.is_empty():
        return None
    else:
        card_to_issue = card_deck.peek()
        card_deck.dequeue()
        return card_to_issue


def create_deck_of_cards(number_of_cards):
    """
    Function to create the deck of cards containing given number of cards.
    :param number_of_cards: Number of cards requested by the user
    :return: deck of n cards where n is number_of_cards
    """
    deck_of_cards = Queue()
    for i in range(1, number_of_cards + 1):
        deck_of_cards.enqueue(i)

    return deck_of_cards


def check_card_can_go_to_victory_pile(victory_pile, card):
    """
    Function to check if card can go straight to the victory pile.
    :param victory_pile: stack representing victory pile.
    :param card: card value.
    :return: boolean indicating if card can be pushed straight to the victory pile.
    """
    if victory_pile.is_empty():
        return card == 1

    victory_pile_top = victory_pile.peek()
    return (victory_pile_top + 1) == card


def transfer_card_to_victory_pile(discard_pile, victory_pile):
    """
    Function to transfer one card from discard pile to victory pile
    :param discard_pile: discard pile from where card needs to be transferred.
    :param victory_pile: victory pile where card needs to be placed.
    :return: None
    """
    victory_pile.push(discard_pile.peek())
    discard_pile.pop()


def move_remaining_cards_from_discard_pile(discard_pile, victory_pile):
    """
    Check if any card from given discard pile can be moved to victory pile.
    This method is called only when the other discard pile is assumed to be empty
    since this method not check if any card moved allows card can be moved from the other discard pile.
    :param discard_pile: Stack representing discard pile.
    :param victory_pile: Stack representing victory pile.
    :return: None
    """
    while not discard_pile.is_empty():
        value_to_be_pushed = victory_pile.peek() + 1
        if discard_pile.peek() != value_to_be_pushed:
            break
        transfer_card_to_victory_pile(discard_pile, victory_pile)


def strategy_2_to_insert_to_discard_piles(discard_pile_1, discard_pile_2, card):
    """
    Performs strategy 1 to insert card into one of the discard piles.
    Refer to step d of Strategy 1 in the documentation of the vegas.py to know the exact logic.
    :param discard_pile_1: Stack representing discard pile 1.
    :param discard_pile_2: Stack representing discard pile 2.
    :param card: drawn card.
    :return: None
    """
    if discard_pile_2.is_empty():
        discard_pile_2.push(card)
    else:
        discard_pile_2.push(card) if card < discard_pile_2.peek() else discard_pile_1.push(card)


def strategy_1_to_insert_to_discard_piles(discard_pile_1, discard_pile_2, card):
    """
    Performs strategy 1 to insert card into one of the discard piles.
    Refer to step d of Strategy 1 in the documentation of the vegas.py to know the exact logic.
    :param discard_pile_1: Stack representing discard pile 1.
    :param discard_pile_2: Stack representing discard pile 2.
    :param card: drawn card.
    :return: None
    """
    if discard_pile_1.is_empty() and discard_pile_2.is_empty():
        discard_pile_1.push(card)

    elif discard_pile_1.is_empty() and discard_pile_2.is_not_empty():
        discard_pile_2.push(card) if discard_pile_2.peek() > card else discard_pile_1.push(card)

    elif discard_pile_1.is_not_empty() and discard_pile_2.is_empty():
        discard_pile_1.push(card) if discard_pile_1.peek() > card else discard_pile_2.push(card)

    else:
        discard_pile_2_top = discard_pile_2.peek()
        discard_pile_1_top = discard_pile_1.peek()
        if discard_pile_1_top > card and discard_pile_2_top > card:
            discard_pile_2.push(card) if discard_pile_1_top > discard_pile_2_top else discard_pile_1.push(card)

        elif discard_pile_1_top < card and discard_pile_1_top < card:
            discard_pile_2.push(card) if discard_pile_1_top < discard_pile_2_top else discard_pile_1.push(card)
        else:
            discard_pile_1.push(card) if discard_pile_1_top > card else discard_pile_2.push(card)


def check_remaining_cards_in_discard_piles(discard_pile_1, discard_pile_2, victory_pile):
    """
    Performs check to see if any cards from discard piles can be moved to victory pile.
    checks and pushes if any number of cards from both discard piles can be pushed till no more cards from discard piles
    can be pushed to victory pile.
    :param discard_pile_1: Stack representing discard pile 1.
    :param discard_pile_2: Stack representing discard pile 2.
    :param victory_pile: Stack representing discard victory pile.
    :return: None
    """
    while not discard_pile_1.is_empty() and not discard_pile_2.is_empty():
        value_needed = victory_pile.peek() + 1
        if discard_pile_1.peek() != value_needed and discard_pile_2.peek() != value_needed:
            break
        if discard_pile_1.peek() == value_needed:
            transfer_card_to_victory_pile(discard_pile_1, victory_pile)
        elif discard_pile_2.peek() == value_needed:
            transfer_card_to_victory_pile(discard_pile_2, victory_pile)

    move_remaining_cards_from_discard_pile(discard_pile_1, victory_pile)
    move_remaining_cards_from_discard_pile(discard_pile_2, victory_pile)


def run_strategy(strategy_number, number_of_cards):
    """
    Runs given Strategy of playing cards. Refer to the documentation of the vegas.py to know the exact logic.
    :param strategy_number: identifier to indicate either strategy 1 or strategy 2.
    :param number_of_cards: number of cards in deck.
    :return: length of the victory pile at the end of the game.
    """
    simulation_mapping = {1: strategy_1_to_insert_to_discard_piles, 2: strategy_2_to_insert_to_discard_piles}

    victory_pile = Stack()
    discard_pile_1 = Stack()
    discard_pile_2 = Stack()
    deck_of_cards = create_deck_of_cards(number_of_cards)

    while not deck_of_cards.is_empty():
        issued_card = issue_card(deck_of_cards)
        if check_card_can_go_to_victory_pile(victory_pile, issued_card):
            victory_pile.push(issued_card)
            check_remaining_cards_in_discard_piles(discard_pile_1, discard_pile_2, victory_pile)
        else:
            simulation_mapping.get(strategy_number)(discard_pile_1, discard_pile_2, issued_card)

    check_remaining_cards_in_discard_piles(discard_pile_1, discard_pile_2, victory_pile)
    return victory_pile.get_length()


def simulate_given_strategy(strategy_number, number_of_cards, no_of_simulations):
    """
    Simulates given strategy for given number of times
    :param strategy_number: Strategy to simulate
    :param number_of_cards: number of cards in the deck.
    :param no_of_simulations: no of times each strategy to be run.
    :return: total victory pile, minimum pile size of victory pile and maximum pile size across all simulations.
    """
    total_victory_pile = 0
    min_pile_size = number_of_cards
    max_pile_size = 0

    print("Simulating games applying strategy {}...".format(strategy_number))
    for _ in range(0, no_of_simulations):
        victory_pile = run_strategy(strategy_number, number_of_cards)
        max_pile_size = max(max_pile_size, victory_pile)
        min_pile_size = min(min_pile_size, victory_pile)
        total_victory_pile += victory_pile

    return total_victory_pile, max_pile_size, min_pile_size


def run_what_happens_in_vegas(no_of_cards, no_of_simulations):
    """
    Function to simulate 'What Happens in Vegas' different strategies and display simulation statistics.
    :param no_of_cards:
    :param no_of_simulations:
    :return: None
    """
    total_victory_pile, max_pile_size, min_pile_size = simulate_given_strategy(1, no_of_cards, no_of_simulations)
    display_simulation_statistics(total_victory_pile / no_of_simulations, max_pile_size, min_pile_size)
    total_victory_pile, max_pile_size, min_pile_size = simulate_given_strategy(2, no_of_cards, no_of_simulations)
    display_simulation_statistics(total_victory_pile / no_of_simulations, max_pile_size, min_pile_size)


def main():
    """
    Main function. Gets required inputs and starts 'What Happens in Vegas'
    :return: None
    """
    no_of_cards = get_number_of_cards_to_use()
    no_of_simulations = get_number_of_simulation()
    run_what_happens_in_vegas(no_of_cards, no_of_simulations)


if __name__ == '__main__':
    main()
