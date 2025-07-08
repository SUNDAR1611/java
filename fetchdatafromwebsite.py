import requests
from bs4 import BeautifulSoup
import mysql.connector

# Step 1: MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5028"  # Change if needed
)
cursor = conn.cursor()

# Step 2: Create New Database and Table
cursor.execute("CREATE DATABASE IF NOT EXISTS scraped_data")
conn.database = "scraped_data"

cursor.execute("DROP TABLE IF EXISTS countries")
cursor.execute("""
    CREATE TABLE countries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        capital VARCHAR(100),
        population INT,
        area FLOAT
    )
""")
print("✅ Database and table ready.")

# Step 3: Scrape Website
url = "https://www.scrapethissite.com/pages/simple/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

country_divs = soup.select("div.country")

countries = []
for div in country_divs:
    name = div.find("h3", class_="country-name").text.strip()
    capital = div.find("span", class_="country-capital").text.strip()
    population = div.find("span", class_="country-population").text.strip().replace(',', '')
    area = div.find("span", class_="country-area").text.strip().replace(',', '')

    try:
        population = int(population)
        area = float(area)
    except:
        population = 0
        area = 0.0

    countries.append((name, capital, population, area))

print(f"✅ Scraped {len(countries)} countries.")

# Step 4: Insert into Database
insert_query = """
INSERT INTO countries (name, capital, population, area)
VALUES (%s, %s, %s, %s)
"""

for country in countries:
    cursor.execute(insert_query, country)

conn.commit()
print(f"✅ Inserted {len(countries)} countries into the database.")

# Step 5: Display Data
cursor.execute("SELECT name, capital, population, area FROM countries")
rows = cursor.fetchall()

print("\n📋 Countries List:")
for row in rows:
    print(f"{row[0]} → Capital: {row[1]} | Population: {row[2]} | Area: {row[3]} km²")

# Step 6: Cleanup
cursor.close()
conn.close()
