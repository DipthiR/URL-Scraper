import requests
from bs4 import BeautifulSoup

# Function to scrape URLs from a webpage
def scrape_urls(url):
    # Send a GET request to the webpage
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Successfully accessed {url}")
        
        # Parse the content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find all anchor tags (<a>) with href attributes
        links = soup.find_all("a", href=True)
        
        print("\nURLs found on the page:")
        for link in links:
            print(link.get("href"))
    else:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")

# Main function
def main():
    # URL of the webpage to scrape
    url = input("Enter the URL of the webpage to scrape: ")
    
    # Call the function to scrape the URLs
    scrape_urls(url)

if __name__ == "__main__":
    main()
