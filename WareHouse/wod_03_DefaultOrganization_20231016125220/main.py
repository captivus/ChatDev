'''
This is the main file of the word of the day application.
'''
from fastapi import FastAPI
import requests
import logging
app = FastAPI()
@app.get("/word-of-the-day/{date}")
def get_word_of_the_day(date: str):
    try:
        # Fetch the word of the day from the DataMuse API
        response = requests.get(f"https://api.datamuse.com/words?ml={date}&max=1")
        response.raise_for_status()
        word = response.json()[0]['word']
        # Fetch the definition of the word from the Dictionary API
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        response.raise_for_status()
        definition = response.json()[0]['meanings'][0]['definitions'][0]['definition']
        # Fetch two example sentences using the word from the Dictionary API
        examples_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        examples_response.raise_for_status()
        examples = examples_response.json()[0]['meanings'][0]['definitions'][0]['exampleUses'][:2]
        return {
            "word": word,
            "definition": definition,
            "examples": examples
        }
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return {
            "error": "An error occurred while fetching the word of the day."
        }