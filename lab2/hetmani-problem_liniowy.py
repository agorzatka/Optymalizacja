

def function(n):
    print "Maximize"
    for i in range (n):
        for j in range (n):
            if i==n-1 and j==n-1:
                print ("x{0}{1}".format(i,j))
                break
            print ("x{0}{1}".format(i,j)+'+'),

def horizontal(n):
    for i in range (n):
        for j in range (n):
            if j==n-1:
                print ("x{0}{1}".format(i,j)+"<=1")
                break
            print ("x{0}{1}".format(i,j)+'+'),


def vertical(n):
    for i in range (n):
        for j in range (n):
            if j==n-1:
                print ("x{1}{0}".format(i,j)+"<=1")
                break
            print ("x{1}{0}".format(i,j)+'+'),
            

def decreasing(n):
    #dolny trójkąt
    for i in range(n):
        j=0
        k=i
        while j!=n-1 and k!=n-1:
            print ("x{0}{1}".format(k,j)+'+'),
            j+=1
            k+=1
        print ("x{0}{1}".format(k,j)+"<=1")
    #górny trójkąt
    for i in range(n):
        j=i
        k=0
        while k!=j and j!=n-1 and k!=n-1:
            print ("x{0}{1}".format(k,j)+'+'),
            j+=1
            k+=1
        if k!=j:
            print ("x{0}{1}".format(k,j)+"<=1")

decreasing(4)

def subject_to(n):
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
            print '0<=x' + a + b + '<=1'
            
def hetmani(n):
    function(n)
    print 
    bounds(n)
