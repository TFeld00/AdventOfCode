DAY,_,_=__file__.rpartition('.')

from alg.cellular import step_list, step_function_game_of_life, parse_list

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

#part 1
m=parse_list(r,'#')
for _ in range(100):
    m=step_list(m, step_function_game_of_life([2,3],[3]), False, False)
    
print(sum(map(sum,m)))

#part 2
m=parse_list(r,'#')
for _ in range(100):
    m=step_list(m, step_function_game_of_life([2,3],[3]), False, False)
    m[0][0]=m[0][-1]=m[-1][0]=m[-1][-1]=True
    
print(sum(map(sum,m)))
