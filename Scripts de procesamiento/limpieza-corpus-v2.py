import os
import re

# Carpeta de entrada que contiene los archivos de texto sucios
input_folder = 'G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\Nivel 3'

# Carpeta de salida para los archivos de texto limpios
output_folder = 'G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\Nivel 4 - v2'

# Expresión regular para encontrar los caracteres no alfabéticos
non_alpha = re.compile(r'[^a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s\d/]+')

num = 1

# Recorre cada archivo en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        # Abre el archivo de entrada y crea un nuevo archivo de salida
        with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as infile, \
             open(os.path.join(output_folder, filename), 'w', encoding='utf-8') as outfile:
            
            # Recorre cada línea del archivo de entrada
            for line in infile:
                # Elimina los caracteres no alfabéticos de la línea
                line = non_alpha.sub('', line)
                # Escribe la línea limpia en el archivo de salida
                outfile.write(line)
            
            print ("Voy en el archivo ")
            print (num)
            num = num + 1
