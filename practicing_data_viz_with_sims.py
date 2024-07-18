# practicing viz with my sims

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

# navigate to the folder
os.getcwd()
os.chdir('../../Git_Stuff/sims_stuff/extracted_data/')
os.listdir()

# just going to pick one to practice with
# (for my personal use, I would concat all these different spreadsheets)
os.chdir('veronaville/')
os.listdir()
os.chdir('Rufio')
os.listdir()

# pull in a CSV to play with
sims = pd.read_csv('ExportedSims.csv', encoding_errors = 'replace')
sims_clean = sims.copy(deep = True)

# explore
sims.shape
sims.describe()
sims.info()

# rename columns
# winging it with regexes!  thanks to
# https://stackoverflow.com/questions/5658369/how-to-input-a-regex-in-string-replace
sims = sims_clean.copy(deep = True)
sims.columns
sims.columns = [re.sub(r'([a-z])([A-Z])', r'$1\_$2', x) for x in list(sims.columns)]
sims.columns = [x.replace(r'[[:lower:]][[:upper:]]', f"{r'[[:lower:]]'}_{r'[[:lower:]]'}").replace(' ', '_').lower() for x in list(sims.columns)]
sims.columns
