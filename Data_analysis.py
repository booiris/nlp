import arpa
import pickle


f = open("Train_cache.txt","rb")
models = pickle.load(f)
f.close()

lm = models[0]
print(lm.log_s("都 是 为了 完善 社会主义 制度"))
