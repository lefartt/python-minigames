import random

SUITS = ["♠", "♥", "♦", "♣"]

RANKS = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "J", "Q", "K", "A"
]


def create_deck():
    deck = []

    for suit in SUITS:
        for rank in RANKS:
            deck.append(f"{rank}{suit}")

    return deck


def deal_card(deck):
    return deck.pop()


def calculate_score(hand):
    score = 0
    aces = 0

    for card in hand:
        rank = card[:-1]

        if rank in ["J", "Q", "K"]:
            score += 10

        elif rank == "A":
            score += 11
            aces += 1

        else:
            score += int(rank)

    # Change Ace from 11 to 1 if the hand would bust
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def is_blackjack(hand):
    return len(hand) == 2 and calculate_score(hand) == 21


def play_round():
    # -------------------------
    # Create and shuffle deck
    # -------------------------

    deck = create_deck()
    random.shuffle(deck)

    # -------------------------
    # Deal initial cards
    # -------------------------

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # -------------------------
    # Initial display
    # -------------------------

    print("\n========== BLACKJACK ==========\n")

    print("Your cards:", player_hand)
    print("Your score:", player_score)

    # Hide dealer's second card
    print("\nDealer's cards:", dealer_hand[0], "[?]")

    # -------------------------
    # Check for Blackjack
    # -------------------------

    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    if player_blackjack or dealer_blackjack:

        print("\n========== BLACKJACK CHECK ==========")

        print("Dealer's cards:", dealer_hand)
        print("Dealer's score:", dealer_score)

        if player_blackjack and dealer_blackjack:
            print("\nBoth have Blackjack! It's a draw.")

        elif player_blackjack:
            print("\nBlackjack! You win!")

        else:
            print("\nDealer has Blackjack! You lose.")

        return

    # -------------------------
    # Player's turn
    # -------------------------

    while player_score < 21:

        choice = input(
            "\nDo you want to Hit or Stand? (h/s): "
        ).lower()

        if choice == "h":

            new_card = deal_card(deck)
            player_hand.append(new_card)

            player_score = calculate_score(player_hand)

            print("\nYou drew:", new_card)
            print("Your cards:", player_hand)
            print("Your score:", player_score)

            if player_score > 21:
                print("\nYou bust!")
                break

        elif choice == "s":

            print("\nYou stand.")
            break

        else:

            print("Invalid choice. Please enter 'h' or 's'.")

    # -------------------------
    # Dealer's turn
    # -------------------------

    if player_score <= 21:

        print("\n========== DEALER'S TURN ==========")

        # Reveal hidden card
        print("Dealer reveals:", dealer_hand)
        print("Dealer's score:", dealer_score)

        while dealer_score < 17:

            print("\nDealer hits!")

            new_card = deal_card(deck)
            dealer_hand.append(new_card)

            dealer_score = calculate_score(dealer_hand)

            print("Dealer drew:", new_card)
            print("Dealer's cards:", dealer_hand)
            print("Dealer's score:", dealer_score)

        if dealer_score > 21:
            print("\nDealer busts!")

        else:
            print("\nDealer stands.")

    # -------------------------
    # Final result
    # -------------------------

    print("\n========== FINAL RESULT ==========")

    print("Your cards:", player_hand)
    print("Your score:", player_score)

    print("Dealer's cards:", dealer_hand)
    print("Dealer's score:", dealer_score)

    if player_score > 21:

        print("\nYou lose! You busted.")

    elif dealer_score > 21:

        print("\nYou win! Dealer busted.")

    elif player_score > dealer_score:

        print("\nYou win!")

    elif player_score < dealer_score:

        print("\nDealer wins!")

    else:

        print("\nIt's a draw.")


# -------------------------
# Game loop
# -------------------------

while True:

    play_round()

    while True:

        replay = input("\nPlay again? (y/n): ").lower()

        if replay == "y":
            break

        elif replay == "n":
            print("\nThanks for playing Blackjack!")
            print("Goodbye!")
            exit()

        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
