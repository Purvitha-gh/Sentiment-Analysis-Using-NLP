from flask import Flask, render_template, request
from textblob import TextBlob
from wordcloud import WordCloud
from collections import Counter
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    confidence = 0
    word_count = 0
    polarity = 0
    top_words = []

    if request.method == "POST":
        text = request.form["text"]

        if text.strip():
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            word_count = len(text.split())

            # Determine sentiment
            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            confidence = abs(polarity) * 100

            # Create word cloud
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text.lower())
            wordcloud.to_file(os.path.join("static", "wordcloud.png"))

            # Calculate top 5 words
            words = [w.lower() for w in text.split() if w.isalpha()]
            word_freq = Counter(words)
            top_words = word_freq.most_common(5)

    return render_template("index.html",
                           sentiment=sentiment,
                           confidence=round(confidence, 1),
                           word_count=word_count,
                           polarity=round(polarity, 2),
                           top_words=top_words)

if __name__ == "__main__":
    app.run(debug=True)
