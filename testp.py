import pandas as pd
import csv

with open("test1.csv") as file:

 ca = csv.reader("test1.csv")
 cs = pd.read_csv("test1.csv")

print(cs["Week"][3])

from random import randint

print(randint(1,10))


