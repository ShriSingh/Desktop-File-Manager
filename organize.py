"""Imported modules"""
# Module to navigate and manipulate files and folders
import os
# Module to conduct high-level file operations
import shutil
from datetime import datetime


def organize_by_extension(path):
    """
    This function organizes files from a folder based on their extension
    :param path: Takes the path of the folder to be organized
    :return: None
    """
    # Get the list of files in the directory
    file_list = os.listdir(path)
    # Getting the name of the folder to be organized
    folder_name = os.path.basename(path)
    # Setting the default message to be displayed to the user
    message = f"The folder {folder_name} is organized."

    # Checking if the folder is already organized
    if organized_check(1, path):
        # Alerting the user if so
        message = f"The folder {folder_name} is already organized."
    else:
        # Iterate through each file in the directory
        for file_name in file_list:
            file_extension = os.path.splitext(file_name)[1].lower()
            # Creating a folder for the extensions if it doesn't exist
            extension_folder = os.path.join(path, file_extension[1:])
            os.makedirs(extension_folder, exist_ok=True)

            # Moving the file to the folder
            shutil.move(os.path.join(path, file_name), os.path.join(extension_folder, file_name))

    return message


def organize_by_time(path):
    """
    This function organizes files from a folder based on their time of creation
    :param path: Takes the path of the folder to be organized
    :return: None
    """
    # Get the list of files in the directory
    file_list = os.listdir(path)
    # Getting the name of the folder to be organized
    folder_name = os.path.basename(path)
    # Setting the default message to be displayed to the user
    message = f"The folder {folder_name} is organized."

    # Checking if the folder is already organized
    if organized_check(2, path):
        # Alerting the user if so
        message = f"The folder {folder_name} is already organized."
    else:
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

    return message


def organized_check(choice, path):
    """
    This function checks if the folder is already organized
    :param choice: Choice of organization type
    :param path: Path of the folder to be organized
    :return: True if the folder is organized, False if not
    """
    # Get the list of files in the directory
    file_list = os.listdir(path)

    # Checking if the folder is already organized based on the choice
    if choice == 1:
        # Checking if the extension sub-folders exist
        folders_exist = all(os.path.isdir(os.path.join(path, folder)) for folder in file_list)
        return folders_exist
    elif choice == 2:
        # Checking if the year sub-folders exist
        years_exist = all(os.path.isdir(os.path.join(path, str(year))) for year in range(1900, 2101))
        return years_exist

    return False
