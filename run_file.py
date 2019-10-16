import copy
noCloseTag=["img","br","link"]


class Tag:

    def __init__(self,tag):
        self.tag=tag
        self.className=""
        self.id=""
        self.content=""
        self.children=[]
        self.sibling=[]
        self.parent=[]

    def setClassName(self,className):
        self.className+=" "+className

    def setId(self,id):
        self.id=id
    def setContent(self,content):
        self.content=content

    def __repr__(self):
        return self.makeTag() + self.content + self.getChildren()+self.makeCloseTag(self.tag)+self.getSibling()

    def getChildren(self):
        temp =""
        for c in self.children:
            temp+=c.__repr__()
        return temp

    def getSibling(self):
        temp=""
        for c in self.sibling:
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
            return "</"+tag+">"

    def getLayout(self):
        if self.tag=='img':
            return "<img src='' alt=''"
        elif self.tag=='link':
            return "<link rel='stylesheet' href='"
        elif self.tag=='a':
            return "<a href=''"
        else:
            return "<"+self.tag





stack=[]
def run(p):

    if type(p)==str:
        return Tag(p)

    if p[0]=='>':
        return inside(run(p[1]),run(p[2]))
    elif p[0]=='+':
        return sibling(run(p[1]), run(p[2]))
    elif p[0]=='^':
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
        temp.setContent(p[2])
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
    for _ in range(p2-1):
        p1.addSibling(obj)
    return p1


def parent(p1,p2):
    p1.addParent(p2)
    return p1
