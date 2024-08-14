# Coca Cola Scholarship Analyzer

This Python script scrapes biographies from the Coca-Cola Scholars Foundation website, classifies them into various categories based on keywords, and generates a CSV file and a bar chart of the categorized data.

## Features

- **Scraping**: Retrieves biographies from specified URLs on the Coca-Cola Scholars Foundation website.
- **Classification**: Categorizes biographies based on predefined keyword categories.
- **Data Storage**: Saves classified data into a CSV file.
- **Visualization**: Plots a bar chart showing counts of each category.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library
- `matplotlib` library

You can install the required libraries using pip:

```
pip install requests beautifulsoup4 pandas matplotlib
```

## Usage
- Set Up URLs: Modify the urls list in the script to include the URLs of the pages you want to scrape.

Run the Script: Execute the script. It will:
- Scrape biographies from the given URLs.
- Classify the biographies based on predefined categories.
- Save the classified data into a CSV file named classified_bios.csv.
- Generate a bar chart showing the counts of each category and save it as plot.png.

## Check Output:
- The classified data will be saved in classified_bios.csv.
- The bar chart will be saved as plot.png in the current directory.


## Acknowledgments
- Coca-Cola Scholars Foundation
- BeautifulSoup
- Pandas
- Matplotlib


Feel free to modify any sections to better fit your needs or to include additional details which categorize the results even more.