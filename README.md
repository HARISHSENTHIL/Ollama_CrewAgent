# Web Scraping and Cleaning Agent

This project demonstrates how to create an AI-powered agent using the CrewAI library to scrape and clean data from websites. The agent uses the requests and BeautifulSoup libraries for web scraping and applies natural language processing (NLP) techniques to clean the text. The cleaned data is then formatted into a JSON structure. All operations are powered by Ollama models, which run locally.

## Features

- Scrapes data from a specified URL using requests and BeautifulSoup.
- Cleans the data by removing HTML tags, special characters, and stopwords.
- Lemmatizes the words to their root form.
- Returns the cleaned data in a structured JSON format.
- Utilizes Ollama models running locally for AI-driven tasks.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- `requests` library
- `BeautifulSoup4` library
- `nltk` library
- `CrewAI` and `langchain_openai` libraries
- Ollama 
## Installation

1. **Clone the repository:**

    ```bash
    git clone 
    ```

2. **Set up a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install requests beautifulsoup4 nltk crewai langchain_openai
    ```

4. **Download NLTK data:**

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

## Environment Variables

`OPENAI_API_KEY` is not required but keep as placeholder 
## Run the project 

- Start Ollama locally by running it on your machine.
- Run the main script:
        $$ python3 main.py

This will execute the web scraping and data cleaning process using the locally running Ollama models, and return the cleaned data in JSON format.

Created by @HARISHSENTHIL