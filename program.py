"""Imported modules/packages"""
import sys
# Libraries to navigate and manipulate files and folders
import os
import shutil

def navigate_directory(input):
    """
    This function navigates and changes to the directory entered by the user
    : param input: Directory chosen by the user
    : return: Newly set path of the directory
    """ 
    # Setting the target directory
    target_directory = input
    # Finding the current working directory
    current_path = os.getcwd()
    
    return current_path


def organizing_files():
    """
    This function organizes files from a folder based on their extensions
    or file type
    """
    # Asking user which folder they want to organize
    folder_name = input("Choose the folder you want to organize: ")
    # Finding the current working directory path
    dir_path = navigate_directory(folder_name)
    print("The current working directory is: ", dir_path)
    pass
    

def removing_files():
    """
    This function removes files from a folder after a specified time
    """
    # Asking user which folder they want to remove files from
    folder_name = input("Choose the folder you want to remove files from: ")
    # Finding the current working directory path
    dir_path = navigate_directory(folder_name)
    print("The current working directory is: ", dir_path)
    pass


def copying_files():
    """
    This function copies files from a folder to another folder
    """
    # Asking user which folder they want to copy files from
    folder_name = input("Choose the folder you want to copy files from: ")
    # Finding the current working directory path
    dir_path = navigate_directory(folder_name)
    # Asking user which folder they want to copy files to
    folder_name = input("Choose the folder you want to copy files to: ")
    # Finding the current working directory path
    dir_path = navigate_directory(folder_name)
    pass

def menu():
    """
    This function displays a welcome message to the user
    """
    # Welcome message
    print("***************Welcome to Desktop File Manager!****************")
    print("This program will help you organize your files on your desktop.")
    print("***************************************************************\n")

    # Showing the Menu Screen
    print("***************Menu****************")
    print("1. Organize files")
    print("2. Copy files")
    print("3. Remove files")
    print("4. Exit")
    print("***********************************\n")

    # Asking the user for their choice
    choice = input("Please enter your choice from the above menu: ")
    # Action based on the user's choice
    if choice == "1":
        print("Organizing the files in the folder...")
        organizing_files()
    elif choice == "2":
        print("Copying files from one folder to another...")
        copying_files()
    elif choice == "3":
        print("Removing the files from the folder...")
        removing_files()
    elif choice == "4":
        print("Exiting the program...")
        sys.exit()
    else:
        # If the user enters an invalid choice, restart the menu
        print("You did not enter a valid choice. Please try again.\n")
        menu()

if __name__ == "__main__":
    # Welcome message, the menu screen and the user's choice
    menu()
