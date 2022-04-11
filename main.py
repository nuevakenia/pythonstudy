from ast import Pass
import random
from this import s

enemigos = []




class Personaje:

    def __init__(self,id, nombre, nivel, fuerza,defensa,vida, vida_actual, exp, en_batalla):
        """Constructor de clase Personaje"""
        self.__id = id
        self.__nivel = nivel
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__defensa = defensa
        self.__vida = vida
        self.__vida_actual = vida_actual
        self.__exp = exp
        self.__en_batalla = en_batalla
    

 # GETTERS
 #  
    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        
        return self.__nombre
    
    def get_nivel(self):
        
        return self.__nivel

    def get_fuerza(self):
        
        return self.__fuerza

    def get_defensa(self):
        
        return self.__defensa
    
    def get_vida(self):
        
        return self.__vida

    def get_vida_actual(self):
        
        return self.__vida_actual
    
    def get_exp(self):
        
        return self.__exp

# SETTERS
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_vida(self, vida):
        self.__vida = vida
    
    def set_vida_actual(self, vida_actual):
        self.__vida_actual = vida_actual

    def set_fuerza(self, fuerza):
        self.__fuerza = fuerza

    def set_exp(self, exp):
        self.__exp = exp
    
    def set_nivel(self, nivel):
        self.__nivel = nivel


# OTROS
    def batalla(self):
        print("Bienvenido a la batalla")
        print("LISTA ENEMIGOS: ", enemigos)
        selector = random.randint(0, len(enemigos))
        print("Enemigo: ",selector)
        enemy = enemigos[selector-1]
        print("Enemigo: ", enemy )
        menu_batalla(self,enemy)
        resultado = []

        return resultado

    def entrar_dungeon(self,personaje,nivel):
        if nivel >= 2 or self.__en_batalla:
            print("Entraste al dungeon")
            self.__en_batalla = True
            self.batalla()
        else:
            print("no puedes entrar, necesitas nivel 2 o mas")
        pass
    
 
    

class Enemigo(Personaje):
    def __init__(self, nombre, nivel, fuerza,defensa, vida,vida_actual,exp):
        """Constructor de clase Personaje"""
        self.__nivel = nivel
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__defensa = defensa
        self.__vida = vida
        self.__vida_actual = vida_actual
        self.__exp = exp

     # GETTERS
 #        
    def get_nombre(self):
        
        return self.__nombre
    
    def get_nivel(self):
        
        return self.__nivel

    def get_fuerza(self):
        
        return self.__fuerza

    def get_defensa(self):
        
        return self.__defensa
    
    def get_vida(self):
        
        return self.__vida

    def get_vida_actual(self):
        
        return self.__vida_actual

    def get_exp(self):
        
        return self.__exp


    def __str__(self):
        return f'{self.__nombre}({self.__nivel})'
        #return "{self.nombre}({self.nivel})".format(self=self)
# SETTERS
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_vida(self, vida):
        self.__vida = vida
    
    def set_vida_actual(self, vida_actual):
        self.__vida_actual = vida_actual

    def set_fuerza(self, fuerza):
        self.__fuerza = fuerza

    def set_exp(self, exp):
        self.__exp = exp

    def set_nivel(self, nivel):
        self.__nivel = nivel

class Item:
    def __init__(self, id,nombre, nivel,precio):
        self.__id = id
        self.__nivel = nivel
        self.__nombre = nombre
        self.__precio = precio

    def __str__(self):
        return f'{self.__nombre}({self.__nivel}) {self.__precio}$'

class Equipo(Item):
    def __init__(self, id,nombre, nivel,precio,fuerza,defensa,vida):
        self.__id = id
        self.__nivel = nivel
        self.__nombre = nombre
        self.__precio = precio
        self.__fuerza = fuerza
        self.__defensa = defensa
        self.__vida = vida

    def __str__(self):
        return f'{self.__nombre}({self.__nivel}) ${self.__precio} Fuerza({self.__fuerza}) Defensa({self.__defensa}) HP({self.__vida})'

class Consumible(Item):
    def __init__(self, id,nombre, nivel,precio, vida):
        self.__id = id
        self.__nivel = nivel
        self.__nombre = nombre
        self.__precio = precio
        self.__vida = vida
    def __str__(self):
        #vals = super().__str__()
        return f'{self.__nombre}({self.__nivel}) ${self.__precio} HP({self.__vida})'
    
    def consumir():
        
    def get_lista_items(self):
        
        return self.__lista_items
        
        
    
class Inventario:
    def __init__(self, id,personaje_id, espacios,lista_items):
        self.__id = id
        self.__personaje_id = personaje_id
        self.__espacios = espacios
        self.__lista_items = lista_items

    def ver_inventario(inventario):
        lista = inventario.get_lista_items()
        for x in lista:
            print("\n Item: ",x)
        print("\n ___________\n")
        
        pass    

    def eliminar_item():
        pass

    def recoger_item():
        pass

    def get_lista_items(self):
        
        return self.__lista_items

# METODOS GENERALES
    
