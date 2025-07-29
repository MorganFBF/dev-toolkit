# url-shortener.py
import requests

def shorten_url(long_url):
    api_url = "http://tinyurl.com/api-create.php?url="
    response = requests.get(api_url + long_url)
    if response.status_code == 200:
        return response.text
    else:
        return None

if __name__ == "__main__":
    url = input("Enter the URL to shorten: ")
    short_url = shorten_url(url)
    if short_url:
        print("Shortened URL:", short_url)
    else:
        print("Failed to shorten the URL.")
