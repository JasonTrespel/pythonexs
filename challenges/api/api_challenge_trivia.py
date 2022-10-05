#!/usr/bin/env python3

"""Trivia API challenge answer!"""

# import requests
import requests

# set up URL variable for trivia
# URL = "https://opentdb.com/api.php?amount=15&category=10&difficulty=medium&type=boolean"
URL = "https://opentdb.com/api.php?amount=1&category=10&difficulty=medium&type=multiple&token="
token = "f9e0a82ec29c61c5d3d2cc0a485b8ecbe337b8b6c34a4c25b07a3d660355853b"
# let the fun begin
def main():
    """Connect to open trivia and return JSON."""
    # set a while loop to keep prompting the user for questions.
    while(True):

    # finish the url
    resp = requests.get(f"{URL}{token}")
    
    question = resp.json().get("reults")
    print(results)

    


if __name__ == "__main__":
    main()
