# Data_Mining
Program written in python3. Libraries used: os, sys, random, numpy. All of these ran fine on the school linux servers when I used Eros. The program takes in a single file called "input.txt". I simply copy/pasted the inputs from input1, input2, etc. into that file and re-ran the program on it. This way, you won't have to continually specify the file and can just re-run the previous command.

To run and get results (not formatted in a pretty way):

$python3 kmeans2.py k > output.txt

with k being whatever the k value for the set is. The output.txt will be the output of the program and to format it to the pretty way to plug in to gen.exe (if necessary) just run:
 
$python3 outputfix.py

This will trim the unwanted characters and output in the way specified in the assignment description. It is a very brute force way, so I apologize. The new, formatted results will be found in output.txt (ignore output2, etc.).
