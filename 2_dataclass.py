"""
Here using of DataClass increases memory usage efficiency up to 25% and takes 10.4 MB,
eases understanding expected data types.
"""

import random
from dataclasses import dataclass

from pympler import asizeof


def humanize_bytes(num, suffix='B'):
    """Formats bytes size into humanized code"""
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


@dataclass
class RecordDataClass:
    commodity_id: int
    quantity: int
    import_rate: int
    VAT_rate: int
    import_duty_paid: int
    VAT_paid: int


data_dataclass = []
for i in range(10000):
    data_dataclass.append({
        'import_country': 'ITALY',
        'export_country': 'CHINA',
        'goods_profile': [
            RecordDataClass(
                commodity_id=random.randint(10000, 99000),
                quantity=random.randint(1, 2500),
                import_rate=random.randint(0, 25),
                VAT_rate=random.randint(0, 25),
                import_duty_paid=random.randint(0, 25),
                VAT_paid=random.randint(0, 25),
             ) for n in range(3)
        ]
    })

print(f'The second way List[Dataclass] now takes: '
      f'{humanize_bytes(asizeof.asizeof(data_dataclass))}')
