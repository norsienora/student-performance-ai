import os
import pandas as pd

base_dir = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_dir, "..", "data", "student-mat.csv"))

print("Reading from:", file_path)

df = pd.read_csv(file_path, sep=";")
print(df.head())
