import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re
import time

def get_leaders():
    
    root_url = "https://country-leaders.onrender.com"   #  root URL

    
    cookie_url = root_url + "/cookie"     # cookies
    cookies = requests.get(cookie_url)
    cookies_to_use = cookies.cookies

    
    countries_url = root_url + "/countries"     # list of countries
    response = requests.get(countries_url, cookies=cookies_to_use)
    countries = response.json()

   
    leaders_per_country = {}      # Loop over countries and get their leaders
    for country in countries:
        leaders_url = root_url + "/leaders"
        response = requests.get(leaders_url, cookies=cookies_to_use, params={"country": country})
        leaders = response.json()
        leaders_per_country[country] = leaders

    
    return leaders_per_country      #  Return the dictionary





#  collect Wikipedia URLs only ---
def get_wikipedia_urls_per_country():
    leaders_data = get_leaders()  # get all leaders
    urls_per_country = {}         # empty dictionary to store results

    for country, leaders in leaders_data.items():
        print("Processing country:", country)      #This is nice to have while waiting for the firts paragragh extraction at last. 
        wiki_urls = []            # start an empty list for this country

        for leader in leaders:    # loop over each leader
            url = leader.get("wikipedia_url")
            if url:               # if the link exists
                wiki_urls.append(url)

        urls_per_country[country] = wiki_urls  # save the list to the dictionary

    return urls_per_country




""" I have provided a smaple of the paragrapghs in different languges(one link per country) and aksed ChatGPT to write suitable regx for me, 
it was so messy so I pu it as a separate function to fit neater in get_first_paragraph function. """ 

# --- Step 1: Define a regex-based cleaner ---
def clean_wikipedia_text(text):
    # 1. Remove footnotes like [1], [a], [12]
    text = re.sub(r'\[[^\]]*\]', '', text)
    
    # 2. Remove pronunciation icons or similar symbols (ⓘ, ⚫, †, etc.)
    text = re.sub(r'[ⓘ⚫•†‡]', '', text)
    
    # 3. Remove pronunciation parentheses (like (uitspraakⓘ))
    text = re.sub(r'\([^()]*uitspraak[^()]*\)', '', text, flags=re.IGNORECASE)
    
    # 4. Replace multiple spaces or newlines with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # 5. Remove non-breaking spaces
    text = text.replace('\xa0', ' ')
    
    # 6. Trim extra spaces at beginning and end
    return text.strip()




def get_first_paragraph():
    #print(wikipedia_url)  # we can have this for debugging / monitoring
    
    all_paragraphs = [] 

    urls_per_country = get_wikipedia_urls_per_country()
    
    for country, links in urls_per_country.items():
        for link in links:
            time.sleep(1)

            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0"}
            response = requests.get(link, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
        
        # Loop over <p> tags and find the first non-empty paragraph
                for p in soup.find_all('p'):
                    if p.find("b"):
                        text = p.get_text().strip()
                        if text:  # ensure paragraph is not empty
                            cleaned_text = clean_wikipedia_text(text)  # apply regex cleaning
                            all_paragraphs.append({
                                "country": country,
                                "url": link,
                                "paragraph": cleaned_text
                            })
                            break   #we break inside the loop so that it doesnot go through the next paragraphs - it stops the firts time that finds a text :-)
                else:
                    print("Error:", response.status_code)
                    return None
    
    return all_paragraphs


import json
with open("leaders_per_country.json", "w", encoding="utf-8") as f:
    json.dump(get_first_paragraph(), f, ensure_ascii=False, indent=2)
