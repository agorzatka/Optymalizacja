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
