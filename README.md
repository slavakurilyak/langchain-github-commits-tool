LangChain GitHub Commits Tool
=============================

This tool allows you to fetch all the commits from a given GitHub repository. It is built using the LangChain library and the OpenAI language model.

Requirements
------------

-   Python 3.7 or higher
-   `langchain` library
-   `requests` library
-   `dotenv` library

Installation
------------

1.  Clone or download the repository
2.  Install the required libraries using pip: `pip install -r requirements.txt`
3.  Copy the `.env.example` file to a new file called `.env`: `cp .env.example .env`
4.  Edit the `.env` file and set the following variables:
    -   `OPENAI_API_KEY`: your OpenAI API key
    -   `GITHUB_API_TOKEN`: your GitHub API token
    -   `GITHUB_OWNER`: the owner of the repository
    -   `GITHUB_REPO_NAME`: the name of the repository you want to fetch commits from
5.  Run the script: `python main.py`

Usage
-----

After completing the installation, you can use the tool by running the `main.py` script. The script will fetch the commits for the specified repository and print them to the console.

Note: The `.env` file contains sensitive information such as API keys and access tokens. Make sure to keep it private and do not share it with others.

To Do
-----

-  [ ] Fix error 404