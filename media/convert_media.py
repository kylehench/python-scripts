import argparse, os

OLD_EXTENSION = '.wma'
NEW_EXTENSION = '.mp3'

# parse shell arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='Specify an input directory name', required=True)
args = parser.parse_args()
input_dir = args.i
output_dir = args.i + NEW_EXTENSION.replace('.', '_')
if not os.path.isdir(input_dir):
    raise FileNotFoundError("Supplied input directory does not exist")

# Create the destination directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over the directory structure
for dirpath, dirnames, filenames in os.walk(input_dir):
    # Create corresponding directories in the destination directory
    relative_dirpath = os.path.relpath(dirpath, input_dir)
    dest_subdir = os.path.join(output_dir, relative_dirpath)
    if not os.path.exists(dest_subdir):
        os.makedirs(dest_subdir)

    # file operations
    for file in filenames:
        # ex: new_file='song'; extension='.wma
        new_file, extension = os.path.splitext(file)
        if extension.lower() != OLD_EXTENSION.lower():
            continue
        source_file_path = os.path.join(dirpath, file)
        dest_file_path = os.path.join(dest_subdir, new_file) + NEW_EXTENSION
        os.system(f'ffmpeg -i "{source_file_path}" "{dest_file_path}"')