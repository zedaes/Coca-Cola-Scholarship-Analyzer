import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

def scrapeBios(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 403:
        print(f"Access denied for {url}")
        
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"HTML content from {url[:50]}...") 
    print(soup.prettify()[:1000]) 
    
    richTextDivs = soup.find_all('div', class_='fl-rich-text')
    print(f"Found {len(richTextDivs)} rich-text divs in {url}")
    
    bios = []
    for div in richTextDivs:
        paragraphs = div.find_all('p')
        print(f"Found {len(paragraphs)} paragraphs in a rich-text div")
        bios.extend(paragraphs)
    
    bioTexts = [bio.get_text(separator=' ').strip() for bio in bios]
    print(f"Extracted {len(bioTexts)} bios from {url}")
    
    return bioTexts

def classifyBio(bio, categories):
    bioLower = bio.lower()
    classified = defaultdict(list)
    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(r'\b' + keyword + r'\b', bioLower):
                classified[category].append(keyword)
                break  
            
    return dict(classified)

def classifyAllBios(bios, categories):
    return [classifyBio(bio, categories) for bio in bios]

def saveClassifiedData(classifiedBios, filename='classified_bios.csv'):
    df = pd.DataFrame(classifiedBios)
    df.to_csv(filename, index=False)
    
    return df

def plotCategoryCounts(df):
    categoryCounts = df.apply(lambda x: x.count(), axis=0)
    print(categoryCounts)
    
    categoryCounts.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title('Category Counts in Bios')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('plot.png') 


categories = {
    'Research': [
        'research', 'study', 'experiment', 'analysis', 'data', 'survey', 
        'hypothesis', 'laboratory', 'investigation', 'examination', 
        'fieldwork', 'pilot', 'observation', 'sampling', 'methodology', 
        'test', 'clinical', 'trial', 'measurement', 'theory'
    ],
    'Volunteering': [
        'volunteer', 'service', 'help', 'community work', 'nonprofit', 
        'aid', 'assistance', 'outreach', 'charity', 'philanthropy', 
        'social work', 'humanitarian', 'support', 'mentorship', 
        'civic engagement', 'public service', 'advocacy', 'donation'
    ],
    'Leadership': [
        'president', 'founder', 'leader', 'director', 'head', 'chair', 
        'captain', 'chief', 'commander', 'executive', 'officer', 
        'supervisor', 'manager', 'administrator', 'principal', 
        'coordinator', 'controller', 'boss', 'ruler', 'lead'
    ],
    'STEM': [
        'science', 'technology', 'engineering', 'math', 'stem', 'robotics', 
        'computer', 'programming', 'coding', 'biology', 'chemistry', 
        'physics', 'geology', 'astronomy', 'mathematics', 'calculus', 
        'algebra', 'statistics', 'data science', 'informatics', 
        'software', 'hardware', 'AI', 'artificial intelligence', 
        'machine learning', 'innovation', 'invention'
    ],
    'Advocacy': [
        'advocate', 'advocacy', 'campaign', 'awareness', 'lobbying', 
        'support', 'promotion', 'activism', 'representation', 
        'petition', 'protest', 'rally', 'demonstration', 'rights', 
        'equality', 'justice', 'cause', 'movement', 'initiative', 
        'policy', 'reform'
    ],
    'CreativeArts': [
        'art', 'music', 'performance', 'writing', 'painting', 'drawing', 
        'sculpture', 'dance', 'theatre', 'film', 'photography', 
        'literature', 'poetry', 'craft', 'design', 'media', 'acting', 
        'cinema', 'animation', 'composing', 'singing', 'musician'
    ],
    'Athletics': [
        'athlete', 'sports', 'team', 'coach', 'captain', 'player', 
        'trainer', 'fitness', 'competition', 'game', 'match', 'race', 
        'tournament', 'league', 'event', 'marathon', 'championship', 
        'olympics', 'exercise', 'physical', 'health', 'gym', 'workout'
    ],
    'Awards': [
        'congressional award', 'presidential award', 'scholarship', 
        'grant', 'fellowship', 'prize', 'honor', 'recognition', 
        'accolade', 'achievement', 'medal', 'commendation', 'distinction', 
        'certificate', 'nomination', 'title', 'trophy', 'badge', 'reward'
    ]
}

def main(urls):
    allBios = []
    for url in urls:
        bios = scrapeBios(url)
        allBios.extend(bios)
    classifiedBios = classifyAllBios(allBios, categories)
    df = saveClassifiedData(classifiedBios)
    plotCategoryCounts(df)
    
    return df

urls = [
    'https://www.coca-colascholarsfoundation.org/about/2020-scholar-bios/',
    'https://www.coca-colascholarsfoundation.org/about/2021-scholar-bios/',
    'https://www.coca-colascholarsfoundation.org/about/2022-scholar-bios/',
    'https://www.coca-colascholarsfoundation.org/about/2023-scholar-bios/',
    'https://www.coca-colascholarsfoundation.org/about/2024-scholar-bios/'
]

classifiedDf = main(urls)
