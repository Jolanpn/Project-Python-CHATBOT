import os
import math


def list_of_files(directory, extension):
  files_names = []
  for filename in os.listdir(directory):
    if filename.endswith(extension):
      files_names.append(filename)
  return files_names


def extract_names(files_names):
  #liste de sortie pour les noms
  list_names = []
  #boucle for pour gérer chaque item de la liste et retirer le "Nomination_" et ".txt"
  for new_names in files_names:
    new_names = new_names[11:-4]
    #apprend le nom si cela ne se termine ni par 1 ou 2
    if new_names[-1] != '1' and new_names[-1] != '2':
      list_names.append(new_names)
    elif new_names[-1] == '1':
      #permet d'apprendre les noms en double qui se terminent par 1 en enlevant le 1, j'ignore pour ce qu'il       se termine par 2
      new_names = new_names[:-1]
      list_names.append(new_names)
  return list_names


def prenom_nom(
    list_names):  #fonction qui associe a chanque president un prenom
  prenom = ['Jacques', 'Nicolas', 'François', 'Emmanuel', 'Valéry', 'François']
  #dictionnaire pour associer les noms a un prenom
  complete_names = {}
  for i in range(len(prenom)):
    complete_names[list_names[i]] = prenom[i]
  return complete_names


def lower(files_names, directory):
  new_folder = "./cleaned"
  # Créez le nouveau dossier s'il n'existe pas déjà
  if not os.path.exists(new_folder):
    os.makedirs(new_folder)

  for i in range(len(files_names)):
    file_path = os.path.join(directory, files_names[i])
    
    with open(file_path, 'r') as f1:
      new_file_path = os.path.join(new_folder, files_names[i])

      with open(new_file_path, 'w') as f2:
        for ligne in f1:
          f2.write(ligne.lower())
  return True


def clean_char(files_names):
  new_folder = "./cleaned"
  for i in range(len(files_names)):
    file_path = os.path.join(new_folder, files_names[i])
    #changement des fichiers
    with open(file_path, 'r', encoding="utf-8") as f1:
      new_text = f1.read()
      #création d'un dictionnaire pour les caractères spéciaux, la clé pour le caractère, la valeur que nous voulons la clé à être remplacée
      #" ' " auront un espace et les tirets également
      L = {":": "",";": "",",": "","!": "",'"': "","?": "","(": "",")": "",".": "","-": " ","'": " ",}
      for i, j in L.items():
        new_text = new_text.replace(i, j)
      with open(file_path, 'w', encoding="utf-8") as f1:
        f1.write(new_text)

  return True


#Partie TF-IDF
def compteur_mots(chaine):
  occurences = {}
  mots = chaine.split()

  if mots in occurrences:
    occurrences[mots] += 1
  else:
    occurrences[mots] = 1
