from py2_rand_bst import *

d = estimate_list_probs_in_rand_bsts(5, 200, 1000, 0, 500000)
for k, v in d.iteritems():
    print('probability of linearity in rbsts with %d nodes = %f' % (k, v[0]))

d = estimate_balance_probs_in_rand_bsts(5, 200, 1000, 0, 500000)
for k, v in d.iteritems():
    print('probability of balance in rbsts with %d nodes = %f' % (k, v[0]))