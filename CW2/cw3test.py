import ssl
import urllib.request
from ucimlrepo import fetch_ucirepo
ssl._create_default_https_context = ssl._create_unverified_context

# fetch dataset
congressional_voting_records = fetch_ucirepo(id=105)
# Create an unverified SSL context
# data (as pandas dataframes)
X = congressional_voting_records.data.features
y = congressional_voting_records.data.targets

# metadata
print(congressional_voting_records.metadata)

# variable information
print(congressional_voting_records.variables)
