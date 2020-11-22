import linecache


def speech_analysis(Filename):
    correct_cnt = 0
    sum_cnt = 0
    real_cnt = 0
    with open(Filename, "r", encoding='utf-8') as predict_f:
        linenumber = 1
        for predict_line in predict_f:
            real_line = linecache.getline("File/real_data.txt", linenumber)
            real_line = real_line.split()
            real_list = []
            now = 0
            for word in real_line:
                word = word.split("/")
                now_str = ""
                for char in word[0]:
                    if '\u4e00' <= char <= '\u9fa5':
                        now_str += char
                if now_str:
                    str_len = len(now_str)
                    real_list.append((now, now + str_len - 1,word[1]))
                    now = now + str_len

            predict_list = []
            now1 = 0
            predict_line = predict_line.split()
            for word in predict_line:
                word = word.split("/")
                now_str = ""
                for char in word[0]:
                    if '\u4e00' <= char <= '\u9fa5':
                        now_str += char
                if now_str:
                    str_len = len(now_str)
                    predict_list.append((now1, now1 + str_len - 1,word[1]))
                    now1 = now1 + str_len
            if now != now1:
                print("asdfsadf")

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
    print("%.3f%%" % (P * 100))
    print("%.3f%%" % (R * 100))
    print("%.3f%%" % (F1 * 100))

    return P, R, F1


speech_analysis("Speech/Statistics_Speech_out.txt")
