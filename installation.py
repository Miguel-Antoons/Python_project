import subprocess
from configparser import ConfigParser
from os import path
from os import system


def installer():
    print("--------------------------------------------------------------------------------------------------")
    print("*******************Welcome to the installation program for the tic-tac-toe game.*******************")
    print("--------------------------------------------------------------------------------------------------")
    print("This program is exclusively designed to turn on WINDOWS ONLY !")
    print("Before installing the game, please be sure to have git bash accessible from command line")

    system('pause')

    download_program_files()
    install_mysql()
    create_config_file()
    create_ai_database()


def download_program_files():
    print("Downloading program files...")
    if not path.exists("Python_project") and not path.exists("../Python_project"):
        subprocess.Popen("git clone https://github.com/Miguel-Antoons/Python_project.git", shell=True)
    print("Done")


def install_mysql():
    print("*****Steps in order to download and install MySQL*****")
    if input("If you already have MySQL and the MySQL Python connector installed,\nYou can skip this step by pressing 0") == "0":
        return

    subprocess.Popen("explorer https://dev.mysql.com/downloads/installer/", shell=True)
    print("1. Go to https://dev.mysql.com/downloads/installer/ and download the MySQL installer\n")
    print("2. Open the MySQL installer\n")
    print("3. Accept all default settings until the 'Check requirements' page\n")
    print("4. When the page 'Check requirements' shows up, the installation program could ask to\n   install visual studio, juste ignore it and continue the installation\n")
    print("5. Accept all default settings until the 'Accounts and Roles' page\n")
    print("6. When the page 'Accounts and Roles' shows up, set a password for your database, your\n   default username will be 'root'. Remember your password and username as you will\n   need them later during the installation.\n")
    print("7. Click next and the 'Windows Service' page shows up. Make sure the\n  'Start the MySQL Server as System Startup' option is checked\n")
    print("8. Accept all default settings until the 'Connect to Server' page\n")
    print("9. When the page 'Connect to Server' shows up, enter your previously chosen password\n   in the password field and click next. If there is a green mark next to the check\n   button, you can proceed. Again, be sure to remember you password and username !\n")
    print("10. Accept all the default settings until you reach the end of the installation program\n    The MySQL shell and MySQL Workbench could open, you won't need them so they may be closed\n")
    print("\n--MySQL should be installed !--\n")
    return


def create_config_file():
    if not path.exists("config.ini") and not path.exists("./Python_project/config.ini"):
        print("Creating configuration file...")
        configuration_content = ConfigParser()

        configuration_content["system_var"] = {
            "epsilon": "0.5"
        }

        configuration_content["user_info"] = {
            "admin": ""
        }

        configuration_content["database_login"] = {
            "username": "",
            "password": ""
        }

        with open("config.ini", "w") as conf:
            configuration_content.write(conf)
        print("Done")

    return


def create_ai_database():
    import mysql.connector

    mysql_server = ""
    mysql_cursor = ""
    incorrect_values = True

    while incorrect_values:
        user = input("Enter the username of the mysql server : ")
        password = input("Enter the password of the mysql server : ")

        configuration_content = ConfigParser()
        configuration_content["database_login"]["username"] = user
        configuration_content["database_login"]["password"] = password

        try:
            print("Attempting to connect to local MySQL server...")
            mysql_server = mysql.connector.connect(
                host="localhost",
                user=user,
                password=password
            )

            mysql_cursor = mysql_server.cursor()

            incorrect_values = False
            print("Done")

        except mysql.connector.Error as error:
            print(f"Error connecting to database: {error}")

            if input("Enter 0 if you want to exit the installation process.") == "0":
                return 0

    mysql_cursor.execute("SHOW DATABASES LIKE tictactoe")
    results = mysql_cursor.fetchall()

    if not len(results):
        print("Creating database...")
        mysql_cursor.execute("CREATE DATABASE tictactoe")
        mysql_cursor.execute("USE tictactoe")
        print("Done")
        print("Creating AI database tables...")
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
        print("Done")

    mysql_cursor.close()
    mysql_server.close()
    return


if __name__ == "__main__":
    installer()
    system('pause')
