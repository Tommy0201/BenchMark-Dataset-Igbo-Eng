from nltk.translate.bleu_score import corpus_bleu, sentence_bleu


def calculate_bleu(trans_path,ref_path):
    with open(ref_path,'r',encoding="utf-8") as f:
        references = f.readlines() #List of sentences
        
    with open(trans_path,'r',encoding="utf-8") as g:
        translations = g.readlines() #List of sentences
        
    ref_new = [ref.split() for ref in references]
    trans_new = [tran.split() for tran in translations]

    # ref1 = ref_new[0]
    # trans1 = trans_new[0]
    # print("ref: ",ref1)
    # print("tran: ",trans1)
    # bleu_score = sentence_bleu([ref1], trans1)
    # print("BLEU Score: ", bleu_score)
#thêse ảe comments from gẻorge and i ưant to tell u in the bést syntax possible that i love u bizzle and we will stay in touch

    ref_new_list = [[ref] for ref in ref_new]
    bleu_score_corpus = corpus_bleu(ref_new_list, trans_new)
    return bleu_score_corpus


if __name__ == "__main__":
    trans_paths = [
        # "GPT-Benchmark/FLORES200/eng_gpt.devtest",
        # "GPT-Benchmark/FLORES200/eng_gpt.dev",
        # "GPT-Benchmark/MAFAND-MT/test_gpt.eng", 
        # "GPT-Benchmark/MAFAND-MT/val_gpt.eng", 
        # "GPT-Benchmark/JW300/test_gpt.en",
        # "GPT-Benchmark/JW300/val_gpt.en",
        "GPT-Benchmark/FLORES200/eng_gpt4o.devtest",
        "GPT-Benchmark/FLORES200/eng_gpt4.devtest",
        "GPT-Benchmark/MAFAND-MT/val-test_gpt4o.eng",
        "GPT-Benchmark/MAFAND-MT/val-test_gpt4.eng",
        "GPT-Benchmark/JW300/val-test_gpt4o.en",
        # "GPT-Benchmark/JW300/val-test_gpt4.en",
        "GPT-Benchmark/AmazonTrans/test_gpt4o.en",
        "GPT-Benchmark/AmazonTrans/test_gpt4o.en"
    ]
    ref_paths = [
        # "GPT-Benchmark/FLORES200/eng_Latn.devtest",
        # "GPT-Benchmark/FLORES200/eng_Latn.dev",
        # "GPT-Benchmark/MAFAND-MT/test.eng",
        # "GPT-Benchmark/MAFAND-MT/val.eng", 
        # "GPT-Benchmark/JW300/test.en",
        # "GPT-Benchmark/JW300/val.en",
        "GPT-Benchmark/FLORES200/eng_Latn.devtest",
        "GPT-Benchmark/FLORES200/eng_Latn.devtest",
        "GPT-Benchmark/MAFAND-MT/val-test.eng",
        "GPT-Benchmark/MAFAND-MT/val-test.eng",
        "GPT-Benchmark/JW300/val-test.en", 
        # "GPT-Benchmark/JW300/val-test.en", 
        "GPT-Benchmark/AmazonTrans/test.en",
        "GPT-Benchmark/AmazonTrans/test.en",
    ]
    

    for trans_path, ref_path in zip(trans_paths, ref_paths):
        # Extract the relevant part of the path to display
        display_name = f"{trans_path[len('GPT-Benchmark/'):]}"
        bleu_score = calculate_bleu(trans_path, ref_path)
        print(f"BLEU Score for {display_name}: {round(bleu_score,4)}")
    



# BLEU SCORE

#RESULT GPT 4o mini versus human translated benchmark dataset

#IGBO - ENGLISH

    #FLORES200/eng_gpt.test  - news corpus
        # GPT-4o: 0.1923 
        # GPT-4: 0.0888
        # NLLB original: 0.1934
        # NLLB finetune: 0.2183  -- 10.53%
        # ByT5 finetune: 0.0904  -- 
        # DeltaLM finetune: 0.144
        
    #JW300  - bible, gnome
        # GPT-4o: 0.1055 
        # GPT -4: N/A
        # NLLB original: 0.1887 
        # NLLB finetune: 0.2424  --  28.25%
        # ByT5 finetune: 0.1781  
        # DeltaLM finetune: 0.2476 --
    
        
    #MAFAND-MT/val-test_gpt.eng  - 
        # GPT-4o: 0.1467
        # GPT-4: 0.1052
        # NLLB original: 0.127  
        # NLLB finetune: 0.2067  -62.78%
        # ByT5 finetune: 0.1717
        # DeltaLM finetune: 0.2868  --
    
    #Amazon_Translator _Benchmark  - news corpus
        # GPT-4: 0.1823
        # GPT-4o: 0.2844
        # NLLB original: 0.255
        # NLLB finetune: 0.436  -- 70.98
        # ByT5 finetune: 0.2735
        # DeltaLM finetune: 0.3472
        
    # Average score:
    # GPT-4o: 0.1567
    # NLLB org: 0.191
    # NLLB finetune: 0.2759
    # delta lm: 0.2564
    # byt5: 0.1784