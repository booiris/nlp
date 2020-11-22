import jieba
import jieba.posseg as pseg


with open("../File/test_data.txt", "r", encoding="utf-8") as f:
    f1 = open("Jieba_out.txt", "w+", encoding="utf-8")
    cnt = 0
    for line in f:
        words = pseg.cut(line)
        res = ""
        for word, flag in words:
            res += word + "/" + flag + " "
        f1.writelines(res)
        cnt += 1
    f1.close()