def defender(personaje,enemigo,ataque,turno):
    dado_def = random.randint(0, 2)
    
    if turno == True:
        # true = jugador Ataca
        defensa = enemigo.get_defensa()
        print("defensa: ",defensa)
        defensa += dado_def
        vida = enemigo.get_vida_actual()
        vida -= (ataque - defensa)
        print(enemigo.get_nombre()," Defendió con ", defensa," de escudo!")
        print(personaje.get_nombre(), "Atacó con ",ataque-defensa," de daño directo!")
        enemigo.set_vida_actual(vida)
        print("El enemigo tiene: ",enemigo.get_vida_actual()," de HP!")
        if enemigo.get_vida_actual() <= 0:
            ganador = True
            resolucion(personaje,enemigo,ataque,defensa,vida,ganador)
        else:
            turno = False
            atacar(personaje,enemigo,turno)  

    else:
        # false = enemigo Ataca
        defensa = personaje.get_defensa()
        print("defensa: ",defensa)
        defensa += dado_def
        vida = personaje.get_vida_actual()
        vida -= (ataque - defensa)
        print(personaje.get_nombre()," Defendió con ", defensa," de escudo!")
        print(enemigo.get_nombre(), "Atacó con ",ataque-defensa," de daño directo!")
        personaje.set_vida_actual(vida)
        print("Tienes: ",personaje.get_vida_actual()," de HP!")
        if personaje.get_vida_actual() <= 0:
            ganador = False
            resolucion(personaje,enemigo,ataque,defensa,vida,ganador)
        else:
            turno = True
            menu_batalla(personaje,enemigo)

      
def atacar(personaje,enemigo,turno):
    dado_atk = random.randint(0, 6)
    if turno:
        ataque = personaje.get_fuerza()
        ataque += dado_atk
        print(personaje.get_nombre()," Atacó con ", ataque," de daño!")  
        defender(personaje,enemigo,ataque,turno)
    else:
        ataque = enemigo.get_fuerza()
        ataque += dado_atk
        print(enemigo.get_nombre()," Atacó con ", ataque," de daño!")  

        defender(personaje,enemigo,ataque,turno)

def resolucion(personaje,enemigo,ataque,defensa,vida,ganador):
    
    if ganador:
        exp = personaje.get_exp()
        print(enemigo.get_nombre()," Ha Muerto!")
        print(enemigo.get_nombre()," Defendió con ", defensa," de escudo!")
        print(enemigo.get_nombre(), "Recibió ",ataque-defensa," de daño directo!")
        print(enemigo.get_nombre(), " tiene ", vida," de vida!")
        print("GANASTE! {0} puntos de Experiencia!".format(enemigo.get_exp()))
        personaje.set_exp(exp+enemigo.get_exp())
        print("Total Experiencia: ",personaje.get_exp())
        enemigo.set_vida_actual(enemigo.get_vida)
        exp_check(personaje)
    else:
        print(personaje.get_nombre()," Ha Muerto!")
        print(personaje.get_nombre()," Defendió con ", defensa," de escudo!")
        print(personaje.get_nombre(), "Recibió ",ataque-defensa," de daño directo!")
        print(personaje.get_nombre(), " tiene ", vida," de vida!")

    menu_principal(personaje)    

def respawn():
    pass



def exp_check(personaje):
    levels = [10, 20, 40, 60, 90,110,140,180,220,270,330,400,550,720,950,1200]
    exp = personaje.get_exp()
    lvl = len([x for x in levels if exp >x])
    personaje.set_nivel(lvl)
    print("Tu nivel es: ", personaje.get_nivel())
    menu_principal(personaje)
    pass

def menu_batalla(personaje,enemigo):
    
    print(":::: MENU BATALLA ::::")
    print("1:Atacar")
    print("2:Defender")
    print("3:Usar Item")
    print("4:Huir")
    print("_________")
    input_batalla = int(input())
    print(input_batalla)
    if input_batalla == 1:
        print("x")
        turno = True
        atacar(personaje,enemigo,turno) 
        
    if input_batalla == 2:
        dado_def = random.randint(0, 1)
    if input_batalla == 3:
        inventario = pj1_inv
        inventario.ver_inventario()
    if input_batalla == 4:
        print("Huiste como una gallina")
        menu_principal(personaje)
    return    

def menu_principal(personaje):
    
    print(":::: MENU PRINCIPAL ::::")
    print("1:Stats")
    print("2:Entrar a Dungeon")
    print("3:Tienda")
    print("4:Descansar")
    print("_________")
    input_principal = int(input())
    print(input_principal)
    if input_principal == 1:
        stats(personaje)
    if input_principal == 2:
        personaje.entrar_dungeon(personaje,personaje.get_nivel())
    if input_principal == 4:
        print("zzzzz Descansando zzzzzz")
        hp = personaje.get_vida()
        print("Tu vida era de: ",personaje.get_vida_actual()," HP")
        personaje.set_vida_actual(hp)
        print("Tu vida actual es: ",personaje.get_vida_actual()," HP")
    return    

def stats(personaje):
    print("\n_________\n")
    print(":::: STATS ::::")
    print(":: ",personaje.get_nombre()," ::")
    print("::Nivel: ",personaje.get_nivel()," ::")
    print("::Fuerza: ",personaje.get_fuerza()," ::")
    print("::Vida Máxima: ",personaje.get_vida()," ::")
    print("::Vida Actual: ",personaje.get_vida_actual()," ::")
    print("::Experiencia: ",personaje.get_exp()," ::")
    print("\n_________\n")
    print(":::: Inventario ::::\n")
    inventario = pj1_inv
    inventario.ver_inventario()
    print("\n_________\n")
    menu_principal(personaje)
        
    return  

enemigo1 = Enemigo("Duende",1,2,2,6,6,3)
enemigo2 = Enemigo("Orco",2,3,3,7,7,6)
enemigo3 = Enemigo("Warlord",3,5,6,15,15,10)

enemigos.append(enemigo1)
enemigos.append(enemigo2)
enemigos.append(enemigo3)

posion1 = Consumible(2,"posion 1",2,10,10)
posion2 = Consumible(3,"posion 2",2,10,5)
espada1 = Equipo(1,"Espada 1",2,5,3,0,10)
pj1 = Personaje(1,"perro 423424",3,4,1,15,15,40,False)
pj1_inv = Inventario(1,1,5,[posion1,posion2,espada1])



pj1.set_nombre("RAUL")

menu_principal(pj1)






