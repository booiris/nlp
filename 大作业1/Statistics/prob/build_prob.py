import re

one_word_prob = {
    'B': 0,
    'M': 0,
    'E': 0,
    'S': 0
}
begin_prob = {
    'B': 0,
    'M': 0,
    'E': 0,
    'S': 0
}
trans_prob = {
    'B': {'B': 0, 'M': 0, 'E': 0, 'S': 0},
    'M': {'B': 0, 'M': 0, 'E': 0, 'S': 0},
    'E': {'B': 0, 'M': 0, 'E': 0, 'S': 0},
    'S': {'B': 0, 'M': 0, 'E': 0, 'S': 0}
}
emit_prob = {
    'B': {},
    'M': {},
    'E': {},
    'S': {}
}

pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）|——|《|》|：|\n|\r|．|”|“|『|』|[１-９]'
with open("train_dict.txt", "r", encoding='utf-8') as f:
    father = '#'
    for line in f:
        line = line.split()
        for i in line:
            if i == '，' or i == '。' or i == '！' or i == '？':  # 标点符号分句
                father = '#'
                continue

            temp_str = re.split(pattern, i)  # 处理标点和文本中和中文在一起的奇怪的符号
            temp = list(filter(None, temp_str))
            if not temp:
                continue
            now_str = temp[0]
            if len(now_str) == 1:
                if father == '#':
                    begin_prob['S'] += 1
                one_word_prob['S'] += 1
                if now_str not in emit_prob['S']:
                    emit_prob['S'][now_str] = 0
                emit_prob['S'][now_str] += 1
            else:
                for char in now_str:
                    pass
