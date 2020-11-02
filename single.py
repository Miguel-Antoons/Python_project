import common


def single_play():
    """
    Runs the single play mode
    :return: None
    """
    incorrect_sign = True                                   # loop statement
    game = common.game()                                    # sign the player will use
    human = common.player(input("Enter your name : "))      # name of the human player
    computer = common.player("computer")
    passing_order = []

    # As long as there is no valid entry, the loop keeps asking which sign the player wants
    while incorrect_sign:
        incorrect_sign = False
        human.sign = input("Enter the sign you want to play (O begins first) : ")

        if human.sign == "O":
            computer.sign = "X"
            passing_order = [human, computer]

        elif human.sign == "X":
            computer.sign = "O"
            passing_order = [computer, human]

        else:
            incorrect_sign = True

    print(f"{human.user_name}, you will represent the {human.sign} plays and {computer.user_name} will represent the {computer.sign} plays.\n")

    input("Press any key to continue...")

    print("Let's begin !")
    game.print_board()

    # As long as there is no winner, the game continues
    while not game.end:
        for i in passing_order:
            if i == human:
                while not game.end and game.make_move(input(f"Your turn {i.user_name} !\nEnter a number : "), i):
                    pass
            else:
                while not game.end and game.make_move(computer_plays(game), i):
                    pass

    common.announce_winner(computer, human)


def computer_plays(game):
    print("Computer's turn")
    play = game.available_plays[common.random_number(end=len(game.available_plays))]
    print(f"The computer chose number {common.game_board[play]}")
    return play
