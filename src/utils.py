"""Utility functions for data processing and analysis"""

import pandas as pd
from typing import Dict, List
import json


def extract_resources_info(package_data: Dict) -> pd.DataFrame:
    """
    Extract resource information from a package into a DataFrame
    
    Args:
        package_data: Package data from package_show
        
    Returns:
        DataFrame with resource information
    """
    resources = package_data['result']['resources']
    
    df = pd.DataFrame(resources)
    
    # Select useful columns
    useful_cols = ['id', 'name', 'format', 'url', 'size', 
                   'created', 'last_modified', 'description']
    available_cols = [col for col in useful_cols if col in df.columns]
    
    return df[available_cols]


def search_by_keywords(api, keywords: List[str], limit: int = 20) -> pd.DataFrame:
    """
    Search for datasets by keywords
    
    Args:
        api: OpenCanadaAPI instance
        keywords: List of keywords to search
        limit: Maximum number of results
        
    Returns:
        DataFrame with search results
    """
    query = " OR ".join(keywords)
    results = api.package_search(query=query, rows=limit)
    
    packages = results['result']['results']
    
    return pd.DataFrame([{
        'id': pkg['id'],
        'name': pkg['name'],
        'title': pkg.get('title_translated', {}).get('en', pkg['name']),
        'organization': pkg.get('organization', {}).get('title', 'N/A'),
        'num_resources': pkg.get('num_resources', 0),
        'metadata_modified': pkg.get('metadata_modified', ''),
    } for pkg in packages])


def save_json(data: Dict, filepath: str) -> None:
    """Save data to JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(filepath: str) -> Dict:
    """Load data from JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)