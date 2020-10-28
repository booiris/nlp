import numpy as np
import pickle
from collections import defaultdict

f = open("varname.txt", "rb")
varname = pickle.load(f)
dic = varname["dic"]
transmat = varname["transmat"]
word_list = varname["word_list"]
speech_list = varname["speech_list"]

ini = "多/年/来/最/重要/承诺"
string = ini.split("/")
for i in string:
    print(word_list[i])
print("")

dp = np.zeros((len(string), len(dic)))
for key in word_list[string[0]]:
    dp[0, dic[key]] = 1

path = defaultdict(list)
for i in dic:
    path[i].append(i)

for i in range(1, len(string)):
    states = []
    for j in word_list[string[i]]:
        if j in dic.keys():
            states.append(j)

    for j in states:

        max_prob = 0
        for k in dic:
            now_prob = dp[i - 1, dic[k]] * (transmat[dic[k], dic[j]] / speech_list[k]) * (
                        word_list[string[i]][j] / speech_list[j])
            if now_prob > max_prob:
                max_prob = now_prob
                max_state = k

        dp[i, dic[j]] = max_prob
        newpath = []
        for state in path[max_state]:
            newpath.append(state)
        newpath.append(j)
        path[j]=newpath


prob = 0
res = None
for state in dic:
    if dp[len(string) - 1, dic[state]] > prob:
        prob = dp[len(string) - 1, dic[state]]
        res = state

print(path[res])
