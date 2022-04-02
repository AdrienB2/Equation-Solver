import requests

input = input("Input: ")
input.replace(" ", "")
input.replace("+", "%2B")
input.replace("=", "%3D")
url = "http://api.wolframalpha.com/v2/query?appid=JKH45G-G722WWV59H&format=plaintext&output=json&includepodid=Result&input=solve " + input
r = requests.get(url).json()

data = r["queryresult"]["pods"][0]["subpods"][0]
plaintext = data["plaintext"]

print(plaintext)