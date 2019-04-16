'''
################################################################################################################
# Written By:- Aadish Joshi
# email: aadish.joshi@utdallas.edu
# Command to execute: python Hw2_CKYparser.py grammar1.txt sentence.txt
################################################################################################################
'''

################################################################################################################
# GLOBAL HashMAP to store rules
################################################################################################################
HASHMAP = {}

################################################################################################################
# read grammar file
################################################################################################################
def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [x.replace("->", "").split() for x in lines]

################################################################################################################
# Grammar - Context Free Grammar
################################################################################################################
def CNF(grammar):
    UP, result = [], []
    helper_append = result.append
    index = 0
    for rule in grammar:
        split_rule = []
        if rule[1][0] != "'" and len(rule) == 2: 
            UP.append(rule)
            append_rule(rule)
            continue
        elif len(rule) > 2:
            T = [(key, i) for i, key in enumerate(rule) if key[0] == "'"]
            if T:
                for key in T:
                    rule[key[1]] = f"{rule[0]}{str(index)}"
                    split_rule += [f"{rule[0]}{str(index)}", key[0]]
                index += 1
            while len(rule) > 3:
                split_rule += [f"{rule[0]}{str(index)}", rule[1], rule[2]]
                rule = [rule[0]] + [f"{rule[0]}{str(index)}"] + rule[3:]
                index += 1
        append_rule(rule)
        helper_append(rule)
        if split_rule:
            helper_append(split_rule)
    while UP:
        rule = UP.pop()
        if rule[1] in HASHMAP:
            for key in HASHMAP[rule[1]]:
                add_rule = [rule[0]] + key
                if len(add_rule) > 2 or add_rule[1][0] == "'":
                    helper_append(add_rule)
                else:
                    UP.append(add_rule)
                append_rule(add_rule)
    return result

################################################################################################################
# add rule to hashmap
################################################################################################################
def append_rule(rule):
    global HASHMAP
    if rule[0] not in HASHMAP:
        HASHMAP[rule[0]] = []
    HASHMAP[rule[0]].append(rule[1:])