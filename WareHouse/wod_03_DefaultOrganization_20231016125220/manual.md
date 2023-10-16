# Word of the Day Application User Manual

## Introduction

The Word of the Day Application is an API that generates a word of the day for a given date. It uses the DataMuse API to fetch the word of the day and the Dictionary API to fetch the definition and example sentences for the word. This user manual provides instructions on how to install the application, use the API, and run unit tests.

## Installation

To install the Word of the Day Application, follow these steps:

1. Create a virtual environment for your project.
2. Activate the virtual environment.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## API Usage

The Word of the Day Application API provides the following endpoint:

```
GET /word-of-the-day/{date}
```

### Parameters

- `date` (required): The date for which to get the word of the day in the format `YYYY-MM-DD`.

### Response

The API returns a JSON response with the following structure:

```json
{
  "word": "string",
  "definition": "string",
  "examples": ["string", "string"]
}
```

- `word`: The word of the day.
- `definition`: The definition of the word.
- `examples`: Two example sentences using the word.

### Example

To get the word of the day for a specific date, send a GET request to the following endpoint:

```
GET /word-of-the-day/2022-01-01
```

The response will be a JSON object with the word, definition, and examples:

```json
{
  "word": "example",
  "definition": "a thing characteristic of its kind or illustrating a general rule",
  "examples": [
    "this small skirmish is a typical example of fighting at sea",
    "she refused to give an example of a time when she had acted dishonestly"
  ]
}
```

## Error Handling

If the application encounters any errors, they will be logged to the console. The API will return a JSON response with an error message in case of an error.

## Unit Tests

The Word of the Day Application includes unit tests to ensure the correctness of the API. To run the unit tests, follow these steps:

1. Activate the virtual environment.
2. Run the following command:
   ```
   pytest test_main.py
   ```

The unit tests will be executed, and the results will be displayed in the console.

## Conclusion

The Word of the Day Application is a powerful API that generates a word of the day for a given date. It provides the word, definition, and example sentences for the word. By following the instructions in this user manual, you can easily install the application, use the API, and run unit tests to ensure its correctness. Enjoy exploring new words every day with the Word of the Day Application!