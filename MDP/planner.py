import argparse
from cmath import inf


parser = argparse.ArgumentParser()
import numpy as np
from pulp import *
class reader():
    def __init__(self,mdp) :
        
        self.num_states = None
        self.num_actions = None
        self.end = []
        self.transition = []
        self.mdp_type = None
        self.gamma = None
        #transition has current, action, next, reward, probab
        with open(mdp) as f:
            lines = f.readlines()
        self.n = len(lines)
        nummy = lines[0].split()
        self.num_states = int(nummy[1])
        actionny = lines[1].split()
        self.num_actions = int(actionny[1])
        endlines = lines[2].split()
        self.end = [int(x.strip()) for x in endlines[1:]]
        
        # for i in range(len(lines[2])-5):
        #     self.end[i] = lines[2][i+4]
        for i in range(3,self.n-2,1):
            trans = lines[i].split()
            self.transition.append([float(x.strip()) for x in trans[1:]])    
        type = lines[self.n-2].split()
        self.mdp_type = type[1]
        dis = lines[self.n-1].split()
        self.gamma = float(dis[1])
        
        

        #print(self.transition)
    def lp(self):
        v = LpVariable.dicts("one", (range(self.num_states)))
        objective = LpProblem('lp', LpMinimize)
        objective += lpSum([v[i] for i in range(self.num_states)])
        for s in range(self.num_states):
            for a in range(self.num_actions):
                objective += v[s] >= lpSum([values[4]*(values[3] + self.gamma*v[int(values[2])]) if (values[0] == s and values[1] == a) else -100 for values in self.transition])
        objective.solve(PULP_CBC_CMD(msg=0))

        V = [value(v[s]) for s in range(self.num_states)]
        action = np.zeros(self.num_states)

        for s in range(self.num_states):
            maxi = -np.inf
            for a in range(self.num_actions):
                vfxn = sum([values[4]*(values[3] + self.gamma*V[int(values[2])]) if (values[0] == s and values[1] == a) else -100 for values in self.transition])
                if vfxn > maxi:
                    maxi = vfxn
                    action[s] = a
        
        for i in range(self.num_states):
            
            print(round(V[i],6), action[i])
        pass
    def vi(self):

        old = np.zeros(self.num_states)
        A = np.zeros(self.num_states)
        while True:
            new = np.zeros(self.num_states)
            for s in range(self.num_states):
                maxi = -np.inf

                for a in range(self.num_actions):
                    vfxn = 0

                    for values in self.transition:
                        if values[0] == s and values[1] == a:
                            vfxn += values[4]*(values[3] + self.gamma*old[int(values[2])])

                    if vfxn > maxi:
                        maxi = vfxn
                        A[s] = a
                new[s] = maxi

            comparison = old == new
            equal_arrays = comparison.all()

            if equal_arrays:
                break
            else:
                old = new.copy()

        for i in range(self.num_states):
            print(old[i], int(A[i]))

    def poleval(self, policy):
        old = np.zeros(self.num_states)
        # [0 for i in range(self.num_states)]

        while True:
            new = np.zeros(self.num_states)

            for s in range(self.num_states):
                vfxn= 0
                for values in self.transition:
                    if values[0]==s and values[1]==policy[s]:
                        vfxn += values[4]*(values[3] + self.gamma*old[int(values[2])])
                new[s] = vfxn
            comparison = old == new
            equal_arrays = comparison.all()
            if equal_arrays:
                break
            else:
                old = new.copy()

        
        
        return old


    def hpi(self):
        action = np.zeros(self.num_states)
        policy = self.poleval(action)
        while True:
            flag = True
            policy = self.poleval(action)
            for s in range(self.num_states):
                if s in self.end:
                    continue
                else:
                    for a in range(self.num_actions):
                        if action[s] == a:
                            continue
                        avp = sum([values[4]*(values[3] + self.gamma*policy[int(values[2])]) if (values[0] == s and values[1] == a) else 0 for values in self.transition])
                        if avp >= policy[s]:
                            action[s] = a
                            flag = False
                            break
            if flag:
                break
        for i in range(self.num_states):
            print(policy[i], action[i])
        return

            




if __name__ == "__main__":
    parser.add_argument("--mdp", type = str)
    parser.add_argument("--algorithm", type = str, default = "lp")
    parser.add_argument("--policy", type = str)
 
    
    
    args = parser.parse_args()
   
    caller = reader(args.mdp)
    if args.policy is not None:
        with open(args.policy) as f:
            lines = f.readlines()
        linesint = [int(lines[i]) for i in range(len(lines))]
        # print(linesint)
        Value = caller.poleval(linesint)
        
        for i in range(caller.num_states):
            print(Value[i], linesint[i])
        

    elif args.algorithm == 'lp' or args.algorithm == None:
        caller.lp()
    elif args.algorithm == 'hpi':
        caller.hpi()
    elif args.algorithm == 'vi' :
        caller.vi()

