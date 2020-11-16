import pickle
import re


def build_trie():
    # 将下载的字典保存为trie树

    dic = {}
    now = dic
    with open("dict.txt", "r", encoding='utf-8') as f:
        for line in f:
            word = line.split()
            now = dic
            for char in word[0]:
                if char not in now:
                    now[char] = {}
                now = now[char]
            now[True] = True

    with open("dict.p", "wb") as f:
        pickle.dump(dic, f)


def dijkstra(p):
    dis = [0x3f3f3f3f for _ in range(len(p))]
    vis = [False for _ in range(len(p))]
    father = [-1 for _ in range(len(p))]

    dis[0] = 0
    for i in range(len(p)):
        now = -1
        maxd = 0x3f3f3f3f
        for j in range(len(p)):
            if vis[j] is False and dis[j] < maxd:
                maxd = dis[j]
                now = j
        if now == -1:
            break
        vis[now] = True
        for j in p[now]:
            if now == j:
                v = 0
            else:
                v = 1
            if dis[j] > dis[now] + v:
                dis[j] = dis[now] + v
                father[j] = now

    path = []
    now = len(p) - 1
    while now != -1:
        path.append(now)
        now = father[now]
    path.reverse()

    return path


def d_ptcp(test_str, dic):
    # 采用最短路匹配实现字典分词

    pattern = r'(,|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）|—|\d+|《|》|：)'
    test_str = re.split(pattern, test_str)

    res = ""
    for word in test_str:
        if word == '':
            continue
        temp = re.split(pattern, word)
        if len(temp) != 1 or word.isdigit():
            res += word + ' '
            continue
        p = [[] for _ in range(len(word) + 1)]
        for i in range(len(word)):
            j = i
            if word[j] not in dic:
                p[i].append(j + 1)
                continue
            now = dic[word[j]]
            while j < len(word):
                if True in now:
                    p[i].append(j + 1)
                j += 1
                if j == len(word) or word[j] not in now:
                    break
                now = now[word[j]]

        path = dijkstra(p)
        for i in range(len(path) - 1):
            s = path[i]
            e = path[i + 1]
            for j in range(s, e):
                res += word[j]
            res += ' '

    return res


# build_trie()
with open("dict.p", "rb") as f:
    dic = pickle.load(f)

out = ""
with open("train_data.txt", "r") as f:
    cnt = 0
    res = ""
    for line in f:
        line = line.strip('\n')
        res = d_ptcp(line, dic)
        if cnt < 10:
            print(line)
            print(res)
            print("")
        cnt += 1
        out += res + '\n'

with open("out_data.txt", "w") as f:
    f.writelines(out)
