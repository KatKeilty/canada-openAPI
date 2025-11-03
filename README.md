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
```
CanadaOpenAPI/
├── .devcontainer/
│   └── devcontainer.json          # Codespaces config (keep as is)
├── data/                           # Your data files
├── docker/                         # ALL Docker configs in one place
│   ├── jupyter/
│   │   └── Dockerfile             # Jupyter-specific Dockerfile
│   └── superset/
|       ├── superset_config.py     # Superset python config
│       ├── docker-compose.yml     # Superset docker-compose
│       └── .env                   # Superset environment vars
├── examples/
│   └── basic_usage.py
├── notebooks/
│   └── *.ipynb
├── src/
│   ├── __init__.py
│   ├── api_client.py
│   └── utils.py
├── tests/
├── .gitignore
├── docker-compose.yml             # Main docker-compose (for Jupyter)
├── requirements.txt               # Python dependencies
└── README.md
```

## API Documentation

- Base URL: https://open.canada.ca/en/working-data-api/api
- Official Docs: https://open.canada.ca/en/open-government-licence-canada
- CKAN API Docs: https://docs.ckan.org/en/2.8/api/

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

# Data accessed through this API is licensed under the Open Government Licence - Canada

## Open Government Licence - Canada

You are encouraged to use the Information that is available under this licence with only a few conditions.

# Using Information under this licence

    Use of any Information indicates your acceptance of the terms below.
    The Information Provider grants you a worldwide, royalty-free, perpetual, non-exclusive licence to use the Information, including for commercial purposes, subject to the terms below.

# You are free to:

    Copy, modify, publish, translate, adapt, distribute or otherwise use the Information in any medium, mode or format for any lawful purpose.

# You must, where you do any of the above:

    Acknowledge the source of the Information by including any attribution statement specified by the Information Provider(s) and, where possible, provide a link to this licence.
    If the Information Provider does not provide a specific attribution statement, or if you are using Information from several information providers and multiple attributions are not practical for your product or application, you must use the following attribution statement:

# Contains information licensed under the Open Government Licence – Canada.

The terms of this licence are important, and if you fail to comply with any of them, the rights granted to you under this licence, or any similar licence granted by the Information Provider, will end automatically.

