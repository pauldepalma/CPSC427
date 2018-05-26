import string
import sys

'''
Recursive descent parser for simple propositional logic
Valid Symbols:
 Propositional symbols: A .. Z
 Logic symbols: true, false
 negation: ~
 binary operators: V, ^, :, =
 ( : is implication)

 Grammar:
 S -> prop_s S | neg_s S | operator_s
 prop_s -> A | B | ... | Z | true | false
 operator_s -> S op S
 neg_s -> ~ S
 op -> ~ | ^ | V | : | =
 
'''

#converts space delimited string to a list
def tokenize(sent):
    return sent.split()


def rdp(sent):
    idx = sentence_h(sent,0)
    sentence(sent,idx)

#Makes sure what is in string matches what should be there
#Error condition will not happen with logic grammar
def match(sent,idx,token):
    if sent[idx] == token:    
        idx = nexttoken(idx)  
        return idx
    print("match error") #will never occur with logic grammar

#Gets next token
def nexttoken(idx):
    return idx + 1

#handles the first token sequence in the string.
#Must be 0 or more ~ followed by a proposition
def sentence_h(sent,idx):
    if sent[idx] == '~':
        idx = neg_s(sent,idx,'~')
    idx = prop_s(sent,idx)
    return idx

#Invokes functions for non-terminals except for the first sequence
#Calls itself recursively
def sentence(sent,idx):
    if idx == len(sent):
        print "Yes"
        sys.exit()
    idx = operator_s(sent,idx)
    if sent[idx] == '~':
        idx = neg_s(sent,idx,'~')
    idx = prop_s(sent,idx)
    sentence(sent,idx)

#Handles negation, e.g., ~A, ~~A etc.
def neg_s(sent,idx,neg):
    while (sent[idx] == neg):
        idx = match(sent,idx,sent[idx])
        if idx == len(sent):
            print "negation error"
            sys.exit()
    return idx

#Handles binary operators       
def operator_s(sent,idx):
    if sent[idx] in ['V','^',':','=']:
        idx = match(sent,idx,sent[idx])
        return idx
    print "operator error"
    sys.exit()

#Handles propositions
def prop_s(sent,idx):
    if sent[idx] in string.uppercase or sent[idx] in ['true', 'false']:
        idx = match(sent,idx,sent[idx])
        return idx
    print "proposition error"
    sys.exit()

def main():
    sent = "~ ~ A V B : C V ~ ~ X"
    sent = tokenize(sent)
    rdp(sent)                      

main()
