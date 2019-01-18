/*
* Extract the titles found under a search term for an specific webpage.
* In this case, titles found under the artificial intelligence search term,
* in the ted page.
*/

#!/usr/bin/env python3.6

import urllib.request

term = "artificial intelligence"
page_number = 1
per_page = 20

u = urllib.request.urlopen('https://www.ted.com/search?page={}&per_page={}&q={}'.format(page_number, per_page, term.replace(" ", "+")))
data = u.read()

from lxml import html
doc = html.document_fromstring(data)

for title in doc.cssselect("article.seach_result h3 a"):
    print(title.text_content())
