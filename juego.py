#sleep()
from time import sleep
import os


class Personaje():
    vida = 100
    atk = 10
    atk_sp = 15
    ataque = False
    def __init__(self,nombre='enemigo'):
        self.nombre = nombre
        self.objetivo = None
    def atacar(self,objetivo):
        self.ataque = True
        self.objetivo = objetivo
        if self.nombre == 'campesino':
            self.objetivo.vida  = self.objetivo.vida - self.atk
        elif self.nombre == 'caballero':
            self.objetivo.vida  = self.objetivo.vida - self.atk
        elif self.nombre == 'mago':
            self.objetivo.vida = self.objetivo.vida - self.atk_sp
    def __repr__(self):
        if self.nombre == 'campesino':
            return f'{self.nombre} ha atacado a {self.objetivo.nombre} y le ha hecho {self.atk} de daño dejandolo a {self.objetivo.vida} PS' if self.ataque and self.objetivo else f'Soy {self.nombre}'
        elif self.nombre == 'caballero':
            return f'{self.nombre} ha atacado a {self.objetivo.nombre} y le ha hecho {self.atk} de daño dejandolo a {self.objetivo.vida} PS' if self.ataque and self.objetivo else f'Soy {self.nombre}'
        elif self.nombre == 'mago':
            return f'{self.nombre} ha atacado a {self.objetivo.nombre} y le ha hecho {self.atk_sp} de daño dejandolo a {self.objetivo.vida} PS' if self.ataque and self.objetivo else f'Soy {self.nombre}'

class Fisico(Personaje):
    atk = Personaje.atk*2

class Especial(Personaje):
    atk_sp = Personaje.atk_sp*2

campesino = Personaje('campesino')
caballero_enemigo = Fisico('caballero_enemigo')
brujo = Especial('brujo')
caballero = Fisico('caballero')
mago = Especial('mago')

while True:
    try:
        print('1. Caballero')
        print('2. Mago')
        print('3. Campesino')
        elegir = int(input('Elige uno de los tres personajes jugables (1/2/3): '))

        if elegir==1:
            elegir=caballero
            break
        elif elegir==2:
            elegir=mago
            break
        elif elegir==3:
            elegir=campesino
            break
        else:
            print('Solo puedes elegir 1, 2 o 3 idiota')
            sleep(1)
            os.system('cls')
    except:
        print('Solo puedes elegir 1, 2 o 3 idiota')
        sleep(1)
        os.system('cls')

print('----------------------------')

while True:
    try:
        print('1. Caballero Enemigo')
        print('2. Brujo')
        elegir2 = int(input('Elige uno de los dos enemigos para enfrentarte (1/2): '))

        if elegir2==1:
            elegir2=caballero_enemigo
            break
        elif elegir2==2:
            elegir2=brujo
            break
        else:
            print('Solo puedes elegir 1 o 2 idiota')
            sleep(1)
            os.system('cls')
    except:
        print('Solo puedes elegir 1 o 2 idiota')
        sleep(1)
        os.system('cls')

print('')
print(f'Eres {elegir.nombre} y te vas a enfrentar a {elegir2.nombre} que tiene {elegir2.vida}')

print('      -------------         ')
print('----------------------------')
while True:
    if elegir2.vida>0:
        print(elegir)
        elegir.atacar(elegir2)
    else:
        print(f'{elegir.nombre} ha derrotado a {elegir2.nombre}')
        break
    print('----------------------------')
print('      -------------         ')