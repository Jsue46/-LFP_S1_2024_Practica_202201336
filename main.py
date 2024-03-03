from datetime import datetime
import re
import graphviz


class PetManager:
    def __init__(self):
        self.mascotas = {}

    def ejecutar_comando(self, comando):
        instruccion = comando[0]
        if instruccion == "Crear_Gato":
            self.crear_gato(comando[1])
        elif instruccion == "Dar_de_Comer":
            self.dar_de_comer(*comando[1:])
        elif instruccion == "Jugar":
            self.jugar_con_mascota(*comando[1:])
        elif instruccion == "Resumen_Mascota":
            self.resumen_mascota(comando[1])
        elif instruccion == "Resumen_Global":
            self.resumen_global()

    def crear_gato(self, nombre):
        self.mascotas[nombre] = {"energia": 1, "vivo": True}
        self._escribir_en_archivo("Prueba.petworld_result", f"Se creo el gato {nombre}")

    def dar_de_comer(self, nombre, peso):
        if nombre in self.mascotas:
            energia_aumentada = 12 + int(peso)
            self.mascotas[nombre]["energia"] += energia_aumentada
            if self.mascotas[nombre]["energia"] <= 0:
                self.mascotas[nombre]["vivo"] = False
                self._escribir_en_archivo("Prueba.petworld_result", f"{nombre}: Muy tarde. Ya me morí después de comer.")
            else:
                self._escribir_en_archivo("Prueba.petworld_result", f"{nombre}: Gracias, ahora mi energia es {self.mascotas[nombre]['energia']}")
        else:
            print(f"[{datetime.now()}] No se encontró la mascota con nombre {nombre}")

    def jugar_con_mascota(self, nombre, tiempo):
        if nombre in self.mascotas:
            energia_perdida_por_tiempo = 0  # Valor predeterminado
            if isinstance(tiempo, int):
                energia_perdida_por_tiempo = int(0.1 * tiempo)
            self.mascotas[nombre]["energia"] -= energia_perdida_por_tiempo
            if self.mascotas[nombre]["energia"] <= 0:
                self.mascotas[nombre]["energia"] = 0
                self.mascotas[nombre]["vivo"] = False
                self._escribir_en_archivo("Prueba.petworld_result", f"{nombre}: Muy tarde. Ya me morí después de jugar.")
            else:
                self._escribir_en_archivo("Prueba.petworld_result", f"{nombre}: Gracias por jugar conmigo, ahora mi energia es {self.mascotas[nombre]['energia']}")
        else:
            (f"[{datetime.now()}] No se encontró la mascota con nombre {nombre}")


    def resumen_mascota(self, nombre):
        if nombre in self.mascotas:
            estado = "Vivo" if self.mascotas[nombre]["vivo"] else "Muerto"
            self._escribir_en_archivo("Prueba.petworld_result", f"{nombre}, Energia: {self.mascotas[nombre]['energia']}, Gato, {estado}")
        else:
            print(f"No se encontro la mascota con nombre {nombre}")

    def resumen_global(self):
        resumen = "------------------Resumen Global------------------\n"
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        for nombre, gato in self.mascotas.items():
            estado = "Vivo" if gato["vivo"] else "Muerto"
            resumen += f"[{fecha_actual}] {nombre}, Energia: {gato['energia']}, Gato, {estado}\n"
        self._escribir_en_archivo("Prueba.petworld_result", resumen)
        self.generar_grafico()

    

    
    def generar_grafico(self):
        dot = graphviz.Graph(comment='Prueba')
        dot.attr('node', shape='square', style='filled', fillcolor='lightblue')  
        dot.attr('edge', color='red', style='dashed')  
        for nombre, gato in self.mascotas.items():
            dot.node(nombre, label=nombre)
            dot.node(f"{nombre}_energia", label=f"Energia: {gato['energia']}")
            dot.node(f"{nombre}_tipo", label="Tipo: Gato")
            dot.node(f"{nombre}_estado", label=f"Estado: {'Vivo' if gato['vivo'] else 'Muerto'}")
            dot.edge(nombre, f"{nombre}_energia")
            dot.edge(nombre, f"{nombre}_tipo")
            dot.edge(nombre, f"{nombre}_estado")
        dot.render('Prueba', format='png', cleanup=True)    

    def _escribir_en_archivo(self, nombre_archivo, contenido):
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f"[{fecha_actual}] {contenido}\n")

def leer_archivo(pet_manager):
    prueba = input("Ingresa el nombre del archivo .petworld: ")
    try:
        with open(prueba, 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                comando = re.split(r':|,', linea.strip())
                pet_manager.ejecutar_comando(comando)
    except FileNotFoundError:
        print("El archivo especificado no existe.")


def mostrar_menu_principal():
    print("")
    print("")
    print("===========================================")
    print("         Bienvenido a PetWorld Manager ")
    print("     Lenguajes Formales y de Programación")
    print("                 Sección  A+             ")
    print("                  202201336                   ")
    print("Menú Principal")
    print("1. Ir al módulo PetManager")
    print("2. Salir")
    print("===========================================")
    return input("Ingresa la acción que quieras realizar: ").strip().lower()
    print("")
    print("")

def mostrar_menu_petmanager():
    print("")
    print("")
    print("===========================================")
    print("     Bienvenido a PetWorld Manager ")
    print("Menú PetManager")
    print("1. Cargar archivo ")
    print("2. Salir")
    print("===========================================")
    return input("Ingresa la opción a realizar: ").strip().lower()

def main():
    while True:
        respuesta = mostrar_menu_principal()
        if respuesta == "1":
            respuesta_modulo1 = mostrar_menu_petmanager()
            if respuesta_modulo1 == "1":
                pet_manager = PetManager()  
                leer_archivo(pet_manager)
            elif respuesta_modulo1 == "2":
                print("¡Hasta luego!")
                break
            else:
                print("Respuesta inválida, intenta nuevamente")
        elif respuesta == "2":
            print("¡Hasta luego!")
            break
        else: 
            print("Respuesta no válida. Intenta nuevamente")

if __name__ == "__main__":
    main()
