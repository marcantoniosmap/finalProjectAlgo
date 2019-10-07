
class Token:
    def __init__(self,tags,id=None,_classType=None,content=None,children=None,parent=None,list=None):
        self.tags=tags
        self.id=id
        self.classType=_classType
        self.content=content
        self.parent=parent
        self.list=list
        if children: self.children=children
        else: self.children=[]
    def __repr__(self):
        parentName=''
        if self.list:
            parentName='YES'
        else: parentName='None'

        return "({} tags id={} class= {} " \
               "content={} children " \
               "Token ={} hv list={})".format(self.tags,self.id,self.classType,
                                             self.content,self.children,parentName)

    def setChildren(self,children):
        self.children=children.copy()

    def addChildren(self,token):
        self.children.append(token)
    def addId(self,id):
        self.id=id
    def addClassType(self,classType):
        if self.classType:
            self.classType=self.classType+" "+classType
        else:
            self.classType=classType
    def addContent(self,content):
        self.content=content
    def copy(self):
        copy=Token(self.tags,self.id,self.classType,self.content,self.children,self.parent,self.list)
        # copy.setChildren(self.children)
        return copy
