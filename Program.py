"""For ending the program"""
import sys
"""Importing libraries to navigate and manipulate files and folders"""
import os
import shutil


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
        print("You did not enter a valid choice. Please try again.\n")
        menu()


# Aiming for the function to be able to navigate to the following directories:
# C:\Users\User\OneDrive\Pictures\Screenshots
# C:\Users\User\Downloads
def navigate_directory(input):
    """
    This function navigates to a directory entered by the user
    : param input: Directory chosen by the user
    """ 
    # Setting the target directory
    target_directory = input
    pass


def removing_files():
    """
    This function removes files from a folder after a specified time
    """
    #TODO: Removing files from folder
    pass


def organizing_files():
    """
    This function organizes files from a folder based on their extensions
    or file type
    """
    #TODO: Organizing files from folder


def copying_files():
    """
    This function copies files from a folder to another folder
    """
    #TODO: Copying files from folder


if __name__ == "__main__":
    # Welcome message, the menu screen and the user's choice
    menu()