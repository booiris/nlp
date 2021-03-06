import math
import pickle

maxnum = 4e5 # 词的总数位无法统计，取新华字典中出现的词的近似值
s = set()
# 第一遍遍历获取训练集中有多少个词性，便于构建概率矩阵
with open("../../File/train_prob.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.split()
        for word in line:
            word_list = word.split("/")
            temp_str = word_list[0]
            now_str = ""
            for char in temp_str:
                if '\u4e00' <= char <= '\u9fa5':
                    now_str += char
            if now_str:
                s.add(word_list[1])

begin_prob = {key: 0 for key in s}
trans_prob = {key1: {key2: 0 for key2 in s} for key1 in s}
emit_prob = {key: {} for key in s}

# 第二遍遍历，训练参数，获取概率矩阵
with open("../../File/train_prob.txt", "r", encoding='utf-8') as f:
    for line in f:
        father = '#'
        line = line.split()
        for word in line:
            word_list = word.split("/")
            temp_str = word_list[0]
            now_str = ""
            for char in temp_str:
                if '\u4e00' <= char <= '\u9fa5':
                    now_str += char
            if now_str:
                now_state = word_list[1]
                if father == '#':
                    begin_prob[now_state] += 1
                else:
                    trans_prob[father][now_state] += 1
                father = now_state

                if now_str not in emit_prob[now_state]:
                    emit_prob[now_state][now_str] = 0
                emit_prob[now_state][now_str] += 1

# 计算初始概率矩阵
temp_sum = 0
for key in begin_prob:
    temp_sum += begin_prob[key]
for key in begin_prob:
    begin_prob[key] /= temp_sum
    if begin_prob[key] != 0:
        begin_prob[key] = math.log(begin_prob[key])
    else:
        begin_prob[key] = -3.14 * 1e+100

# 计算转移概率矩阵
for i in trans_prob:
    temp_sum = 0
    for j in trans_prob[i]:
        temp_sum += trans_prob[i][j]
    for j in trans_prob[i]:
        trans_prob[i][j] /= temp_sum
        if trans_prob[i][j] != 0:
            trans_prob[i][j] = math.log(trans_prob[i][j])
        else:
            trans_prob[i][j] = -3.14 * 1e+100

# 计算发射概率矩阵
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
