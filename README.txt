# Archive of Our Own (AO3) Data Scraper and Analyzer

This Python script allows you to scrape data from your "Archive of Our Own" (AO3) reading history, store it in an SQLite database, and perform basic data analysis on it. You can also export the data to a CSV file for further analysis in spreadsheet software like Excel.

## Prerequisites

Before you can use this script, make sure you have the following installed:

- Python 3.x
- Required Python packages (you can install them using `pip`):
  - requests
  - beautifulsoup4
  - sqlite3

## Usage

1. Clone or download this repository to your local machine.

2. Open the `ao3_scraper.py` file and edit the following variables:

   - `base_url`: Replace `"YourUsernameHere"` with your actual AO3 username.
   - `database_name`: Specify the name of the SQLite database where the scraped data will be stored.
   - `csv_file_name`: Specify the name of the CSV file where the data will be exported.

3. Save your changes in `ao3_scraper.py`.

4. Open a terminal or command prompt and navigate to the directory containing `ao3_scraper.py`.

5. Run the script by executing the following command:

   ```bash
   python ao3_scraper.py
