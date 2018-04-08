# the value of 'infile' will need to be changed to match where you have downloaded your files


# read a file and print the length of each line and its contents
infile = r'D:\Intro_to_programming_09042018\data\Rio_medals_table.csv'
fr = open(infile, 'r')
for line in fr:
    print (str(len(line)) , "<>" , line)

fr.close()

# read a file and write each line to a different file
infile = 'D:/Intro_to_programming_09042018/data/Rio_medals_table.csv'
outfile = 'D:/Intro_to_programming_09042018/data/Rio_medals_table_out.csv'
fr = open(infile, 'r')
fw = open(outfile, 'w')

for line in fr:
    # this is where your main processing goes
    # that changes the input to produce the output
    # you would then write your output, not a copy of the input
    fw.write(line)

fr.close()
fw.close()


# read a file and print the first ten lines
#infile = r'D:\Intro_to_programming_09042018\data\Rio_medals_table.csv'
#fr = open(infile, 'r')
#for i in range(10):
#    print (fr.readline().strip())
#
#fr.close()
