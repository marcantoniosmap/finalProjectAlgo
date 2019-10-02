from tokens import *
from errors import *
from lorem import *
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
        self.lastTag=None
    def advance(self):
        self.pos+=1
        self.current_char=self.text[self.pos] if self.pos <len(self.text) else None

    def make_tokens(self):
        tokens=[]
        activelist=tokens
        active='tags'
        parent=None


        while self.current_char!=None:

            #ignoring all the space
            if self.current_char in ' \t':
                self.advance()

            #if it encounters a * operator
            elif self.current_char == "*":
                number=self.getNumber()-1
                if number and len(activelist)>0:
                    multipliedTags=activelist[-1].copy()
                    for i in range(number):
                        activelist.append(multipliedTags)

            #if it encounters a word
            elif self.current_char in WORD:
                if active=="tags":
                    tag=self.getWord()
                    if tag in tagList:
                        if parent:
                            activelist.append(Token(tag,parent=parent,))
                        else:
                            activelist.append(Token(tag))
                        self.lastTag=tag
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
                        activelist[-1].addClassType(classType)

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
                parent=activelist[-1]
                parent.list=activelist
                activelist=activelist[-1].children
                active="tags"
                self.advance()

            #create sibling tag
            elif self.current_char == '+':
                active="tags"
                self.advance()

            #to create content
            elif self.current_char == '{':
                content=self.getContent()
                if content:
                    activelist[-1].addContent(content)

            #to move up a level
            elif self.current_char == '^':
                #if the current one have a parent, move one
                if activelist[-1].parent:
                    activelist=activelist[-1].parent.list
                    self.lastTag=activelist[-1].tags
                    self.advance()
                else:
                    error = IllegalCharError("it aint got no parent".format(self.current_char),
                                             self.pos + 1)
                    return [], error


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

        if returnNumber>0 and returnNumber<1000:
            return returnNumber
        else:
            return None

    def getWord(self):
        word_string = ''
        while self.current_char in ' \t':
            self.advance()

        while self.current_char != None and (self.current_char in WORD or self.current_char in DIGITS):
            word_string += self.current_char
            self.advance()

        return word_string

    def getContent(self):
        word_string = ''
        self.advance()
        while self.current_char in ' \t':
            self.advance()
        while self.current_char != '}' and self.current_char != None and self.current_char in WORD:
            word_string += self.current_char
            self.advance()

        if word_string.lower() == 'lorem':
            return self.getLorem()
        else:
            self.advance()
            if len(word_string)>0:
                return word_string
            else: return None

    def getLorem(self):
        # while self.current_char in ' \t':
        #     self.advance()
        print(self.current_char)
        if self.current_char == '*':
            number=self.getNumber()
            self.advance()
            return getLorem(number)
        else :
            self.advance()
            return getLoremParagraph(self.lastTag)


if __name__ == '__main__':
    while True:
        s=input(">>")
        lexer=Lexer(s)
        token,error=lexer.make_tokens()
        if error:
            print(error.as_string())
        else:
            for t in token:
                print(t)
                pass


