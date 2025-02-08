import os
from langchain_community.tools.tavily_search import TavilySearchResults

# Load environment variables (if using a .env file)
from dotenv import load_dotenv
load_dotenv()

# Retrieve the Tavily API key from the environment
tavily_api_key = os.getenv("TAVILY_API_KEY")
if not tavily_api_key:
    raise ValueError("Tavily API key not found. Please set the TAVILY_API_KEY environment variable.")

# Initialize the TavilySearchResults tool
search = TavilySearchResults(max_results=3, tavily_api_key=tavily_api_key)

# Define a test query
query = "What is the capital of India?"

# Perform the search
search_results = search.invoke(query)

# Display the results
print("Search Results:")
for i, result in enumerate(search_results, start=1):
    print(f"\nResult {i}:")
    print(f"URL: {result['url']}")
    print(f"Content: {result['content']}")