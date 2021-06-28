import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def hashtagCount():
	df=pd.read_csv('result.csv')
	hash_values = df['hashtag'].value_counts().keys().tolist()

	if "None" in hash_values:
		hash_values.remove("None")
	return hash_values

def sourceCount():
	df=pd.read_csv('result.csv')
	src_values = df['source'].value_counts().keys().tolist()
	src_counts = df['source'].value_counts().tolist()

	src = pd.DataFrame([src_values,src_counts]).T
	return src.values.tolist()