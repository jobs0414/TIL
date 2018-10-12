import glob, os

inputPath = 'day13'
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))

my_letters = ['a','b','c','d','e','f','g','h']
# output.txt -> a,b,c,d,e,f,g,h\n
filewriter = open('output.txt', 'a') # append
max_index = len(my_letters)
for index_value in range(max_index):
    if index_value < (max_index - 1):
        filewriter.write(my_letters[index_value] + ',')
    else:
        filewriter.write(my_letters[index_value] + '\n')
filewriter.close()
