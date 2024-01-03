"""Importing files & modules"""
# To end the program
import sys
# Calling the program file that contains methods
import program as script


def main_menu():
    """
    This function displays a welcome message to the user
    """
    # Welcome message
    print("***************Welcome to Desktop File Manager!****************")
    print("This program will help you organize your files on your desktop.")
    print("***************************************************************\n")

    # Showing the Menu Screen
    print("-----------------Menu----------------")
    print("1. Organize files")
    print("2. Copy files")
    print("3. Remove files")
    print("4. Exit")
    print("-------------------------------------\n")

    # Asking the user for their choice
    choice = input("Please enter your choice from the above menu: ")
    # Action based on the user's choice
    if choice == "1":
        print("Organizing the files in the folder...")
        organizing_files_menu()
    elif choice == "2":
        print("Copying files from one folder to another...")
        copying_files_menu()
    elif choice == "3":
        print("Removing the files from the folder...")
        removing_files_menu()
    elif choice == "4":
        print("Exiting the program...")
        sys.exit()
    else:
        # If the user enters an invalid choice, restart the menu
        print("You did not enter a valid choice. Please try again.\n")
        main_menu()


def organizing_files_menu():
    """
    Sub-menu for the organizing files that calls methods
    from the script to do so
    """
    # Asking user which folder they want to organize
    folder_name = input("Choose the folder you want to organize: ")
    # Finding the current working directory path
    dir_path = script.navigate_directory(folder_name)
    # Checking if the folder asked by the user exists
    if dir_path == "C:\\Users\\User":
        print("The folder you entered does not exist. Please try again.\n")
        organizing_files_menu()

    # Organizing Files Menu
    print("-----------Organize By-----------")
    print("1. File Type")
    print("2. Time of Creation")
    print("3. Exit")
    print("---------------------------------\n")
    # Find out how the user wants to organize the files in the given folder
    organizing_type = input(f"How would you like to organize the files {folder_name}(enter a number): ")

    # Calling methods based on the user's choice
    if organizing_type in range(1, 3):
        script.organizing_files(organizing_type, dir_path)
    elif organizing_type == 3:
        main_menu()
    else:
        print("You did not enter a valid choice. Please try again.\n")
        organizing_files_menu()


def copying_files_menu():
    """
    Sub-menu for copying files from one folder to another
    that calls methods from the script to do so
    """
    # Asking user which folder they want to copy files from
    folder_name_1 = input("Choose the folder you want to copy files from: ")
    # Finding the current working directory path
    from_folder = script.navigate_directory(folder_name_1)
    # Checking if the folder asked by the user exists
    if from_folder == "C:\\Users\\User":
        print("The folder you entered cannot be copied from. Please try again.\n")
        copying_files_menu()

    # Asking user which folder they want to copy files to
    folder_name_2 = input("Choose the folder you want to copy files to: ")

    # Calling the method to copy files from one folder to another
    script.copying_files(folder_name_1, folder_name_2)


def removing_files_menu():
    """
    Sub-menu for removing files from a folder that calls
    methods from the script to do so
    """
    # Asking user which folder they want to remove files from
    folder_name = input("Choose the folder you want to remove files from: ")
    # Finding the current working directory path
    dir_path = script.navigate_directory(folder_name)
    # Checking if the folder asked by the user exists
    if dir_path == "C:\\Users\\User":
        print("The folder you entered cannot be copied from. Please try again.\n")
        removing_files_menu()

    # Calling the method to remove files from a folder
    script.removing_files(dir_path)


if __name__ == '__main__':
    main_menu()
