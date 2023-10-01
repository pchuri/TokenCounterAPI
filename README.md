# TokenCounterAPI

A simple and fast API for counting tokens in a text string using FastAPI and tiktoken.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/pchuri/TokenCounterAPI.git
cd TokenCounterAPI
```

2.	Create a virtual environment and activate it:
`python3 -m venv env
source env/bin/activate`


3.	Install the requirements:
`pip install -r requirements.txt`

4.	Run the FastAPI application:
`uvicorn main:app --reload`

## Usage

Send a GET request to the /count_tokens endpoint with model_name and text query parameters:

http://127.0.0.1:8000/count_tokens?model_name=gpt-4&text=hello%20world

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.