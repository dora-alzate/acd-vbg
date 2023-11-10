# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:36:20 2023

@author: MARIA
"""

import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

# Descarga los datos de NLTK si no se han descargado previamente
nltk.download('punkt')
nltk.download('stopwords')

def identify_topic(line):
    stop_words = set(stopwords.words("spanish"))
    words = word_tokenize(line)
    
    # Filtra las palabras que no sean stopwords y que sean alfabéticas
    filtered_words = [word.lower() for word in words if word.isalpha() and word not in stop_words]
    
    # Cuenta la frecuencia de las palabras y devuelve la palabra más común como tema
    word_freq = Counter(filtered_words)
    most_common_word = word_freq.most_common(1)
    
    if most_common_word:
        return most_common_word[0][0]
    else:
        return "Unknown"

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile, delimiter=';')
        csv_writer.writerow(['Line', 'Topic'])
        
        for line in infile:
            line = line.strip()
            if line:
                topic = identify_topic(line)
                csv_writer.writerow([line, topic])

if __name__ == '__main__':
    input_file = 'G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\temas\\temas.txt'  # Asegúrate de reemplazar esto con la ruta a tu archivo de entrada
    output_file = 'G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\temas\\output_csv.csv'  # Asegúrate de reemplazar esto con la ruta a tu archivo de salida
    process_file(input_file, output_file)

    