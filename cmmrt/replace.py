import gdown
import os
import shutil
import subprocess

def replace_file_with_downloaded(old_file_path, new_file_url):
    if not os.path.exists(old_file_path):
        print(f"Error: File '{old_file_path}' not found.")
        return

    try:
        # Get the directory of the original file
        file_directory = os.path.dirname(old_file_path)

        # Download the new file using gdown
        new_file_temp_path = os.path.join(file_directory, "temp_new_file.tmp")
        gdown.download(new_file_url, new_file_temp_path, quiet=False)

        # Remove the old file and replace it with the downloaded file
        os.remove(old_file_path)
        shutil.move(new_file_temp_path, old_file_path)

        print(f"File '{old_file_path}' replaced with newly downloaded file from '{new_file_url}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Get the current username using the whoami command
username = subprocess.check_output(['whoami']).decode('utf-8').strip()
# Set the target directory within the user's home directory
target_directory = os.path.join('/home', username, '.local/lib/python3.10/site-packages/cmmrt-0.3.0-py3.10.egg/cmmrt/rt/data.py')

#checking if user is on a WSL Instance
if os.path.exists(target_directory):
    print("Downloading to WSL Instance path: " + target_directory)
    replace_file_with_downloaded(target_directory, new_file_url= 'https://drive.google.com/uc?id=1Hm45PeD820cr47PFv2f6miOBoClODI2E&export=download')

#Downloading to cmmrt/rt/
cmmrt_path = os.path.join(os.getcwd(), 'cmmrt/rt/data.py')
if os.path.exists(cmmrt_path):
    print("Downloading to" + os.path.join(os.getcwd()), 'cmmrt/rt')
    replace_file_with_downloaded(old_file_path=os.path.join(os.getcwd(), 'cmmrt/rt/data.py'), new_file_url= 'https://drive.google.com/uc?id=1Hm45PeD820cr47PFv2f6miOBoClODI2E&export=download')

#Checking if we are on a linux instance
if os.path.exists('/root/.local/lib/python3.10/site-packages/cmmrt-0.3.0-py3.10.egg/cmmrt/rt/data.py'):
    print("Downloading to Linux Instance")
    replace_file_with_downloaded(old_file_path='/root/.local/lib/python3.10/site-packages/cmmrt-0.3.0-py3.10.egg/cmmrt/rt/data.py', new_file_url= 'https://drive.google.com/uc?id=1Hm45PeD820cr47PFv2f6miOBoClODI2E&export=download')