import linecache
import re


def analysis():
    correct_cnt = 0
    sum_cnt = 0
    real_cnt = 0
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）|——|《|》|：|\n|\r|．|”|“|『|』'
    with open("Dictionary/Dictionary_out.txt", "r", encoding='utf-8') as predict_f:
        linenumber = 1
        for predict_line in predict_f:
            real_line = linecache.getline("File/real_data.txt", linenumber)
            real_line = real_line.split()
            real_list = []
            now = 0
            for word in real_line:
                word = word.split("/")
                word = re.split(pattern, word[0])
                if word[0] == '':
                    continue
                str_len = len(word[0])
                real_list.append((now, now + str_len - 1))
                now = now + str_len

            predict_list = []
            now = 0
            predict_line = predict_line.split()
            for word in predict_line:
                word = re.split(pattern, word)
                if word[0] == '':
                    continue
                str_len = len(word[0])
                predict_list.append((now, now + str_len - 1))
                now = now + str_len

            correct_cnt += len(set(predict_list) & set(real_list))
            sum_cnt += len(predict_list)
            real_cnt += len(real_list)

            linenumber += 1

    # print(correct_cnt)
    # print(sum_cnt)
    # print(real_cnt)
    P = correct_cnt / sum_cnt
    R = correct_cnt / real_cnt
    F1 = (2 * P * R) / (P + R)
    print("%.f%%" % (P * 100))
    print("%.f%%" % (R * 100))
    print("%.f%%" % (F1 * 100))

    return P, R, F1


analysis()
