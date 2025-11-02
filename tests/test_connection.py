from src.api_client import OpenCanadaAPI

api = OpenCanadaAPI()
result = api.package_search(query="climate", rows=1)
print(f"✓ Connection successful! Found {result['result']['count']} datasets")