Instructions des programmes 

- list_of_files(directory, extension):
  Le chemin où les fichiers sont stockés pour l'extension et l'extension ("txt", "doc")
  permet d'obtenir le nom et l'extension des fichiers dans une liste.

- extract_names(files_names)
  Demande la liste des noms des fichiers .txt
  retire l'extension '.txt' et 'Nomination_' pour isoler le nom. Le sauvegarde dans une liste.

- prenom_nom(list_names)
  Demande la liste des noms des fichiers .txt
  crée un dictionnaire avec pour clé les noms et la valeur les prénoms.

- def lower(files_names, directory):
  Demande la liste des noms des fichiers .txt mais aussi le directoire donc le chemin où les fichiers sont stockés
  permet de mettre tous les caractères en minuscule, files_names est la listes des noms .txt inclus, directory est le chemin à prendre

- def clean_char(files_names):
  Remplace les caractères spéciaux par une suppression de ce caractères ou un remplacement par un espace.
  Le fonctionnement est d'utiliser un dictionnaire avec en clé le caractère spécial et en valeur par ce que nous voulons en faire, remplacer ou supprimer.
  En paramètre, il prends la liste des noms en .txt

- def clean_char_str(new_text):
  Remplace les caractères spéciaux par une suppression de ce caractères ou un remplacement par un espace.
  Le fonctionnement est d'utiliser un dictionnaire avec en clé le caractère spécial et en valeur par ce que nous voulons en faire, remplacer ou supprimer.
  En paramètre, il prends une chaine de caractère

- def counter_word(chaine):
  Cette fonction prends en paramètre une chaine de caractères pour compter l'occurrence de chaque mot à l'aide d'un slice.
  Il retourne un dictionnaire avec pour clé les mots et en valeur le nombre d'occurrence
  Et le nombre total de mots dans la chaine de caractères

- def counter_word_list(liste):
  Cette fonction prends en paramètre une liste de caractères pour compter l'occurrence de chaque mot.
  Il retourne un dictionnaire avec pour clé les mots et en valeur le nombre d'occurrence
  Et le nombre total de mots dans la chaine de caractères

- def calcul_tf(new_text):
  Le paramètre new_text est une chaine de caractère pour ensuite utiliser la fonction compteur_mots
  Il retourne la valeur TF (term frequency) en forme de dictionnaire, en clé le mot et en valeur le TF

- def calcul_list_mots(files_names):
  En paramètre cela prend la liste des noms des documents .txt
  Il calcul le tf de chaque document puis retourne une liste des mots de chaque document

- def word_frequency(files_names):
  En prenant pour paramètre une liste des noms des fichiers .txt, il retourne un dictionnaire qui dit la présence du mot dans les documents

- def calcul_idf(directory):
  Cette fonction demande le directoire pour retourner la valeur IDF de chaque mot dans un dictionnaire
  Pour clé le mot et en valeur l'IDF

- def calcul_tf_idf(directory):
  Toujours en paramètre le directoire, il calcul le TF-IDF de chaque document.
  Puis il y a une création d'une matrice de liste, en ligne les mots et en colonnes le mot puis les valeurs TF-IDF de chaque document.
  Attention, la valeur mot[0] donnera le mot en chaine de caractère puis de 1 à n les valeurs TF-IDf
  Cette fonction retourne cette matrice

- def mots_non_importants(directory):
  Le directoire en paramètre, il retourne les mots ayant une valeur TF-IDF de 0 dans tous les documents.
  En une liste

- def mots_plus_importants(directory, n):
  Pour les paramètres, il y a le directoire et également n qui est le nombre de mots que nous voulons
  Pour n = 5, il prendra les 5 mots les plus importants, cette variable est demandé à l'utilisateur lorsqu'il choisit d'utiliser cette fonction
  Cette fonction retourne la liste des mots les plus importants

- def mots_plus_repetes_chirac(directory):
  Toujours le directoire en paramètre, le fonctionnement est identique à la fonction mots_plus_importants cependant elle ne prendra qu'en compte les textes de Chirac
  Cette fonction retourne une liste de mots

- def president_parlant_de_nation(directory, mot):
  En paramètre le directoire, si vous choisissez dans le menu :
  "4. Les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois\n"
  le paramètre mot aura la valeur "nation"
  Cependant, cette fonction à la possilité de chercher un autre mot à l'aide de la variable mot
  Il retourne le président ayant le plus grand tf-idf de ce mot et la liste de clé qui représente les présidents ayant utilisé ce mot

- def premier_president_climat_ecologie(directory):
  En paramètre le directoire
  Cette fonction retourne le président ayant le plus mentionner le mot climat et pour l'écologie
  Dans le cas où il n'y a pas de mention d'un des deux mots ou les deux mots
  un message : aucun président n'a mentionné le mot écologie/climat apparaitra
  retourne une chaine de caractères

- def mots_evoques_par_tous(directory):
  En paramètre le directoire
  Pour l'utilisation, vous pouvez modifier la valeur du pourcentage (entre 0 et 1) afin d'obtenir les mots présent dans 8 * (entre 0 et 1) des documents
  Car si nous prenons un mot présent dans tous les documents, son tf-idf sera forcément égal à 0 ce qui le mettrait dans les mots les moins importants
  Il retourne une liste de mots ayant été dans le document

- def question_split(question):
  prend une chaine de caractère pour retourner une liste de mots sans caractères spéciaux et en minuscule

- def calcul_tf_question(question):
  Retourne un dictionnaire du tf de chaque mot, le paramètre d'entrée est une chaine de caractère

- def id_term_question(question):
  En entrée, une chaine de caractère et retourne les mots présents dans cette chaine de caractère qui sont dans le corpus de documents en forme de liste

- def score_tfidf_question(question, directory):
  En paramètre le directoire (le chemin des documents) et la chaine de caractère
  il retourne le TFIDF de chaque mot présent dans le corpus et dans la question

- def scalar_product(question, directory, files_names):
  Entrées : une chaine de caractère, le chemin pour les documents du corpus et la liste des noms des documents .txt
  Cette fonction retourne un dictionaire avec pour clé chaque document et la valeur du produit scalaire entre le vecteur de la question et le corpus du document

- def calculate_vector_norm(question, directory, files_names):
  Entrées : une chaine de caractère, le chemin pour les documents du corpus et la liste des noms des documents .txt
  Cette fonction retourne un dictionaire avec pour clé chaque document et la valeur de la racine carré du produit entre le vecteur de la question et le corpus du document

- def calcul_similarity(question, directory, files_names):
  Entrées : une chaine de caractère, le chemin pour les documents du corpus et la liste des noms des documents .txt
  Retourne un dictionnaire avec pour clé les noms des documents et la valeur de similarité pour chacuns

- def doc_pertinence(question, directory, files_names):
  Entrées : une chaine de caractère, le chemin pour les documents du corpus et la liste des noms des documents .txt
  Retourne le nom du document avec la plus grande valeur de similarité entre les documents

- def reponse(question, directory, files_names):
  Entrées : une chaine de caractère, le chemin pour les documents du corpus et la liste des noms des documents .txt
  Retourne une réponse en forme de chaine de caractère, la phrase contenant le mot ayant le plus élevé dans la question au sein du document ayant la plus grande pertinence