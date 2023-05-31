import argparse, datetime, os, subprocess

# parse shell arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='Specify an input directory name', required=True)
args = parser.parse_args()
input_dir = args.i
if not os.path.isdir(input_dir):
  raise FileNotFoundError("Supplied input directory does not exist")

# output file placed in input_dir
today = datetime.date.today()
git_list = os.path.join(input_dir, f'{today}_git_list.txt')

print(f'Writing to: {git_list} ...')

for dirpath, dirnames, filenames in os.walk(input_dir):

  with open(git_list, 'w') as text:
    # write remote origin url of each subfolder to git_list.txt
    for dirname in dirnames:
      command = ['cmd.exe', '/c', f'cd {os.path.join(input_dir, dirname)} && git config --get remote.origin.url']
      result = subprocess.run(command, capture_output=True, text=True)
      text.write(result.stdout)

  # We only want dirnames of input_dir, do not walk into subfolders
  break

print('...done')