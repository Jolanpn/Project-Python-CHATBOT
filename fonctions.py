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
      #permet d'apprendre les noms en double qui se terminent par 1
      #en enlevant le 1, j'ignore pour ce qu'il se termine par 2
      new_names = new_names[:-1]
      list_names.append(new_names)
  return list_names


def prenom_nom(list_names):
  #fonction qui associe a chanque president un prenom
  prenom = ['Jacques', 'Nicolas', 'François', 'Emmanuel', 'Valéry', 'François']
  #dictionnaire pour associer les noms a un prenom
  complete_names = {}
  for i in range(len(prenom)):
    complete_names[list_names[i]] = prenom[i]
  return complete_names


#converti tous les fichiers textes en minuscules
def lower(files_names, directory):
  new_folder = "./cleaned"
  # Créez le nouveau dossier s'il n'existe pas déjà
  if not os.path.exists(new_folder):
    os.makedirs(new_folder)

  for i in range(len(files_names)):
    #création du chemin pour lire les textes un par un
    file_path = os.path.join(directory, files_names[i])
    #changement des fichiers
    with open(file_path, 'r') as f1:
      new_file_path = os.path.join(new_folder, files_names[i])
      #création du nouveau fichier
      with open(new_file_path, 'w') as f2:
        #boucle for pour gérer chaque ligne et le mettre en minuscule
        for ligne in f1:
          f2.write(ligne.lower())
  return True


def clean_char(files_names):
  new_folder = "./cleaned"
  #boucle pour enlever les caractères spéciaux de chaque fichier
  for i in range(len(files_names)):
    file_path = os.path.join(new_folder, files_names[i])
    #changement des fichiers
    with open(file_path, 'r', encoding="utf-8") as f1:
      new_text = f1.read()
      L = {
          ":": "",
          ";": "",
          ",": "",
          "!": "",
          '"': "",
          "?": "",
          "(": "",
          ")": "",
          ".": "",
          "-": " ",
          "'": " "
      }
      #remplacement des caractères
      for i, j in L.items():
        new_text = new_text.replace(i, j)
      with open(file_path, 'w', encoding="utf-8") as f1:
        f1.write(new_text)

  return True


#Partie TF-IDF
def compteur_mots(chaine):
  liste = chaine.split()
  occurrences = {}
  #calcul des occurrences
  for mots in liste:
    if mots in occurrences:
      occurrences[mots] += 1
    else:
      occurrences[mots] = 1
      #ajout du nombre de mot total pour calculer le tf par la suite
  total_word = len(liste)
  return occurrences, total_word


def calcul_tf(new_text):
  #ouvre chaque texte pour calculer le TF
  occurrences, total_mots_doc = compteur_mots(new_text)
  TF = {}
  #calcul du TF pour chaque mot
  for mots in occurrences:
    TF[mots] = occurrences[mots] / total_mots_doc
  return TF


def word_frequency(files_names):
  frequence_mot_doc = {}
  new_folder = "./cleaned"
  #boucle classique par fichier
  for i in range(len(files_names)):
    file_path = os.path.join(new_folder, files_names[i])
    with open(file_path, 'r', encoding="utf-8") as f1:
      new_text = f1.read()
      occurrences, total_word = compteur_mots(new_text)
      #ajouter 1 pour la présence du mot dans le dictionnaire frequence_mot_doc
      for mots in occurrences:
        if mots not in frequence_mot_doc:
          frequence_mot_doc[mots] = 1
        else:
          frequence_mot_doc[mots] += 1

  return frequence_mot_doc


def calcul_idf(directory):
  IDF = {}
  files_names = list_of_files(directory, "txt")
  total_files = len(files_names)
  #j'ai crée une fonction word_frequency qui permet de calculer si un mot est présent dans un texte et d'ajouter 1 dans un compteur pour ensuite utiliser cette fonction dans calcul_idf
  frequence_mots = word_frequency(files_names)
  #calcul de l'IDF pour chaque mot
  for mots in frequence_mots:
    if mots not in IDF:
      IDF[mots] = math.log(total_files / frequence_mots[mots])
  return IDF


