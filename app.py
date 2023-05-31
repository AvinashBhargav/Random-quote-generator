import requests
import random

def get_random_quote():
    url = "https://type.fit/api/quotes"

    response = requests.get(url)
    data = response.json()
    random_quote = random.choice(data)

    # Extract the quote and author from the random quote
    quote = random_quote["text"]
    author = random_quote["author"]
    return quote, author
quote, author = get_random_quote()
print(f'"{quote}" - {author}')
