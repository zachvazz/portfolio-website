import os

def rename_files_in_folder(folder_path):
    # List all files in the directory
    files = os.listdir(folder_path)
    # Filter out directories, keep only files
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    
    # Sort files to maintain any logical order they might have
    files.sort()

    # Rename each file to 'imageX.ext' where X is the index and ext is the original file extension
    for index, file_name in enumerate(files):
        # Get the file extension
        extension = os.path.splitext(file_name)[1]
        # Define the new file name
        new_file_name = f"image{index + 1}{extension}"
        # Define the old and new file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{file_name}' to '{new_file_name}'")

# Example usage
folder_path = 'images'  # Replace with your folder path
rename_files_in_folder(folder_path)