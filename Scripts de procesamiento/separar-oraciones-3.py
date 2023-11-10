# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:51:37 2023

@author: MARIA
"""

import os
import spacy
import pandas as pd
from nltk.tokenize import sent_tokenize
from spacy.lang.es import Spanish

def separar_oraciones(texto):
    oraciones = sent_tokenize(texto, language='spanish')
    return oraciones

def analizar_oracion(nlp, oracion):
    doc = nlp(oracion)
    agente = ""
    verbo = ""
    paciente = ""
    voz_activa = True

    for token in doc:
        if "subj" in token.dep_:
            agente = token.text
        elif "obj" in token.dep_:
            paciente = token.text
        elif token.pos_ == "VERB":
            verbo = token.text
            voz_activa = "nsubj" in token.dep_

    return agente, verbo, paciente, voz_activa

def procesar_archivos(input_folder, output_folder):
    nlp = spacy.load('es_core_news_sm')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
                texto = f.read()

            oraciones = separar_oraciones(texto)

            data = []
            for oracion in oraciones:
                agente, verbo, paciente, voz_activa = analizar_oracion(nlp, oracion)
                data.append([oracion, agente, verbo, paciente, voz_activa])

            df = pd.DataFrame(data, columns=["Oración", "Agente", "Verbo", "Paciente", "Voz activa"])
            df.to_csv(os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_oraciones.csv"), index=False, encoding='utf-8', sep=';')

if __name__ == "__main__":
    input_folder = "G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\Subcorpus1"
    output_folder = "G:\\Mi unidad\\96 UdeA - RUG\\01 TDG Dora Alzate\\Corpus V2\\Subcorpus1"
    procesar_archivos(input_folder, output_folder)
