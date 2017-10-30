#!/usr/bin/env python3

from datetime import timedelta
import dateutil.parser
import tkinter as tk
from tkinter import filedialog

# Ask user for new file or existing file.
fileType = ""
while fileType != "new" and fileType != "existing":
    print("Do you want to create a to do list in a new or existing file?\n"
          "Type 'new' to create a new text document, 'existing' to append to "
          "an existing file, or 'exit' to quit.\n")
    fileType = input().lower()

    if fileType == "exit":
        print("Exiting. Goodbye.")
        exit()
    elif fileType != "new" and fileType != "existing":
        print("Unrecognized input. Please try again.")

tk.Tk().withdraw()  # Hides tkinter GUI.
if fileType == "new":
    openType = "w"
    print("Pleave navigate to the directory to create the text file.")

    # Can't use an empty string here because that's what pressing cancel in the file dialog returns.
    filePath = "filePath"
    filePath = filedialog.askdirectory()
    fileName = filePath + "/" + \
        str(input("Enter in a file name (do not type the .txt extension).\n")) + ".txt"
elif fileType == "existing":
    openType = "a"
    print("Please navigate to the text file to append.")

    # Can't use an empty string here because that's what pressing cancel in the file dialog returns.
    fileName = "fileName"

    while not(fileName.endswith(".txt")):
        fileName = filedialog.askopenfilename()
        print(fileName + " was selected.")

        if fileName == "":
            print("Exiting. Goodbye.")
            exit()
        elif not(fileName.endswith(".txt")):
            print("A text file wasn't selected. Please try again.")

# TODO: Need error handler.
# Ask user for start date.
startDate = str(input("Enter a starting date: \n"))
startDate = dateutil.parser.parse(startDate)

# TODO: Need error handler.
# Ask user for the number of days to output.
numDays = int(input("How many days forward would you like the to do list to extend to?\n"
                    "Please type in a number.\n"))

with open(fileName, openType) as f:
    # TODO: If file isn't empty, add a newline.

    # Create string with "dddd, mmmm, dd, yyyy" format.
    for i in range(numDays + 1):
        currentDate = startDate + timedelta(days=i)

        dateStr = currentDate.strftime("%A, %B %d, %Y").upper()
        f.write(dateStr)
        f.write("\n")
        f.write("-" * len(dateStr))
        f.write("\n" * 3)

print("Done")
