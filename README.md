# URL-Scraper
# 🌐 URL Scraper

A simple Python script to scrape all the URLs present on a webpage. This tool uses **BeautifulSoup** and **requests** libraries to extract and display all hyperlinks (`<a>` tags with `href` attributes) from a given webpage.

---

## 📌 Project Overview

This Python script:
- Fetches the HTML content of a given URL.
- Scrapes all the URLs embedded within the webpage using `BeautifulSoup`.
- Displays the URLs found on the page.

---

## 🛠 How to Run

1. Clone or download this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
Run the url_scraper.py script:

python url_scraper.py
You will be prompted to enter the URL of the webpage you want to scrape.

The script will then print all the URLs found on that page.

## 🎮 Example Usage
Input:
Enter the URL of the webpage to scrape: https://example.com
Output:
Successfully accessed https://example.com

URLs found on the page:
https://example.com/page1
https://example.com/page2
https://example.com/contact
...
## 🚀 Features
URL Extraction: Scrapes all URLs (href attributes in <a> tags) from a given webpage.

User-Friendly: Prompts you for a URL and displays the extracted links.

Easy to Use: Run with a single command and get all links from a webpage.
