# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:20:29 2022

@author: danil
"""


from io import open
import os
import time
from clases import Futbolista, Medico, Entrenador



######################################################
#   LISTAS DE ALAMACENAMIENTO DE OBJETOS Y FICHEROS  #
######################################################



miembrosFutbolistas = []
miembrosMedicos = []
miembrosEntrenadores = []
miembros = [miembrosFutbolistas, miembrosMedicos, miembrosEntrenadores]

fichero_opt = open("opciones.txt", "r")  #  Opciones para el menu
fichero_read = open("data.txt", "a+")   #   Fichero para guardar datos



##############################
#   RECUPERAR OBJETOS DATE   #
##############################


def asset(datos):
    print(datos)
    for element in datos:
        values = element.split("-")
        print("Miembro encontrado...")
        time.sleep(1)
        print(values)
        if values[0] == "Futbolista":
            print("Guardando...")
            time.sleep(1)
            print("Incluido!")
            miembrosFutbolistas.append(Futbolista(values[1], values[2], int(values[3]), int(values[4]), values[5]))
        if values[0] == "Medico":
            print("Guardando...")
            time.sleep(1)
            print("Incluido!")
            miembrosMedicos.append(Medico(values[1], values[2], int(values[3]), values[4], int(values[5])))
        if values[0] == "Entrenador":
            print("Guardando...")
            time.sleep(1)
            print("Incluido!")
            miembrosEntrenadores.append(Entrenador(values[1], values[2], int(values[3]), values[4]))



def recover():
    print("CARGANDO BASE DE DATOS DE MIEMBROS...")
    time.sleep(1)
    fichero_read.seek(0)
    asset(fichero_read)


#####################################
#   MENU SECUNDARIO DE AGREGACION   #
#####################################



def addFutbolista():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    dorsal = int(input("Dorsal: "))
    posicion = input("Posicion: ")

    miembrosFutbolistas.append(Futbolista(nombre, apellido, edad, dorsal, posicion))
    time.sleep(3)


def addMedico():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    experiencia = int(input("Experiencia: "))
    titulacion = input("Titulacion: ")

    miembrosFutbolistas.append(Medico(nombre, apellido, edad, titulacion, experiencia))
    time.sleep(3)


def addEntrenador():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    estrategia = input("Estrategia: ")

    miembrosFutbolistas.append(Entrenador(nombre, apellido, edad, estrategia))
    time.sleep(3)


def removeMembers(fichero):
    fichero.close()
    fichero = open("data.txt", "w")
    fichero.close()
    fichero = open("data.txt", "a+")


def removeObjets():
    miembrosFutbolistas.clear()
    miembrosMedicos.clear()
    miembrosEntrenadores.clear()




###################################
#   MENU PRINCIPAL DE SELECCION   #
###################################


def viajarEquipo():
    print()
    for listMiembro in miembros:
        for miembro in listMiembro:
            print(type(miembro).__name__ + ": " + miembro.getNombre() + " " +
                  miembro.getApellido() + " -> " + miembro.viajar())
            
    input("\nPulse una tecla para continuar...")


def entrenamientoEquipo():
    print()
    for listMiembro in miembros:
        for miembro in listMiembro:
            print(type(miembro).__name__ + ": " + miembro.getNombre() + " " +
                  miembro.getApellido() + " -> " + miembro.entrenamiento())
            
    input("\nPulse una tecla para continuar...")


def partidoEquipo():
    print()
    for listMiembro in miembros:
        for miembro in listMiembro:
            print(type(miembro).__name__ + ": " + miembro.getNombre() + " " +
                  miembro.getApellido() + " -> " + miembro.partidoFutbol())
            
    input("\nPulse una tecla para continuar...")


def planificarEntrenamiento():
    print()
    for listMiembro in miembros:
        for miembro in listMiembro:
            if type(miembro).__name__ == "Entrenador":
                print(type(miembro).__name__ + ": " + miembro.getNombre() +
                      " " + miembro.getApellido() + " -> " + miembro.planificarEntrenamiento())
                
    input("\nPulse una tecla para continuar...")                
     
           
def entrevistaEquipo():
    print()
    for listMiembro in miembros:
        for miembro in listMiembro:
            if type(miembro).__name__ == "Futbolista":
                print(type(miembro).__name__ + ": " + miembro.getNombre() +
                      " " + miembro.getApellido() + " -> " + miembro.entrevista())
                
    input("\nPulse una tecla para continuar...")


def curarEquipo():
    print()
    for listMiembro in miembros:
        for miembro in listMiembro:
            if type(miembro).__name__ == "Medico":
                print(type(miembro).__name__ + ": " + miembro.getNombre() +
                      " " + miembro.getApellido() + " -> " + miembro.curarLesion())
                
    input("\nPulse una tecla para continuar...")
    


##################################
#   MENU SELECCION DE OPCIONES   #
##################################

def title(tit):
    os.system("cls")
    print()
    os.system(f"title {tit}")

def recursosHumanos():
    title("RECURSOS HUMANOS")
    print("""1. Agregar un Jugador.
