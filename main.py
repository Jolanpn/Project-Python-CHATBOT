from fonctions import *

if __name__ == '__main__':
  directory = "./speeches-20231107"
  files_names = list_of_files(directory, "txt")
  list_names = extract_names(files_names)
  print(prenom_nom(list_names))
  lower(files_names, directory)
