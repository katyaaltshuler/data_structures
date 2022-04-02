"""
The most simple and least effective way (in terms of RAM) of storing complex/nested data structures:
using List and Dict without specifying any expected data type in current example takes 15.2 MB

Imagine we have some data that tends to become big-scale
(records of imported goods and customs duties paid in logistic company)
"""

import random

from pympler import asizeof


def humanize_bytes(num, suffix='B'):
    """Formats bytes size into humanized code"""
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


data_dicts = []
for i in range(10000):
    data_dicts.append({
        'import_country': 'ITALY',
        'export_country': 'CHINA',
        'goods_profile': [{
                'commodity_id': random.randint(10000, 99000),
                'quantity': random.randint(1, 2500),
                'import_rate': random.randint(0, 25),
                'VAT_rate': random.randint(0, 22),
                'import_duty_paid': random.randint(0, 25),
                'VAT_paid': random.randint(0, 25)
                } for n in range(3)]
    })

print(f'The simpliest way of storying data with List[Dict] takes: '
      f'{humanize_bytes(asizeof.asizeof(data_dicts))}')
