import http.client

conn = http.client.HTTPSConnection("realty-in-us.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'X-RapidAPI-Host': "realty-in-us.p.rapidapi.com"
}

conn.request("GET", "/locations/v2/auto-complete?input=new%20york&limit=10", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))