import requests
from bs4 import BeautifulSoup


def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to retrieve content from {url}")
        return None


def extract_article_data(html_content):
    if html_content is not None:
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extracting the title
        title = soup.find('h1', class_='title').text.strip()

        # Extracting additional information (modify based on the actual structure)
        author = soup.find('div', class_='author').text.strip()
        date = soup.find('div', class_='date').text.strip()
        content = soup.find('div', class_='content').text.strip()

        return {'title': title, 'author': author, 'date': date, 'content': content}
    else:
        return None


def main():
    url = 'https://metbuat.az/news/1484577/ilham-eliyevin-receb-tayyib-erdogan-ile-gorusu-olub.html'

    html_content = get_html_content(url)

    article_data = extract_article_data(html_content)

    if article_data:
        print("Title:", article_data['title'])
        print("Author:", article_data['author'])
        print("Date:", article_data['date'])
        # Print only the first 200 characters of content
        print("Content:", article_data['content'][:200])
    else:
        print("No data extracted.")

if __name__ == "__main__":
    main()

