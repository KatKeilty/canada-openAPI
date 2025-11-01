"""
Client for interacting with the Open Canada API
Documentation: https://open.canada.ca/en/access-our-application-programming-interface-api
"""

import requests
import json
from typing import Dict, List, Optional
from urllib.parse import urljoin


class OpenCanadaAPI:
    """Client for Open Canada API (CKAN-based)"""
    
    BASE_URL = "https://open.canada.ca/data/api/3/action/"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'Accept-Language': 'en'
        })
    
    def package_search(self, query: str = "*:*", rows: int = 10, 
                      start: int = 0, **kwargs) -> Dict:
        """
        Search for datasets
        
        Args:
            query: Search query (default "*:*" for all)
            rows: Number of results to return
            start: Offset for pagination
            **kwargs: Additional CKAN search parameters
                     (e.g., fq for filter queries, sort)
        
        Returns:
            Dictionary containing search results
        """
        url = urljoin(self.BASE_URL, "package_search")
        params = {
            'q': query,
            'rows': rows,
            'start': start,
            **kwargs
        }
        
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def package_show(self, package_id: str) -> Dict:
        """
        Get details about a specific dataset
        
        Args:
            package_id: Dataset ID or name
            
        Returns:
            Dictionary containing dataset metadata
        """
        url = urljoin(self.BASE_URL, "package_show")
        params = {'id': package_id}
        
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def resource_show(self, resource_id: str) -> Dict:
        """
        Get details about a specific resource
        
        Args:
            resource_id: Resource ID
            
        Returns:
            Dictionary containing resource metadata
        """
        url = urljoin(self.BASE_URL, "resource_show")
        params = {'id': resource_id}
        
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def organization_list(self, all_fields: bool = False) -> Dict:
        """
        List all organizations
        
        Args:
            all_fields: If True, return full organization details
            
        Returns:
            Dictionary containing organization list
        """
        url = urljoin(self.BASE_URL, "organization_list")
        params = {'all_fields': all_fields}
        
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def tag_list(self, all_fields: bool = False) -> Dict:
        """
        List all tags
        
        Args:
            all_fields: If True, return full tag details
            
        Returns:
            Dictionary containing tag list
        """
        url = urljoin(self.BASE_URL, "tag_list")
        params = {'all_fields': all_fields}
        
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def download_resource(self, resource_url: str, 
                         output_path: str) -> None:
        """
        Download a resource file
        
        Args:
            resource_url: Direct URL to the resource
            output_path: Local path to save the file
        """
        response = self.session.get(resource_url, stream=True)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)