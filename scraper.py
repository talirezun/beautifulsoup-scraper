import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://croatiarevealed.com/best-teranino-cocktail-recepies/"  # Replace with your target URL

# Send an HTTP request to the website
headers = {"User-Agent": "Mozilla/5.0"}  # Mimics a real browser
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract visible text from the webpage
    text = soup.get_text(separator="\n", strip=True)

    # Save the extracted text to a file
    with open("scraped_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("Scraping successful! Text saved in 'scraped_text.txt'.")
else:
    print(f"Failed to fetch page. Status Code: {response.status_code}")
