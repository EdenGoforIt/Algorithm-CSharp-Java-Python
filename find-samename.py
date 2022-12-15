from typing import List
from collections import Counter


def find_same_name(names: List[str]) -> List[str]:
    name_count = Counter(names)
    result = set()

    for name in names:
        if name_count[name] > 1:
            result.add(name)

    return result


print(find_same_name(["Tom", "Jerry", "Mike", "Tom"]))
