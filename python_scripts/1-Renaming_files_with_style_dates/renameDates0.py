#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
# included functionality to prompt the user for the target directory.


import shutil, os, re


# Prompt the user for the target directory.
targetDir = input("Enter the path of the target directory: ")

# Change the working directory to the specified path.
try:
    os.chdir(targetDir)
    print(f"Changed working directory to: {os.getcwd()}")
except FileNotFoundError:
    print(f"Error: The directory '{targetDir}' does not exist.")
    exit()

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
                            ((0|1)?\d)- # one or two digits for the month
                            ((0|1|2|3)?\d)- # one or two digits for the day
                            ((19|20)\d{2}) # four digits for the year
                            (.*?)$ # all text after the date
                            """, re.VERBOSE)
# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:
        continue
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFilename = f'{beforePart}{dayPart}-{monthPart}-{yearPart}{afterPart}'

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename, euroFilename)  # This is the one that actually renames the file.
    # shutil.move() will overwrite files with the same name, so be careful!
    
    
    
    
    
    
    # If you want to avoid overwriting files, you can check if the file already exists before renaming it.
    # if os.path.exists(euroFilename):
    #     print(f'Error: "{euroFilename}" already exists.')
    # else:
    #     shutil.move(amerFilename, euroFilename)  # This is the one that actually renames the file.
    # You can also use os.rename() instead of shutil.move() if you don't need to move the file to a different directory.
    # os.rename(amerFilename, euroFilename)  # This is the one that actually renames the file.
    # os.rename() will not overwrite files with the same name, so be careful!
    # If you want to avoid overwriting files, you can check if the file already exists before renaming it.
    # if os.path.exists(euroFilename):
    #     print(f'Error: "{euroFilename}" already exists.')
    # else:
    #     os.rename(amerFilename, euroFilename)  # This is the one that actually renames the file.
    # You can also use os.replace() instead of shutil.move() if you want to replace the file if it already exists.
    # os.replace() will overwrite files with the same name, so be careful!
    # If you want to avoid overwriting files, you can check if the file already exists before renaming it.
    # if os.path.exists(euroFilename):
    #     print(f'Error: "{euroFilename}" already exists.')
    # else:
    #     os.replace(amerFilename, euroFilename)  # This is the one that actually renames the file.

    # done
