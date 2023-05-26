import argparse, os

EXTENSION = '.mp3'
TESTING = False

# parse shell arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='Specify an input directory name', required=True)
args = parser.parse_args()
input_dir = args.i
if not os.path.isdir(input_dir):
  raise FileNotFoundError("Supplied input directory does not exist")

for dirpath, dirnames, filenames in os.walk(input_dir):
  dest_dirs = set()
  for i, file in enumerate(filenames):
    extension = os.path.splitext(file)[1]
    if extension.lower() != EXTENSION.lower():
      continue
    book_id, track, book = [name for name in file.split('_') if name][:3]
    book = book.replace('ENGESVN2DA.mp3','')

    dest_dir = os.path.join(dirpath, f'{book_id}_{book}')
    if not TESTING and dest_dir not in dest_dirs:
      if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        dest_dirs.add(dest_dir)

    source_path = os.path.join(dirpath, file)
    dest_path = os.path.join(dest_dir, f'{book}_{track}{extension}')
    if not TESTING:
      os.rename(source_path, dest_path)
    else:
      track_int = int(track)
      if track_int < 3 or track_int == 10 or track_int==100:
        print(dest_dir)
        print(dest_path + '\n')