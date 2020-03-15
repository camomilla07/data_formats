import json
import xml.etree.ElementTree as ET

with open("newsafr.json", encoding='utf-8') as f:
    w_file = json.load(f)
items = w_file["rss"]["channel"]["items"]
description_l = []
for news in items:
    description = news["description"]
    description_l.append(description)


tree = ET.parse("newsafr.xml")
root = tree.getroot()
descriptions = root.findall("channel/item/description")
description_list = []
for description in descriptions:
    description_list.append(description.text)


def ranking(words_l):
    string_join = " ".join(words_l)
    words = string_join.split(" ")

    words_list = []

    for word in words:
        word = word.lower()
        if len(word) > 6:
            words_list.append(word)

    def get_count(s):
        x = words_list.count(s)
        return x

    sorted_list = (sorted(words_list, key=get_count, reverse=True))
    unique_list = []
    for word in sorted_list:
        if word not in unique_list:
            unique_list.append(word)
    return unique_list[0:10]


print(f'топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для json:\n{ranking(description_l)}')

print(f'топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для xml:\n{ranking(description_list)}')
