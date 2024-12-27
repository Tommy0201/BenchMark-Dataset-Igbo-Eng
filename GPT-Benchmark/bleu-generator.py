from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, T5ForConditionalGeneration
from nltk.translate.bleu_score import corpus_bleu
from datasets import load_dataset
from concurrent.futures import ThreadPoolExecutor
import time
import json


finetuned_model_path = "/content/Users/tommynguyen/Downloads/Pidgin_batch_results.csv/drive/MyDrive/NLLB_model/NLLB_model_Amazon"
finetuned_model = AutoModelForSeq2SeqLM.from_pretrained(finetuned_model_path)
tokenizer = AutoTokenizer.from_pretrained(finetuned_model_path, src_lang="ibo_Latn", tgt_lang="eng_Latn")



test_datasets = load_dataset("Tommy0201/Igbo_To_Eng_Amazon_Translator",split='test')
test_source_sentences = test_datasets["igbo_input"]
test_reference_translations = test_datasets["eng_output"]
src_lang = "ibo_Latn"
tgt_lang = "eng_Latn"

print(test_source_sentences[:2])

# def translate_sentence(model, tokenizer, sentence):
#     inputs = tokenizer(sentence, return_tensors="pt")
#     translated_tokens = model.generate(
#         **inputs,
#         forced_bos_token_id=tokenizer.convert_tokens_to_ids("eng_Latn"),
#         max_length=256
#     )
#     translation = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
#     return translation


# start = time.time()
# translations = []
# for sent in test_source_sentences:
#   translation = translate_sentence(finetuned_model, tokenizer, sent)
#   translations.append(translation)
# end = time.time()
# og_file_path = '/content/drive/MyDrive/NLLB_flores200_test/NLLB_finetuned_amazon-trans.json'
# with open(og_file_path, 'w') as f:
#     json.dump(translations, f)

# print(f"Time for translating 1996 sentences (finetune): {(end - start) / 60:.2f} minutes")