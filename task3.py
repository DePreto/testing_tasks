import os
import re


def has_valid_elems(item: str) -> bool:
    pattern = "^[A-Za-z0-9]*$"
    return bool(re.match(pattern, item))


def biggestPath(X: dict) -> str:
    result = ""
    for key, value in X.items():
        if len(set(value)) != len(value) or not has_valid_elems(key):
            continue
        crt_path = key
        if isinstance(value, dict):
            path = biggestPath(value).strip(os.path.sep)
            crt_path = os.path.join(crt_path, path)
        if isinstance(value, list):
            for file in value:
                if has_valid_elems(file):
                    crt_path = os.path.join(crt_path, file)
                    break
        if len(result.split(os.path.sep)) < len(crt_path.split(os.path.sep)) <= 255:
            result = crt_path
    return os.path.join(os.path.sep, result)
    

d1 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}

d2 = {'dir1': ['file1', 'file1']}

d3 = {'dir1': ['file1', 'file2', 'file3']} #TODO в ТЗ указано, что в в одной папке не могут находится директории/файлы с одинаковыми именами, однако последний пример содержит файлы с одинаковыми именами, в связи с чем исходные данные для 3 задачи были изменены

print(biggestPath(d1))
print(biggestPath(d2))
print(biggestPath(d3))
