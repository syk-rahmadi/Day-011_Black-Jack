import random

def deal_card():
    """Returns a random card from the deck."""
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def calculate_score(cards):
    """Calculates the score of a hand."""
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards[cards.index(11)] = 1  # Change first 11 to 1
    return 0 if score == 21 and len(cards) == 2 else sum(cards)

def compare_scores(user_score, computer_score):
    """Compares scores and returns the result."""
    if user_score > 21:
        return "You went over, you lose." if computer_score <= 21 else "Both went over, you lose."
    return "Draw." if user_score == computer_score else "You win." if user_score == 0 or computer_score > 21 or user_score > computer_score else "You lose."

def play_game():
    user_cards, computer_cards = [deal_card(), deal_card()], [deal_card(), deal_card()]

    while (user_score := calculate_score(user_cards)) < 21 and input("Your cards: {}. Score: {}. Get another card? (y/n): ".format(user_cards, user_score)) == 'y':
        user_cards.append(deal_card())

    if user_score <= 21:
        while (computer_score := calculate_score(computer_cards)) < 17:
            computer_cards.append(deal_card())
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, calculate_score(computer_cards)))

while input("Play Blackjack? (y/n): ") == 'y':
    play_game()
