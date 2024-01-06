from bs4 import BeautifulSoup


def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator='\n', strip=True)



# Example usage
html_content = "<html><body><p>This is an <b>email</b> message.</p></body></html>"
plain_text = extract_text_from_html(html_content)
print(plain_text)
