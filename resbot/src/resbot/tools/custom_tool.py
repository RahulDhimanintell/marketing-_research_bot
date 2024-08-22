from crewai_tools import BaseTool
import json
import os
import requests
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()


class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."



class SearchTools:
    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet 
        about a given topic and return relevant results"""
        top_result_to_return = 10
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json().get('organic', [])
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(string)

    @tool("Search news on the internet")
    def search_news(query):
        """Useful to search news about a company, stock or any other
        topic and return relevant results"""
        top_result_to_return = 10
        url = "https://google.serper.dev/news"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json().get('news', [])
        string = []
        for result in results[:top_result_to_return]:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(string)
