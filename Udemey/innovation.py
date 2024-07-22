import requests
from bs4 import BeautifulSoup

# URL of the documentation page you want to scrape
url = 'https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Security-Guide-v6_7:Nutanix-Security-Guide-v6_7'

# Fetch the page
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Assuming documentation is within article tags (adjust selector as needed)
documentation_content = soup.find('body')

# Optional: Clean up the content, removing script and style tags
for script_or_style in documentation_content(['script', 'style']):
    script_or_style.decompose()

# Get the cleaned HTML as a string
clean_html = str(documentation_content)

# Process or save the clean_html as needed
print(clean_html)