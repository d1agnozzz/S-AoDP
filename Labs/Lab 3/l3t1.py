
from ast import pattern


def prefix_function(string: str) -> list[int]:
    prefix_lenghts = [0] * len(string)

    j = 0
    i = 1
    while i < len(string) and j < len(string):
        if string[i] == string[j]:
            j += 1
            prefix_lenghts[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix_lenghts[j - 1]
            else:
                prefix_lenghts[i] = 0
                i += 1

    return prefix_lenghts


def kmp_find_pattern(_text: str, _pattern: str, case_sensitive = True) -> set[int]:
    # Applying case insensitivity in case 
    if not case_sensitive:
        text = _text.lower()
        pattern = _pattern.lower()
    else: 
        text = _text
        pattern = _pattern

    # Getting prefixes lengths for pattern
    pattern_prefixes = prefix_function(pattern)

    text_prefixes = [0] * len(text)
    occurences_indexes = set()

    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            j += 1
            text_prefixes[i] = j
            if j == len(pattern):
                occurences_indexes.add(i)
            j %= len(pattern)
            i += 1
        else:
            if j != 0:
                j = pattern_prefixes[j - 1]
            else:
                text_prefixes[i] = 0
                i += 1
    print(text_prefixes)
    print(pattern_prefixes)
    return occurences_indexes


def get_offset_table(string: str) -> dict[str:int]:
    offsets = {}
    table = [0] * len(string)

    for i in range(len(string) - 2, -1, -1):
        char = string[i]
        offset = len(string) - i - 1
        if char in offsets.keys():
            table[i] = offsets[char]
        else:
            offsets[char] = offset
            table[i] = offsets[char]
    if string[-1] in offsets.keys():
        table[-1] = offsets[string[-1]]
        return offsets
    else:
        offsets[string[-1]] = len(string)
        table[-1] = len(string)
        return offsets


def boyer_moore(_text: str, _pattern: str, case_sensitive = True) -> set[int]:
    if not case_sensitive:
        text = _text.lower()
        pattern = _pattern.lower()
    else:
        text = _text
        pattern = _pattern

    occurences_indexes = set()
    offset_table = get_offset_table(pattern)

    offset = 0
    index = len(pattern) - 1
    while index + offset < len(text):
        backwards = 0
        while backwards < len(pattern) and text[index + offset - backwards] == pattern[index - backwards]:
            backwards += 1
        if backwards == len(pattern):
            occurences_indexes.add(index+offset)
            offset += len(pattern)
        elif backwards > 0:
            offset += offset_table[pattern[-1]] 

        else:
            if  text[index+offset] in offset_table.keys():
                offset += offset_table[text[index+offset]]

            else:
                offset += len(pattern)
    return occurences_indexes


if __name__ == '__main__':
    text = "банбанбан"
    pattern = "банбан"

    print(kmp_find_pattern(text, pattern))
    print(boyer_moore(text, pattern))

    print(prefix_function(""))
