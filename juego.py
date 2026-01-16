#sleep()
from time import sleep


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
        if self.nombre == 'enemigo_fisico':
            self.objetivo.vida  = self.objetivo.vida - self.atk
        elif self.nombre == 'enemigo_especial':
            self.objetivo.vida = self.objetivo.vida - self.atk_sp
    def __repr__(self):
        if self.nombre == 'enemigo_fisico':
            return f'{self.nombre} ha atacado a {self.objetivo.nombre} y le ha hecho {self.atk} de daño dejandolo a {self.objetivo.vida} PS' if self.ataque and self.objetivo else f'Soy {self.nombre}'
        if self.nombre == 'enemigo_especial':
            return f'{self.nombre} ha atacado a {self.objetivo.nombre} y le ha hecho {self.atk_sp} de daño dejandolo a {self.objetivo.vida} PS' if self.ataque and self.objetivo else f'Soy {self.nombre}'

class Fisico(Personaje):
    atk = Personaje.atk*2

class Especial(Personaje):
    atk_sp = Personaje.atk_sp*2


enemigo_fisico = Fisico('enemigo_fisico')
enemigo_especial = Especial('enemigo_especial')
caballero = Fisico('caballero')
mago = Especial('mago')

print('----------------------------')
print(enemigo_especial)

enemigo_especial.atacar(caballero)

print(enemigo_especial)
print('----------------------------')

enemigo_fisico = Fisico('enemigo_fisico')
enemigo_especial = Especial('enemigo_especial')
caballero = Fisico('caballero')
mago = Especial('mago')

print(enemigo_fisico)

enemigo_fisico.atacar(caballero)

print(enemigo_fisico)