import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from nltk.sentiment import SentimentIntensityAnalyzer
import openai
import seaborn as sns


# analyze the sentiment with openAI
def analyze_sentiment(text, key):
    # Set up OpenAI API credentials
    openai.api_key = key

    # Define the sentiment analysis prompt
    prompt = f"what is the sentiment of sentence '{text}\n'"

    # Generate the sentiment analysis using OpenAI
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        temperature=0,
        top_p=1,
        n=1,
        stop=None,

    )

    # Extract the sentiment from the OpenAI response
    sentiment = response.choices[0].text.strip().lower()

    return sentiment


# draw the bar graph
def bar_drawing(data, num, label, title):
    # ref: https://proclusacademy.com/blog/customize_matplotlib_piechart/
    sns.set(font_scale=1.0)
    plt.figure(figsize=(8, 8))

    patches, texts, autotexts = plt.pie(
        x=data,
        labels=label,
        autopct='%1.1f%%',
        colors=sns.color_palette('Set2'),
        labeldistance=0.8,
        # Distance of percent labels from the center
        pctdistance=0.5,
        explode=[0.05] * num
    )

    # Customize text labels
    for text in texts:
        text.set_horizontalalignment('center')

    # Customize percent labels
    for autotext in autotexts:
        autotext.set_horizontalalignment('center')
        autotext.set_fontstyle('italic')

    for patch in patches:
        patch.set_edgecolor('black')

    # autotexts[4].set_visible(False)
    plt.title(title)
    plt.show()


# get the sentiment of nltk
def get_sentiment(x):
    sia = SentimentIntensityAnalyzer()
    point = sia.polarity_scores(x)
    if point["compound"] > 0:
        return "positive"
    elif point["compound"] < 0:
        return "negative"
    else:
        return "netural"


# create wordcloud plot
def wc_create(text, mask, stopwords, maxwords=100):
    wc = WordCloud(background_color="white", max_words=maxwords, mask=mask,
                   stopwords=stopwords)

    # Generate a wordcloud
    wc.generate(text)

    # show
    plt.figure(figsize=[20, 10])
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
