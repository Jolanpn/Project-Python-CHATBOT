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


def clean_char_str(new_text):
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
  # remplacement des caractères
  for i, j in L.items():
    new_text = new_text.replace(i, j)
  return new_text


#Partie TF-IDF
def compteur_mots(chaine):
  list = chaine.split()
  occurrences = {}
  #calcul des occurrences
  for mots in list:
    if mots in occurrences:
      occurrences[mots] += 1
    else:
      occurrences[mots] = 1
      #ajout du nombre de mot total pour calculer le tf par la suite
  total_word = len(list)
  return occurrences, total_word


def compteur_mots_liste(liste):
  occurrences = {}

  for mot in liste:
    if mot in occurrences:
      occurrences[mot] += 1
    else:
      occurrences[mot] = 1

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


def calcul_liste_mots(files_names):
  new_folder = "./cleaned"
  liste_mots = []
  for i in range(len(files_names)):
    file_path = os.path.join(new_folder, files_names[i])
    with open(file_path, 'r', encoding="utf-8") as f1:
      new_text = f1.read()
      TF = calcul_tf(new_text)
      for mots in TF.keys():
        if mots not in liste_mots:
          liste_mots.append(mots)
  return liste_mots


def matrice_tf(directory):
  new_folder = "./cleaned"
  list_temp_tf = []
  final_dict = {}
  files_names = list_of_files(directory, "txt")

  for i in range(len(files_names)):
    file_path = os.path.join(new_folder, files_names[i])
    with open(file_path, 'r', encoding="utf-8") as f1:
      new_text = f1.read()
      tf_doc = calcul_tf(new_text)
      list_temp_tf.append(tf_doc)
      if i != 1 and i != 6:  # Use 'and' instead of 'or'
        for key, value in tf_doc.items():
          final_dict.setdefault(key, 0)
          final_dict[key] += value

  return final_dict


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
      #changement du calcul de l'idf??? +1 cependant la formule était total_files/frequence_mots, par précaution, nous gardons la formule de wikipédia
      IDF[mots] = math.log((total_files / frequence_mots[mots]))
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
  longueur = 0
  resultat = calcul_tf_idf(directory)
  for ligne in resultat:
    cpt = 0
    #la ligne 0 commence par le mot, on cherchera que toutes les valeurs sauf la première est égale à 0 pour son tf-idf
    for i in range(1, len(ligne)):
      if ligne[i] == 0.0:
        cpt += 1
      if cpt == (len(ligne) - 1):
        non_important.append(ligne[0])
      longueur = len(non_important)
      #enregistre ligne[0] car c'est le mot, les 7 autres valeurs ne sont pas utile pour l'utilisateur
  return non_important, longueur


def mots_plus_importants(directory, n):
  # Initialisation de la liste à retourner
  important = []
  # Pour prendre les 10 mots les plus importants
  list_mot = {}

  resultat_matrice = calcul_tf_idf(directory)

  for lignes in resultat_matrice:
    # Permet de vérifier s'il n'y a pas de problème pour chaque ligne et de pouvoir récupérer le mot
    #isinstance vérifie le type de la variable
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


def mots_plus_repetes_chirac(directory, n):
  #initialisation de la liste à retourner
  mots_repetes_chirac = []
  list_mot = {}
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


def president_parlant_de_nation(directory, mot):
  tfidf_matrix = calcul_tf_idf(directory)
  liste_finale = {}
  #on cherche le mot nation dans la matrice tf-idf
  for ligne in tfidf_matrix:
    if ligne[0] == mot:
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
    ecologie = "aucun président n'a mentionné le mot écologie"
    climat = "aucun président n'a mentionné le mot climat"
    if premier_ecologie == 0:
      return premier_climat, ecologie
    if premier_climat == 0:
      return climat, premier_ecologie
    if premier_climat == 0 and premier_ecologie == 0:
      return climat, ecologie
  return premier_climat, premier_ecologie


def mots_evoques_par_tous(directory, president1, president2, president3,
                          president4):

  # Récupérer les noms des fichiers de discours de chaque président
  files_names = list_of_files(directory, "txt")
  files_chirac1 = [
      file for file in files_names if president1.lower() in file.lower()
  ]
  files_chirac2 = [
      file for file in files_names if president2.lower() in file.lower()
  ]
  files_mitterrand1 = [
      file for file in files_names if president3.lower() in file.lower()
  ]
  files_mitterrand2 = [
      file for file in files_names if president4.lower() in file.lower()
  ]

  # Calculer le TF pour chaque président séparément
  tf_chirac1 = calcul_tf_idf(directory, files_chirac1)
  tf_chirac2 = calcul_tf_idf(directory, files_chirac2)
  tf_mitterrand1 = calcul_tf_idf(directory, files_mitterrand1)
  tf_mitterrand2 = calcul_tf_idf(directory, files_mitterrand2)

  # Liste des mots avec TF > 0 pour les quatre présidents combinés
  mots_combines = [
      mot for mot in tf_chirac1
      if tf_chirac1[mot] > 0 and tf_chirac2.get(mot, 0) > 0
      and tf_mitterrand1.get(mot, 0) > 0 and tf_mitterrand2.get(mot, 0) > 0
  ]

  # Enlever les mots non importants
  non_importants, _ = mots_non_importants(directory)
  mots_combines_sans_non_importants = [
      mot for mot in mots_combines if mot not in non_importants
  ]

  return mots_combines_sans_non_importants


"""pour cette question, combiner le tf de chirac1 et chirac2, mitterant même chose 
puis vérifier si les mots ont tous un tf > 0
en faire une liste
enlever les mots qui sont aussi présent dans la liste de non-mots_non_importants()
return la nouvelle liste"""
"""Début partie 2"""


