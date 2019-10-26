# NON - SUBLIME
# from parsing_HTML import run
# from plyparseCopy import parser

while True:
    try:
        s = input(">> ")
    except EOFError:
        break # ctrl + D ends the program
    if not s: continue
    result = parser.parse(s)
    # print(result)
    if not result is None:
        final = run(result)
        print(final)
    else:
        print(s)