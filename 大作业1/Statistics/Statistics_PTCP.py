import pickle


def s_ptcp(test_str, probs):
    begin_prob = probs["begin_prob"]
    trans_prob = probs["trans_prob"]
    emit_prob = probs["emit_prob"]
    if test_str[len(test_str) - 1] != '\n':
        test_str += '\n'

    res = ""
    word = ""
    for char in test_str:
        if '\u4e00' <= char <= '\u9fa5':
            word += char
        else:
            if word:
                print(word)
                dp = [{} for _ in range(len(word))]  # 初始概率矩阵
                dp[0]["B"] = begin_prob["B"] + emit_prob["B"][word[0] if word[0] in emit_prob["B"] else False]
                dp[0]["M"] = begin_prob["M"] + emit_prob["M"][word[0] if word[0] in emit_prob["M"] else False]
                dp[0]["E"] = begin_prob["E"] + emit_prob["E"][word[0] if word[0] in emit_prob["E"] else False]
                dp[0]["S"] = begin_prob["S"] + emit_prob["S"][word[0] if word[0] in emit_prob["S"] else False]
                path = [{"B": [], "M": [], "E": [], "S": []} for _ in range(len(word))]  # 保存状态序列
                for i in begin_prob:
                    path[0][i].append(i)

                for i in range(1, len(word)):
                    for j in begin_prob:
                        max_state = None
                        max_prob = -3.14 * 1e+100
                        for k in begin_prob:
                            if word[i] in emit_prob[j]:
                                now_prob = dp[i - 1][k] + trans_prob[k][j] + emit_prob[j][word[i]]
                            else:
                                now_prob = dp[i - 1][k] + trans_prob[k][j] + emit_prob[j][False]

                            if now_prob > max_prob:
                                max_prob = now_prob
                                max_state = k
                        dp[i][j] = max_prob
                        newpath = []
                        for state in path[i - 1][max_state]:
                            newpath.append(state)
                        newpath.append(j)
                        path[i][j] = newpath

                prob = -3.14 * 1e+100
                for state in ['S', 'E']:
                    if dp[len(word) - 1][state] > prob:
                        prob = dp[len(word) - 1][state]
                        res_state = state
                res_path = path[len(word) - 1][res_state]
                for i in range(len(res_path)):
                    res += word[i]
                    if res_path[i] == 'S' or res_path[i] == 'E':
                        res += ' '

            if char != '\n':
                res += char + ' '
            word = ""

    return res + "\n"


with open("prob/probs.p", "rb") as f:
    probs = pickle.load(f)

with open("../File/test_data.txt", "r", encoding='utf-8') as f:
    f1 = open("Statistics_out.txt", "w+", encoding='utf-8')
    for line in f:
        f1.writelines(s_ptcp(line, probs))
    f1.close()
print(s_ptcp("编辑代码一般是用插入模式", probs))
