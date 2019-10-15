from plyparseCopy import parser

while True:
    try:
        s = input(">> ")
    except EOFError:
        break # ctrl + D ends the program
    if not s: continue
    result = parser.parse(s)
    print(result)   