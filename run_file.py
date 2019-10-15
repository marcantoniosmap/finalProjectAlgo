stack=[]
def run(p):

    if type(p)==str:
        if "<" in p:
            return p
        else:
            stack.append(p)
            return createBracket(p)

    if p[0]=='>':
        return inside(run(p[1]),run(p[2]))
    elif p[0]=='+':
        return sibling(run(p[1]), run(p[2]))
    elif p[0]=='^':
        pass
    elif p[0]=='.':
        pass
    elif p[0]=='#':
        pass
    elif p[0]=='{':
        pass
    elif p[0]=='*':
        pass

def inside(p1,p2):
    return (p1)+(p2)+closingTag()+closingTag()

def sibling(p1,p2):
    if len(stack)<=1:
        return p1+p2+closingTag()
    else:
        s = closingTag()
        return (p1)+closingTag()+(p2)+s

def closingTag():
    temp=stack[-1]
    stack.pop(-1)
    return "</"+temp+">"
# def closingTag(p):
#     return "closing"+p

# def openingTag(p):
#     return "<"+p+">"
#     # return p

def createBracket(p):
    return "<" + p + ">"