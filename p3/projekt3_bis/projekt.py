import numpy as np 
import numpy.linalg 

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
            drzewo1.__init__(szef,szef, a)
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
            drzewo1.__init__(szef,szef, a)
    przeszukaj_union(drzewo1, liczba_pracownikow, tab)
    return drzewo1

#wypisuje funkcje, którą chcemy zminimalizować
def minimal(liczba_pracownikow):
    print "Minimize"
    for i in range(liczba_pracownikow-1):
        print ("x{} ".format(i)+'+'),
    a=liczba_pracownikow-1
    print 'x'+ str(a)
    
def przeplyw1(drzewo, ojciec):
    A=ojciec.getChilds()
    l=len(A)
    for i in range(l):
        print "x_{0}_{1}_{2} +".format(ojciec.name, A[i].name, drzewo),


def condition_1(drzewo, ojciec):
    if ojciec.isNode()==True:
        przeplyw1(drzewo, ojciec)
    print "x{0} >= {1}".format(ojciec.name, ojciec.min_dep),
    
def condition1_all(drzewo, ojciec):
    condition_1(drzewo, ojciec)
    if ojciec.isNode()==True:
        A=ojciec.getChilds()
        l=len(A)
        for i in range(l):
            print 
            condition1_all(drzewo, A[i])
            
def przeplyw2(drzewo, ojciec):
    A=ojciec.getChilds()
    l=len(A)
    for i in range(l):
        print "- x_{0}_{1}_{2}".format(ojciec.name, A[i].name, drzewo),  
        
def condition2(drzewo, ojciec):
    if ojciec.__parent__==ojciec.name:
        A=ojciec.getChilds()
        l=len(A)
        for i in range(l):
            print "x_{0}_{1}_{2} +".format(ojciec.name, A[i].name, drzewo),
        print "x_{0}>= {1}".format(ojciec.name, ojciec.min_dep)
    else:
        if ojciec.isNode()==True:
            print "x{0}_{1}_{2}".format(ojciec.__parent__.name, ojciec.name, drzewo),
            przeplyw2(drzewo, ojciec)
            print "-x{0} = 0".format(ojciec.name)
            
def condition2_all(drzewo, ojciec):
    condition2(drzewo, ojciec)
    if ojciec.isNode()==True:
        A=ojciec.getChilds()
        l=len(A)
        for i in range(l):
            condition2_all(drzewo, A[i])
    else:
        print "x{1}_{0}_{2} - x{0} = 0".format(ojciec.name, ojciec.__parent__.name, drzewo)

def subject_to(tab1, tab2):
    print
    print "Subject to"
    condition1_all(0, tab1)
    print 
    print
    condition1_all(1, tab2)
    print
    print
    condition2_all(0, tab1)
    print
    print
    condition2_all(1, tab2)

    
#Bounds
def zlicz(ojciec):
    A=ojciec.getChilds()
    l=len(A)
    sum=0
    for i in range(l):
        sum+=zlicz(A[i])
    k=ojciec.min_dep+sum
    return k

def bound_przeplyw(drzewo, ojciec):
    if ojciec.__parent__!=ojciec.name:
        print "0 <= x_{1}_{0}_{2} <= {3}".format(ojciec.name, ojciec.__parent__.name, drzewo, zlicz(ojciec))

    A=ojciec.getChilds()
    l=len(A)
    for i in range(l):
        bound_przeplyw(drzewo, A[i])
    

def bounds(liczba_pracownikow, tab1, tab2):
    print
    print "Bounds"
    for i in range(liczba_pracownikow):
        a=str(i)
        print '0 <= x' + a + ' <= 1'
    print
    bound_przeplyw(0, tab1)
    print
    bound_przeplyw(1, tab2)
    
#Generals
def general_przeplyw(drzewo, ojciec):
    if ojciec.__parent__!=ojciec.name:
        print "x_{1}_{0}_{2}".format(ojciec.name, ojciec.__parent__.name, drzewo)
    A=ojciec.getChilds()
    l=len(A)
    for i in range(l):
        general_przeplyw(drzewo, A[i])


def generals(liczba_pracownikow, tab1, tab2):
    print
    print "Generals"
    for i in range(liczba_pracownikow):
        a=str(i)
        print 'x' + a
    general_przeplyw(0, tab1)
    general_przeplyw(1, tab2)
    
def problem_liniowy(n, tab):
    A=create_tree_WSA(n, tab)
    B=create_tree_union(n, tab)
    minimal(n)
    subject_to(A, B)
    bounds(n, A, B)
    generals(n, A, B)
    print "End"
    
problem_liniowy(n, tab)
