import os

def get_file_info(directory):
    # Create an empty list to store file information
    file_list = []

    # Loop through each file in the directory
    for file_name in os.listdir(directory):
        # Get the full file path
        file_path = os.path.join(directory, file_name)

        # Check if it is a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file size
            file_size = os.path.getsize(file_path)

            # Create a directory with file path and size
            file_info = {'path': file_path, 'size': file_size}

            #Append the dictionary to the list
            file_list.append(file_info)

    return file_list

# Get file information from the current working directory
file_info_list = get_file_info('.')

# Print the list of dictionaries
print(file_info_list)