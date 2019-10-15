import copy
noCloseTag=["img","br"]

level=0
class Tag:

    def __init__(self,tag):
        self.tag=tag
        self.className=""
        self.id=""
        self.content=""
        self.children=[]
        self.sibling=[]
        self.parent=None

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
    # def getParent(self):
    #     temp = ""
    #     for c in self.parent:
    #         temp += c.__repr__()
    #     return temp
    def addSibling(self,tag):
        self.sibling.append(tag)

    def addChildren(self,children):
        self.children.append(children)

    def makeTag(self):
        if self.className !="" and self.id !="":
            return "<"+self.tag +" class='"+self.className+"' id='"+self.id+"'>"
        if self.className !="":
            return "<"+self.tag +" class='"+self.className+"'>"
        elif self.id !="":
            return "<"+self.tag +" id='"+self.id+"'>"
        else:
            return "<"+self.tag+">"

    def makeCloseTag(self,tag):
        if tag in noCloseTag:
            return ""
        else:
            return "</"+tag+">"





stack=[]
def run(p):

    if type(p)==str:
        return Tag(p)

    if p[0]=='>':
        return inside(run(p[1]),run(p[2]))
    elif p[0]=='+':
        return sibling(run(p[1]), run(p[2]))
    elif p[0]=='^':
        # return parent(run(p[1]),run(p[2]))
        pass
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
    return p1

def sibling(p1,p2):
    p1.addSibling(p2)
    return p1


def multiply(p1,p2):
    obj = copy.deepcopy(p1)
    for _ in range(p2-1):
        p1.addSibling(obj)
    return p1



