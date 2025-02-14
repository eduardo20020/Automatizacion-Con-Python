import os

def search_files(directory):
  
  for file in os.listdir(directory):
    
    full_path = os.path.join(directory, file)
    

    if os.path.isdir(full_path):
      search_files(full_path)
    else:
      print(full_path)


search_files(r"Y:\ENTRETENIMIENTO\POST ENTRETENIMIENTO\To_GALILEO")

