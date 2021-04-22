# -*- coding: utf-8 -*-

"""
Created on Sun Dec 22 19:08:46 2019

@author: ASUS
"""

#Kullanacağımız kütüphaneleri ekleyelim
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split #Data setimizi test ve eğitim olarak bölmek için,
from sklearn.feature_extraction.text import CountVectorizer #Metini özelliklerin geçme sıklığı matrisine çevirmek için,
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, accuracy_score, recall_score, f1_score, precision_score
#Sonuçlarımızı değerlendirmek için accuracy ve area under curve kriterlerini kullanacağız.
from sklearn.feature_extraction.text import TfidfVectorizer #Metini özelliklerin ağırlığı matrisine çevirmek için,
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns;
#Data setini ekleyip sütunları isimlendirelim
column = ['Yorum',"Değerlendirme"]
data = pd.read_excel('yorum_temiz.xlsx', encoding ='iso-8859-9', sep='"')


#Data setimizi test ve eğitim alt kümelerine rastgele şekilde bölelim

X_train, X_test, y_train, y_test = train_test_split(data['Yorum'], data['Değerlendirme'], test_size=0.2,random_state = 42)


#################################### COUNT VECTORIZER ####################################


#CountVectorizer sınıfından bir nesne üretiyoruz ve eğitim verilerimize uyguluyoruz.
vect = CountVectorizer(encoding ='iso-8859-9',max_features =8000,
                             min_df = 2,
                             ngram_range = (1,2)).fit(X_train.values.astype('U'))
#kelime sayar ve matrisi kelime sayı matrisi olarak oluşturur.
#X_train'deki metinleri bir matrise dönüştürdük.
X_train_vectorized = vect.transform(X_train.values.astype('U')) 


#Programı, vektörize ettiğimiz X eğitim verilerini kullanarak lojistik regresyon ile eğiteceğiz.
model = LogisticRegression(solver='lbfgs',random_state =0)
model.fit(X_train_vectorized, y_train)

#X_test verilerini kullanarak tahminler yapacağız
tahmin = model.predict(vect.transform(X_test))

#Eğittiğimiz modelin bu tahminleri nasıl yaptığını daha iyi anlamak için, 
#oluşturduğumuz matrisin özelliklerini alalım.
#Daha sonra da sıralı modelimizdeki ilk 20 ve son 20 değerlerin karşılık geldiği özellikleri yazdıralım

ozellik_isimleri = np.array(vect.get_feature_names())
sorted_coef_index = model.coef_[0].argsort()
print('\nNegatif:\n',ozellik_isimleri[sorted_coef_index[:20]])
print('\nPozitif:\n',ozellik_isimleri[sorted_coef_index[:-21:-1]])


print('*'*20,'lojistik regresyon','*'*20)

#başarı göster
print(classification_report(y_test, tahmin))

#karmaşıklık matrisi
score = round(accuracy_score(y_test, tahmin), 3)
matrix1 = confusion_matrix(y_test, tahmin)
sns.heatmap(matrix1, annot=True, fmt=".0f")
plt.xlabel('Öngörülen Değerler')
plt.ylabel('Gerçek değerler')
plt.title('Lojistik Regresyon Doğruluk Skoru: {0}'.format(score), size = 10)
plt.show()

################################################################################



print('*'*20,'naive_bayes','*'*20)
from sklearn.naive_bayes import MultinomialNB

# naive bayes veri kümesine uydurma
model2 = MultinomialNB()
model2.fit(X_train_vectorized, y_train)

#tahmin yapma
tahmin2 = model2.predict(vect.transform(X_test))

#başarı oran
print(classification_report(y_test, tahmin2))

#hata matrisi
score = round(accuracy_score(y_test, tahmin2), 3)
matrix2 = confusion_matrix(y_test, tahmin2)
sns.heatmap(matrix2, annot=True, fmt=".0f")
plt.xlabel('Öngörülen Değerler')
plt.ylabel('Gerçek değerler')
plt.title('Naive Bayes Doğruluk Skoru: {0}'.format(score), size = 10)
plt.show()

