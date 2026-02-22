# Web Mining & Data Extraction Project

A professional data crawler built with **Python** and the **Scrapy** framework. This project was developed to demonstrate automated data collection from a live chocolate online business, focusing on accuracy and efficient navigation.

##  Overview
The goal of this project was to create a resilient "spider" capable of browsing through an entire product catalog, extracting specific details, and saving them into a structured format.

##  Key Features
* **Automated Pagination:** The crawler automatically detects and follows "Next Page" links to ensure no data is missed across the site.
* **Data Sanitization:** Implemented logic to clean raw HTML "noise," ensuring prices and product names are stored in a readable format.
* **Structured Export:** Automatically generates a `CSV` file containing all gathered information.
* **Ethical Crawling:** Configured to respect the website's speed limits and access rules.

##  Data Points Extracted
The project captures:
* **Product Name:** The full title of each item.
* **Price:** Cleaned numerical values.
* **Product Link:** The direct URL to the item for verification.

##  Tech Stack
* **Language:** Python 3.x
* **Framework:** Scrapy

##  How to Use
1.  **Clone this repository:**
    ```bash
    git clone [https://github.com/Ishikakaur8072005/scraping.git](https://github.com/Ishikakaur8072005/scraping.git)
    ```
2.  **Install Scrapy:**
    ```bash
    pip install scrapy
    ```
3.  **Run the crawler:**
    ```bash
    scrapy crawl chocolate_spider -o lab_results.csv
    ```

---
