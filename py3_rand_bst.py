from BSTNode import BSTNode
from BSTree import BSTree
import random

## bugs to vladimir dot kulyukin at gmail dot com

## implement this method
def gen_rand_bst(num_nodes, a, b):
    pass

## implement this method
def estimate_list_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b):
    pass

def estimate_list_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_rbsts, a, b):
    d = {}
    for num_nodes in xrange(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_list_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b)
    return d

## implement this method
def estimate_balance_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b):
    pass

def estimate_balance_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_rbsts, a, b):
    d = {}
    for num_nodes in xrange(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_balance_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b)
    return d

