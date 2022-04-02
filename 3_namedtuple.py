"""
typing.NamedTuple increases memory usage efficiency up to 70% in total and takes only 4.2 MB,
allows indicating expected data types. Best combination is AltDict(NamedTuple) and Tuple.
"""

import random
from typing import NamedTuple, Tuple

from pympler import asizeof


def humanize_bytes(num, suffix='B'):
    """Formats bytes size into humanized code"""
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class RecordNamedTuple(NamedTuple):
    commodity_id: int
    quantity: int
    import_rate: int
    VAT_rate: int
    import_duty_paid: int
    VAT_paid: int


class AltDict(NamedTuple):
    import_country: str
    export_country: str
    goods_profile: Tuple


data_dicts = []
for i in range(1000):
    data_dicts.append(AltDict(
        import_country='ITALY',
        export_country='CHINA',
        goods_profile=(
            RecordNamedTuple(
                commodity_id=random.randint(10000, 99000),
                quantity=random.randint(1, 2500),
                import_rate=random.randint(0, 25),
                VAT_rate=random.randint(0, 25),
                import_duty_paid=random.randint(0, 25),
                VAT_paid=random.randint(0, 25),
            ) for n in range(3)
        ))
    )

print(f'The most efficient way of combination List[NamedTuple] and Tuple takes: '
      f'{humanize_bytes(asizeof.asizeof(data_dicts))}')
