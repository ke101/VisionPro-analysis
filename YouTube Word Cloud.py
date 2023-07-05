import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


# Load in the dataframe
df = pd.read_csv("/Users/lisali/Desktop/ytcomments4.csv", index_col=0)

# Start with one review:
#comment = df.Comment[0]

# Create and generate a word cloud image:
#wordcloud = WordCloud().generate(comment)

# Display the generated image:
#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")
#plt.show()

allcomments = " ".join(Comment for Comment in df.Comment)
# Generate a word cloud image
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(allcomments)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

