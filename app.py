import requests

API_URL = "https://official-joke-api.appspot.com/random_joke"


def get_joke():
    """
    Fetch a random joke from the public API.
    Returns:
        dict: joke data if successful
        None: if request fails
    """
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "setup" in data and "punchline" in data:
            return data
        else:
            print("Unexpected response format from API.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return None


def display_joke():
    joke = get_joke()
    if joke:
        print("\nJoke of the Day")
        print("----------------")
        print(f"Setup: {joke['setup']}")
        print(f"Punchline: {joke['punchline']}")
    else:
        print("Sorry, unable to fetch a joke right now.")


if __name__ == "__main__":
    display_joke()