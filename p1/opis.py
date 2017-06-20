
#PUNKT 1
def potencjalne_zmienne(ss, z):
	return list(ss.possible_entering()).index(z)

# funkcja pomocnicza: wszystkie współczynniki w funkcji celu zmiennych wcześniej wybranych
def coef(ss, z):
    return ss.objective_coefficients()[potencjalne_zmienne(ss,z)]

# funkcja pomocnicza: wybór zmiennych bazowych
def potencjalne_zmienne_b(ss, z):
	return ss.possible_leaving().index(z)

# funkcja pomocnicza: wszystkie współczynniki w funkcji celu zmiennych wcześniej wybranych
def coef_b(ss, z):
    return ss.objective_coefficients()[potencjalne_zmienne_b(ss,z)]

#Pkt 1: Wybór zmiennej o największym wspołczynniku funkcji celu

# Wybór zmiennej o największym wspołczynniku funkcji celu
def largest_coefficient_leaving(self):
    return max(self.possible_leaving(), key=(lambda x: coef_b(self, x) ) )

# Wybór zmiennej o największym wspołczynniku funkcji celu
def largest_coefficient_entering(self):
    return max(self.possible_entering(), key=(lambda x: coef(self, x) ) )

#Punkt 1:
#funkcja potencjalne_zmienne zwraca indeksy zmiennych wchodzących (a raczej za każdym razem jednej)
#funkcja coef zwraca współczynnik funkcji celu dla danej zmiennej wchodzącej
#funkcja largest_coefficient zwraca zmienną o najwiekszym współćzynniku w funkcji celu
#.......
#Teraz jeśli chodzi o nazwy
#Dla zmiennych entering:
#potencjalne_zmienne(self, z), coef(self,z), largest_coefficient_entering(self)
#Dla zmiennych wychodzących:
#potencjalne_zmienne_b(ss,z), coef_b(self,z), largest_coefficient_entering(self)
#...........................................................................

#PUNKT 5
# Zad 5: Wybór losowego elementu (prawdopodobieństwo jednostajne):
#wybór losowy zmiennej
def random_edge_entering(self):
	return list(self.possible_entering())[randrange(len(self.possible_entering()))]

def random_edge_leaving(self):
	return list(self.possible_leaving())[randrange(len(self.possible_leaving()))]
#funckja z listy zmiennych wchodzących/wychodzących wybiera element z listy tak, że patrzy na ilość odpowiednich zmiennych i wywołuje dla nich funkcje randrange
#...............................................................................

#WŁASNE FUNKCJE:
#1. Wybór zmiennej o najmniejszym współczynniku w funkcji celu

# funkcja pomocnicza: wybór mozliwych zmiennych
def p_z_e(ss, z):
	return list(ss.possible_entering()).index(z)

# funkcja pomocnicza: współczynnik dla danej zmiennej
def c_e(ss, z):
    return ss.objective_coefficients()[p_z_e(ss,z)]

# Wybór zmiennej o najmniejszym wspołczynniku funkcji celu
def smallest_coefficient_entering(self):
    return min(self.possible_entering(), key=(lambda x: c_e(self, x) ) )

# funkcja pomocnicza: zmienne wychodzące
def p_z_l(ss, z):
	return ss.possible_leaving().index(z)

# funkcja pomocnicza: współczynnik w funckji celu dla danej zmiennej wchodzącej
def c_l(ss, z):
    return ss.objective_coefficients()[p_z_l(ss,z)]

# Wybór zmiennej o najmniejszym wspołczynniku funkcji celu
def smallest_coefficient_leaving(self):
    return min(self.possible_leaving(), key=(lambda x: c_l(self, x) ) )
#Funkcje podobnie jak przy największym współczynniku
#p_z_e lub p_z_l zwraca indeks zmiennej wchodzącej (p_z_e) lub zmiennej wychodzącej (p_z_l)
#c_e lub c_l zwraca współczynnik funkcji celu dla zmiennej odpowiednio wchodzącej lub wychodzącej
# smallest_coefficient_... bierze minimum po współczynnikach odpowiednich zmiennych i je zwraca
