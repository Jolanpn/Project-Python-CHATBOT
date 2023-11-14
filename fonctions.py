import os
import math

def extraction_nom():
    #obtenir la liste des noms des documents dans le dossier
    repertoire = '/Users/renkang/Documents/EFREI/python/projet/speeches-20231107'
    L = os.listdir(repertoire)
    #retirer Nomination_ et .txt
    for i in range(len(L)):
        L[i] = L[i][11:-4]
    #alternative, faire une nouvelle liste au lieu de supprimer etc...
    #Enlever les 1 et 2 à la fin des éléments de la liste
    for i in range(len(L)):
        if L[i][-1] == '1' :
            L[i] = L[i][:-1]
        if L[i][-1] == '2' :
            del L[i]
    return L

def prenom_nom(L):
    prenom = ['Valéry','François','Nicolas','Jacques','Emmanuel','François']
    end = {}
    minimum = min(len(L), len(prenom))
    for i in range(minimum):
        end[prenom[i]] = L[i]
    return end
