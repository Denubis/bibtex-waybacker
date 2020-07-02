#!/usr/bin/env python3
# GPL v3. Brian Ballsun-Stanton.
# It really should be the CRAPL license.
# This is such a hack. I am so so so sorry. But this needs to be given to the department tomorrow morning sooooo....

import fileinput
#https://stackoverflow.com/a/290494

import get_wayback_machine
import time
import re
from tqdm import tqdm
import requests

# import bibtexparser

# with open('bibliography.bib') as bibtex_file:
#     bib_database = bibtexparser.load(bibtex_file)

# print(bib_database.entries)

# response = get_wayback_machine.get('https://en.wikipedia.org')
# if response:
#     print(response.status_code)

#with open("bibliography.bib") as bibtex_file:

BIBFILE = "bibliography.bib"
lines = 0
with open(BIBFILE) as f:
    for i, l in enumerate(f):
        pass
    lines = i+1

for line in tqdm(fileinput.input(BIBFILE, inplace=True), total=lines):
#for line in tqdm(fileinput.input(BIBFILE), total=lines):
    if "url" in line and "web.archive.org" not in line and "doi" not in line:
        #print(line)
        try:
            url = re.search(r'(http[^"}]*)["}]', line).group(1)
            #tqdm.write("https://web.archive.org/save/{}".format(url))
            r = requests.get("https://web.archive.org/save/{}".format(url))
            print(re.sub(r'http','https://web.archive.org/web/http', line))
            # response = get_wayback_machine.get(url)
            # if response.status_code == 200:
            #     print(re.sub(r'http','http://web.archive.org/web/http', line))
            # else:
            #     r = requests.get(re.sub(r'http','http://web.archive.org/save/http', url))
            #     print(re.sub(r'http','http://web.archive.org/web/http', line))
        except Exception as e:
            print("%", e)
            print(line)
        time.sleep(1)

    else:
        #pass
        print(line, end="")