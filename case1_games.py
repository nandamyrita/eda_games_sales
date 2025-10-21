import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import argparse

sns.set(style="whitegrid", palette="pastel")
plt.rcParams["figure.figsize"] = (10, 6)
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


