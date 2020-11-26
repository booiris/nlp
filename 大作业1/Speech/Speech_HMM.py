import pickle


def speech_hmm(test_str, probs):
    begin_prob = probs["begin_prob"]
    trans_prob = probs["trans_prob"]
    emit_prob = probs["emit_prob"]
    test_str = test_str.split()
    if not test_str:
        return "\n"
    if test_str[len(test_str) - 1] != '\n':
        test_str += '\n'
    word = []
    res = ""
    for test_word in test_str:
        word.append(test_word)
        if not '\u4e00' <= test_word[0] <= '\u9fa5':
            # if not (test_word == '\n'):
            #     continue
            if word:
                dp = [{}, {}]  # 初始概率矩阵
                now_p = 0
                while now_p < len(word) and not ('\u4e00' <= word[now_p] <= '\u9fa5'):
                    if word[now_p] != '\n':
                        res += word[now_p] + ' '
                    now_p += 1
                if now_p == len(word):
                    word = []
                    continue
                for key in begin_prob:
                    dp[0][key] = begin_prob[key] + emit_prob[key][
                        word[now_p] if word[now_p] in emit_prob[key] else False]

                path = [{key: [] for key in begin_prob} for _ in range(2)]  # 保存状态序列
                for i in begin_prob:
                    path[0][i].append(i)
                now = 1
                father = 0

                for i in range(1, len(word)):
                    if not '\u4e00' <= word[i][0] <= '\u9fa5':
                        continue
                    for j in begin_prob:
                        max_state = None
                        max_prob = -3.14 * 1e+100
                        for k in begin_prob:
                            if word[i] in emit_prob[j]:
                                now_prob = dp[father][k] + trans_prob[k][j] + emit_prob[j][word[i]]
                            else:
                                now_prob = dp[father][k] + trans_prob[k][j] + emit_prob[j][False]

                            if now_prob > max_prob:
                                max_prob = now_prob
                                max_state = k
                        dp[now][j] = max_prob
                        newpath = []
                        for state in path[father][max_state]:
                            newpath.append(state)
                        newpath.append(j)
                        path[now][j] = newpath
                    now = father
                    if now == 1:
                        father = 0
                    else:
                        father = 1

                prob = -3.14 * 1e+100
                for state in begin_prob:
                    if dp[father][state] > prob:
                        prob = dp[father][state]
                        res_state = state
                res_path = path[father][res_state]
                now = 0
                for i in range(len(word)):
                    if not '\u4e00' <= word[i][0] <= '\u9fa5':
                        if word[i] != '\n':
                            res += word[i] + ' '
                        continue
                    res += word[i] + "/" + res_path[now] + ' '
                    now += 1

            word = []

    return res + '\n'


with open("prob/probs.p", "rb") as f:
    probs = pickle.load(f)

with open("../File/speech_test_data.txt", "r", encoding='utf-8') as f:
    f1 = open("Divide_Speech_out.txt", "w+", encoding='utf-8')
    for line in f:
        res = speech_hmm(line, probs)
        # print(res)
        # if cnt >= 1:
        #     break
        f1.writelines(res)
    f1.close()
