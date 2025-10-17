from random import randint
from math import*

class Cbulle:
    def __init__ (self):
        self.xc=randint(0,100)
        self.yc=randint(0,100)
        self.rayon=randint(1,10)
        self.dirx=float(randint(-1,1))
        self.diry=float(randint(-1,1))
        self.couleur=randint(1,65535)
        
    def bouge(self):
        self.xc+=self.dirx
        self.yc+=self.diry
        
    def distanceEntreBulles(self,B):
        return sqrt((self.xc -B.xc)**2+(self.yc -B.yc)**2)
    def compare(self,B):
        if self.rayon>B.rayon:
            return
        
    def __str__(self):
        return f"centre ({self.xc},{self.yc}) de rayon {self.rayon} de couleur {self.couleur} et de vitesse ({self.dirx},{self.diry})"
    
    def bullesEnContact(self,B):
        return self.distanceEntreBulles(B)<=(self.rayon+B.rayon)
        

bulle1=Cbulle()
print(bulle1)
bulle2=Cbulle()
print(bulle2)
bulle3=Cbulle()
print(bulle3)
bulle4=Cbulle()
print(bulle4)
bulle5=Cbulle()
print(bulle5)
bulle6=Cbulle()
print(bulle6)  
mousse=[bulle1,bulle2,bulle3,bulle4,None,bulle6]      

def donnePremierIndiceLibre(mousse):
    i=0
    while i<6 and mousse[i]!= None:
        i=i+1
    return i
k=donnePremierIndiceLibre(mousse)
print(k)
def placeBulle(B):
    k=donnePremierIndiceLibre(mousse)
    mousse[k]=B

placeBulle(bulle5)

print(mousse[k])

"""while not(bulle3.bullesEnContact(bulle4)):
    bulle3.bouge()
    bulle4.bouge()"""
    
 


def collision(indPetite,indGrosse,mousse):
    surfPetite=pi*mousse[indPetite].rayon**2
    surfGrande=pi*mousse[indGrosse].rayon**2
    surfGrosseApresCollision=surfGrande+surfPetite
    mousse[indGrosse].rayon=sqrt(surfGrosseApresCollision/pi)
    mousse[indGrosse].dirx *=0.5
    mousse[indGrosse].diry *=0.5
    
    mousse[indPetite]=None
    
    
    
    
print(bulle1.bullesEnContact(bulle2))
collision(2,3,mousse)
print(donnePremierIndiceLibre(mousse))
    