import threading
from gui import interface
from game_management import common, AI
from user_management import user
from time import sleep


def single_play():
    """
    Runs the single play mode
    :return: None
    """
    incorrect_sign = True                                   # loop statement
    human = common.Player(user.current_user.user_name)      # Instance of Player class which represents the human Player
    computer = common.Player("computer")                    # Instance of Player class, which represents the computer
    passing_order = []                                      # Passing order of the 2 players

    gui = False
    if input("Do you want the game with a graphical user interface? (y / n) ").upper() == "Y":
        common.game = common.Game(True)
        gui = True

    else:
        common.game = common.Game()

    # As long as there is no valid entry, the loop keeps asking which sign the Player wants
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

    print(f"{human.user_name}, you will represent the {human.sign} plays and {computer.user_name} will represent "
          f"the {computer.sign} plays.\n")

    input("Press any key to continue...")

    print("Let's begin !")

    if gui:
        threading_single = threading.Thread(target=interface.start, args=str(human.sign))
        threading_single.start()

    else:
        threading_single = False
        common.game.print_board()

    # As long as there is no winner, the Game continues
    while not common.game.end:
        for i in passing_order:
            if i == human:
                if gui:
                    while True:
                        if common.game.end:
                            break

                        if interface.clickeffectuer["fait"]:
                            interface.id_change.append(int(interface.tableau["mouv"]))
                            common.game.make_move(int(interface.tableau["mouv"]), i)
                            interface.clickeffectuer["fait"] = False
                            break

                else:
                    while not common.game.end and common.game.make_move(
                            input(f"Your turn {i.user_name} !\nEnter "f"a number : "), i):
                        pass

            else:
                if not common.game.end:
                    ordi = computer_plays(common.game)
                    interface.id_change.append(ordi)
                    while not common.game.end and common.game.make_move(ordi, i):
                        pass

    # Function will check who has win
    common.announce_winner(computer, human)
    if threading_single:
        threading_single.join()


def computer_plays(game):
    """
    Represents the computer
    :param game: {class Game} the current state of the Game
    :return: {int} the computer's move
    """
    print("Computer's turn")
    if len(AI.turns) < 8:
        play = AI.ai_move()

        if play == "NOT_FOUND":
            play = game.available_plays[common.random_number(end=len(game.available_plays))]

    else:
        play = game.available_plays[common.random_number(end=len(game.available_plays))]

    print(f"The computer chose number {int(play)}")
    sleep(2.5)
    return int(play)


if __name__ == "__main__":
    single_play()
