import pandas as pd

# Load data
df = pd.read_csv("GPT-Benchmark/selected_pid.csv")
pid_sentences = df["pid_input"].to_list()

# Process sentences to remove first and last words
pid_process = [' '.join(sent.split()[1:-1]) for sent in pid_sentences]

# Load BBC and Naijalingo processed sentences
with open("GPT-Benchmark/AmazonOg/processed_bbc_pidgin.txt", 'r') as f:
    pid_bbc = set(f.read().splitlines())

with open("GPT-Benchmark/AmazonOg/processed_naijalingo.txt", 'r') as g:
    pid_naija = set(g.read().splitlines())

# Match sentences using set intersections
match_bbc = {pid for pid in pid_process if any(pid in sent for sent in pid_bbc)}
unmatched_bbc = [pid for pid in pid_process if pid not in match_bbc]

match_naija = {pid for pid in pid_process if any(pid in sent for sent in pid_naija)}

# Print results
print("Number of matches with BBC:", len(match_bbc))
print("Number of matches with Naijalingo:", len(match_naija))
print("Total sentences processed:", len(pid_process))
print("Unmatched sentences with BBC:")
for sentence in unmatched_bbc:
    print(sentence)