#question 1 partie 2
def question_split(question):
  question = question.lower()
  question = clean_char_str(question)
  liste = question.split()
  return liste


def calcul_tf_question(question):
  tf_score = {}
  word_in_split = id_term_question(question)
  occurrences, total_words_question = compteur_mots_liste(word_in_split)
  for word in word_in_split:
    tf_score[word] = occurrences[word] / total_words_question
  return occurrences


def id_term_question(question):
  mots_present = []
  directory = "./speeches-20231107"
  files_names = list_of_files(directory, "txt")
  #divise la questione n une liste de mot
  liste_question = question_split(question)
  liste_mots = calcul_liste_mots(files_names)
  for mots in liste_question:
    if mots in liste_mots:
      mots_present.append(mots)
  return mots_present


def score_tfidf_question(question, directory):
  TF = calcul_tf_question(question)
  TF_IDF = {}
  directory = "./speeches-20231107"
  #réutilisation du score IDF du corpus pour le calcul du TFIDF
  IDF = calcul_idf(directory)
  termes_question = id_term_question(question)
  #calcul du tfidf de chaque mot de la question
  for mots in termes_question:
    TF_IDF[mots] = IDF[mots] * TF[mots]
  return TF_IDF


def produit_scalaire(question, directory, files_names):
  # Dictionnaire pour retourner le produit scalaire de chaque document
  produit = {}

  # Calcul des scores TF-IDF de la question et des documents
  tfidf_question = score_tfidf_question(question, directory)
  tfidf_documents = calcul_tf_idf(directory)

  for i in range(len(files_names)):
    somme = 0.0
    # Calcul de la somme des produits des TF-IDF correspondants
    for mot, tfidf_question_value in tfidf_question.items():
      for mot_corpus in tfidf_documents:
        # Recherche des valeurs TF-IDF du corpus pour chaque mot
        if mot_corpus[0] == mot:
          # Ajout de i + 1 car la valeur 0 du calcul TF-IDF commence par le mot
          somme += tfidf_question_value * mot_corpus[i + 1]

    produit[files_names[i]] = somme
  return produit


def calculate_vector_norm(question, directory, files_names):
  tfidf_question = score_tfidf_question(question, directory)
  norm_question = 0.0
  norm_doc = {}
  #calcul des normes de chaque document
  for i in range(len(files_names)):
    #calcul du tfidf au carré une seule fois
    if i == 0:
      for val in tfidf_question.values():
        norm_question += val**2
      norm_question = math.sqrt(norm_question)
    somme_doc = 0.0
    #boucle pour calculer chaque mot de la question
    for mot_question in tfidf_question.keys():
      #boucle pour calculer chaque mot du document
      for mot in calcul_tf_idf(directory):
        #rechercher le bon mot dans la matrice tf-idf
        if mot[0] == mot_question:
          somme_doc += float(mot[1 + i])**2
    norm_doc[files_names[i]] = (math.sqrt(somme_doc)) * norm_question
  return norm_doc


def calcul_similarite(question, directory, files_names):
  norm_doc = calculate_vector_norm(question, directory, files_names)
  produit = produit_scalaire(question, directory, files_names)
  similarite = {}
  for name in files_names:
    if norm_doc[name] != 0:
      similarite[name] = produit[name] / norm_doc[name]
    else:
      similarite[name] = 0
  return similarite


def doc_pertinence(question, directory, files_names):
  similarite = calcul_similarite(question, directory, files_names)
  pertinence = max(similarite, key=similarite.get)
  return pertinence


def reponse(question, directory, files_names):
  tfidf_question = score_tfidf_question(question, directory)
  tfidf_question_max = max(tfidf_question, key=tfidf_question.get)
  nom_doc = doc_pertinence(question, directory, files_names)
  questions_reponses = {
      "Peux-tu": "Oui, je peux le faire. ",
      "Pouvez-vous": "Bien sûr, vous pouvez compter sur moi. ",
      "Pourrais-tu": "Absolument, je pourrais vous aider. ",
      "Pourriez-vous": "Bien sûr, vous pouvez compter sur moi. ",
      "Combien": "Le nombre exact dépend de plusieurs facteurs. ",
      "Pourquoi": "Il y a plusieurs raisons possibles, dont : ",
      "Quand": "Cela dépend du contexte, mais généralement : ",
      "Comment": "Il y a plusieurs moyens possibles, dont : ",
      "Où": "L'emplacement précis varie, mais en général : ",
      "Quelle est": "La réponse à cette question est : ",
      "Est-ce que": "Oui. ",
      "Saurais-tu": "Oui, je sais comment le faire. ",
      "Seriez-vous en mesure de": "Oui, je serais en mesure de le faire. ",
      "Peux-tu me dire": "Bien sûr, voici. ",
      "Pouvez-vous expliquer": "Absolument, voici une explication. ",
      "Pourrais-tu me donner": "Bien entendu, voici. ",
      "Pourriez-vous fournir": "Bien sûr, voici les informations. ",
      # Ajoutez d'autres débuts de questions et réponses au besoin
  }
  #création du document
  file_path = os.path.join(directory, nom_doc)
  with open(file_path, 'r', encoding="utf-8") as f1:
    new_text = f1.read()
    new_text = new_text.split(".")
  #detection des mots pour le dictionnaire
  split_question = question.split(" ")

  start_answer_possible = False
  for question in questions_reponses.keys():
    if question in split_question:
      start_answer = questions_reponses[question]
      start_answer_possible = True

  for lines in new_text:
    if tfidf_question_max in lines:
      if start_answer_possible == True:
        reponse = start_answer + lines + "."
      else:
        start_answer = "Bien sûr, voici la réponse à votre question. "
        reponse = start_answer + lines + "."
      return reponse
