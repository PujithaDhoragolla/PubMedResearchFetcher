import argparse
from fetcher import PubMedFetcher

def main():
    parser = argparse.ArgumentParser(description="Fetch papers from PubMed based on query")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Output CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()

    # Initialize fetcher
    fetcher = PubMedFetcher(args.query)
    
    # Fetch paper details
    paper_ids = fetcher.fetch_paper_ids()
    papers = fetcher.fetch_paper_details(paper_ids)

    # Save to file or print to console
    if args.file:
        fetcher.save_to_csv(papers, args.file)
        print(f"✅ CSV file generated: {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
