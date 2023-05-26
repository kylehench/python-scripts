import argparse, os

EXTENSION = '.mp3'
TESTING = True

# parse shell arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='Specify an input directory name', required=True)
args = parser.parse_args()
input_dir = args.i
output_dir = args.i + '_concat'
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

    media_list = os.path.join(dirpath, 'tmp_concat_list.txt')
    media_present = False
    with open(media_list, 'w') as text:
        # file operations
        for file in filenames:
            # ex: new_file='song'; extension='.wma
            new_file, extension = os.path.splitext(file)
            if extension.lower() != EXTENSION.lower():
                continue
            media_present = True
            source_file_path = os.path.join(dirpath, file)
            dest_file_path = os.path.join(dest_subdir, new_file) + EXTENSION

            text.write(f"file '{file}'\n")

    if media_present:
        output_file = os.path.basename(dirpath) + EXTENSION
        output_path = os.path.join(dest_subdir, output_file)
        if not TESTING:
            os.system(f'ffmpeg -f concat -safe 0 -i "{media_list}" -c copy "{output_path}"')
        else:
            print(output_path)

    os.remove(media_list)