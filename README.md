# 🚀 MyAnimeList Data Miner (Scrapy Crawler)

A robust web crawling and scraping tool built with **Python** and **Scrapy** to extract deep data from the MyAnimeList Top Anime rankings. This project was developed as part of a Data Mining study, focusing on asynchronous requests and multi-level data extraction.

---

## 🛠️ Technical Features
* **Deep Crawling:** Unlike simple scrapers, this bot navigates from the main ranking list into each individual anime page to extract full synopses.
* **Asynchronous Data Transfer:** Utilizes Scrapy's `meta` parameter to pass partially scraped data between different parsing functions (`parse` -> `parse_detalhes`).
* **Smart Pagination:** Automatically detects and follows "Next 50" links to crawl the entire ranking database.
* **Data Cleaning:** Implemented Python list comprehensions and `.strip()` methods to sanitize "dirty" HTML, removing extra whitespaces, newlines, and utility layout classes.
* **Anti-Bot Compliance:** Configured with custom `User-Agents`, `AutoThrottle`, and `Download Delays` to mimic human behavior and respect server resources.



---

## 📊 Extracted Data Structure
The spider generates a structured dataset (`CSV` or `JSON`) containing:

| Field | Description | Source |
| :--- | :--- | :--- |
| **Rank** | Current position in the global ranking | Main Table |
| **Title** | Full name of the anime | Main Table (h3) |
| **Score** | Community rating (e.g., 9.38) | Main Table (td.score) |
| **Information** | Cleaned list: Type, Episode count, and Member count | Main Table (div.information) |
| **Synopsis** | Full plot description | Inner Anime Page (p[itemprop]) |

---

## 🚀 How to Run

### 1. Requirements
* Python 3.12+
* Scrapy
* WSL2 (Recommended for Windows users)

### 2. Installation
```bash
# Clone the repo
git clone [https://github.com/rafa0107/MyanimeList-Crawler.git](https://github.com/rafa0107/MyanimeList-Crawler.git)

# Enter the directory
cd MyanimeList-Crawler

# Install dependencies
pip install -r requirements.txt
```

🧠 Execution
    
To run the spider and save the results to a CSV file:

```bash
scrapy crawl animes -o resultados.csv
```



🧠 Challenges & Solutions
1. Handling Multi-level Scraping
The biggest challenge was retrieving the Synopsis, which isn't available on the main ranking page.
Solution: Used scrapy.Request to trigger a secondary callback function (parse_detalhes). By using the meta dictionary, I ensured that data collected in the first step (Rank, Title) stayed attached to the item until the final yield.

2. Network Resolution (WSL2 DNS)
During development, a DNS lookup failure occurred within the WSL2 environment.
Solution: Investigated and resolved via WSL network stack reset (wsl --shutdown) and verifying the host's DNS resolution.

3. CSS Selector Complexity
The HTML on MyAnimeList uses many utility classes like fl-l or ac.
Solution: Focused on Semantic Classes (like .anime_ranking_h3 and .score-label) to create a resilient scraper that doesn't break if the site's layout changes slightly.

📝 Author
Developed by Rafael Blom as part of a Data Mining academic project.