from apiclient import discovery

API_KEY = 'AIzaSyAkDA0SPfM3Tq5tPqxWBSb4_HjCGkJV0v0'
items = GPLUS.activities().search(query='python').execute().get('items', [])

for data in items:
    post = ' '.join(data['title'].strip().split())
    if post:
        print(TMPL % (data['actor']['displayName'],
            data['published'], post))

