import os

# Specify the directory path
directort_path = '/new folder'

# Get the list of files and folders
contents = os.listdir(directort_path)

# Print the contents
print("\nContents of the directory are:")
for item in contents:
    print(item)