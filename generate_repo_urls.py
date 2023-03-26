
import requests from bs4 import BeautifulSoup BASE_URL = "https://github.com/webduhsign/" def generate_repo_urls(): page = requests.get(BASE_URL + "?tab=repositories") soup = BeautifulSoup(page.content, "html.parser") repo_links = soup.find_all("a", itemprop="name codeRepository") repo_urls = [link["href"] + ".git" for link in repo_links] with open("repositories.txt", "w") as f: f.write("\n".join(repo_urls))
