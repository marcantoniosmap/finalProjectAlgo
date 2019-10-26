import copy
import re

from .lorem_generator import getLorem

# from lorem_generator import getLorem
I = 1
storage = []
noCloseTag=["img","br","link","meta","doc"]

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
        return self.setIndentation()+self.makeTag() + self.getChildren()+ self.content+self.makeCloseTag(self.tag)+self.getSibling()

    def setClassName(self, className):
        if className[-1:].isdigit():
            self.className = className[:-1]
            self.className = ''.join((self.className, str(I)))

        elif className[-1:] == '$':
            self.className = className[:-1]
            self.className = ''.join((self.className, str(" ")))

        elif className[-1:] != '$':
            self.className = className
            # self.className = ''.join((self.className, str(I)))

    def setId(self, id):
        if id[-1:].isdigit():
            self.id = id[:-1]
            self.id = ''.join((self.id, str(I)))

        elif id[-1:] == '$':
            self.id = id[:-1]
            self.id = ''.join((self.id, str(" ")))

        elif id[-1:] != '$':
            self.id = id
            # self.className = ''.join((self.className, str(I)))

    # def setClassName(self,className):
    #     self.className+=className+" "
    #
    # def setId(self,id):
    #     self.id=id

    def getChildren(self):
        temp =""
        for c in self.children:
            c.level=self.level+1
            temp+='\n'
            temp+=c.__repr__()
        return temp

    def setContent(self,p,content,level):
        # print(p.level)level
        if("lorem"in content):
            if(content[-1:].isdigit()):
                count = int(re.search(r'\d+', content).group())
                self.content=getLorem(count,level)
            elif p == 'p':
                self.content = getLorem(20,level)
            elif p == "div" or p =="span":
                self.content = getLorem(40,level)
            elif p == "h1" or p =="h2" or p =="ph3" or p =="h4" or p =="h5" or p =="h6":
                self.content = getLorem(30,level)
            else:
                self.content = getLorem(50,level)
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
        if self.className!="": layout=" class='"+self.className+"'"
        else: layout =""
        if self.id!="": layout2=" id='"+self.id+"'"
        else: layout2 =""
        return self.getLayout()+layout2+layout+">"


    def makeCloseTag(self,tag):
        if tag in noCloseTag:
            return ""
        else:
            if self.children:
                return self.setIndentation()+"</"+tag+">\n"
            return "</"+tag+">\n"

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
                   "\n<title>Document</title>" \
                   "</head>" \
                   "\n<body>\n" \
                   "\n</body>" \
                   "\n</html"
        else:
            return "<"+self.tag


levels = 0
def run(p):
    global levels
    if type(p)==str:
        return Tag(p)

    if p[0]=='>':
        levels = 0
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
    global I

    if p1.sibling:
        # print("haha")
        p1.sibling.pop()

    if len(storage)!= 0:
        storage.clear()

    if p1.className and p1.id:
        if p1.className[-1:] == " ":
            p1.className = p1.className[:-1]
            p1.className = p1.className + str(I)
            for q in range(p2):
                if q == 0:
                    storage.append(copy.deepcopy(p1))
                else:
                    I = I + 1
                    storage[q-1].setClassName(p1.className)
                    storage.append(copy.deepcopy(storage[q-1]))

            # print(storage[0].className)

            # for _ in range(0,  p2-1):
            #     p1.addSibling(storage[_])

            I = 1

        elif p1.className[-1:] != " ":
            p1.setClassName(p1.className)
            # I = str(" ")
            # p1.ClassName = ''.join((p1.className, str(I)))

            obj = copy.deepcopy(p1)

            # for j in range(p2 - 1):
            #     p1.addSibling(obj)

            I = 1

        if p1.id[-1:] == " ":
            p1.id = p1.id[:-1]
            p1.id = p1.id + str(I)
            for q in range(p2):
                if q == 0:
                    storage.append(copy.deepcopy(p1))
                else:
                    I = I + 1
                    storage[q-1].setId(p1.id)
                    storage.append(copy.deepcopy(storage[q-1]))

            # print(storage[0].className)

            for _ in range(0,  p2-1):
                p1.addSibling(storage[_])

            I = 1




        elif p1.id[-1:] != " ":
            p1.setId(p1.id)
            # I = str(" ")
            # p1.ClassName = ''.join((p1.className, str(I)))

            obj = copy.deepcopy(p1)

            for j in range(p2-1):
                p1.addSibling(obj)

            I = 1

    elif p1.className :
        if p1.className[-1:] == " ":
            p1.className = p1.className[:-1]
            p1.className = p1.className + str(I)
            for q in range(p2):
                if q == 0:
                    storage.append(copy.deepcopy(p1))
                else:
                    I = I + 1
                    storage[q-1].setClassName(p1.className)
                    storage.append(copy.deepcopy(storage[q-1]))

            # print(storage[0].className)

            for _ in range(0,  p2-1):
                p1.addSibling(storage[_])



            I = 1

        elif p1.className[-1:] != " ":
            p1.setClassName(p1.className)
            # I = str(" ")
            # p1.ClassName = ''.join((p1.className, str(I)))

            obj = copy.deepcopy(p1)

            for j in range(p2-1):
                p1.addSibling(obj)

            I = 1

    elif p1.id:
        if p1.id[-1:] == " ":
            p1.id = p1.id[:-1]
            p1.id = p1.id + str(I)
            for q in range(p2):
                if q == 0:
                    storage.append(copy.deepcopy(p1))
                else:
                    I = I + 1
                    storage[q-1].setId(p1.id)
                    storage.append(copy.deepcopy(storage[q-1]))

            # print(storage[0].className)

            for _ in range(0,  p2-1):
                p1.addSibling(storage[_])

            I = 1




        elif p1.id[-1:] != " ":
            p1.setId(p1.id)
            # I = str(" ")
            # p1.ClassName = ''.join((p1.className, str(I)))

            obj = copy.deepcopy(p1)

            for j in range(p2-1):
                p1.addSibling(obj)

            I = 1



    return p1

# def multiply(p1,p2):
#     obj = copy.deepcopy(p1)
#     for _ in range(p2-1):
#         p1.addSibling(obj)
#     return p1


def parent(p1,p2):
    p1.addParent(p2)
    return p1
