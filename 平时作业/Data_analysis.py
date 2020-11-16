import arpa


models = arpa.loadf("train_lm.txt",encoding="gbk")
print(models)
print(type(models))
print(len(models))
lm = models[0]
print(type(lm))
print(lm.counts())
print(lm.log_p("今天 真 不错"))
print(lm.log_s("都 是 为了 完善 社会主义 制度"))
print(lm.log_s("为了 是 都 制度 社会主义 完善"))


