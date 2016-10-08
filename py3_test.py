##################################################
## module: py3_test.py
## author: Misty Jenkins
## A#: A01489174
## test module for py3_rand_bst
## 10/7/2016
##################################################
from py3_rand_bst import *

print("List probablility:")
d = estimate_list_probs_in_rand_bsts(5, 15, 200, 0, 1000000)
for k, v in d.items():
    print("probability of linearity in rbsts with %d nodes = %f" % (k, v[0]))

print("\n\nBalanced probablility:")
d = estimate_balance_probs_in_rand_bsts(5, 100, 200, 0, 1000000)
for k, v in d.items():
    print("probability of balance in rbsts with %d nodes = %f" % (k, v[0]))