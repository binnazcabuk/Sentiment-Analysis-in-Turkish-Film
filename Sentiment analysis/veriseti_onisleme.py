# -*- coding: utf-8 -*-
#Kütüphanelerin eklenmesi
import pandas as pd
import nltk
import re
import seaborn as sns
import matplotlib.pyplot as plt
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import jpype
from os.path import join
from typing import List
from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM
import seaborn as sns;
#Data setini ekleyip sütunları isimlendirelim
column = ['Yorum',"Değerlendirme"]
data = pd.read_excel('yorumlar.xlsx', encoding ='iso-8859-9', sep='"')

print(data.head(5))

#Data setindeki değerlendirme sütununu 0 ve 1 ile ifade edelim
data["Değerlendirme"] = data["Değerlendirme"].replace("Negatif", 0)
data["Değerlendirme"] = data["Değerlendirme"].replace("Pozitif", 1)

data['text length'] = data['Yorum'].apply(len)
data.head()



x=data['Değerlendirme'].value_counts()
x=x.sort_index()
plt.figure(figsize=(4,4))
ax= sns.barplot(x.index, x.values, alpha=0.8)
plt.title("Yapılan Yorum Sayısı")
plt.ylabel('Yorum Sayısı')
plt.xlabel('Yorum Sınıfı')
rects = ax.patches
labels = x.values
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')
plt.show();

print('######################################################################')


print ('Noktalama işaretlerini kaldırıyor ...')
def noktalamaKaldir(Yorum):
    
     Yorum = ''.join([c for c in Yorum if c not in punctuation])
     return Yorum

data['Yorum'] = data['Yorum'].apply(noktalamaKaldir)
print(data.head(5))

print('######################################################################')
print ('Sayılar kaldırıyor ...')
def sayiKaldir(Yorum):
     sayilar=('0','1','2','3','4','5','6','7','8','9')
     Yorum = ''.join([c for c in Yorum if c not in sayilar])
     return Yorum
 
data['Yorum'] = data['Yorum'].apply(sayiKaldir)
print(data.head(5))

print('######################################################################')

print('Şapkalı karakterleri eşleniği ile değiştiriyor ...')
def karakterDegis(yorum):   
  # degistir listesindeki ilk öğeyi ikincisi ile değiştiriyoruz. 
  #Yani şapkalı harfleri normale çeviriyoruz.
  replace_letter = [('â', 'a'), ('ê', 'e'), ('î', 'i'), ('ô', 'o'), ('û', 'u')]
  for tpl in replace_letter:
     yorum = yorum.replace(tpl[0], tpl[1])
  return yorum

data['Yorum'] = data['Yorum'].apply(karakterDegis)
print(data.head(5))

print('######################################################################')
  
  
print ('Tüm karakterler küçük harfe dönüştürülüyor ...')
def kucukHarfDonus(yorum):
    yorum= re.sub(r"I", "ı", yorum)
    yorum = yorum.lower()
    return yorum

data['Yorum'] = data['Yorum'].apply(kucukHarfDonus)
print(data.head(5))

print('######################################################################')
 
      
print ('Belirtilen alfabede olmayan tüm karakterleri kaldırıyor ...')
def alfabeTemizle(yorum):
    alfabe ='ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz '
    cleaned_text = ''
    for char in yorum:
        if char in alfabe:
            cleaned_text = cleaned_text + char

    return cleaned_text

data['Yorum'] = data['Yorum'].apply(alfabeTemizle)
print(data.head(5))

print('######################################################################')
 
      
print('stopword kaldırılıyor................\n')
def durdurmaKelimeKaldir(yorum):
   
 stopWords = set(stopwords.words('turkish'))
 words = word_tokenize(yorum)
 wordsFiltered = []
 
 for w in words:
     if w not in stopWords:
        wordsFiltered.append(w)
        yorum='  '.join(wordsFiltered)       
 return yorum

data['Yorum'] = data['Yorum'].apply(durdurmaKelimeKaldir)
print(data.head(5))

print('######################################################################')

      
print('tekrarlanan kelimeler kaldırılıyor....\n')
def tekrarSil(yorum):
 word_data =yorum 
 nltk_tokens = nltk.word_tokenize(word_data)

 ordered_tokens = set()
 result = []
 for word in nltk_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result.append(word)
        yorum=' '.join(result)   
 return yorum

data['Yorum'] = data['Yorum'].apply(tekrarSil)
print(data.head(5))

print('######################################################################')


print('Zemberek Kütüphanesi İle Yazım Düzeltme')
print("Veri seti büyük olduğu için bu işlem uzun sürüyor....")    
if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        '-Xmx256m',
        convertStrings=False
    )

    TurkishMorphology=jpype.JClass('zemberek.morphology.TurkishMorphology')
    TurkishSpellChecker=jpype.JClass('zemberek.normalization.TurkishSpellChecker')

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    spell_checker: TurkishSpellChecker = TurkishSpellChecker(morphology)

def kelimeduzeltme(yorum):
 words = word_tokenize(yorum)
 

 for i, word in enumerate(words):
        if spell_checker.suggestForWord(JString(word)):
            if not spell_checker.check(JString(word)):
                words[i] = str(spell_checker.suggestForWord(JString(word))[0])
              

 yorum=' '.join(words) 
 

 return yorum

data['Yorum'] = data["Yorum"].apply(kelimeduzeltme)
print(data.head(5))
jpype.shutdownJVM()


data.to_excel('yorum_temiz.xlsx')
