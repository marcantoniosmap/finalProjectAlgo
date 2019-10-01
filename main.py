class Try:
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
        self.container=[]
    def saveContainer(self,container):
        self.container=container

    def __repr__(self):
        return f'{self.value1}+{self.value2}'


list=[]
list.append(Try(10,2))
list[0].saveContainer(list)

list2=list[0].container
list2.append(Try(19,92))

print(list)



