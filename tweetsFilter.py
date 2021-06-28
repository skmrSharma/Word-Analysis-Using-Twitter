import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def tweetsFilter(pos):
	df=pd.read_csv('result.csv')

	posdf = df[df.polarity > 0]
	negdf = df[df.polarity < 0]
	neutdf = df[df.polarity == 0]

	if pos == 1:
		allhtml = df.to_html(classes = "styled-table", justify = "center", index = False, columns = ["created","username","text"])
		return allhtml
	elif pos == 2:
		poshtml = posdf.to_html(classes = "styled-table", justify = "center", index = False, columns = ["created","username","text"])
		return poshtml
	elif pos == 3:
		neghtml = negdf.to_html(classes = "styled-table", justify = "center", index = False, columns = ["created","username","text"])
		return neghtml
	elif pos == 4:
		neuthtml = neutdf.to_html(classes = "styled-table", justify = "center", index = False, columns = ["created","username","text"])
		return neuthtml
	else:
		return "Invalid button/position passed"	