file_loc = r'/usr/share/wordlists/rockyou.txt'
with open(file_loc,'r') as word_file:
	for i in range(10):
		word_list = word_file.readline()

print(word_list)