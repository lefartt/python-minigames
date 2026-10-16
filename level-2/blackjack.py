import random

SUITS = ["♠", "♥", "♦", "♣"]

RANKS = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "J", "Q", "K", "A"
]


def create_deck():
    """Create a standard 52-card deck."""
    deck = []

    for suit in SUITS:
        for rank in RANKS:
            deck.append(f"{rank}{suit}")

    return deck


def deal_card(deck):
    """Draw and remove one card from the deck."""
    return deck.pop()


def calculate_score(hand):
    """Calculate a hand's score, adjusting Aces when necessary."""
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

    # Change Aces from 11 to 1 if the hand would bust.
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def is_blackjack(hand):
    """Check whether a two-card hand totals 21."""
    return len(hand) == 2 and calculate_score(hand) == 21


def play_round():
    """Play one round of Blackjack."""
    # Create and shuffle a fresh deck.
    deck = create_deck()
    random.shuffle(deck)

    # Deal two cards to each player.
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\n========== BLACKJACK ==========\n")
    print("Your cards:", player_hand)
    print("Your score:", player_score)
    print("\nDealer's cards:", dealer_hand[0], "[?]")

    # Check for Blackjack before the player's turn.
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

    # Player chooses to hit or stand.
    while player_score < 21:
        choice = input(
            "\nDo you want to Hit or Stand? (h/s): "
        ).strip().lower()

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

    # Dealer plays only if the player has not busted.
    if player_score <= 21:
        print("\n========== DEALER'S TURN ==========")
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

    # Compare final scores.
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


def main():
    """Run rounds until the player chooses to quit."""
    while True:
        play_round()

        while True:
            replay = input("\nPlay again? (y/n): ").strip().lower()

            if replay == "y":
                break
            elif replay == "n":
                print("\nThanks for playing Blackjack!")
                print("Goodbye!")
                return
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
