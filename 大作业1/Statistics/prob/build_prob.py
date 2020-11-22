import math
import pickle

begin_prob = {
    'B': 0.0,
    'M': 0.0,
    'E': 0.0,
    'S': 0.0
}
trans_prob = {
    'B': {'B': 0.0, 'M': 0.0, 'E': 0.0, 'S': 0.0},
    'M': {'B': 0.0, 'M': 0.0, 'E': 0.0, 'S': 0.0},
    'E': {'B': 0.0, 'M': 0.0, 'E': 0.0, 'S': 0.0},
    'S': {'B': 0.0, 'M': 0.0, 'E': 0.0, 'S': 0.0}
}
emit_prob = {
    'B': {},
    'M': {},
    'E': {},
    'S': {}
}
one_word_prob = {
    'B': 0.0,
    'M': 0.0,
    'E': 0.0,
    'S': 0.0
}
maxnum = 21003  # gbk编码最大汉字个数

with open("train_dict.txt", "r", encoding='utf-8') as f:
    for line in f:
        father = '#'
        line = line.split()
        for word in line:
            now_str = ""
            for char in word:
                if '\u4e00' <= char <= '\u9fa5':
                    now_str += char
            if now_str:
                if len(now_str) == 1:
                    if now_str not in emit_prob['S']:
                        emit_prob['S'][now_str] = 0
                    emit_prob['S'][now_str] += 1
                    if father == '#':
                        begin_prob['S'] += 1
                    else:
                        trans_prob[father]['S'] += 1
                    father = 'S'
                    one_word_prob['S'] += 1
                else:
                    for j in range(len(now_str)):
                        char = now_str[j]
                        if j == 0:
                            now_state = 'B'
                        elif j == len(now_str) - 1:
                            now_state = 'E'
                        else:
                            now_state = 'M'

                        if father == '#':
                            begin_prob[now_state] += 1
                        else:
                            trans_prob[father][now_state] += 1
                        father = now_state

                        if char not in emit_prob[now_state]:
                            emit_prob[now_state][char] = 0
                        emit_prob[now_state][char] += 1
                        one_word_prob[now_state] += 1

temp_sum = 0
temp_sum1 = 0
for key in begin_prob:
    temp_sum += begin_prob[key]
    temp_sum1 += one_word_prob[key]
for key in begin_prob:
    begin_prob[key] /= temp_sum
    one_word_prob[key] /= temp_sum1
    if begin_prob[key] != 0:
        begin_prob[key] = math.log(begin_prob[key])
    else:
        begin_prob[key] = -3.14 * 1e+100
    if one_word_prob[key] != 0:
        one_word_prob[key] = math.log(one_word_prob[key])
    else:
        one_word_prob[key] = -3.14 * 1e+100

temp_sum = 0
for i in trans_prob:
    for j in trans_prob[i]:
        temp_sum += trans_prob[i][j]
for i in trans_prob:
    for j in trans_prob[i]:
        trans_prob[i][j] /= temp_sum
        if trans_prob[i][j] != 0:
            trans_prob[i][j] = math.log(trans_prob[i][j])
        else:
            trans_prob[i][j] = -3.14 * 1e+100
        trans_prob[i][j] -= one_word_prob[i]
print(trans_prob)
for i in emit_prob:
    temp_sum = maxnum
    for j in emit_prob[i]:
        temp_sum += emit_prob[i][j]
    emit_prob[i][False] = 0
    for j in emit_prob[i]:
        emit_prob[i][j] += 1
        emit_prob[i][j] /= temp_sum
        emit_prob[i][j] = math.log(emit_prob[i][j])

probs = {
    "begin_prob": begin_prob,
    "trans_prob": trans_prob,
    "emit_prob": emit_prob
}
with open("probs.p", "wb") as f:
    pickle.dump(probs, f)
