🌍 World Leaders Data Extractor

Collecting and Cleaning Wikipedia Biographies of World Leaders
<p align="center">
  <img src="world photo.jpg" alt="Global Leaders Data Visualization" width="650"><br>
  <em>Figure: Global data extraction and analysis from Wikipedia.</em>
</p>


📝 Description

World Leaders Data Extractor is a Python program that automatically collects information about world leaders from a public API and extracts the first cleaned paragraph from their Wikipedia pages.

It gathers data from all available countries, cleans unwanted characters and references, and stores the final text in a structured JSON file.

This project demonstrates how web scraping, API requests, and text cleaning can be combined for creating clean and analyzable datasets — ideal for academic, linguistic, or data science applications.

🗂️ Repo Structure
C:.
|   main.py
|   README.md
|   leaders_per_country.json

⚙️ Usage
1. Install Dependencies

Make sure you have Python 3 installed. Then install the required libraries:
````
pip install requests beautifulsoup4
````
2. Run the Program

Execute the script to collect and process leader data:
````
python main.py
````
3. Wait for Processing

The program will connect to the API, retrieve leader data for all countries, and extract the first paragraph from each leader’s Wikipedia page.
A short delay between requests ensures ethical and responsible scraping.

4. View the Results

The collected and cleaned data will be saved as a JSON file:
````
leaders_per_country.json
````
Each entry includes:

Country name

Wikipedia URL

First cleaned paragraph


💡 Example Output
````
{
  "country": "France",
  "url": "https://en.wikipedia.org/wiki/Emmanuel_Macron",
  "paragraph": "Emmanuel Macron is a French politician serving as the President of France since 2017."
}
````
⏱️ Timeline

This project was completed over three days, including debugging, regex refinement, and data cleaning validation.

This project was created as part of my AI and data collection learning journey, integrating web technologies, API communication, and text processing, as part of the AI Boocamp at BeCode.org.

Connect with me on [LinkedIn](https://www.linkedin.com/in/hamideh-be/ ).