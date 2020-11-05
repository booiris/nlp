import arpa
import pickle


models = arpa.loadf("train_lm.txt",encoding="utf-8")

lm = models[0]
print(lm.p("大家 好"))
