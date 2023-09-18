import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import csv

# Function to scrape and store data
def scrape_and_store_data(base_url, database_name):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    stories = soup.find_all("li", class_="reading")

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    for story in stories:
        title = story.find("a", class_="heading").text.strip()
        author = story.find("a", class_="by").text.strip()
        genre = story.find("dd", class_="fandoms").text.strip()
        word_count = int(story.find("dd", class_="words").text.strip().replace(",", ""))
        timestamp = datetime.now()

        cursor.execute("""
        INSERT INTO stories (title, author, genre, word_count, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """, (title, author, genre, word_count, timestamp))

    conn.commit()
    conn.close()

# Function to export data to CSV
def export_to_csv(database_name, csv_file_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM stories")
    rows = cursor.fetchall()

    with open(csv_file_name, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Title", "Author", "Genre", "Word Count", "Timestamp"])
        csvwriter.writerows(rows)

    conn.close()

if __name__ == "__main__":
    base_url = "https://archiveofourown.org/users/YourUsernameHere/readings"
    database_name = "ao3_data.db"
    csv_file_name = "ao3_data.csv"

    # Scrape and store data
    scrape_and_store_data(base_url, database_name)

    # Export data to CSV
    export_to_csv(database_name, csv_file_name)

    # Analyse data (example: finding favorite genres)
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT genre, COUNT(*) as count
    FROM stories
    GROUP BY genre
    ORDER BY count DESC
    """)

    favorite_genres = cursor.fetchall()

    print("Favorite Genres:")
    for genre, count in favorite_genres:
        print(f"{genre}: {count} stories")

    conn.close()

    print(f"Data has been scraped, stored in '{database_name}', and exported to '{csv_file_name}'.")
