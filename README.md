# CanadaOpenAPI

Python client and utilities for querying and analyzing data from the Government of Canada's Open API.

## Quick Start (Codespaces)

1. Open this repo in GitHub Codespaces
2. Wait for dependencies to install automatically
3. Run the example:
```bash
   python examples/basic_usage.py
```

## Local Setup
```bash
git clone https://github.com/KatKeilty/CanadaOpenAPI.git
cd CanadaOpenAPI
pip install -r requirements.txt
```

## Usage
```python
from src.api_client import OpenCanadaAPI

# Initialize client
api = OpenCanadaAPI()

# Search for datasets
results = api.package_search(query="climate", rows=10)

# Get dataset details
dataset = api.package_show("dataset-id")

# List organizations
orgs = api.organization_list(all_fields=True)
```

## Project Structure
CanadaOpenAPI/
├── src/                    # Source code
│   ├── api_client.py      # API client
│   └── utils.py           # Utility functions
├── examples/              # Example scripts
│   └── basic_usage.py     # Basic usage examples
├── notebooks/             # Jupyter notebooks
├── data/                  # Data files (gitignored)
├── tests/                 # Unit tests
└── docs/                  # Documentation

## API Documentation

- Base URL: https://open.canada.ca/data/api/3/action/
- Official Docs: https://open.canada.ca/en/access-our-application-programming-interface-api
- CKAN API Docs: https://docs.ckan.org/en/latest/api/

## Common Endpoints

- `package_search` - Search for datasets
- `package_show` - Get dataset details
- `resource_show` - Get resource details
- `organization_list` - List organizations
- `tag_list` - List tags

## Examples

### Search with filters:
```python
# Search for datasets from Statistics Canada
results = api.package_search(
    query="*:*",
    fq="organization:statcan",
    rows=20
)
```

### Download a resource:
```python
resource_url = "https://open.canada.ca/data/dataset/.../resource.csv"
api.download_resource(resource_url, "data/downloaded_data.csv")
```

## License

Data accessed through this API is licensed under the Open Government Licence - Canada

