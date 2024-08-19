# Text Data Analysis with Sentiment Scoring

This project provides a Python script (`main.py`) designed to analyze text data from an Excel file. It uses the `TextBlob` library to perform sentiment analysis, including calculating the polarity and subjectivity of each statement. The results are saved in a new Excel file for further analysis.

## Features

- **File Upload and Data Loading**: 
  - The script is designed to be run in Google Colab, where it uses the `files.upload()` function to allow users to upload an Excel file containing text data.
  - The uploaded file is read into a Pandas DataFrame for further processing.

- **Text Data Processing**: 
  - The script splits text data based on specific patterns and transposes the resulting DataFrame to structure it for analysis.
  - It counts the number of words in each statement.

- **Sentiment Analysis**:
  - The script calculates the polarity (positive, negative, or neutral) and subjectivity (degree of personal opinion versus factual information) of each statement using the `TextBlob` library.

- **Sentiment Categorization**:
  - Each statement is categorized as 'Positive', 'Negative', or 'Neutral' based on its polarity score.

- **Data Export**:
  - The results, including the sentiment scores and word counts, are saved to a new Excel file named `analysis.xlsx`.

## Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `textblob`
  - `google.colab` (if running in Google Colab)
  - `os`

## How It Works

1. **Upload the Excel File**: 
   - The script starts by allowing the user to upload an Excel file containing text data.

2. **Data Processing**: 
   - The text data is processed by splitting strings and counting the number of words in each statement.

3. **Sentiment Analysis**:
   - The `TextBlob` library is used to calculate the polarity and subjectivity of each statement.

4. **Categorization and Export**:
   - The polarity scores are categorized into 'Positive', 'Negative', or 'Neutral', and the results are saved to an Excel file for further use.

## Acknowledgments

This script utilizes the `TextBlob` library for sentiment analysis and is designed to run in the Google Colab environment for ease of use.
