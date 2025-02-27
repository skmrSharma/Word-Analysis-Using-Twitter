import pandas as pd
import stylecloud
import sys

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv('./result.csv')

newtext=""
for i in range(len(df)):
  newtext+=df.text[i]

list=["https","http","co","to","rt","the","and","for"]
stylecloud.gen_stylecloud(text=newtext, icon_name= "fab fa-twitter",custom_stopwords=list, palette="cartocolors.diverging.TealRose_7",collocations=False, background_color="black", output_name="./static/img/stylecloud_" + sys.argv[1] + ".png")