import csv

def guardarPuntaje(nombre, puntaje, rondas):
   
    to_append = [nombre, puntaje, rondas]
    with open("Puntajes.csv", "a", newline="") as record:
        csv_writer = csv.writer(record, delimiter=";")
        csv_writer.writerow(to_append)