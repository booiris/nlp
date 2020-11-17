import pickle

P = {'B': -0.26268660809250016,
     'E': -3.14e+100,
     'M': -3.14e+100,
     'S': -1.4652633398537678}
with open("begin_prob.p", "wb") as f:
    pickle.dump(P, f)
