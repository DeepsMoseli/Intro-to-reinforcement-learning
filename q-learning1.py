# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 20:07:23 2017

My first reinforcement learning algorithm to help my agent cross a river to the other side

@author: moseli
"""

import numpy as np
import pandas as pd
import time

#global vars
states = [0,1,2,3,4,5,6,7,8,9,10]
actions = ["Left","Right"]
epsilon = 0.9
alpha = 0.2
max_episodes=20
refresh_time=0.3


#helper functions
def create_q_table():
    Q=pd.DataFrame(np.zeros((len(states),len(actions))),columns=actions)
    return Q
    
def choose_action(state,Q_table):
    state_actions=Q_table.iloc[state,:]
    if(np.random.uniform()>epsilon or state_actions.all()==0):#expore
        action_name=np.random.choice(actions)
    else:#act greedy
        action_name=state_actions.argmax()
    return action_name

def get_env_feedback(s,a):
    if a=='Right':
        if s==len(states)-2:
            s='terminal'
            R=1
        else:
            s+=1
            R=0
    else:
        if s==0:
            s=s
        else:
            s-=1
        R=0
    return s,R

    
def update_Q(s,step_counter,episode):
    env_list=['-']*(len(states)-1)+['T']
    if s=='terminal':
        interaction = 'episode: %s , total_steps: %s'%(episode+1,step_counter)
        print('\r{}'.format(interaction))
        time.sleep(2)
        print('\r                              ',end='')
    else:
        env_list[s]='*'
        interaction=''.join(env_list)
        print('\r{}'.format(interaction),end='')
        time.sleep(refresh_time)
            

def rl(s,s_,reward,a):
    if s_ != 'terminal':
        Q[a][s]=((1-alpha)*Q[a][s])+((alpha)*(reward+epsilon*(max([Q['Left'][s_],Q['Right'][s_]]))))
    else:
        Q[a][s]=((1-alpha)*Q[a][s])+((alpha)*(reward+epsilon*(max([Q['Left'][states[-1]],Q['Right'][states[-1]]]))))
#run algorithm

    #create Q table 
Q=create_q_table()

def run_algo():
    for k in range(max_episodes+1):
        s=0
        counter=0
        while s!='terminal':
            counter+=1
            a=choose_action(s,Q)
            s_,reward=get_env_feedback(s,a)
            rl(s,s_,reward,a)
            s=s_
            update_Q(s,counter,k)
            
run_algo()
