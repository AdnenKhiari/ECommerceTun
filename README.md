# Web Scraping Project with Scrapy

## Description:
A Scrapy-based Python web scraper designed for extracting product information from the Mytek Tunisia website. It efficiently navigates through main and sub-categories, collecting data on product titles, prices, and types, and organizes the information into a CSV file for straightforward data analysis.

## Components:
- **Script:** Python implementation utilizing the Scrapy framework.
- **Data File:** CSV file containing organized product details.

## Workflow:
1. The script sends requests to the Mytek Tunisia website, initiating from the main page.
2. It navigates through main and sub-categories, reaching individual product pages.
3. On product pages, the script extracts information like product titles, prices, and types.
4. Extracted data is structured and stored in the CSV file.
5. The process continues until all relevant pages are crawled.

## Technologies:
- **Scrapy Framework:** Utilized for efficient web scraping.
- **Python:** Programming language used for script development.
- **CSV:** Data storage format for the extracted product information.

## Notes:
- The script uses asynchronous processing for efficient handling of multiple requests.
- The CSV file provides an organized output for straightforward analysis.

Note: Ensure compliance with ethical guidelines and legal considerations when using this script for web scraping activities.
