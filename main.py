import os
import requests
from bs4 import BeautifulSoup
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import json
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

os.environ["OPENAI_API_KEY"] = "sk-proj-1111"

llm = ChatOpenAI(
    model="llama3",
    base_url="http://localhost:11434/v1"
)

def scrape_and_clean_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    text_content = soup.get_text(separator="\n", strip=True)

    clean_data = {"data": []}

    for line in text_content.splitlines():
        line = line.strip()
        if line:
            line = re.sub(r'<.*?>', '', line)
            line = re.sub(r'[^a-zA-Z0-9\s]', '', line)

            tokens = word_tokenize(line)

            stop_words = set(stopwords.words('english'))
            tokens = [t for t in tokens if t.lower() not in stop_words]

            lemmatizer = WordNetLemmatizer()
            tokens = [lemmatizer.lemmatize(t) for t in tokens]

            line = ' '.join(tokens)

            clean_data["data"].append(line)

    return json.dumps(clean_data, indent=4)

class WebScrapingAgent(Agent):
    def execute(self, task):
        url = task.description
        cleaned_data = scrape_and_clean_data(url)
        return cleaned_data

scraping_agent = WebScrapingAgent(
    role="Web Scraping Agent",
    goal="Scrape and clean data from a given website",
    backstory="""
        You are a data enthusiast who loves collecting and cleaning data from various sources
        for further processing and analysis.
    """,
    llm=llm
)

task1 = Task(
    description="https://docs.bittensor.com/",  # Replace with the actual URL
    expected_output="Scrape the data from this webpage, clean it, and return it in a usable format.",
    agent=scraping_agent
)

crew = Crew(
    agents=[scraping_agent],
    tasks=[task1],
    verbose=True
)

result = crew.kickoff()

print("############")
print(result)
