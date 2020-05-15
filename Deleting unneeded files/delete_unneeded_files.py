# delete_unneeded_files.py
# The program that walks through a folder tree and searches for exceptionally large files or folders
import os


def findUnneeded(folderPath, rejectSize):
    # Takes user provided folderPath
    root = os.path.abspath(folderPath)

    for doc in os.listdir(root):

        docPath = os.path.join(root, doc)

        if os.path.isdir(docPath):
            size = getDirSize(docPath)
        else:
            size = os.path.getsize(docPath)

        if size > rejectSize:
            print(f'{docPath}: {size}')


# Method finds total size of folder & it's contents.Takes the folderpath as argument
def getDirSize(start_path):
    size = 0

    for folderName, subFolder, filename in os.walk(start_path):
        for file in filename:
            filePath = os.path.join(folderName, file)
            size += os.path.getsize(filePath)

    return size


# Main Method
if __name__ == '__main__':
    findUnneeded('..', 1000)
