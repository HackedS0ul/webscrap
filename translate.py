import csv
from google_trans_new import google_translator 



translator = google_translator(ser)  


my_text = open('fileq.csv', 'r', encoding='utf-8', newline='')
content= my_text.read()

result = translator.translate(content,lang_src='pl', lang_tgt='lt')

with open('file_lt.csv', 'w', encoding='utf-8') as f:
    f.write(result)