2. Agregar un Medico.
3. Agregar un Entrenador.
4. Eliminar miembros (Listas)

5. Cargar base de datos de miembros.
6. Limpiar base de datos.

7. Ir al MENU PRINCIPAL.""")
         
    option = int(input("\n\nOpcion: "))
    
    if option == 1:
        addFutbolista()
    elif option == 2:
        addMedico()
    elif option == 3:
        addEntrenador()
    elif option == 4:
        removeObjets()
    elif option == 5:
        recover()
    elif option == 6:
        removeMembers(fichero_read)
    elif option == 7:
        return
    else:
        print("Opcion no disponible")


def menuOpciones(option):
    if option == 1:
        viajarEquipo()
    if option == 2:
        entrenamientoEquipo()
    if option == 3:
        partidoEquipo()
    if option == 4:
        planificarEntrenamiento()        
    if option == 5:
        entrevistaEquipo()
    if option == 6:
        curarEquipo()
    elif option == 7:
        recursosHumanos()



def menu(fichero):
    title("MENU DE INICIO")
    for i, option in enumerate(fichero):
        print(str(i+1) + ". " + option, end="")
    return int(input("\n\nOpcion: "))



############################
#   GUARDAR OBJETOS DATE   #
############################
        


def save(ptr):
    ptr.close()
    ptr = open("data.txt", "w")
    ptr.seek(0)
    for listMiembro in miembros:
        for miembro in listMiembro:
            if type(miembro).__name__ == "Futbolista":
                    m = (type(miembro).__name__ + "-" + miembro.getNombre() + "-" + miembro.getApellido() +
                     "-" + str(miembro.getEdad()) + "-" + str(miembro.getDorsal()) + "-" + miembro.getPosicion() + "-\n")
            elif type(miembro).__name__ == "Medico":
                    m = (type(miembro).__name__ + "-" + miembro.getNombre() + "-" + miembro.getApellido() +
                     "-" + str(miembro.getEdad()) + "-" + miembro.getTitulacion() + "-" + str(miembro.getExperiencia()) + "-\n")
            elif type(miembro).__name__ == "Entrenador":
                    m = (type(miembro).__name__ + "-" + miembro.getNombre() + "-" + miembro.getApellido() +
                     "-" + str(miembro.getEdad()) + "-" + miembro.getEstrategia() + "-\n")
           
            ptr.write(m)



##############
#   "MAIN"   #
##############





try:
    while(True):
        fichero_opt.seek(0)
        option = menu(fichero_opt)
        if(option == 8):
            break
        menuOpciones(option)
except KeyboardInterrupt:
    save(fichero_read)
    fichero_opt.close()
    print("\n\nPrograma finalizado forzosamente")
    


#################################################
#   GUARDAR DATOS Y CERRAR PUNTEROS A FICHERO   #
#################################################



save(fichero_read)
fichero_opt.close()
    
    
