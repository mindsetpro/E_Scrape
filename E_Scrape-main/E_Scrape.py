import urllib.request
import json
import requests
from bs4 import BeautifulSoup
import os
import wget

class EScrape:
    """
    A utility for fetching and saving various types of content from a URL.
    
    Attributes:
        url (str): The URL to fetch content from.
    """
    
    def __init__(self, url):
        """
        Initialize a new EScrape instance.

        Args:
            url (str): The URL to fetch content from.
        """
        self.url = url

    def fetch_json(self):
        """
        Fetch JSON data from the specified URL.

        Returns:
            dict: A dictionary representing the JSON data.

        Raises:
            ValueError: If there's an issue fetching or parsing the JSON data.
        """
        try:
            with urllib.request.urlopen(self.url) as response:
                data = response.read().decode('utf-8')

            try:
                json_data = json.loads(data)
                return json_data
            except json.JSONDecodeError as e:
                raise ValueError(f"Failed to parse JSON: {str(e)}")

        except urllib.error.URLError as e:
            raise ValueError(f"Failed to fetch data from the URL: {str(e)}")

    def fetch_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            html = response.text
            return html
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Failed to fetch HTML from the URL: {str(e)}")

    def scrape_html(self):
        html = self.fetch_html()
        soup = BeautifulSoup(html, 'html.parser')
        # Now you can extract specific data from the HTML using BeautifulSoup methods.
        return soup

    def copy_website(self, output_directory):
        try:
            os.makedirs(output_directory, exist_ok=True)
            wget.download(self.url, out=output_directory)
            print(f"Website copied to {output_directory}")
        except Exception as e:
            raise ValueError(f"Failed to copy the website: {str(e)}")

    def scrape_images(self, output_directory):
        try:
            html = self.fetch_html()
            soup = BeautifulSoup(html, 'html.parser')
            img_tags = soup.find_all('img')
            for img_tag in img_tags:
                img_url = img_tag.get('src')
                if img_url:
                    response = requests.get(img_url)
                    if response.status_code == 200:
                        with open(os.path.join(output_directory, os.path.basename(img_url)), 'wb') as img_file:
                            img_file.write(response.content)
            print(f"Images scraped and saved to {output_directory}")
        except Exception as e:
            raise ValueError(f"Failed to scrape images: {str(e)}")
