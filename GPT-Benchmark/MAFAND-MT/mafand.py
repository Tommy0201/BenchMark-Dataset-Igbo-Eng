from datasets import load_dataset

raw_data = load_dataset("masakhane/mafand","en-ibo")
train_raw = raw_data['validation']['translation']
eng_sent = []
ibo_sent = []
for pair in train_raw:
  eng_sent.append(pair['en'])
  ibo_sent.append(pair['ibo'])
  
file_name_en = "GPT-Benchmark/MAFAND-MT/val.eng"
file_name_ibo = "GPT-Benchmark/MAFAND-MT/val.ibo"

with open(file_name_en, 'w') as f:
    for sent in eng_sent:
        f.write(sent+'\n')
with open(file_name_ibo, 'w') as g:
    for sent in ibo_sent:
        g.write(sent+'\n')
        