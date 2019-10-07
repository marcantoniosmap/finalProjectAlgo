required=["img","br"]


######################################################
###############   PARSER CLASS     ###################
######################################################


class Parser:
    def __init__(self,tokens):
        self.tokens=tokens
        self.activeList = tokens
        self.stack=[]
        self.result=[]
        self.level=0
        self.indexList=[-1,-1,-1,-1,-1,-1]
        self.advance()

    def advance(self):
        if self.indexList[self.level]<len(self.activeList)-1:
            self.current_tok=self.activeList[self.indexList[self.level]+1]
        else:
            self.current_tok=None

    def parse(self):

        while self.current_tok:
            self.result.append(self.createTag(self.current_tok))
            self.stack.append(self.current_tok)
            self.indexList[self.level] = self.indexList[self.level] + 1

            #if the current tok had children
            if self.current_tok.children:
                self.level=self.level+1
                self.activeList =self.current_tok.children
                self.current_tok=self.current_tok.children[0]

            #if the current_tok had sibling but not children
            elif self.haveSibling():
                self.closeTag()
                self.advance()

            # if the current_tok had no sibling and children
            elif self.current_tok.parent:
                self.indexList[self.level] =-1
                self.level = self.level -1
                self.closeTag()
                self.closeTag()
                self.activeList=self.current_tok.parent.list
                self.current_tok=self.current_tok.parent
                self.advance()

            else:
                self.advance()

        while self.stack:
            self.closeTag()

        return self.result


    def haveSibling(self):
        if self.indexList[self.level]<len(self.activeList)-1:
            return True
        return False

    def closeTag(self):
        self.result.append(self.createCloseTag(self.stack[-1]))
        self.stack.pop(-1)
    def createTag(self,token):
        if token.content:
            return  "<{}> {}".format(token.tags,token.content)
        else:
            return "<{}>".format(token.tags)

    def createCloseTag(self,token):
        if token.tags not in required:
            return "</{}>".format(token.tags)
        else:
            return ""
