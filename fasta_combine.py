# create a list variable of all sequences to be combined from folder
files_list = open('sequence_folder_contents.txt').read().split('\n')

# initialise combined sequences file
combined_sequences = open('combined_sequences.txt', 'w')

# loop through list of files to combined
for seq in files_list:
# eliminate empty strings in list
  if '.fasta' not in seq:
    break
# open referenced file and write contents to combine file 
  else:
    sequence = open('./single_sequences/' + seq).read()
    combined_sequences.write(sequence + '\n')
  
combined_sequences.close()
