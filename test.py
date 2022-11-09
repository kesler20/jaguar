

import os




files = [r"interfaces\os_interface.py", r"this\this.py"]
for dir in os.listdir(r"C:\Users\Uchek\protocol"):
  for file in files:
    dirs = file.split(r"\ ".replace(" ", ""))[:-1]
    valid_dirs = search_for_dir(dir,dirs)
