import fonctions

if __name__ == '__main__':
    print(fonctions.extraction_nom())
    dictionnaire = fonctions.prenom_nom(fonctions.extraction_nom())
    print(dictionnaire)
