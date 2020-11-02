import mysql.connector
import subprocess


def installer():
    mysql_server = ""
    mysql_cursor = ""
    incorrect_values = True

    subprocess.Popen("start chrome /new-tab https://dev.mysql.com/downloads/installer/", shell=True)
    git_clone = subprocess.Popen("git clone https://github.com/Miguel-Antoons/tic-tac-toe-ai.git", shell=True, stderr=subprocess.PIPE)
    print(git_clone.stderr)

    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to the installation program for the tic-tac-toe game.")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Please be sure that you have installed a mysql server before continuing the installation !")
    print("If you have not installed mysql, create an account and download the installer at https://dev.mysql.com/downloads/installer/")
    print("!!! Be sure to check the 'Start service on startup' checkbox during the installation !!!")

    input("Press any key to continue...")

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

        except:
            print("Incorrect values, please try again...")

            if input("Enter 0 if you want to exit the installation process.") == "0":
                return 0

    mysql_cursor.execute("CREATE DATABASE tic-tac-toe")
    mysql_cursor.execute("""CREATE TABLE turn_1 
        (id INT AUTO-INCREMENT,
        play INT PRIMARY KEY,
        probability FLOAT)""")


if __name__ == "__main__":
    installer()
