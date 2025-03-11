import requests
import pandas as pd

# Base URL for PubMed API
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# Function to fetch research papers
def fetch_pubmed_papers(query, max_results=10):
    # API Parameters
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    # Sending GET Request
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Extracting paper IDs
    paper_ids = data['esearchresult']['idlist']

    # Fetch paper details (dummy for now)
    papers = []
    for paper_id in paper_ids:
        papers.append({
            "Paper ID": paper_id,
            "Title": f"Title for {paper_id}",
            "Authors": "Author Name",
            "Journal": "Journal Name"
        })

    # Convert to CSV
    df = pd.DataFrame(papers)
    df.to_csv("pubmed_papers.csv", index=False)
    print(f"✅ Successfully saved {len(papers)} papers to 'pubmed_papers.csv'.")

# Main Function
if __name__ == "__main__":
    query = input("Enter your search term (e.g., Cancer Research): ")
    fetch_pubmed_papers(query)
