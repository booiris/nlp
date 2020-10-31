import pickle


f = open("varname.txt", "rb")
varname = pickle.load(f)
dic = varname["dic"]
transmat = varname["transmat"]
word_list = varname["word_list"]
speech_list = varname["speech_list"]

for word in word_list:
    if len(word_list[word]) == 1:
        print(word)
