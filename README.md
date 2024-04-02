# IMDb Web Scraper

This is a Python script to scrape movie details from IMDb based on a specific genre or keyword. It retrieves information such as title, release year, IMDb rating, directors, cast, and plot summary for each movie.

## How to Run

### Setting Up Virtual Environment (Optional but Recommended)

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Developer-DewPool/imdb-web-scraper
   ```

2. Navigate to the project directory:
   ```bash
   cd imdb-web-scraper
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows (cmd):
     ```bash
     venv\Scripts\activate
     ```
   - On Windows (PowerShell):
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Installing Dependencies

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Scraper

1. Run the script:
   ```bash
   python imdb_scraper.py
   ```

2. Follow the prompts to enter the genre or keyword you want to search for and the number of pages to scrape.

3. The script will scrape the IMDb search results, store the data in both JSON and CSV formats, and save the files in the project directory.

### Running Unit Tests

1. To run the unit tests, use the following command:
   ```bash
   python -m unittest test_imdb_scraper.py
   ```

## Project Structure

- `imdb_scraper.py`: The main Python script to scrape IMDb movie details.
- `test_imdb_scraper.py`: Unit tests for the scraper functions.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This file.

## Additional Information

- The scraper uses BeautifulSoup for HTML parsing and requests for making HTTP requests.
- Error handling is implemented to handle unexpected issues gracefully.
- Data is stored in structured formats like JSON and CSV for easy analysis.
- Logging is included to provide information on the scraping process.

Feel free to modify and expand upon this script as needed!