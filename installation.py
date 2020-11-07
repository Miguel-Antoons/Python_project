import mysql.connector
import subprocess
from os import path


def installer():
    subprocess.Popen("explorer https://dev.mysql.com/downloads/installer/", shell=True)

    if path.exists("Python_project"):
        git_clone = subprocess.Popen("git clone https://github.com/Miguel-Antoons/tic-tac-toe-ai.git", shell=True, stderr=subprocess.PIPE)
        print(git_clone.stderr)

    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to the installation program for the tic-tac-toe game.")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Please be sure that you have installed a mysql server before continuing the installation !")
    print("If you have not installed mysql, create an account and download the installer at https://dev.mysql.com/downloads/installer/")
    print("!!! Be sure to check the 'Start service on startup' checkbox during the installation !!!")

    input("Press any key to continue...")

    create_ai_database()


def create_ai_database():
    mysql_server = ""
    mysql_cursor = ""
    incorrect_values = True
    while incorrect_values:
        user = input("Enter the username of the mysql server : ")
        password = input("Enter the password of the mysql server : ")

        try:
            mysql_server = mysql.connector.connect(
                host="localhost",
                user=user,
                password=password
            )

            mysql_cursor = mysql_server.cursor()

            incorrect_values = False

        except mysql.connector.Error as error:
            print(f"Error connecting to database: {error}")

            if input("Enter 0 if you want to exit the installation process.") == "0":
                return 0

    mysql_cursor.execute("CREATE DATABASE tictactoe")
    mysql_cursor.execute("USE tictactoe")
    mysql_cursor.execute("""CREATE TABLE turn_1 (
        play int(11) not null,
        probability float(10, 5) not null,
        n_references int(11) not null,
        CONSTRAINT pk_turn_1 PRIMARY KEY (play)
    )""")
    mysql_cursor.execute("""CREATE TABLE turn_2 (
        play int(11) not null,
        turn_1 int(11) not null,
        probability float(10, 5) not null,
        n_references int(11) not null,
        CONSTRAINT pk_turn_2 PRIMARY KEY (play, turn_1),
        CONSTRAINT fk_turn_2_turn_1 FOREIGN KEY (turn_1) REFERENCES turn_1 (play)
    )""")
    mysql_cursor.execute("""CREATE TABLE turn_3 (
        play int(11) not null,
        turn_1 int(11) not null,
        turn_2 int(11) not null,
        probability float(10, 5) not null,
        n_references int(11) not null,
        CONSTRAINT pk_turn_3 PRIMARY KEY (play, turn_1, turn_2),
        CONSTRAINT fk_turn_3_turn_1 FOREIGN KEY (turn_1) REFERENCES turn_1 (play),
        CONSTRAINT fk_turn_3_turn_2 FOREIGN KEY (turn_2) REFERENCES turn_2 (play)
    )""")
    mysql_cursor.execute("""CREATE TABLE turn_4 (
        play int(11) not null,
        turn_1 int(11) not null,
        turn_2 int(11) not null,
        turn_3 int(11) not null,
        probability float(10, 5) not null,
        n_references int(11) not null,
        CONSTRAINT pk_turn_4 PRIMARY KEY (play, turn_1, turn_2, turn_3),
        CONSTRAINT fk_turn_4_turn_1 FOREIGN KEY (turn_1) REFERENCES turn_1 (play),
        CONSTRAINT fk_turn_4_turn_2 FOREIGN KEY (turn_2) REFERENCES turn_2 (play),
        CONSTRAINT fk_turn_4_turn_3 FOREIGN KEY (turn_3) REFERENCES turn_3 (play)
    )""")
    mysql_cursor.execute("""CREATE TABLE turn_5 (
        play int(11) not null,
        turn_1 int(11) not null,
        turn_2 int(11) not null,
        turn_3 int(11) not null,
        turn_4 int(11) not null,
        probability float(10, 5) not null,
        n_references int(11) not null,
        CONSTRAINT pk_turn_5 PRIMARY KEY (play, turn_1, turn_2, turn_3, turn_4),
        CONSTRAINT fk_turn_5_turn_1 FOREIGN KEY (turn_1) REFERENCES turn_1 (play),
        CONSTRAINT fk_turn_5_turn_2 FOREIGN KEY (turn_2) REFERENCES turn_2 (play),
        CONSTRAINT fk_turn_5_turn_3 FOREIGN KEY (turn_3) REFERENCES turn_3 (play),
        CONSTRAINT fk_turn_5_turn_4 FOREIGN KEY (turn_4) REFERENCES turn_4 (play)
    )""")
    mysql_cursor.execute("""CREATE TABLE turn_6 (
        play int(11) not null,
        turn_1 int(11) not null,
        turn_2 int(11) not null,
        turn_3 int(11) not null,
        turn_4 int(11) not null,
        turn_5 int(11) not null,
        probability float(10, 5) not null,
        n_references int(11) not null,
        CONSTRAINT pk_turn_6 PRIMARY KEY (play, turn_1, turn_2, turn_3, turn_4, turn_5),
        CONSTRAINT fk_turn_6_turn_1 FOREIGN KEY (turn_1) REFERENCES turn_1 (play),
        CONSTRAINT fk_turn_6_turn_2 FOREIGN KEY (turn_2) REFERENCES turn_2 (play),
        CONSTRAINT fk_turn_6_turn_3 FOREIGN KEY (turn_3) REFERENCES turn_3 (play),
        CONSTRAINT fk_turn_6_turn_4 FOREIGN KEY (turn_4) REFERENCES turn_4 (play),
        CONSTRAINT fk_turn_6_turn_5 FOREIGN KEY (turn_5) REFERENCES turn_5 (play)
    );""")
    mysql_cursor.execute("""CREATE TABLE turn_7 (
        play int(11) not null,
        turn_1 int(11) not null,
        turn_2 int(11) not null,
        turn_3 int(11) not null,
        turn_4 int(11) not null,
        turn_5 int(11) not null,
        turn_6 int(11) not null,
        probability float(10, 5) not null,
        n_references int(11) not null,
        CONSTRAINT pk_turn_7 PRIMARY KEY (play, turn_1, turn_2, turn_3, turn_4, turn_5, turn_6),
        CONSTRAINT fk_turn_7_turn_1 FOREIGN KEY (turn_1) REFERENCES turn_1 (play),
        CONSTRAINT fk_turn_7_turn_2 FOREIGN KEY (turn_2) REFERENCES turn_2 (play),
        CONSTRAINT fk_turn_7_turn_3 FOREIGN KEY (turn_3) REFERENCES turn_3 (play),
        CONSTRAINT fk_turn_7_turn_4 FOREIGN KEY (turn_4) REFERENCES turn_4 (play),
        CONSTRAINT fk_turn_7_turn_5 FOREIGN KEY (turn_5) REFERENCES turn_5 (play),
        CONSTRAINT fk_turn_7_turn_6 FOREIGN KEY (turn_6) REFERENCES turn_6 (play)
    )""")
    mysql_cursor.execute("""CREATE TABLE turn_8 (
        play int(11) not null,
        turn_1 int(11) not null,
        turn_2 int(11) not null,
        turn_3 int(11) not null,
        turn_4 int(11) not null,
        turn_5 int(11) not null,
        turn_6 int(11) not null,
        turn_7 int(11) not null,
        probability float(10, 5) not null,
        n_references int(11) not null,
        CONSTRAINT pk_turn_8 PRIMARY KEY (play, turn_1, turn_2, turn_3, turn_4, turn_5, turn_6, turn_7),
        CONSTRAINT fk_turn_8_turn_1 FOREIGN KEY (turn_1) REFERENCES turn_1 (play),
        CONSTRAINT fk_turn_8_turn_2 FOREIGN KEY (turn_2) REFERENCES turn_2 (play),
        CONSTRAINT fk_turn_8_turn_3 FOREIGN KEY (turn_3) REFERENCES turn_3 (play),
        CONSTRAINT fk_turn_8_turn_4 FOREIGN KEY (turn_4) REFERENCES turn_4 (play),
        CONSTRAINT fk_turn_8_turn_5 FOREIGN KEY (turn_5) REFERENCES turn_5 (play),
        CONSTRAINT fk_turn_8_turn_6 FOREIGN KEY (turn_6) REFERENCES turn_6 (play),
        CONSTRAINT fk_turn_8_turn_7 FOREIGN KEY (turn_7) REFERENCES turn_7 (play)
    )""")

    mysql_cursor.close()
    mysql_server.close()


if __name__ == "__main__":
    mysql_module = subprocess.Popen("pip install mysql.connector", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(mysql_module.stdout)
    print(mysql_module.stderr)
    installer()
