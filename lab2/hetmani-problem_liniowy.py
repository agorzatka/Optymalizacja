#funkcja do zmaksymalizowania
def function(n):
    print "Maximize"
    for i in range (n):
        for j in range (n):
            if i==n-1 and j==n-1:
                print ("x{0}_{1} ".format(i,j))
                break
            print ("x{0}_{1} ".format(i,j)+'+'),
#ograniczenia wynikające z tego, że w jedym wierszu nie mogą pojawić się dwie wieże
def horizontal(n):
    for i in range (n):
        for j in range (n):
            if j==n-1:
                print ("x{0}_{1} ".format(i,j)+"<= 1")
                break
            print ("x{0}_{1} ".format(i,j)+'+'),

#ograniczenia wynikające z faktu, że w jedej kolumnie nie mogą pojawić się dwie wieże
def vertical(n):
    for i in range (n):
        for j in range (n):
            if j==n-1:
                print ("x{1}_{0} ".format(i,j)+"<= 1")
                break
            print ("x{1}_{0} ".format(i,j)+'+'),
            
#ograniczenia na skosy opadające
def decreasing(n):
    #dolny trójkąt
    for i in range(n):
        j=0
        k=i
        while j!=n-1 and k!=n-1:
            print ("x{0}_{1} ".format(k,j)+'+'),
            j+=1
            k+=1
        print ("x{0}_{1} ".format(k,j)+"<= 1")
    #górny trójkąt
    for i in range(n):
        j=i
        k=0
        while k!=j and j!=n-1 and k!=n-1:
            print ("x{0}_{1} ".format(k,j)+'+'),
            j+=1
            k+=1
        if k!=j:
            print ("x{0}_{1} ".format(k,j)+"<= 1")

#ograniczenia na skosy rosnące
def growing(n):
    #górny trójkąt
    m=n
    while m!=0:
        k=0
        s=m-1
        while k!=n-1 and s!=0:
            print ("x{0}_{1} ".format(s,k)+'+'),
            k+=1
            s-=1
        print ("x{0}_{1} ".format(s,k)+'<=1')
        m-=1
    #dolny trójkąt

    for i in range(n-1):
        s=i+1
        m=n-1
        while s!=n-1 and m!=0:
            print ("x{0}_{1} ".format(m,s)+'+'),
            m-=1
            s+=1
        print ("x{0}_{1}".format(m,s)+'<=1')

#całe subject to
def subject_to(n):
    print "Subject to"
    horizontal(n)
    vertical(n)
    decreasing(n)
    growing(n)
    

#Bounds
def bounds(n):
    print "Bounds"
    for i in range(n):
        for j in range (n):
            a=str(i)
            b=str(j)
            print '0 <= x' + a+'_' + b + ' <= 1'
#Generals            
def generals(n):
    for i in range(n):
        for j in range(n):
            print "x{0}_{1}".format(i,j)
#Problem liniowy dla hetmanów            
def hetmani(n):
    function(n)
    print 
    subject_to(n)
    print
    bounds(n)
    print
    generals(n)