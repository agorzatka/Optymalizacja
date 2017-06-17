import os
 
 
class Node:
    def __init__(self, name="Node", parent=None):
        self.__parent__=parent
        self.__childs__=[]
        self.name=name #nazwa
    def isRoot(self): #jest korzeniem, czy nie posiada rodzica
        if self.__parent__==None: return True
        return False
    def isNode(self): #jest węzłem, posiada dzieci
        if len(self.__childs__)>=1: return True
        return False
    def getParent(self):
        return self.__parent__
    def getChilds(self):
        return self.__childs__
    def getNext(self): #następny (sąsiad) węzeł z tym samym rodzicem
        if self.__parent__==None: return None
        n=self.__parent__.getChilds()
        this=False
        for child in n:
            if this and child!=self:
                return child
            if child==self:
                this=True
        return None
    def getPrev(self): #poprzedni węzeł z tym samym rodzicem
        if self.__parent__==None: return None
        n=self.__parent__.getChilds()
        p=None
        for child in n:
            if child==self:
                return p
            p=child
        return None
    def removeChild(self, remove): #usuwa z listy dzieci podany węzeł
        if remove in self.__childs__:
            self.__childs__.remove(remove)
    def setParent(self, newParent): #przypisuje węzłowi nowego rodzica
        if newParent.__class__!= Node: return None
        if self.__parent__!=None: #jeśli miał rodzica
            self.__parent__.removeChild(self) #usuwa się z niego
            self.__parent__=newParent #i ustawia nowego
            newParent.addChild(self) #oraz dodaje się do listy jego dzieci
    def addChild(self, newChild): #dodaje dziecko do węzła
        if newChild.__class__!= Node: return None
        if newChild in self.__childs__: return None
        if newChild.getParent()!=None:
            newChild.getParent().removeChild(newChild) #wcześniej musi jednak
                                # usunąć je od poprzedniego rodzica
        self.__childs__.append(newChild)
        newChild.__parent__=self
    def getRoot(self): #szuka korzeni
        root=self
        while root.isRoot()==False:#pobiera kolejnych rodziców tak długo, aż trafi
            root=root.getParent()
        return root
    def printTree(self, intend=0): # metoda rysuje całe drzewo od obecnego elementu
        p=""                       # z podanym wcięciem (zaczynając od 0)
        i=intend
        while i>0:
            if i>1: p+="    +"
            else: p+="    ";
            i-=1 #generowanie wcięcia
        if(self.isNode()):
            print(p+"+"+self.name) #jeśli ma dzieci, rysuje +
        else:
            print(p+"-"+self.name) #nie posiada, -
        for c in self.getChilds(): #i to samo dla każdego dziecka
            c.printTree(intend+1)  #ze zwiększonym wcięciem
