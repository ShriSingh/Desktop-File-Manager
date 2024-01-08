"""Imported modules"""
# Module to navigate and manipulate files and folders
import os
# Module to conduct high-level file operations
import shutil
from datetime import datetime


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

    # Returning the current path
    return current_path


def organizing_files(choice, path):
    """
    This function organizes files from a folder based on either their extension
    or year of creation
    :param choice: Choice of organization type
    :param path: Path of the folder to be organized
    :return message: Message to be displayed to the user that the folder is organized
    """
    # Acting based on type of organization the user wants
    if choice == 1:  # Organizing by extension type
        organize_by_extension(path)
    elif choice == 2:  # Organizing by time of creation(year, month, day)
        organize_by_time(path)

    # Getting the name of the folder to be organized
    folder_name = os.path.basename(path)
    # Returning a message to the user that the folder is organized
    message = f"The folder {folder_name} is organized."
    # Returning the message
    return message


def organize_by_extension(path):
    """
    This function organizes files from a folder based on their extension
    :param path: Takes the path of the folder to be organized
    :return: None
    """
    # Get the list of files in the directory
    file_list = os.listdir(path)

    # Iterate through each file in the directory
    for file_name in file_list:
        file_extension = os.path.splitext(file_name)[1].lower()
        # Creating a folder for the extensions if it doesn't exist
        extension_folder = os.path.join(path, file_extension[1:])
        os.makedirs(extension_folder, exist_ok=True)

        # Moving the file to the folder
        shutil.move(os.path.join(path, file_name), os.path.join(extension_folder, file_name))


def organize_by_time(path):
    """
    This function organizes files from a folder based on their time of creation
    :param path: Takes the path of the folder to be organized
    :return: None
    """
    # Get the list of files in the directory
    file_list = os.listdir(path)

    # Iteration through each file in the directory
    for file_name in file_list:
        file_path = os.path.join(path, file_name)
        # Getting the time of creation of the file
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.fromtimestamp(creation_time).date()

        # Creating a folder for the year if it doesn't exist
        date_folder = os.path.join(path, str(creation_date.year), str(creation_date.month), str(creation_date.day))
        os.makedirs(date_folder, exist_ok=True)

        # Moving the file to the corresponding date folder
        shutil.move(file_path, os.path.join(date_folder, file_name))


def copying_files(from_path, to_path):
    """
    This function copies files from a folder to another folder
    """
    # TODO - Copy files from one folder to another
    pass


def removing_files(path):
    """
    This function removes files from a folder after a specified time
    """
    # TODO - Remove files from a folder after a specified time
    pass
