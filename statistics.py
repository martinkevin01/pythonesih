##Calcul de moyenne
test=[15,20,45]
def total(done):
    if type(done)==list:
        som=0

        for j in done:
            som+=j
            return som
def moyen(done):
    if type(done)==list:
        return total(done)/len(done)
print("moyen nan se: " +str(moyen(test)))


#calcul variance
def varyans(done):
    if type(done)==list:
        som=0
        for j in done:
            som+=(j-moyen(done))**2
        return som/len(done)
print("varyans lan se: " +str(varyans(test)))                  