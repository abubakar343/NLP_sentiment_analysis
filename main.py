# -*- coding: utf-8 -*-

import pandas as pd  # Importing the pandas library for data manipulation and analysis.
from textblob import TextBlob  # Importing TextBlob for performing text processing tasks, such as sentiment analysis.
from google.colab import files  # Importing the 'files' module from Google Colab to upload files within the Colab environment.

# Uploading files in Google Colab
uploaded = files.upload()

import os  # Importing the 'os' library to interact with the operating system, especially for file handling.
cwd = os.getcwd()  # Getting the current working directory.
files = [f for f in os.listdir('.') if os.path.isfile(f)]  # Listing all files in the current directory.
for f in files:
    print(f)  # Printing the name of each file.

# Reading the Excel file into a DataFrame
nd = pd.read_excel('your_data.xlsx')

# Create an empty list to store processed lines.
nf = []

# Iterate over each column (assumes each column contains a line of text).
for ln in nd:
    print(ln)  # Print the column name (or data, depending on content).
    words = ln.split("], [")  # Split the line into words or phrases based on a specific pattern.
    nf.append(words)  # Append the split words/phrases to the 'nf' list.

# Convert the list of words/phrases into a DataFrame
df = pd.DataFrame(nf)

# Transpose the DataFrame to switch rows and columns
new_df = df.T

# Set column names for the new DataFrame
new_df.columns = ['Statements']  # Rename the single column to 'Statements'.

# Display the 'Statements' column
new_df['Statements']

# Function to count the number of words in a statement
def find_count(statmnt):
    count1 = statmnt.split(" ")  # Split the statement into words using spaces.
    return len(count1)  # Return the count of words.

# Apply the find_count function to each statement and create a new column 'stmt_count'
new_df['stmt_count'] = new_df['Statements'].apply(find_count)

# Function to get the subjectivity of a statement
def getSubjectivity(statement):
    return TextBlob(statement).sentiment.subjectivity  # Return the subjectivity score using TextBlob.

# Function to get the polarity of a statement
def getPolarity(statement):
    return TextBlob(statement).sentiment.polarity  # Return the polarity score using TextBlob.

# Apply the sentiment functions to the 'Statements' column
new_df['pol_textblob'] = new_df['Statements'].apply(getPolarity)  # Apply polarity function and store the result.
new_df['Subjectivity_textblob'] = new_df['Statements'].apply(getSubjectivity)  # Apply subjectivity function.

# Function to categorize the sentiment polarity into Positive, Negative, or Neutral
def get_score(val):
    if val > 0:
        return 'Positive'  # Return 'Positive' for positive polarity.
    elif val < 0:
        return 'Negative'  # Return 'Negative' for negative polarity.
    else:
        return 'Neutral'  # Return 'Neutral' for zero polarity.

# Apply the get_score function to categorize the polarity scores
new_df['pol_score'] = new_df['pol_textblob'].apply(get_score)

# Save the resulting DataFrame to an Excel file
new_df.to_excel('analysis.xlsx')

# Display descriptive statistics of the DataFrame
new_df.describe()
