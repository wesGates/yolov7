import os
import glob

# # Directories containing images relative to the current working directory
# image_directory_train = 'images/train/'
# image_directory_val = 'images/val/'
# image_directory_test = 'images/test/'
# Directories containing images relative to the current working directory
image_directory_train = 'images/train2017/'
image_directory_val = 'images/val2017/'
image_directory_test = 'images/test/'

# Directory to save the .txt files: CHANGE THIS FOR DIFFERENT DATASETS
output_directory = '.'

# Check if the output directory exists, and create it if it doesn't
os.makedirs(output_directory, exist_ok=True)

# Search for png images in the directories
image_paths_train = glob.glob(os.path.join(image_directory_train, '*.png'))
image_paths_val = glob.glob(os.path.join(image_directory_val, '*.png'))
image_paths_test = glob.glob(os.path.join(image_directory_test, '*.png'))

# Define the names of the output txt files with the output directory included
output_file_train = os.path.join(output_directory, 'train.txt')
output_file_val = os.path.join(output_directory, 'val.txt')
output_file_test = os.path.join(output_directory, 'test.txt')

# Write the image paths to the files in the chess directory
with open(output_file_train, 'w') as file:
    for path in image_paths_train:
        unix_path = path.replace(os.sep, '/')
        file.write(f'../{unix_path}\n')  # Adjust the relative path if necessary

with open(output_file_val, 'w') as file:
    for path in image_paths_val:
        unix_path = path.replace(os.sep, '/')
        file.write(f'../{unix_path}\n')  # Adjust the relative path if necessary

with open(output_file_test, 'w') as file:
    for path in image_paths_test:
        unix_path = path.replace(os.sep, '/')
        file.write(f'../{unix_path}\n')  # Adjust the relative path if necessary

# Print out confirmation messages
print(f'Paths to all .png images in {image_directory_train} have been written to {output_file_train}')
print(f'Paths to all .png images in {image_directory_val} have been written to {output_file_val}')
print(f'Paths to all .png images in {image_directory_test} have been written to {output_file_test}')
