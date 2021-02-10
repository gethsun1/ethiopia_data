from requests_html import HTML

with open('EMML228.xml') as html_file:
    source = html_file.read()
    html = HTML(html=source)


match = html.find('title', first=True)
print(match.html)