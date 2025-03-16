import json
import urllib.request, urllib.parse, urllib.error

url = 'https://py4e-data.dr-chuck.net/comments_2194953.json'
print('Retrieving', url)

try:
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    js = json.loads(data)
    
    # Extract comments and calculate sum
    comments = js['comments']
    count = len(comments)
    total = sum(comment['count'] for comment in comments)
    
    print('Count:', count)
    print('Sum:', total)
    
except urllib.error.URLError as e:
    print('Error: Failed to retrieve URL -', str(e))
except json.JSONDecodeError as e:
    print('Error: Invalid JSON data -', str(e))
except KeyError as e:
    print('Error: Missing required field in JSON -', str(e))
except Exception as e:
    print('Error:', str(e))



答案：2732
