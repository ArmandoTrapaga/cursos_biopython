class animal():
  nombre = ''
  edad = 0
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def hacer_ruido(self):
    """Este método imprime el sonido característico del animal."""
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH')

class perro(animal):
  def hacer_ruido(self):
    print('Guau Guau')

class gato(animal):
  usa_arenero = True
  def hacer_ruido(self):
    print('Meaw Meaw')

senna = gato('Senna', 1)
senna.usa_arenero
print(senna.__dict__)
print(senna.usa_arenero)
senna.hacer_ruido()

freya = perro('Freya', 7)
print(freya.__dict__)
freya.hacer_ruido()