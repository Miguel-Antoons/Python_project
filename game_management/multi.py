from game_management import common


def multi_play():
    """
    Runs the multiplayer mode
    :return: None
    """
    common.game = common.Game()      # loop statement (bool: shows if the Game is done or not, string: shows the winning sign)
    multi_player_1 = common.Player(input("Enter the name of the first Player : "), "O")   # name of the first Player
    multi_player_2 = common.Player(input("Enter the name of the second Player : "), "X")  # name of the second Player

    print(f"{multi_player_1.user_name} will represent the {multi_player_1.sign} plays and {multi_player_2.user_name} will represent the {multi_player_2.sign} plays.\n")

    input("Press any key to continue...")

    print("Let's begin !")
    common.game.print_board()

    # As long as the Game is unfinished, the loop will continue
    while not common.game.end:
        for i in [multi_player_1, multi_player_2]:
            while not common.game.end and common.game.make_move(input(f"Your turn {i.user_name} !\nEnter a number : "), i):
                pass

    common.announce_winner(multi_player_1, multi_player_1)
