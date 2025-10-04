import os
from urllib.request import urlopen

# api_key = os.environ["NPR_API_KEY"]

for id_, filename in [(3, 'npr_morning_edition.xml'), (2, 'npr_all_things_considered.xml')]:
    # url = f"https://api.npr.org/query?id={id_}&output=podcast&apiKey={api_key}"
    url = f"https://feeds.npr.org/{id_}/rss.xml"
    with urlopen(url) as response:
        content = response.read()  # Download as bytes
    with open(filename, "wb") as file:
        file.write(content)
