import glob
from pathlib import Path
import pandas as pd 
import numpy as np
 
files = glob.glob('Match_outcome_predictor/Data/*.csv')

df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)

df.to_csv("combined_data.csv", index=False)



