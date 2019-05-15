# Exercise 3
from pathlib import Path
import utils as u
# import functions from utils here


data_dir = Path("data")
output_dir = Path("solution")

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

text = Path(data_dir, "cars.txt")

# 2. Read the text file [2P]

cars = open(str(text), "r").read()

# 3. Count the occurences of each item in the text file [2P]

carlist=list(cars.split("\n"))
counts=u.countwords(carlist)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

u.dircheck(output_dir)

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]

with open('counts.csv', 'w') as f:
    for key in counts.keys():
        f.write("%s,%s\n"%(key,counts[key]))
        
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
