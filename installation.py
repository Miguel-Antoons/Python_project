import mysql.connector


def installer():
    mysql_server = ""
    incorrect_values = True

    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to the installation program for the tic-tac-toe game.")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Please be sure that you have installed a mysql server before continuing the installation !")
    print("If you have not installed mysql, create an account and download the installer at https://dev.mysql.com/downloads/installer/")
    print("!!! Be sure to check the 'Start service on startup' checkbox during the installation !!!")

    if input("Press any key to continue..."):
        pass

    while incorrect_values:
        user = input("Enter the username of the mysql server : ")
        password = input("Enter the password of the mysql server : ")

        try:
            mysql_server = mysql.connector.connect(
                host="localhost",
                user=user,
                password=password
            )

            incorrect_values = False

        except:
            print("Incorrect values, please try again...")

            if input("Enter 0 if you want to exit the installation process.") == "0":
                return 0

    print(mysql_server)


if __name__ == "__main__":
    installer()
