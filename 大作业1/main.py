import os
import pickle
import time

from Analysis import analysis
from Dictionary_PTCP import d_ptcp
from Speech_HMM import speech_hmm
from Speech_analysis import speech_analysis
from Statistics_PTCP import s_ptcp

with open("Statistics/prob/probs.p", "rb") as f:
    probs = pickle.load(f)
with open("Dictionary/Dict/dict.p", "rb") as f:
    dic = pickle.load(f)
with open("Speech/prob/probs.p", "rb") as f:
    speechprobs = pickle.load(f)
# fsize = os.path.getsize("File/test_data.txt") / 1024.0
#
# time_start = time.time()
# with open("File/test_data.txt", "r", encoding='utf-8') as f:
#     f1 = open("Dictionary/Dictionary_out.txt", "w+", encoding='utf-8')
#     for line in f:
#         f1.writelines(d_ptcp(line, dic, True))
#     f1.close()
# time_end = time.time()
# time_cost = time_end - time_start
# print("字典分词：")
# print('time cost', time_cost, 's')
# print("speed", fsize / time_cost, 'kb/s')
# analysis("Dictionary/Dictionary_out.txt")
#
# time_start = time.time()
# with open("File/test_data.txt", "r", encoding='utf-8') as f:
#     f1 = open("Statistics/Statistics_out.txt", "w+", encoding='utf-8')
#     for line in f:
#         f1.writelines(s_ptcp(line, probs))
#     f1.close()
# time_end = time.time()
# time_cost = time_end - time_start
# print("统计分词：")
# print('time cost', time_cost, 's')
# print("speed", fsize / time_cost, 'kb/s')
# analysis("Statistics/Statistics_out.txt")

# fsize = os.path.getsize("test.txt") / 1024.0
time_start = time.time()
with open("real_dat.txt", "r", encoding='utf-8') as f:
    f1 = open("Speech/Speech_out.txt", "w+", encoding='utf-8')
    for line in f:
        f1.writelines(speech_hmm(line, speechprobs))
    f1.close()
# time_end = time.time()
# time_cost = time_end - time_start
# print("词性标注：")
# print('time cost', time_cost, 's')
# print("speed", fsize / time_cost, 'kb/s')
# speech_analysis("Speech/Speech_out.txt")
