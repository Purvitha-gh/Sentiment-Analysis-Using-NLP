# Sentiment-Analysis-Using-NLP
Sentiment Analysis Web Application

A simple and interactive web-based sentiment analysis system built using Flask, TextBlob, and WordCloud. The application allows users to enter any text and instantly receive insights such as sentiment prediction, confidence score, polarity value, word frequency analysis, and an auto-generated word cloud.

🚀 Project Overview

This project demonstrates how Natural Language Processing (NLP) techniques can be integrated into a user-friendly web interface. Users input text into the system, which then:

Predicts Positive, Negative, or Neutral sentiment

Calculates a confidence score based on polarity

Displays the polarity value

Counts the number of words

Extracts the top 5 most frequent words

Generates a word cloud image

The app provides a clean UI with minimal styling (via style.css) to keep the experience simple and intuitive.

📁 Project Structure
├── app.py               # Main Flask backend application
├── static/
│   └── wordcloud.png    # Auto-generated word cloud (created at runtime)
├── templates/
│   └── index.html       # Frontend HTML file (not provided here)
├── style.css            # Styling for the web interface
└── README.md            # Project documentation

🧠 Key Features
✔️ Sentiment Classification

Uses TextBlob to analyze user text and classify sentiment.

✔️ Confidence & Polarity Scoring

Confidence is calculated using the absolute polarity value.

✔️ Word Cloud Generation

Creates a dynamic word cloud using the WordCloud library and saves it to /static.

✔️ Word Frequency Insights

Extracts and displays the top 5 repeated words.

✔️ Responsive UI

Minimal, clean interface built using HTML & custom CSS.

🛠️ Technologies Used
Component	Technology
Backend	Flask (Python)
NLP	TextBlob
Visualizations	WordCloud
Styling	CSS
Frontend	HTML Templates
📌 How It Works

Below is a simplified explanation of what happens inside app.py:

User enters text in the input form

Flask receives the text via POST

TextBlob analyzes sentiment → polarity → sentiment label

Confidence percentage is calculated

WordCloud generates wordcloud.png dynamically

Counter extracts top 5 words

All results are sent back to the HTML template for display

🧩 Core Code Snippet
blob = TextBlob(text)
polarity = blob.sentiment.polarity

if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

confidence = abs(polarity) * 100

📦 Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/sentiment-analysis-app.git
cd sentiment-analysis-app

2. Install Dependencies
pip install -r requirements.txt


If you do not have a requirements file, install manually:

pip install flask textblob wordcloud
python -m textblob.download_corpora

3. Run the App
python app.py

4. Open in Browser

Go to:

http://127.0.0.1:5000/

📸 Interface Preview Description

The interface features a clean and minimal design where users can enter text into an input box, submit their query, and instantly view the sentiment prediction, confidence score, top words, and a dynamically generated word cloud.

📈 Example Output

Sentiment: Positive

Confidence: 87.5%

Polarity: 0.63

Word Count: 15

Top Words: ['great', 'love', 'happy', ...]

Word Cloud: Generated in static/wordcloud.png

🎯 Project Purpose

This project highlights the potential of NLP in understanding human language and extracting meaningful insights. It can be extended for:

Customer review analysis

Social media sentiment monitoring

Chatbot integration

Text emotion detection

🔮 Future Enhancements

Add multilingual sentiment analysis

Deploy on Heroku / Render

Store previous analyses

Add charts for sentiment over time

Improve UI with Bootstrap or React

📜 License

This project is open-source and free to use under the MIT License.
