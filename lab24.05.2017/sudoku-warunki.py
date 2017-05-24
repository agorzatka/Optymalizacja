
#warunki, że żadna liczba nie powtarza się w wierszu
def wiersz():
    for k in range(9):
        for i in range(9):
            for j in range(9):
                A[j]="X" + str(i)+"_"+str(j)+"_"+str(k)
            print '+'.join(map(str,A))
    return A   
            

#warunki, że liczba nie powtarza się w kolumnie


#warunki, że w każdym małym kwadraciku nie powtarza się liczba
