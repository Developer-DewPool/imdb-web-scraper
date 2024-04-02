import unittest
import csv
import json
from imdb_scraper import scrape_movie_details, scrape_search_results, save_to_json, save_to_csv


class TestIMDBScraper(unittest.TestCase):
    def test_scrape_movie_details(self):
        # Updated movie URL for testing
        movie_url = "https://www.imdb.com/title/tt0468569/"
        movie_details = scrape_movie_details(movie_url)
        self.assertIsNotNone(movie_details)
        self.assertIn('Title', movie_details)
        self.assertIn('Release Year', movie_details)
        self.assertIn('IMDb Rating', movie_details)
        self.assertIn('Directors', movie_details)
        self.assertIn('Cast', movie_details)
        self.assertIn('Plot Summary', movie_details)

    def test_scrape_search_results(self):
        keyword = "comedy"
        pages = 2
        movies = scrape_search_results(keyword, pages)
        self.assertIsNotNone(movies)
        self.assertIsInstance(movies, list)

    def test_save_to_json(self):
        data = [{'Title': 'Movie1', 'Release Year': '2022', 'IMDb Rating': '8.0'}]
        filename = "test_movies.json"
        save_to_json(data, filename)
        with open(filename, 'r') as f:
            saved_data = json.load(f)
        self.assertEqual(saved_data, data)

    def test_save_to_csv(self):
        data = [{'Title': 'Movie1', 'Release Year': '2022', 'IMDb Rating': '8.0'}]
        filename = "test_movies.csv"
        save_to_csv(data, filename)
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            saved_data = [row for row in reader]
        self.assertEqual(saved_data, data)


if __name__ == '__main__':
    unittest.main()