def calcul_tf_idf(directory):
  new_folder = "./cleaned"
  # Dictionnaire pour stocker le TF-IDF de chaque mot pour chaque fichier
  tf_idf_dict = {}

  # Calculer IDF une seule fois pour tous les fichiers
  files_names = list_of_files(directory, "txt")
  idf = calcul_idf(directory)

  # Boucle pour calculer le TF-IDF de chaque document
  for i in range(len(files_names)):
    file_path = os.path.join(new_folder, files_names[i])
    with open(file_path, 'r', encoding="utf-8") as f1:
      new_text = f1.read()
      tf = calcul_tf(new_text)

      # Calculer le TF-IDF pour chaque mot du document
      for mot in tf:
        tf_idf_score = tf[mot] * idf[mot]

        # Stocker le résultat dans le dictionnaire et en fonction du ficher
        #Crée un nouvel espace avec en temps que clé le mot pour que j'enregistre la valeur TF-IDF du mot dans cette clé.
        if mot not in tf_idf_dict:
          tf_idf_dict[mot] = {}
        tf_idf_dict[mot][files_names[i]] = tf_idf_score

  # Construire la matrice TF-IDF
  resultat_matrice = []

  # Obtenir la liste de mots avec les clés du dictionnaire pour une liste
  list_word_total = list(tf_idf_dict.keys())

  # Boucle pour créer la matrice TF-IDF avec comme ligne le mot et nous allons ajouter les valeurs pour chaque document ci-dessous
  for mot in list_word_total:
    ligne = [mot]
    #récupération du nom de chaque fichier pour faire une boucle
    for file_name in files_names:
      # Obtenir la valeur du dictionnaire tf_idf_dict pour chaque mot et chaque fichier avec la fonction get
      tf_idf_score = tf_idf_dict[mot].get(file_name, 0)
      ligne.append(tf_idf_score)

    # Ajouter la ligne à la matrice
    resultat_matrice.append(ligne)

  return resultat_matrice


def mots_non_importants(directory):
  non_important = []
  resultat = calcul_tf_idf(directory)
  for ligne in resultat:
    cpt = 0
    #la ligne 0 commence par le mot, on cherchera que toutes les valeurs sauf la première est égale à 0 pour son tf-idf
    for i in range(1, len(ligne)):
      if ligne[i] == 0:
        cpt += 1
      if cpt == (len(ligne) - 1):
        non_important.append(ligne[0])
        #enregistre ligne[0] car c'est le mot, les 7 autres valeurs ne sont pas utile pour l'utilisateur
  return non_important


def mots_plus_importants(directory):
  # Initialisation de la liste à retourner
  important = []
  # Pour prendre les 10 mots les plus importants
  n = 10
  list_mot = {}

  resultat_matrice = calcul_tf_idf(directory)

  for lignes in resultat_matrice:
    # Permet de vérifier s'il n'y a pas de problème pour chaque ligne et de pouvoir récupérer le mot
    if len(lignes) > 1 and isinstance(lignes[0], str):
      word = lignes[0]
      values = lignes[1:]

      # Index des valeurs maximum
      max_index = values.index(max(values))

      # obtenir le bon mot avec la bonne valeur
      if max_index == 0:
        max_word = word
      else:
        max_word = word

      # Apprend le mot avec la valeur maximal
      list_mot[max_word] = max(values)

  for i in range(n):
    # On cherche le mot le plus important pour ensuite l'apprendre
    max_key = max(list_mot, key=list_mot.get)
    important.append(max_key)
    # On enlève le mot le plus important de la liste
    del list_mot[max_key]

  return important


