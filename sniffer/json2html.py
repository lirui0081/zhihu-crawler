# -*- coding:utf-8 -*-
import json
import codecs

with open('output/search2.json', 'r') as f:
    data = json.load(f)

with codecs.open('output/search2.html', 'w', 'utf8') as f:
    f.write('\n'.join(data['htmls']))
