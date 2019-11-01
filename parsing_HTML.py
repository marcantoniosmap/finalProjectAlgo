import copy
import re

from .lorem_generator import getLorem
from .plytoken import lerror

# from lorem_generator import getLorem

I = 1
storage = []
noCloseTag=["img","br","link","meta"]

class Tag():
    def __init__(self,tag):
        self.tag=tag
        self.className=""
        self.id=""
        self.content=""
        self.level = 0
        self.children=[]
        self.sibling=[]
        self.parent=[]

    def __repr__(self):
        return self.setIndentation()+self.makeTag() + self.getChildren()+ self.content+self.makeCloseTag()+self.getSibling()

    def setClassName(self,className):
        self.className+=className+" "

    def setId(self,id):
        self.id=id

    def checkIncrement(self,num):
        num=str(num)
        if "$" in self.className:
            self.className=self.className.replace("$",num)
        if "$" in self.id:
            self.id=self.id.replace("$",num)
        if "$" in self.content:
            self.content = self.content.replace("$",num)

    def getChildren(self):
        temp =""
        for c in self.children:
            c.level=self.level+1
            temp+='\n'
            temp+=c.__repr__()
        return temp

    def setContent(self,p,content,level):
        if("lorem"in content):
            if(content[-1:].isdigit()):
                count = int(re.search(r'\d+', content).group())
                self.content=getLorem(count,level)
            elif p == 'p':
                self.content = getLorem(40,level)
            else:
                self.content = getLorem(10,level)
        else:
            self.content=content

    def setIndentation(self):
        return ('\t'*self.level)

    def getSibling(self):
        temp=""
        for c in self.sibling:
            c.level=self.level
            temp+=c.__repr__()
        return temp

    def addSibling(self,tag):
        self.sibling.append(tag)

    def addChildren(self,children):
        self.children.append(children)

    def addParent(self,parent):
        self.parent.append(parent)

    def makeTag(self):
        if self.className != "":
            layout = " class='"+self.className+"'"
        else:
            layout = ""
        if self.id != "":
            layout2 = " id='"+self.id+"'"
        else:
            layout2 = ""
        if self.tag in noCloseTag:
            return self.getLayout()+layout2+layout+">\n"
        return self.getLayout()+layout2+layout+">"


    def makeCloseTag(self):
        if self.tag in noCloseTag:
            return ""
        else:
            if self.tag=='doc':
                if self.children:
                    return self.setIndentation()+"</body>\n"+ \
                    self.setIndentation()+"</html>\n" 
                return self.setIndentation()+"\n\n</body>\n"+ \
                    self.setIndentation()+"</html>\n"
            if self.children:
                return self.setIndentation()+"</"+self.tag+">\n"
            return "</"+self.tag+">\n"

    def getLayout(self):
        if self.tag=='img':
            return "<img src='' alt=''"
        elif self.tag=='link':
            return "<link rel='stylesheet' href='"
        elif self.tag=='a':
            return "<a href=''"
        elif self.tag == 'doc':
            return "<!DOCTYPE html>\n<html lang='en'>\n<head>\n\t<meta charset='utf-8'>" \
                   "\n\t<meta name='viewport' content='width=device-width, initial-scale=1.0'>" \
                   "\n\t<meta http-equiv='X-UA-Compatible' content='ie=edge'>" \
                   "<title>Document</title>" \
                   "</head>" \
                   "\n<body"
        else:
            return "<"+self.tag


levels = 0
def run(p):
    global levels
    if type(p)==str:
        return Tag(p)

    if p[0]=='>':
        levels = levels + 1
        return inside(run(p[1]),run(p[2]))
    elif p[0]=='+':
        return sibling(run(p[1]), run(p[2]))
    elif p[0]=='^':
        levels = levels -1
        return parent(run(p[1]),run(p[2]))
    elif p[0]=='.':
        temp=run(p[1])
        temp.setClassName(p[2])
        return temp
    elif p[0]=='#':
        temp = run(p[1])
        temp.setId(p[2])
        return temp
    elif p[0]=='{':
        temp = run(p[1])
        temp.setContent(p[1],p[2],levels)
        levels = 0
        return temp
    elif p[0]=='*':
        return multiply(run(p[1]), p[2])


def inside(p1,p2):
    p1.addChildren(p2)
    for p in p2.parent:
        p1.addSibling(p)
    return p1

def sibling(p1,p2):
    p1.addSibling(p2)
    return p1

def multiply(p1,p2):
    obj = copy.deepcopy(p1)
    p1.checkIncrement(1)
    for increment in range(2,p2+1):
        objectCopied = copy.deepcopy(obj)
        objectCopied.checkIncrement(increment)
        p1.addSibling(objectCopied)
    return p1

def parent(p1,p2):
    p1.addParent(p2)
    return p1
