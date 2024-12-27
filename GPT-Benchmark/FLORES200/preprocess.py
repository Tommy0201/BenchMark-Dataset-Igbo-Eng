
file1 = "GPT-Benchmark/MAFAND-MT/archive/val.ibo"
file2 = "GPT-Benchmark/MAFAND-MT/archive/test.ibo"

with open(file1,'r') as f:
    lines1 =f.readlines()
with open(file2,'r') as g:
    lines2 =g.readlines()
    
lines3 = lines1+lines2
with open("GPT-Benchmark/MAFAND-MT/val-test.ibo",'w',encoding='utf-8') as file:
    for line in lines3:
        file.write(line)