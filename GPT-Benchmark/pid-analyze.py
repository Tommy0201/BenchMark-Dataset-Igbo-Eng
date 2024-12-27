import pandas as pd
from datasets import Dataset, DatasetDict, load_dataset
from huggingface_hub import login

# login("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")
df = pd.read_csv("GPT-Benchmark/selected_pid.csv")


selected = df[["pid_input","eng_output"]]

ds = load_dataset("Tommy0201/Igbo_To_Eng_Amazon_Translator")

igbo = ds["train"]["igbo_input"] + ds["validation"]["igbo_input"] + ds["test"]["igbo_input"]
print(type(igbo))
print(len(igbo))

list_pid = selected["pid_input"].tolist()
list_eng= selected["eng_output"].tolist()

def aver(lst):
    total_words = 0
    total_sent = len(lst)
    for sent in lst:
        l_sent = sent.split()
        total_words += len(l_sent)
    print("average words per sentence:", total_words/total_sent)
    
pid = list_pid
print("pid: ", aver(pid))
print("ibo: ", aver(igbo))
print("combined: ", aver(pid+igbo))

    
