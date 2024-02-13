import googletrans
import time
trans = googletrans.Translator().translate

hi = 'Hi'

xxx= trans(hi, dest = 'ko')
    

file_path = 'text.txt'

output_text = ''

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()  
for line_num in range(len(lines)):
    line = lines[line_num]
    if line == '\n':
        continue
    elif line_num == len(lines)-1:
        trans_text = trans(line, dest = 'ko').text
        output_text += (line + '\n' + trans_text + '\n\n')
    else:
        trans_text = trans(line, dest = 'ko').text
        output_text += (line + trans_text + '\n\n')

print(output_text)



output_file_path = 'output.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(output_text) 
