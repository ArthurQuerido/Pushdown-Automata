# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:00:09 2021

@author: Arthur Querido Lopes
"""

def PDA(transitions, state, acceptance_states, string, stack):
    
    #Always update string to make possible empty transition at the end
    if string == '':
        string = '-'
    
    for transition in transitions:
         #To simulate the pop when the automata starts to remove symbols from stack
        if transition[4] == '-':
            transition [4] = ''
        #Check each transition in the list and verify if what we are trying is valid
        #First we try with string's first symbol
        if state == transition[0] and string[0] == transition[1] and (
                    stack[0] == transition[2]) and string[0] != '-':
            new_state = transition[3]
            if PDA(transitions, new_state, acceptance_states, string[1:], transition[4]+stack[1:]):
                return True
        #Then we check for any empty transition and try it
        if state == transition[0] and transition[1] == '-' and (
                                                    stack[0] == transition[2]):
            new_state = transition[3]
            if PDA(transitions, new_state, acceptance_states, string, transition[4]+stack[1:]):
                return True
    
    #Check if current state is in acceptance set when string is consumed
    if string == '-':
        if state in acceptance_states:
            return True
        else: 
            return False
        
    return False

transitions = []

#Receiving number of states from user and creating state keys
n = input()

#Receiving alphabet symbols
k, alphabet = input().split(' ', 1)
alphabet = alphabet.split()

#Receiving stack symbols
s, stack_symbols = input().split(' ', 1)
stack_symbols = stack_symbols.split()

#Receiving acceptance states from user
k, acceptance_states = input().split(' ', 1)
acceptance_states = set(acceptance_states.split())

#Receiving number of transitions from user
t = int(input())

transitions = []
#Receiving transitions from user
for i in range(t):
    trans = input().split()
    transitions.append(trans)

#Receiving number of strings to be tested
c = int(input())
 
#Receiving strings one by one
strings = []
for i in range(c):
    strings.append(str(input()))
    
#Testing all strings
for string in strings:
    if (PDA(transitions, '0', acceptance_states, string, 'Z')):
        print("accept")
    else:
        print("reject")