import pickle


def build_trie():
    # 将下载的字典保存为trie树

    dic = {}
    now = dic
    with open("Dict/dict.txt", "r", encoding='utf-8') as f:
        for line in f:
            word = line.split()
            now = dic
            for char in word[0]:
                if char not in now:
                    now[char] = {}
                now = now[char]
            now[True] = int(word[1])

    with open("Dict/dict.p", "wb") as f:
        pickle.dump(dic, f)


def dijkstra(p, add_value):
    dis = [0x3f3f3f3f for _ in range(len(p))]
    vis = [False for _ in range(len(p))]
    father = [-1 for _ in range(len(p))]
    cost = [0 for _ in range(len(p))]

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
            if now == j[0]:
                v = 0
            else:
                v = 1
            if dis[j[0]] > dis[now] + v:
                dis[j[0]] = dis[now] + v
                cost[j[0]] = cost[now] + j[1]
                father[j[0]] = now

            if add_value and dis[j[0]] == dis[now] + v and cost[j[0]] < cost[now] + j[1]:
                cost[j[0]] = cost[now] + j[1]
                father[j[0]] = now

    path = []
    now = len(p) - 1
    while now != -1:
        path.append(now)
        now = father[now]
    path.reverse()

    return path


def d_ptcp(test_str, dic, add_value=False):
    # 采用最短路匹配实现字典分词
    res = ""
    word = ""
    if test_str[len(test_str) - 1] != '\n':
        test_str += '\n'
    for char in test_str:
        if '\u4e00' <= char <= '\u9fa5':
            word += char
        else:
            if word != "":
                p = [[] for _ in range(len(word) + 1)]
                for i in range(len(word)):
                    j = i
                    node = [j + 1, 0]
                    p[i].append(node)
                    if word[j] not in dic:
                        continue
                    now = dic[word[j]]
                    while j < len(word):
                        if True in now:
                            node = [j + 1, now[True]]
                            p[i].append(node)
                        j += 1
                        if j == len(word) or word[j] not in now:
                            break
                        now = now[word[j]]

                path = dijkstra(p, add_value)
                for i in range(len(path) - 1):
                    s = path[i]
                    e = path[i + 1]
                    for j in range(s, e):
                        res += word[j]
                    res += ' '
            if char != '\n':
                res += char + ' '
            word = ""

    return res + '\n'


# build_trie()

# with open("Dict/dict.p", "rb") as f:
#     dic = pickle.load(f)

# with open("../File/test_data.txt", "r", encoding='utf-8') as f:
#     f1 = open("Dictionary_out.txt", "w+", encoding='utf-8')
#     for line in f:
#         f1.writelines(d_ptcp(line, dic, True))
#     f1.close()

# print(d_ptcp("编辑代码一般是用插入模式",dic,True))
