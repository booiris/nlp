import pickle


def s_ptcp():
    with open("prob/begin_prob.p", "rb") as f:
        begin_prob = pickle.load(f)
    with open("prob/trans_prob.p", "rb") as f:
        trans_prob = pickle.load(f)
    with open("prob/emit_prob.p", "rb") as f:
        emit = pickle.load(f)
    print(begin_prob)
    print(trans_prob)



s_ptcp()
