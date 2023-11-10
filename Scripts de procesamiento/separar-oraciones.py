# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:36:36 2023

@author: MARIA
"""

import os
import nltk
from nltk.tokenize import sent_tokenize

# Descargar el paquete 'punkt' para tokenizar oraciones
nltk.download('punkt')

def separar_oraciones(texto):
    oraciones = sent_tokenize(texto, language='spanish')
    return oraciones

def leer_archivo_txt(input_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

def guardar_archivo_txt(oraciones, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for oracion in oraciones:
            file.write(oracion + '\n\n')

# Cambia esta ruta a la de la carpeta donde se encuentran tus archivos de texto plano
input_folder = "G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\Subcorpus1"

# Cambia esta ruta a la de la carpeta donde deseas guardar los archivos de salida
output_folder = input_folder

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, f"output_{filename}")

        # Leer el archivo de texto plano
        texto = leer_archivo_txt(input_file_path)

        # Separar el texto en oraciones
        oraciones = separar_oraciones(texto)

        # Guardar el nuevo archivo con las oraciones separadas por un enter
        guardar_archivo_txt(oraciones, output_file_path)

        print(f"Procesado y guardado: {output_file_path}")
