#oddzielenie punktów białych od czarnych

#Dane problemu
B=[(1,6),(1,5),(2,4),(3,5)]
C=[(3,1),(4,1),(6,3),(7,2)]

#rozwiązanie problemu

delta = MixedIntegerLinearProgram()
a,b,c = delta.new_variable(real=True), delta.new_variable(real=True), delta.new_variable(real=True)

def warunkiB (B):
    for i in range(3):
       x=B[i,0], y=B[i,1]
    delta.add_constraint(a*x+b*y+c>delta)
    
def warunkiC (C):
    for i in range(3):
       x=C[i,0], y=C[i,1]
    delta.add_constraint(a*x+b*y+c<-delta)
    
warunkiB(B)
warunkiC(C)
    
#rozwiazanie problemu

delta.solve()
round(delta.get_values(a))
round(delta.get_values(b))
round(delta.get_values(c))
