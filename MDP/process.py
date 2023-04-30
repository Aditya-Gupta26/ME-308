import start
import argparse
parser = argparse.ArgumentParser()

cont = start.options_1
entr = start.ind1
exit = start.ind2
class reader():
    def __init__(self,states) :
        # file = io.open('data.txt','r', encoding='utf-16-le')
        with open(states,'r',encoding='utf-16-le') as f:
            lines = f.readlines()
        self.lines=[]
        self.path=[[]]
        for i in range(len(lines)):
            
            self.lines.append(lines[i])
        
    def printer(self):
        print(self.lines)

    def caller(self):
        length = len(self.lines)
        end = entr
        ite = 0
        with open('MDP_final.txt', 'r') as file:
                # Read the content of the file into a list
                file_content = file.readlines()
                

        while(end!=exit):
        # while(ite<3):
            ini = end
            final = self.lines[ite].split(" ") 
            var = final[-1][:-1]
            argend = cont.index(end)
            
            # var = int(var)
            print(4+argend*23+var)
            final2 = file_content[4+argend*23+var].split(" ")
            end = cont.index(final2[3])
            mode = ""
            if var <=19:
                mode = "Road"
            elif var <=21:
                mode = "Local"
            else:
                mode = "Bus"
            self.path.append([mode,ini,end])
            ite = ite + 1
             
            #index i ke liye 3 + i*numACtions + 1 se start hai aur action j is on 4 + i*numActions + j
            
           
            
            


    
    

if __name__ == "__main__":
    
    parser.add_argument("--states", type = str,default = 'filename.txt')
    

    args = parser.parse_args()
   
    caller = reader(args.states)
    
    caller.printer()
    caller.caller()
