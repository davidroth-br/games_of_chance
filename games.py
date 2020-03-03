import random

money = 100


# Write your game of chance functions here
def make_bet():
    bet = money + 1
    while bet > money:
        try:
            bet = float(input(f"You have ${money:.2f}. How much would you like to bet? $"))
        except ValueError:
            print("You must enter a numeric amount of money to bet!")
            bet = money + 1
            continue
        if bet > money:
            print("You can't bet more money than you have!")
            continue
        elif bet < 0:
            print("You must bet a positive amount!")
            bet = money + 1
            continue
        elif bet == 0:
            print("You have to bet something!")
            bet = money + 1
            continue
    return bet


def make_choice(question, low_option, high_option, error_message):
    choice = -1
    while choice not in range(low_option, high_option + 1):
        try:
            choice = int(input(question))
        except ValueError:
            print(error_message)
            continue
        if choice not in range(low_option, high_option + 1):
            print(error_message)
            continue
        else:
            return choice


def results(amount_won_or_lost):
    global money
    money += amount_won_or_lost
    if amount_won_or_lost < 0:
        print(f"Sorry, you lost ${amount_won_or_lost * -1:.2f}.")
        if money > 0:
            print(f"Now you only have ${money:.2f} to bet with.\n")
        else:
            print("You ran out of money to bet.")
    elif amount_won_or_lost > 0:
        print(f"Congratulations! You won ${amount_won_or_lost:.2f}! Now you have ${money:.2f} to bet with!\n")
    else:
        print(f"You didn't win or lose any money. You still have ${money:.2f} to bet with!\n")


def play_again(jogo):
    if money <= 0:
        return "N"
    else:
        again = "a"
        while again.upper() != "Y" and again.upper() != "N":
            again = input("Would you like to play '" + jogo + "' again? (Y/N) ")
        return again.upper()


def format_card_name(card):
    if card > 39:
        suit = "clubs"
        card -= 39
    elif card > 26:
        suit = "hearts"
        card -= 26
    elif card > 13:
        suit = "spades"
        card -= 13
    else:
        suit = "diamonds"
    if card == 1:
        name = "ace"
    elif card == 11:
        name = "jack"
    elif card == 12:
        name = "queen"
    elif card == 13:
        name = "king"
    else:
        name = str(card)
    name += " of " + suit
    return name, card


def heads_or_tails(bet, call):
    flip = random.randint(1, 2)
    if flip == 1:
        print("Heads!")
    else:
        print("Tails!")
    if flip != call:
        bet *= -1
    results(bet)


def cho_han(bet, call):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice = die1 + die2
    print("You rolled " + str(dice) + ".")
    if (dice % 2) == 0:
        print("Even!")
        odd_or_even = 2
    else:
        print("Odd!")
        odd_or_even = 1
    if odd_or_even != call:
        bet *= -1
    results(bet)


def pick_a_card(bet):
    player_card = random.randint(1, 52)
    card_name, player_card = format_card_name(player_card)
    print("You picked the " + card_name + ".")
    computer_card = player_card
    while computer_card == player_card:
        computer_card = random.randint(1, 52)
    card_name, computer_card = format_card_name(computer_card)
    print("I picked the " + card_name + ".")
    if player_card == computer_card:
        bet = 0
    elif computer_card > player_card:
        bet *= -1
    results(bet)


def roulette(bet, call):
    ball = random.randint(0, 36)
    if ball == 0:
        color = ""
    elif ball in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
        color = " red"
    else:
        color = " black"
    if call == 1:
        if ball == make_choice("Choose a number between 0 and 36: ", 0, 36, "Invalid choice."):
            bet *= 35
        else:
            bet *= -1
    elif call == 2:
        if color != " red":
            bet *= -1
    elif call == 3:
        if color != " black":
            bet *= -1
    elif call == 4:
        if ball == 0 or (ball % 2) != 0:
            bet *= -1
    elif call == 5:
        if (ball % 2) == 0:
            bet *= -1
    print("The ball stopped on number " + str(ball) + color + ".")
    results(bet)


# Game menu
while money > 0:
    print("1 - Heads or Tails\n2 - Cho-Han\n3 - Pick a Card\n4 - Roulette\n0 - Exit\n")
    game = make_choice("Choose a game: ", 0, 4, "You must choose an option from the menu. Try again.")
    if game == 0:
        break
    elif game == 1:
        play = "Y"
        while play == "Y":
            bet_amount = make_bet()
            print("1 - Heads\n2 - Tails\n")
            heads_or_tails(bet_amount, make_choice("Heads or tails? ", 1, 2,
                                                   "You must choose an option from the menu. Try again."))
            play = play_again("Heads or Tails")
    elif game == 2:
        play = "Y"
        while play == "Y":
            bet_amount = make_bet()
            print("1 - Odd\n2 - Even\n")
            cho_han(bet_amount, make_choice("Odd or even? ", 1, 2,
                                            "You must choose an option from the menu. Try again."))
            play = play_again("Cho-Han")
    elif game == 3:
        play = "Y"
        while play == "Y":
            bet_amount = make_bet()
            pick_a_card(bet_amount)
            play = play_again("Pick a Card")
    elif game == 4:
        play = "Y"
        while play == "Y":
            bet_amount = make_bet()
            print("1 - Number\n2 - Red\n3 - Black\n4 - Even\n5 - Odd\n")
            roulette(bet_amount, make_choice("What would you like to bet on? ", 1, 5,
                                             "You must choose an option from the menu. Try again."))
            play = play_again("Roulette")


if money > 0:
    print(f"You finished playing with a total of ${money:.2f}")
print("Thanks for playing!")
