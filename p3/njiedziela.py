import numpy as np 
import numpy.linalg 
tab=np.array([[1,0,1,2], [2,0,1,2], [2,1,2,0], [2,1,0,1], [1,3,0,0]])
print tab
n=5

class Node:
    def __init__(self, name="Node", parent=None, minimal=Integer):
        self.__parent__=parent
        self.__childs__=[]
        self.min_dep=minimal
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

def przeszukaj_WSA(ojciec, liczba_pracownikow, tab):
    #przeszukiwanie w tablicy dzieci dla ojca
    for j in range(liczba_pracownikow):
        if tab[j][0]==ojciec.name and j!=ojciec.name:
            drzewo=Node()
            drzewo.__init__(j, ojciec, tab[j][2])
            ojciec.addChild(drzewo)
            print drzewo.name
            przeszukaj_WSA(drzewo, liczba_pracownikow, tab)
    return ojciec
            
            
#funkcja tworząca drzewo z tablicy
def create_tree_WSA(liczba_pracownikow, tab):
    #wyszukanie szefa i utworzenie drzewa
    drzewo1=Node()
    for i in range(liczba_pracownikow):
        if tab[i][0]==i:
            szef=i
            a=tab[i][2]
            drzewo1.__init__(szef,0, a)
    print "WSA"
    print drzewo1.name
    przeszukaj_WSA(drzewo1, liczba_pracownikow, tab)
    return drzewo1

def przeszukaj_union(ojciec, liczba_pracownikow, tab):
    #przeszukiwanie w tablicy dzieci dla ojca
    for j in range(liczba_pracownikow):
        if tab[j][1]==ojciec.name and j!=ojciec.name:
            drzewo=Node()
            drzewo.__init__(j, ojciec, tab[j][3])
            ojciec.addChild(drzewo)
            print drzewo.name
            przeszukaj_union(drzewo, liczba_pracownikow, tab)
    return ojciec
            
            
#funkcja tworząca drzewo z tablicy
def create_tree_union(liczba_pracownikow, tab):
    #wyszukanie szefa i utworzenie drzewa
    drzewo1=Node()
    for i in range(liczba_pracownikow):
        if tab[i][1]==i:
            szef=i
            a=tab[i][3]
            drzewo1.__init__(szef,0, a)
            print "union"
            print drzewo1.name
    przeszukaj_union(drzewo1, liczba_pracownikow, tab)
    return drzewo1

def bounds(liczba_pracownikow):
    print "Bounds:"
    for i in range(liczba_pracownikow):
        a=str(i)
        print '0<=x' + a + '<=1'
        

def childs(wezel, liczba_pracownikow):
    A=np.zeros(liczba_pracownikow)
    print A


def suma(drzewo, p):
    s=len(drzewo.getChilds())
    if s==0 and p==0:
        print 'x'+ str(drzewo.name),
    for i in range(s):
        if p==0:
            print 'x'+ str(drzewo.name),
        print '+',
        print ("x{}".format(drzewo.getChilds()[i].name)),
        p=1
    if drzewo.isNode()==True:
        suma(drzewo.getChilds()[0],1)
    return 0

def contraint(drzewo):
    suma(drzewo,0)
    print '>=', drzewo.min_dep
    return 0

def contraints(drzewo):
    contraint(drzewo)
    if drzewo.isNode()==True:
        s=len(drzewo.getChilds())
        for i in range(s):
            contraints(drzewo.getChilds()[i])
    return 0

def minimal(liczba_pracownikow):
    print "Minimize"
    for i in range(liczba_pracownikow-1):
        print ("x{}".format(i)+'+'),
    a=liczba_pracownikow-1
    print 'x'+ str(a)
        

def linear_problem(tab, liczba_pracownikow):
    A=create_tree_WSA(liczba_pracownikow,tab)
    #B=create_tree_union(liczba pracownikow,tab)
    minimal(liczba_pracownikow)
    print
    print "Subject to"
    contraints(A)
    print
    bounds(liczba_pracownikow)
    return 0
linear_problem(tab, n)
