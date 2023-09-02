import gdown
import os
import shutil
import subprocess

# Get the absolute path of the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
target_directory = os.path.abspath(os.path.join(script_directory, os.pardir))  # Go up one level
target_directory = os.path.join(target_directory + '/test_cmmrt')  # Go up one level

print(script_directory)
print(target_directory)

# Check if the script is in the target directory
if os.getcwd() != target_directory:
    print("Please run the file in the 'test_cmmrt' directory!")
    exit(1)

print("Downloading Filtered Fingerprints to " + os.path.join(script_directory, 'filtered_data/SMRT_fingerprints_filtered.csv'))
gdown.download("https://drive.google.com/uc?id=1SRXW4WwntgPdbjpfU6qMzrRmYRsnlPKA&export=download", os.path.join(script_directory, 'filtered_data/SMRT_fingerprints_filtered.csv'))

print("Downloading Filtered Descriptors to " + os.path.join(script_directory, 'filtered_data/SMRT_descriptors_filtered.csv'))
gdown.download("https://drive.google.com/uc?id=1svJNLp2GFm53VupsND6LlSNfJkWqn5F4&export=download", os.path.join(script_directory, 'filtered_data/SMRT_descriptors_filtered.csv'))

