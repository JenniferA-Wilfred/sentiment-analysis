import pandas as pd
import folium
from folium.plugins import HeatMap
from textblob import TextBlob

# Step 1: Load the entire dataset
file_path = '/content/dutch_tweets_chunk0.json.zip'
print("Loading data...")
data = pd.read_json(file_path)

# Step 2: Define a function to classify sentiment
def get_sentiment(text):
    analysis = TextBlob(str(text))  # Convert to string in case of NaN
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Step 3: Apply function to create new column
data['sentiment'] = data['desc_translation'].apply(get_sentiment)

# Step 4: Display result
print(data[['desc_translation', 'sentiment']].head())

# Step 5: Save the result to a CSV file
output_file = "/content/dutch_tweets_with_sentiment.csv"
data.to_csv(output_file)
print(f"\nCSV file saved to: {output_file}")
