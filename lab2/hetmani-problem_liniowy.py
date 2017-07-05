

def function(n):
    print "Maximize"
    for i in range (n):
        for j in range (n):
            if i==n-1 and j==n-1:
                print ("x{0}{1}".format(i,j))
                break
            print ("x{0}{1}".format(i,j)+'+'),
function(5)

def subject_to(n):
    horizontal(n)
    vertical(n)
    decreasing(n)
    

#Bounds
def bounds(n):
    print "Bounds"
    for i in range(n):
        for j in range (n):
            a=str(i)
            b=str(j)
            print '0<=x' + a + b + '<=1'
            
bounds(5)
def hetmani(n):
    function(n)
    print 
    bounds(n)
