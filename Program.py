# Importing libraries to manipulate files and folders
import os
import shutil

def welcome_message():
    """
    This function displays a welcome message to the user
    """
    # Welcome message
    print("***************Welcome to Desktop File Manager!****************")
    print("This program will help you organize your files on your desktop.")
    print("***************************************************************\n")

def menu():
    """
    This function displays the menu to the user
    """
    # Showing the Menu Screen
    print("***************Menu****************")
    print("1. Organize files")
    print("2. Copy files")
    print("3. Remove files")
    print("4. Exit")
    print("***********************************\n")


# Aiming for the function to be able to navigate to the following directories:
# C:\Users\User\OneDrive\Pictures\Screenshots
# C:\Users\User\Downloads
def nagivate_directory(input):
    """
    This function navigates to a directory entered by the user
    : param input: Directory chosen by the user
    """ 
    # Setting the target directory
    target_directory = input


def removing_files(directory, time):
    """
    This function removes files from a folder after a specified time
    : param directory: Directory to remove files from
    : param time: Time to remove files after
    """
    #TODO: Removing files from folder


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
    # Welcome message
    welcome_message()