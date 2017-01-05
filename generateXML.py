# Generates XML Code for Reserve Table

import fileinput

first = True
print ("What file would you like to convert to XML?")
print ("Currently supports .csv files (can be made from spreadsheet)")
print ("Please include typecode in first line for column- String, Number, etc.")
fileName = input("Please enter file to read: ")
output = input("Please name your output file (no file extension): ")

#infile = open(fileName,'r')
#outfile = open(output+".xml", "w")

#typecodes = f.readline()
#types = header.split(",")

#nextline = f.readline()
for line in fileinput.input():
    if(first):
      types = line.rstrip().split(",")
      first = False
    elif(line != "\n"):
        line_chunks = line.rstrip().split(",")
        print("<Row>")
        #outfile.write("<Row>\n")
        i=0
        for chunk in line_chunks:
            #outfile.write("<Cell><Data ss:Type=\"" + types[chunk] + "\">"+ line_chunks[chunk] + "</Data></Cell>\n")
            print("<Cell><Data ss:Type=\"" + types[i] + "\">"+ chunk + "</Data></Cell>")
            i += 1
        #outfile.write("</Row>\n")
        print("</Row>")
