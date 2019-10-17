from parsing_HTML import run
from plyparseCopy import parser

list=[]

s=input("HTML file: ")
s=s+'.html'
file=open(s,'r')
counter=1
for line in file.read().split("\n"):
    counter+=1
    if "markupy" not in line:
        list.append(line)
    else:
        line=line[7:]
        result = parser.parse(line)
        if result:
            final = run(result)
            list.append(str(final))
            print("Found MarkuPy syntax at line",counter)
            print("Syntax: ",line)
            print("Translated into: ")
            print(str(final))
        else:
            list.append(line)

file.close()
file=open(s,'w')
for l in list:
    file.write(l+'\n')
file.close()


