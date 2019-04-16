'''
################################################################################################################
# Written By:- Aadish Joshi
# email: aadish.joshi@utdallas.edu
# Command to execute: python Hw2_CKYparser.py grammar.txt sentence.txt

Sales of the company to return to normalcy
the new products and services contributed to increase revenue
Dow falls as recession indicator flashed red and economical worries continue through the month
Figure skater lands historic quadruple jump in senior international competition at the 2019 World Figure Skating Championships on Day 3 but could only clinch a silver medal


################################################################################################################
'''


################################################################################################################
# imports
################################################################################################################

import os.path
import argparse
import Helper

################################################################################################################
# Helper Node class
################################################################################################################
class Node:
    def __init__(self, Priority, l_child, r_child=None):
        self.Priority = Priority
        self.l_child = l_child
        self.r_child = r_child
    def __repr__(self):
        return self.Priority

################################################################################################################
# Recursive function to get the tree via node priority and children
################################################################################################################
def getTree(node):
    if node.r_child is None:
        return f"[{node.Priority} '{node.l_child}']"
    return f"[{node.Priority} {getTree(node.l_child)} {getTree(node.r_child)}]"


################################################################################################################
# CKYclass
################################################################################################################
class CKY:
    def __init__(self, grammar, sentence):
        self.TABLE = None
        self.grammar = None
        if os.path.isfile(grammar):
            self.get_file(grammar)
        self.__call__(sentence)

    def __call__(self, sentence, parse=False):
        if os.path.isfile(sentence):
            with open(sentence) as inp:
                m = inp.readline()
                print(m)
                self.input = m.split()
                if parse:
                    self.parse()
        else:
            self.input = sentence.split()
    ################################################################################################################
    # Read Grammar file
    ################################################################################################################

    def get_file(self, grammar):
        self.grammar = Helper.CNF(Helper.read_file(grammar))

    ################################################################################################################
    # display bracketed parsing
    ################################################################################################################
    def Display(self, output=True):
        start = self.grammar[0][0]
        End = [n for n in self.TABLE[-1][0] if n.Priority == start]
        if End:
            if output:
                print("\nPossible parse(s):")
            trees = [getTree(node) for node in End]
            if output:
                for tree in trees:
                    print(tree)
            else:
                return trees
        else:
            print("Error in grammar: Sentence cannot be formed!")

    ################################################################################################################
    # Parse the sentence
    ################################################################################################################
    def parse(self):
        length = len(self.input)
        self.TABLE = [[[] for x in range(length - y)] for y in range(length)]

        for i, key in enumerate(self.input):
            for rule in self.grammar:
                if f"'{key}'" == rule[1]:
                    self.TABLE[0][i].append(Node(rule[0], key))
        for words in range(2, length + 1):
            for cell_begin in range(0, length - words + 1):
                for lsize in range(1, words):
                    rsize = words - lsize
                    cell_L = self.TABLE[lsize - 1][cell_begin]
                    cell_r = self.TABLE[rsize - 1][cell_begin + lsize]
                    for rule in self.grammar:
                        left_nodes = [n for n in cell_L if n.Priority == rule[1]]
                        if left_nodes:
                            right_nodes = [n for n in cell_r if n.Priority == rule[2]]
                            self.TABLE[words - 1][cell_begin].extend(
                                [Node(rule[0], left, right) for left in left_nodes for right in right_nodes]
                            )
################################################################################################################
# Main function
################################################################################################################
if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("grammar",
                           help="Grammar File")
    argparser.add_argument("sentence",
                           help="Sentence.txt file")
    args = argparser.parse_args()
    CYK = CKY(args.grammar, args.sentence)
    CYK.parse()
    CYK.Display()