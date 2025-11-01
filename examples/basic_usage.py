"""
Basic usage examples for the Open Canada API
Run from repo root: python examples/basic_usage.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.api_client import OpenCanadaAPI
from src.utils import extract_resources_info, search_by_keywords, save_json
import pandas as pd


def main():
    # Initialize API client
    api = OpenCanadaAPI()
    
    # Example 1: Search for datasets about climate
    print("=== Searching for climate datasets ===")
    climate_results = api.package_search(query="climate", rows=5)
    print(f"Found {climate_results['result']['count']} total results")
    print(f"Showing first 5:\n")
    
    for pkg in climate_results['result']['results']:
        title = pkg.get('title_translated', {}).get('en', pkg['name'])
        print(f"- {title}")
    
    print("\n")
    
    # Example 2: Get details about a specific dataset
    # Using the Open Government API dataset as an example
    print("=== Getting dataset details ===")
    dataset_id = "2d90548d-50ef-4802-91f8-c59c5cf68251"
    dataset_info = api.package_show(dataset_id)
    
    print(f"Title: {dataset_info['result']['title_translated']['en']}")
    print(f"Organization: {dataset_info['result']['organization']['title']}")
    print(f"Number of resources: {len(dataset_info['result']['resources'])}")
    
    # Extract resource information
    resources_df = extract_resources_info(dataset_info)
    print("\nResources:")
    print(resources_df[['name', 'format', 'size']])
    
    print("\n")
    
    # Example 3: Search by multiple keywords
    print("=== Searching by keywords ===")
    keywords = ["employment", "statistics", "canada"]
    results_df = search_by_keywords(api, keywords, limit=10)
    print(results_df[['title', 'organization', 'num_resources']])
    
    # Save results
    Path('data').mkdir(exist_ok=True)
    save_json(dataset_info, 'data/example_dataset.json')
    results_df.to_csv('data/search_results.csv', index=False)
    print("\n=== Results saved to data directory ===")


if __name__ == "__main__":
    main()