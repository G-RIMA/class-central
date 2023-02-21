import os
import requests

url = "https://www.classcentral.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 response codes
except requests.exceptions.RequestException as e:
    print("Error: Failed to fetch the homepage HTML")
    print(e)
else:
    pic_content = response.text
    # do something with the HTML content
    with open("links.html", "w", encoding="utf-8") as file:
        file.write(pic_content)