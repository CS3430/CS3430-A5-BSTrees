##################################################
## module: py3_rand_bst.py
## author: Misty Jenkins
## A#: A01489174
## estimates the probability of a binary search tree being a list
##  or a balanced tree by generating multiple random binary trees
## 10/7/2016
##################################################
from BSTree import BSTree
import random

## bugs to vladimir dot kulyukin at gmail dot com

def gen_rand_bst(num_nodes, a, b):
    tempBst = BSTree()
    while tempBst.getNumNodes() < num_nodes:
        tempBst.insertKey(random.randint(a,b))
    return tempBst

def estimate_list_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b):
    rbsts = [gen_rand_bst(num_nodes,a,b) for i in range(0, num_rbsts)]
    numLists = sum(b.isList() for b in rbsts)
    prob = numLists/float(num_rbsts)
    return (prob, rbsts)

def estimate_list_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_rbsts, a, b):
    d = {}
    for num_nodes in range(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_list_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b)
    return d

def estimate_balance_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b):
    rbsts = [gen_rand_bst(num_nodes, a, b) for i in range(0, num_rbsts)]
    numLists = sum(b.isBalanced() for b in rbsts)
    prob = numLists / float(num_rbsts)
    return (prob, rbsts)

def estimate_balance_probs_in_rand_bsts(num_nodes_start, num_nodes_end, num_rbsts, a, b):
    d = {}
    for num_nodes in range(num_nodes_start, num_nodes_end+1):
        d[num_nodes] = estimate_balance_prob_in_rand_bsts_with_num_nodes(num_rbsts, num_nodes, a, b)
    return d

