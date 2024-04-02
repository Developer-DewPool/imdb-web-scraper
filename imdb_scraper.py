import requests
import json
import logging
import sys
from bs4 import BeautifulSoup
import csv
import time
import random
import unittest
from typing import List
from concurrent.futures import ThreadPoolExecutor

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# Function to scrape movie details
def scrape_movie_details(movie_url):
    try:
        logging.info(f"Scraping movie details from URL: {movie_url}")
        
        # Read local HTML file for testing
        with open('test_data/movie_page.html', 'r') as file:
            movie_soup = BeautifulSoup(file, 'html.parser')

        title_element = movie_soup.find('h1')
        if not title_element:
            logging.error(f"Title not found for {movie_url}")
            return None
        title = title_element.text.strip()

        year_element = movie_soup.find('span', class_='TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex')
        if not year_element:
            logging.error(f"Release year not found for {movie_url}")
            return None
        year = year_element.text.strip()

        rating_element = movie_soup.find('span', class_='AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV')
        if not rating_element:
            logging.error(f"IMDb rating not found for {movie_url}")
            return None
        rating = rating_element.text.strip()

        directors = [director.text.strip() for director in movie_soup.find_all('a', class_='StyledComponents__CastListItem-y9ygcu-6 hWtTli')]

        cast_list = []
        for actor in movie_soup.find_all('a', class_='StyledComponents__ActorName-y9ygcu-8 eBIsDA'):
            cast_list.append(actor.text.strip())

        plot_summary_element = movie_soup.find('span', class_='GenresAndPlot__TextContainerBreakpointL-cum89p-3 wUBQtm')
        if not plot_summary_element:
            logging.error(f"Plot summary not found for {movie_url}")
            return None
        plot_summary = plot_summary_element.text.strip()

        movie_details = {
            'Title': title,
            'Release Year': year,
            'IMDb Rating': rating,
            'Directors': directors,
            'Cast': cast_list,
            'Plot Summary': plot_summary
        }

        return movie_details
    except Exception as e:
        logging.error(f"Error scraping {movie_url}: {e}")
        return None

# Function to scrape search results
def scrape_search_results(keyword: str, pages: int) -> List[dict]:
    base_url = f"https://www.imdb.com/search/title/?title_type=feature&genres={keyword}&start="
    all_movies = []

    for page in range(pages):
        url = base_url + str(page * 50 + 1)
        logging.info(f"Scraping page {page + 1}...")
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            movie_links = [a['href'] for a in soup.select('.lister-item-header a')]
            
            with ThreadPoolExecutor(max_workers=5) as executor:
                movie_details = list(executor.map(scrape_movie_details, [f"https://www.imdb.com{link}" for link in movie_links]))
            
            all_movies.extend(movie_details)
            
            # Random sleep to avoid hitting server too hard
            time.sleep(random.uniform(1, 2))
        except Exception as e:
            logging.error(f"Error scraping page {page + 1}: {e}")

    return all_movies

# Function to save data to JSON
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Function to save data to CSV
def save_to_csv(data, filename):
    keys = data[0].keys() if len(data) > 0 else []
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Main function
def main():
    # Input for genre or keyword
    keyword = input("Enter genre or keyword (e.g., 'comedy', 'action'): ")

    # Input for number of pages to scrape
    try:
        pages = int(input("Enter number of pages to scrape: "))
    except ValueError:
        logging.error("Invalid input. Please enter a valid number of pages.")
        return

    # Scrape search results
    logging.info(f"Scraping IMDb search results for '{keyword}'...")
    movies = scrape_search_results(keyword, pages)

    if not movies:
        logging.error("No movies found. Exiting.")
        return

    # Save to JSON
    json_filename = f"{keyword}_movies.json"
    save_to_json(movies, json_filename)
    logging.info(f"Data saved to {json_filename}")

    # Save to CSV
    csv_filename = f"{keyword}_movies.csv"
    save_to_csv(movies, csv_filename)
    logging.info(f"Data saved to {csv_filename}")

if __name__ == "__main__":
    main()
