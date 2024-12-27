import openai
import time
import requests
import concurrent.futures
import os
from datasets import load_dataset
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def call_api(sent):
    completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a professional translator specializing in Nigerian languages. Your task is to translate Igbo sentences into English."},
        {"role": "user", "content": f'Translate this sentence to English: {sent}. Please provide the most accurate translation possible. Only include the translated sentence in your response.'},
    ]
    )
    translation = completion.choices[0].message.content.strip()
    return sent, translation

def concurrent_translate(sentences):
    pairs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(call_api,sent) for sent in sentences]
        count = 0
        for future in concurrent.futures.as_completed(futures):
            sentence,translation = future.result()
            if translation:
                pairs.append((sentence,translation))
                count +=1
            if count%100==0:
                time.sleep(5)
    return pairs

def main():
    source_path = "GPT-Benchmark/MAFAND-MT/val-test.ibo"
    out_path = "GPT-Benchmark/JW300/val-test_gpt4.eng"
    
    
    #USING DATASET FROM DIRECTORY    
    with open(source_path,'r',encoding='utf-8') as f: #getting translated pairs from gpt
        ibo_lines = f.read()
    sentences =ibo_lines.split('\n')
    
    #IMPORTING DATASET FROM HUGGING FACE
    # dataset = load_dataset("Tommy0201/Igbo_To_Eng_Amazon_Translator", split='test')  # Adjust the split as necessary
    # sentences = dataset['igbo_input']
    translated_pairs = concurrent_translate(sentences)
    
    
    
    out = [] #setting output array to write to new file
    for sent in sentences:
        for pair in translated_pairs:
            if pair[0] == sent:
                out.append(pair[1])
                break
        
    mode = "w"
    if os.path.isfile(out_path):
        mode = "a"
    with open(out_path,mode) as f:
        for x in out:
            f.write(x+"\n")
    

if __name__ == "__main__":
    # main()

    print(call_api("Nafdac na-eme nyocha ndịa maka nchọpụta BBC mere gbasara ọgwụ ahụ"))



                
#Total Generation from GPT
    #FLORES200 - Facebook
        #eng_gpt.dev: 997
        #eng_gpt.devtest: 1012
    #JW300 
        #test_gpt.en: 2707
        #val_gpt.en: 1500
    #MAFAND-MT
        #test_gpt.eng: 1500
        #val_gpt.eng: 1500
        
    #9216 sentences in total
    
    #JW300 got 400k more if needed
    #MAFAND-MT got 7k more if neede