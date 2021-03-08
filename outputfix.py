with open('output.txt', 'r') as infile, open('output2.txt', 'w') as outfile:
    temp = infile.read().replace("[", "")
    outfile.write(temp)
with open('output2.txt', 'r') as infile, open('output3.txt', 'w') as outfile:
    temp2 = infile.read().replace("]","")
    outfile.write(temp2)
with open('output3.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    temp2 = infile.read().replace(".","")
    outfile.write(temp2)