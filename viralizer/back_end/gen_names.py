import os

os.chdir(
    "/Users/royalshrestha/Library/Mobile Documents/com~apple~CloudDocs/Coding Folder/Python Folder/iGEM Project/Back_End/amino_acids")

# 6vxx_D614H
# Original Name is DA614_DB614_DC614
# The H represents which amino acid has been mutated

name_checker = ["_", "model"]
name_checker_2 = ["Raw", "Average", "Dif", "List"]
aa_order = ["G", "A", "V", "L", "I", "M", "F", "W", "P", "S",
            "T", "C", "Y", "N", "Q", "D", "E", "K", "R", "H"]

# Example is DA614_DB614_DC614
global_file_names = []
# Example is # D614H in 6vxx_D614H
global_cleaned_names = []


# Mainly for OS module to loop through all the 1300 + files
for global_file in os.listdir():
    global_file_names.append(global_file)

global_file_names.pop(0)

# Makes the title of the actual file name that has all of that amino acid point mutations
# Example, it will create the D614 in the example of 6vxx_D614H
for file in global_file_names:
    first_letter = file[0]
    file_splitter = file.split("_")

    first_instance = file_splitter[0]
    numbers = first_instance[2:]
    full_name = first_letter + numbers
    global_cleaned_names.append(full_name)


def remove_bad_files(count):
    os.chdir(
        f"/Users/royalshrestha/Library/Mobile Documents/com~apple~CloudDocs/Coding Folder/Python Folder/iGEM Project/Back_End/amino_acids/{global_file_names[count]}")

    removed = 0

    for pdb_file in os.listdir():
        file_name, file_extension = os.path.splitext(pdb_file)

        for iter in name_checker:
            if removed == 0:
                if iter not in file_name:
                    os.remove(pdb_file)
                    removed = 1

        if removed == 0:
            for iter_2 in name_checker_2:
                if removed == 0:
                    if iter_2 in file_name:
                        os.remove(pdb_file)
                        removed = 1

        if removed == 0:
            count = file_name.count("_")
            if count != 5:
                os.remove(pdb_file)

        removed = 0


def clean_files():
    for pdb_file in os.listdir():
        file_name, file_extension = os.path.splitext(pdb_file)
        splitter = file_name.split("_")
        if splitter[-1] != "4":
            os.remove(pdb_file)


def rename_files(count):
    num = 0
    for pdb_file in os.listdir():
        file_name, file_extension = os.path.splitext(pdb_file)
        splitter = file_name.split("_")
        first_attribute = splitter[0]
        constant = global_cleaned_names[count]

        renamed_file = ("{}_{}{}.pdb".format(first_attribute, constant, aa_order[num]))
        num += 1
        os.rename(pdb_file, renamed_file)

#IMPORTANT - AUTOMATE ALL 1300 files. Specify exactly how many files there are and replace it with total_FILES
total_FILES = 4
for count in range(total_FILES):
    remove_bad_files(count)
    clean_files()
    rename_files(count)
