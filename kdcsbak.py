from os import mkdir, rename
from os.path import split, join, exists, expanduser
from glob import iglob
from re import search


base_folder = join(expanduser('~'), 'Saved Games\kingdomcome')
save_folder = join(base_folder, 'saves')
playlines = list()
for i in range(3):
	playline = join(save_folder, 'playline' + str(i))
	if exists(playline):
		playlines.append(playline)

print(f'base_folder: {base_folder}')
print(f'save_folder: {save_folder}')
print(f'playlines:')
for i,v in enumerate(playlines):
	print(f'{" "*4}{i}: {v}')
		
		

def main():
	if not exists(base_folder):
		print(f'{base_folder} does not exist')
		return
	for playline in playlines:
		backup_folder = join(playline, 'backup')
		if not exists(backup_folder):
			print(f'Creating new backup folder in {playline}')
			mkdir(backup_folder)
		save_max_number = 0
		saves = list()
		for save in iglob(join(playline, '*.whs')):
			save_name = split(save)[1]
			if not save_name or save_name == 'exit.whs':
				continue
			save_number = int(search(r'\d+', save_name).group(0))
			if save_max_number < save_number:
				save_max_number = save_number
			saves.append((save, save_name, save_number))
		
		for save, save_name, save_number in saves:
			if not save_number == save_max_number:
				new_save = join(backup_folder, save_name)
				print(f'Backing up {save_name}')
				rename(save, new_save)
		

main()
for i in range(3):
	print(f'exiting in {i}..')