def mots_plus_repetes_chirac(directory):
  #initialisation de la liste à retourner
  mots_repetes_chirac = []
  list_mot = {}
  n = 5
  #on pourra demander à l'utilisateur jusqu'à combien de mot il a besoin
  resultat_matrice = calcul_tf_idf(directory)
  for lignes in resultat_matrice:
    #permet de vérifier s'il n'y a pas de problème pour chaque ligne et de pouvoir récupérer le mot
    if len(lignes) > 1 and isinstance(lignes[0], str):
      word = lignes[0]
      values = lignes[1:]

      # index des valeurs maximum
      max_index = values.index(max(values))

      #calcul de la valeur maximal
      if max_index == 0:
        max_word = word
      else:
        max_word = word

      # apprend le mot avec la valeur maximal
      list_mot[max_word] = max(values)

  for i in range(n):
    #on cherche le mot le plus important pour ensuite l'apprendre
    max_key = max(list_mot, key=list_mot.get)
    mots_repetes_chirac.append(max_key)
    #on enlève le mot le plus important de la liste
    del list_mot[max_key]
  return mots_repetes_chirac


def president_parlant_de_nation(directory):
  tfidf_matrix = calcul_tf_idf(directory)
  liste_finale = {}
  #on cherche le mot nation dans la matrice tf-idf
  for ligne in tfidf_matrix:
    if ligne[0] == "nation":
      #nous prennons les valeurs de la ligne avec le mot nation
      nation_valeurs = ligne[1:]
      liste_president = {
          0: "Chirac",
          1: "Chirac",
          2: "Giscard dEstaing",
          3: "Hollande",
          4: "Macron",
          5: "Mitterrand",
          6: "Mitterrand",
          7: "Sarkozy"
      }
      for i in range(len(nation_valeurs)):
        if nation_valeurs[i] != 0:
          liste_finale[liste_president[i]] = nation_valeurs[i]
      maximum = max(liste_finale, key=liste_finale.get)

  return maximum, liste_finale.keys()


def premier_president_climat_ecologie(directory):
  tfidf_matrix = calcul_tf_idf(directory)
  liste_finale_climat = {}
  liste_finale_ecologie = {}
  premier_climat = 0
  premier_ecologie = 0
  liste_president = {
      0: "Chirac",
      1: "Chirac",
      2: "Giscard dEstaing",
      3: "Hollande",
      4: "Macron",
      5: "Mitterrand",
      6: "Mitterrand",
      7: "Sarkozy"
  }
  #on cherche le mot climat dans la matrice tf-idf
  for ligne in tfidf_matrix:
    if ligne[0] == "climat":
      #nous prennons les valeurs de la ligne avec le mot nation
      nation_valeurs = ligne[1:]

      for i in range(len(nation_valeurs)):
        if nation_valeurs[i] != 0:
          liste_finale_climat[liste_president[i]] = nation_valeurs[i]
      premier_climat = max(liste_finale_climat, key=liste_finale_climat.get)

  #nous allons faire la même chose pour le mot écologie
  for ligne in tfidf_matrix:
    if ligne[0] == "écologie":
      #nous prennons les valeurs de la ligne avec le mot nation
      nation_valeurs = ligne[1:]
      for i in range(len(nation_valeurs)):
        if nation_valeurs[i] != 0:
          liste_finale_ecologie = {}[liste_president[i]] = nation_valeurs[i]
      premier_ecologie = max(liste_finale_ecologie,
                             key=liste_finale_ecologie.get)

    #renvoyer le nom du président si le mot a été rencontré, sinon la valeur 0 dans le cas où aucun président en a parlé
    if premier_ecologie == 0:
      ecologie = "aucun président n'a mentionné le mot écologie"
      return premier_climat, ecologie
  return premier_climat, premier_ecologie


def mots_evoques_par_tous(directory):
  mots_evoques_par_tous = []
  resultat = calcul_tf_idf(directory)
  for ligne in resultat:
    cpt = 0
    #la ligne 0 commence par le mot
    for i in range(1, len(ligne)):
      #les mots étant présent dans tous les documents ont un idf = 0 et donc leurs tf-idf également
      if ligne[i] == 0:
        cpt += 1
      if cpt == (len(ligne) - 1):
        mots_evoques_par_tous.append(ligne[0])
        #enregistre ligne[0] car c'est le mot, les 7 autres valeurs ne sont pas utile pour l'utilisateur
  return mots_evoques_par_tous