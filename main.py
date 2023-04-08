import subprocess

api_key = 'YOUR-API-KEY'
search_query = 'YOUR-SEARCH-QUERY' 

print("Running scan_sentiment.py...")
subprocess.call(["python", "scan_sentiment.py", api_key, search_query])

print("Running sentiment_analysis.py...")
subprocess.call(["python", "sentiment_analysis.py"])