import json
import os

import requests
from langchain.tools import tool


class SearchTools():

  @tool("Search internet")
  def search_internet(query):
    """Useful to search the internet about a given topic and return relevant
    results."""
    return SearchTools.search(query)

  @tool("Search LinkedIn")
  def search_linkedin(query):
    """Useful to search for LinkedIn posts and professional content about a given topic and return relevant
    results."""
    query = f"site:linkedin.com {query}"
    return SearchTools.search(query)

  @tool("Search Twitter")
  def search_twitter(query):
    """Useful to search for Twitter/X posts about a given topic and return relevant
    results."""
    query = f"site:twitter.com OR site:x.com {query}"
    return SearchTools.search(query)

  def search(query, n_results=5):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    string = []
    for result in results[:n_results]:
      try:
        string.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    content = '\n'.join(string)
    return f"\nSearch result: {content}\n"

