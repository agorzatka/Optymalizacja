import numpy as np 
import numpy.linalg 
tab=np.array([[1,0,1,2], [2,0,1,2], [2,1,2,0], [2,1,0,1], [1,3,0,0]])
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
    def removeChild(self, remove): #usuwa z listy dzieci podany węzeł
        if remove in self.__childs__:
            self.__childs__.remove(remove)
    def addChild(self, newChild): #dodaje dziecko do węzła
        if newChild.__class__!= Node: return None
        if newChild in self.__childs__: return None
        if newChild.getParent()!=None:
            newChild.getParent().removeChild(newChild) #wcześniej musi jednak
                                # usunąć je od poprzedniego rodzica
        self.__childs__.append(newChild)
        newChild.__parent__=self
 
#funkcja pomocnicza dla funkcji tworzącej drzewo
def przeszukaj_WSA(ojciec, liczba_pracownikow, tab):
    #przeszukiwanie w tablicy dzieci dla ojca
    for j in range(liczba_pracownikow):
        if tab[j][0]==ojciec.name and j!=ojciec.name:
            drzewo=Node()
            drzewo.__init__(j, ojciec, tab[j][2])
            ojciec.addChild(drzewo)
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
    przeszukaj_WSA(drzewo1, liczba_pracownikow, tab)
    return drzewo1

def przeszukaj_union(ojciec, liczba_pracownikow, tab):
    #przeszukiwanie w tablicy dzieci dla ojca
    for j in range(liczba_pracownikow):
        if tab[j][1]==ojciec.name and j!=ojciec.name:
            drzewo=Node()
            drzewo.__init__(j, ojciec, tab[j][3])
            ojciec.addChild(drzewo)
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
    przeszukaj_union(drzewo1, liczba_pracownikow, tab)
    return drzewo1
#Bounds
def bounds(liczba_pracownikow):
    print "Bounds"
    for i in range(liczba_pracownikow):
        a=str(i)
        print '0<=x' + a + '<=1'

#funkcja zwracająca tablice zer i jedynek, na podstawie której piszemy ograniczenia
def suma(drzewo, p, Z):
    s=len(drzewo.getChilds())
    if s==0:
        Z[drzewo.name]=1
    for i in range(s):
        Z[drzewo.name]=1
        p=1
    if drzewo.isNode()==True:
        for i in range(s):
            Z=suma(drzewo.getChilds()[i],1,Z)
    return Z
#funkcja wypisująca dla korzenia ograniczenia
def contraint(drzewo, liczba_pracownikow):
    Z=[0]*liczba_pracownikow
    S=suma(drzewo,0,Z)
    k=0
    for i in range(liczba_pracownikow):
        if S[i]==1:
            if k==0:
                print "x" + str(i),
                k=1
            else:
                print "+"+ "x" + str(i),
            
    
    print '>=', drzewo.min_dep
    return 0
#funkcja wypisują wszystkie oigraniczenia dla każdego korzenia
def contraints(drzewo, liczba_pracownikow):
    contraint(drzewo, liczba_pracownikow)
    if drzewo.isNode()==True:
        s=len(drzewo.getChilds())
        for i in range(s):
            contraints(drzewo.getChilds()[i], liczba_pracownikow)
    return 0
#wypisuje funkcje, którą chcemy zminimalizować
def minimal(liczba_pracownikow):
    print "Minimize"
    for i in range(liczba_pracownikow-1):
        print ("x{}".format(i)+'+'),
    a=liczba_pracownikow-1
    print 'x'+ str(a)
        
#problem liniowy dla WSA
def linear_problem_WSA(tab, liczba_pracownikow):
    print "Problem liniowy dla WSA"
    A=create_tree_WSA(liczba_pracownikow,tab)
    #B=create_tree_union(liczba pracownikow,tab)
    minimal(liczba_pracownikow)
    print
    print "Subject to"
    contraints(A, liczba_pracownikow)
    print
    bounds(liczba_pracownikow)
    return 0
#problem liniowy dla union
def linear_problem_union(tab, liczba_pracownikow):
    print "Problem liniowy dla union"
    B=create_tree_union(liczba_pracownikow,tab)
    minimal(liczba_pracownikow)
    print
    print "Subject to"
    contraints(B, liczba_pracownikow)
    print
    bounds(liczba_pracownikow)
    return 0

linear_problem_WSA(tab, n)
print
linear_problem_union(tab, n)