################################################################################


print('*'*20,'SVM','*'*20)
from sklearn.svm import SVC


# svm veri kümesine uydurma
model3 = SVC(kernel ='linear')
model3.fit(X_train_vectorized, y_train)

#tahmin yaptırma
tahmin3 = model3.predict(vect.transform(X_test))

#başarı ,hassasiyet,geri çağırma
print(classification_report(y_test, tahmin2))


#hata matrisi gösterimi
score = round(accuracy_score(y_test, tahmin3), 3)
matrix3 = confusion_matrix(y_test, tahmin3)
sns.heatmap(matrix3, annot=True, fmt=".0f")
plt.xlabel('Öngörülen Değerler')
plt.ylabel('Gerçek değerler')
plt.title('SVM Doğruluk Skoru: {0}'.format(score), size = 10)
plt.show()


###############################################################################


# TF-İDF DAHA BAŞARILI SONUÇLAR VERDİĞİ İÇİN YORUM İÇİN O KULLANILMIŞTIR#####



'''
#yorum ekranııı 

def yorumYap():
    olumsuzsay=0
    yorum=str(yorumgiris.get())
    ab=yorum.strip().split()
    search_keywords=['değil','değildi',]
    
#search_keywords içindeki bir kelimeyi içeriyorsa olumsuz sonucu verir   
    for sentence in ab:
     if (any(map(lambda word: word in sentence, search_keywords))):
      olumsuzsay=olumsuzsay+1
      #kelime kontrolü yapıp sayma
     else:
       continue
     
    if olumsuzsay>0:
      sonuc['text']="\nOLUMSUZ"
#
    else:
        
       if(model2.predict(vect.transform([yorum]))==[0]):
            
            sonuc['text']="\nOLUMSUZ"   
       elif(model2.predict(vect.transform([yorum]))==[1]):
           sonuc['text']="\nOLUMLU"
           
    
           
def temiz_metin():
        yorumgiris.delete(0, 'end') 
        sonuc.delete(0,'end')
    
from tkinter import *

#görsel tasarım
pencere=Tk()
pencere.title("DUYGU ANALİZİ")
pencere.geometry("500x450")
pencere.iconbitmap('favicon.ico')
pencere['bg'] = '#49A'
photo = PhotoImage(file = "m.png")
photo2 = PhotoImage(file = "u.png")

#yorum yazılacak kutu tasarımı
yorum=Label(pencere,text="BİR YORUM GİRİNİZ...",font=("Consolas",15),bg='#49A')
yorum.pack()
yorumgiris=Entry(pencere,font=("Consolas",15),width=40)
yorumgiris.pack()

#sonuc yazma labeli
yazi=Label(pencere,text="ANALİZ SONUÇ",font=("Times New Roman",15),bg='#49A')
yazi.pack()

#yorumu analiz buton
analiz=Button(pencere,text="ANALİZ ET", font=("Consolas",15),bg='#ddd3ed',command=yorumYap)

#ekrana tasarım amaçlı resim yerleştirme
analiz.pack()
resim1 = Label(pencere, image=photo,bg='#49A')
resim1.pack()
resim2= Label(pencere, image=photo2,bg='#49A')
resim2.pack()

#temizleme butonu
temiz_button =Button(pencere, text="TEMİZLE",font=("Consolas",15),bg='#ddd3ed', command=temiz_metin)
temiz_button.pack()

sonuc=Label(pencere,text="",font=("Consolas",24),bg='#49A')
sonuc.pack()
#yerleşim yerleri
yorum.place(x=150,y=20)
yorumgiris.place(x=35,y=55,height=100)
analiz.place(x=55,y=200)
temiz_button.place(x=350,y=200)
sonuc.place(x=200,y=320)
resim1.place(x=30)
resim2.place(x=430)

yazi.place(x=185,y=300)
pencere.mainloop()        
'''