import random

def get_random_quote():
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
        "The best way to predict the future is to create it. - Peter Drucker",
        "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    quote = get_random_quote()
    print(quote)
