class Token:
    def __init__(self,tags,id=None,_classType=None,content=None,children=None,parent=None):
        self.tags=tags
        self.id=id
        self.classType=_classType
        self.content=content
        self.parent=parent
        if children: self.children=children
        else: self.children=[]
    def __repr__(self):
        return "{} tags, id={}, class= {}, content={}, children Token ={}".format(self.tags,self.id,self.classType,self.content,self.children)

    def addChildren(self,token):
        self.children.append(token)
    def addId(self,id):
        self.id=id
    def addClassType(self,classType):
        if self.classType:
            self.classType=self.classType+" "+classType
        else:
            self.classType=classType

    def copy(self):
        return Token(self.tags,self.id,self.classType,self.content,self.children,self.parent)