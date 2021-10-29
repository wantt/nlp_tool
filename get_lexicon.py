
from g2pM import G2pM
import pypinyin
model = G2pM()
import re
import jiagu
word2lex={}
def get_sheng(word_pinyin):
  sheng = pypinyin.style._utils.get_initials(word_pinyin,strict=False)
  yun = word_pinyin.replace(sheng,'')
  return [sheng,yun]
def get_lexs(text):
  text = ''.join(re.findall(r'[\u4e00-\u9fa5]',text)).strip()
  words = jiagu.seg(text)
  for word in words:
    tmp_pinyin = model(word, tone=True, char_split=False) 
    all_pinyin = []
    for p in tmp_pinyin:
      for k in get_sheng(p):
        if not k:
          continue
        all_pinyin.append(k) 
    result = ' '.join(all_pinyin)
    word2lex[word] = result


if  __name__ == "__main__":
  with  open('text','r') as f,open('result.txt','w+',encoding='utf-8') as f2:
    for line in f.readlines():
      sline  = line.strip().split(' ')[1]
      get_lexs(sline)
    for x in word2lex:
      f2.write('%s\t%s\n'%(x,word2lex[x]))
    


