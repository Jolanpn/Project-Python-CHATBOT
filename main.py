from fonctions import *

if __name__ == '__main__':
  #directoire où se trouve les fichiers txt Ouais tu as raisons je modif pour le directory
  directory = "./speeches-20231107"
  files_names = list_of_files(directory, "txt")
  list_names = extract_names(files_names)
  print(prenom_nom(list_names))
  lower(files_names, directory)
  clean_char(files_names)
while True:

  user_choice = int(
      input(
          "Entrer un chiffre entre 1 et 6 afin d'accéder aux fonctions ci-dessous:\n"
          "1. La liste des mots les moins importants\n"
          "2. Les mots ayant le score TF-IDF le plus élevé\n"
          "3. Les mots les plus répétés par le président Chirac\n"
          "4. Les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois\n"
          "5. Le premier président à parler du climat et/ou de l'écologie\n"
          "6. Les mots que tous les présidents ont évoqués hormis ceux non importants\n"
          "0. Quitter le programme\n"))
  #pour sortir du programme et du menu
  if user_choice == 0:
    exit()

  if user_choice == 1:
    print(mots_non_importants(directory))

  elif user_choice == 2:
    print(mots_plus_importants(directory))

  elif user_choice == 3:
    print(mots_plus_repetes_chirac(directory))

  elif user_choice == 4:
    print(
        "La première valeur est le président parlant le plus de la nation et le dictionnaire de clé est la liste des présidents utilisant ce mot"
    )
    print(president_parlant_de_nation(directory))

  elif user_choice == 5:
    print("le premier président à parler du climat ou de l'écologie est : ",
          premier_president_climat_ecologie(directory))

  elif user_choice == 6:
    print(mots_evoques_par_tous(directory))

  else:
    print("Veuillez entre une chiffre entre 1 et 6")
