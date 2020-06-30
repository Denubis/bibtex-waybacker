#!/usr/bin/env python3
# GPL v3. Brian Ballsun-Stanton.
# It really should be the CRAPL license.
# This is such a hack. I am so so so sorry. But this needs to be given to the department tomorrow morning sooooo....

import fileinput
#https://stackoverflow.com/a/290494

import get_wayback_machine
import time
import re


# import bibtexparser

# with open('bibliography.bib') as bibtex_file:
#     bib_database = bibtexparser.load(bibtex_file)

# print(bib_database.entries)

# response = get_wayback_machine.get('https://en.wikipedia.org')
# if response:
#     print(response.status_code)

#with open("bibliography.bib") as bibtex_file:
for line in fileinput.input("bibliography.bib", inplace=True):
    if "\\url" in line:
        response = get_wayback_machine.get('https://en.wikipedia.org')
        if response.status_code == 200:
            print(re.sub(r'http','http://web.archive.org/web/http', line))
        else:
            r = requests.get(re.sub(r'http','http://web.archive.org/save/http', line))
            print(re.sub(r'http','http://web.archive.org/web/http', line))
        time.sleep(5)

    else:        
        print(line, end="")