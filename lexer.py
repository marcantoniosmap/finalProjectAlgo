from tokens import *
from errors import *

DIGITS='0123456789'
WORD='qwertyuiopasdfghjklzxcvbnm-_'
tagList=["a","address","div","span","p","h1","h2","h1","h2","h1","h2",
         "ul","li","table","td","tr"
            ]
############lexer
class Lexer:
    def __init__(self,text):
        self.text = text
        self.pos=-1
        self.current_char=None
        self.advance()

    def advance(self):
        self.pos+=1
        self.current_char=self.text[self.pos] if self.pos <len(self.text) else None

    def make_tokens(self):
        tokens=[]
        activelist=tokens
        active='tags'


        while self.current_char!=None:

            #ignoring all the space
            if self.current_char in ' \t':
                self.advance()

            #if it encounters a * operator
            elif self.current_char == "*":
                number=self.getNumber()
                if number and len(activelist)>0:
                    multipliedTags=activelist[-1].copy()
                    for i in range(number):
                        activelist.append(multipliedTags)

            #if it encounters a word
            elif self.current_char in WORD:
                if active=="tags":
                    tag=self.getWord()
                    if tag in tagList:
                        activelist.append(Token(tag))
                    else:
                        error=InvalidSyntaxError("{} is not a HTML tag!".format(tag),self.pos-len(tag)+1)
                        return [],error
                elif active=="id":
                    id=self.getWord()
                    if len(activelist)>0:
                        activelist[-1].addId(id)
                elif active=="classType":
                    classType=self.getWord()
                    if len(activelist)>0:
                        activelist[-1].addId(classType)

            #if it meets the hash symbol
            elif self.current_char == '#':
                active="id"
                self.advance()

            #if it meets the dot symbol
            elif self.current_char == '.':
                active="classType"
                self.advance()

            #get inside the tag
            elif self.current_char == '>':
                activelist=tokens[-1].children
                active="tags"
                self.advance()
            else:
                error=IllegalCharError("The character {} can't be defined!".format(self.current_char),self.pos+1)
                return [],error

        return tokens,None

    def getNumber(self):
        num_str = ''
        self.advance()
        while self.current_char in ' \t':
            self.advance()

        while self.current_char != None and self.current_char in DIGITS:
            num_str+=self.current_char
            self.advance()
        returnNumber=int(num_str)

        if returnNumber>0 and returnNumber<100:
            return returnNumber
        else:
            return None

    def getWord(self):
        word_string = ''
        while self.current_char in ' \t':
            self.advance()

        while self.current_char != None and self.current_char in WORD:
            word_string += self.current_char
            self.advance()

        return word_string

if __name__ == '__main__':
    while True:
        s=input(">>")
        lexer=Lexer(s)
        token,error=lexer.make_tokens()
        if error:
            print(error.as_string())
        else:
            print(token)


