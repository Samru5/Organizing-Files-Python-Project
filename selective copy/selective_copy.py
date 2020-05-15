# selective_copy.py

import os

"""The shutil module helps you automate copying files and directories. 
This saves the steps of opening, reading, writing and closing files when there is no actual processing."""
import shutil

# Methods takes inputfolder as input and takes the extension from user to know which type of file we have to copy  from input folder to output folder
def selectiveCopy(inputFolder, ext, outputFolder):

    # Takes output folder path
    resultFolder = os.path.abspath(outputFolder)

    # Walks through a folder tree & searches for files with a certain file extension
    for folderName, subFolder, filename in os.walk(inputFolder):

        for file in filename:
            # Searches for a file name ending with extension provided by the user.Here we are searching for .png files
            if file.endswith(ext):

                filepath = os.path.join(os.path.abspath(folderName), file)

                if not os.path.exists(resultFolder):
                    # create result folder if it doesn't exist
                    os.makedirs(resultFolder)

                if os.path.dirname(filepath) != resultFolder:
                    # prevent copying files from result folder
                    shutil.copy(filepath, resultFolder)
                    print(f'Copied {filepath} to result folder')


# Main Method
if __name__ == '__main__':
    # Providing current input folder path,png extension to extract png files from input folder to copy them in output folder,output folder name
    selectiveCopy('.', 'png', 'output_data_folder')
