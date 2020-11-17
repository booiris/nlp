import jieba

with open("../File/test_data.txt", "r", encoding="utf-8") as f:
    f1 = open("Jieba_out.txt", "w+", encoding="utf-8")
    cnt = 0
    for line in f:
        line = jieba.cut(line)
        line = " ".join(line)
        f1.writelines(line)
        cnt += 1
    f1.close()
