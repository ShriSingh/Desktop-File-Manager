"""Imported modules"""
# Module to navigate and manipulate files and folders
import os
# Module to conduct high-level file operations
import shutil


def navigate_directory(target_directory):
    """
    This function navigates and changes to the directory entered by the user
    : param target_directory: Directory chosen by the user
    : return: Newly set path of the directory
    """
    # Setting the current path to a directory that will be a parent to a target directory
    current_path = "C:\\Users\\User"

    # Finding the target directory in the path
    for root, dirs, files in os.walk(current_path):  # Traverse the directory tree
        # Checking if the target directory is in the current path
        if target_directory in dirs:
            # Setting the current path to the target directory
            current_path = os.path.join(root, target_directory)

    return current_path


def organizing_files(choice, path):
    """
    This function organizes files from a folder based on either their extension
    or year of creation
    """
    # TODO - Organize files based on their extensions
    # Acting based on type of organization the user wants
    if choice == 1:
        pass
    elif choice == 2:
        pass

    pass


def copying_files():
    """
    This function copies files from a folder to another folder
    """
    # TODO - Copy files from one folder to another
    pass


def removing_files():
    """
    This function removes files from a folder after a specified time
    """
    # TODO - Remove files from a folder after a specified time
    pass

