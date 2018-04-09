from sys import argv

input_path = argv[1]
output_path = argv[2]

labels = {
          'javascript': 1,
          'java': 2,
          'python': 3,
          'ruby': 4,
          'php': 5,
          'c++': 6,
          'c#': 7,
          'go': 8,
          'scala': 9,
          'swift': 10
         }


def to_vw_format(document, label):
    return label + ' |text ' + document.replace(':', '').replace('|', '') + '\n'


def get_tag(tags_str):
    search_tags = set(labels.keys()).intersection(tags_str.split())
    if len(search_tags) != 1: return None
    return labels[search_tags.pop()]


with open(input_path, encoding='utf-8') as infile, \
        open(output_path, 'w', encoding='utf-8') as outfile:

    for line in infile:

        if line.count('\t') != 1: continue
        splited_line = line.split("\t")
        text, tags = splited_line

        tag_index = get_tag(tags)
        if not get_tag(tags): continue

        outfile.write(to_vw_format(text, tag_index))