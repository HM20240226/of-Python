import json
import urllib.request, urllib.parse, urllib.error

location = input("Enter location: ")
base_url = "http://py4e-data.dr-chuck.net/opengeo?"
params = {'q': location}
url = base_url + urllib.parse.urlencode(params)

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

try:
    js = json.loads(data)
    # 打印完整的JSON结构以便调试
    print(json.dumps(js, indent=2))
    # 检查JSON结构并获取plus_code
    if "results" in js and len(js["results"]) > 0:
        plus_code = js["results"][0].get("plus_code", "")
        if plus_code:
            print("Plus code", plus_code)
        else:
            print("Plus code not found")
    else:
        print("No results found")
except Exception as e:
    print("Error:", str(e))



答案  "plus_code": "87JC9V2W+5P",
