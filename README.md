

<p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115793736-54bd8480-a3d5-11eb-8113-f4a6b801a1ae.PNG" width="500"></a>
 </p>
<hr>
<div align="center">
   <h1>Proje İşleyişi</h1> 
</div>
<p> 
    <b>1.</b> Veri setini oluşturma
<br>
  <b>2.</b> Veri seti önişleme
<br>
  <b>3.</b> Count Vectorizer Özellik vektörü çıkarımı ve  matrise dönüştürme
<br>
  <b>4.</b>Lojistik Regresyon, Naive Bayes ve Destek Vektör Makineleri ile  ayrı ayrı eğitme
<br>
  <b>5.</b> TF-IDF Vectorizer Özellik vektörü çıkarımı ve matrise dönüştürme
<br>
  <b>6.</b>Lojistik Regresyon, Naive Bayes ve Destek Vektör Makineleri ile  ayrı ayrı eğitme
<br>
  <b>7.</b> İki özellik vektörü ile yapılan eğitimlerin başarı oranları karşılaştırması yapma
<br>
  <b>8.</b> Başarılı modeli kullanarak kullanıcıya yorum ekranı sunma

</p>

<hr>
<div align="center">
   <h1>Veri Seti</h1> 
</div>
<p>Çeşitli film izleme platformlarından  toplanmış  11.506 negatif, 12.144 pozitif yorum olmak üzere toplam 23.650 yorum içermektedir.</p>
<p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115794578-e679c180-a3d6-11eb-9174-15fcb2d8775e.PNG" ></a>
 </p>
<hr>
<div align="center">
   <h1>Ön İşleme</h1> 
</div>

<p> 
 Günlük konuşma dili ile yazılmış olan yorumlar çokça gereksiz kelime, anlamsız karakter içermektedir ve buda anlam karmaşasına sebep olmaktadır. Bunu önlemek ve daha sade veri seti elde etmek için ön işleme uygulanmıştır.
 <br>
Noktalama işaretleri de kelimeleri sayısal vektörlere dönüştürme aşamasında gereksiz yere vektörlerin büyüklüğünü arttıracak bir unsur olduğundan tüm noktalama işaretleri ve sayılar temizlenmiştir. Türkçe alfabede yer almayan tüm karakterler kaldırılmıştır. Şapkalı karakterler eşleniği ile değiştirilmiştir. Kelime vektörlerinin bütünlüğünü sağlamak için tüm harfler küçük harfe dönüştürülmüştür. 
</p>
<p><i>Zemberek Kütüphanesi Kullanılmıştır.</i>
<hr>
<div align="center">
   <h1>Count Vectorizer)
</h1> 
</div>
<p>
    Bir metin belgesindeki  terim / jeton sayımlarını vektöre dönüştürmek için kullanılır. 
</p>
<p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115794954-a9fa9580-a3d7-11eb-8e89-22551aa58e03.PNG" ></a>
 </p>
 <p>Çok fazla terim olduğu için sınırlama koyulur ve  vektör boyutları böylece daha küçük  tutulur.<br>
    <b>vect = TfidfVectorizer(min_df = 2,ngram_range=(1,2)).fit(X_train)</b><br>
Projede 2 metinden daha az metinde gözüken kelimeleri, listeden kaldırdım.
</p>
<p>Bu sınıf kullanılarak yapılan özellik çıkarımında  ilk  ve son 20 özellik
</p>
<p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115795135-052c8800-a3d8-11eb-8522-a92c501920c5.PNG" ></a>
 </p>

 <hr>
<div align="center">
   <h1>TF-IDF Vectorizer
</h1> 
</div>
<p>
    Bir metinde geçen terimlerin çıkarılması ve bu terimlerin geçtiği miktara göre çeşitli hesapların yapılması üzerine kuruludur.
</p>
<p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115795313-62283e00-a3d8-11eb-96e9-3ef60936c08a.PNG" ></a>
 </p>
<p>Örneğin, 
0 – Bu film gerçekten muhteşem.<br>
1 – Yaptığı muhteşem filmlerden sadece biri bu.<br>
2 –Bu kadar sıkıcı film görmedim.<br>
 Birinci metin içinde muhteşem terimi için hesaplamamızı yaparsak <br>
    <b>  TF = 2 / 4 = 0.5IDF = log(3/2) = 0.18 </b>  <br>
    <b>  TF-IDF =0.5*0.18=0,09 </b>
</p>
  <p>Projede TF-IDF  ile ilk ve son 20 özellik listelendiğinde 
</p>  
<p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115795711-1d50d700-a3d9-11eb-9bb9-dd8a35b133e7.PNG" ></a>
 </p>
 <hr>
<div align="center">
   <h1>Lojistik Regresyon
</h1> 
</div>
<p>
 <b>Bu teoremde S biçimli bir eğri olan Lojistik Fonksiyon kullanıldığı için bu adı almıştır.</b><br></p>
    <p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115795892-7587d900-a3d9-11eb-9057-dbfba412bb19.PNG" ></a>
 </p>
<p>Bir yorumun iyi ya da kötü olduğunu hesaplarken eğer olasılık n(t)>= 0.5 ise pozitif bir yorumdur. Yani eğri altında kalan sonuçlar negatif, üstünde kalanlar ise pozitif yorumdur.</p>
<hr>
<div align="center">
   <h1>Naive Bayes

</h1> 
</div>
<p><b>Naive Bayes</b> sınıflandırıcısının temeli <i>Bayes</i> teoremine dayanır ve her değeri diğer değerlerden bağımsız olarak sınıflandırır. Olasılık kullanarak ve belirli bir dizi özelliğe dayanarak bir sınıfı, kategoriyi tahmin etmemizi sağlar. 

</p>
 <p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115796063-ca2b5400-a3d9-11eb-8fe3-4311cfc474b8.PNG" ></a>
 </p>
 <p><b>A Pozitif – B Negatif</b>
P ( A | B ) = B olayı gerçekleştiğinde A olayının gerçekleşme olasılığı <br<
P ( A ) = A olayının gerçekleşme olasılığı<br>
P ( B | A ) = A olayı gerçekleştiğinde B olayının gerçekleşme olasılığı<br>
P ( B ) = B olayının gerçekleşme olasılığı<br>
</p>
<hr>
<div align="center">
   <h1>Destek Vektör Makineleri
</h1> 
</div>
<p>
Bu algoritmada, her bir veri maddesini belirli bir koordinatın değeri olan her özelliğin değeri ile birlikte n-boyutlu boşluğa (burada n sahip olduğunuz özelliklerin sayısı) bir nokta olarak çizilir. Ardından, iki sınıftan oldukça iyi ayrım yapan hiper-düzlemi bularak sınıflandırma gerçekleştirilir
</p>
 <p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115796253-373ee980-a3da-11eb-939b-c4b70c741797.PNG" ></a>
 </p>
 <p>Pozitif yorumların mavi renk, negatif yorumların kırmızı olduğunu düşünürsek, yapılan tahmin bu hiper-düzlem üzerinde olursa <b>pozitif</b> altta kalırsa <b>negatif</b> yorum olarak sınıflandırılır. 
</p>
<hr>
<div align="center">
   <h1>Model Başarı Karşılaştırma
</h1> 
</div>
<p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115796535-aa486000-a3da-11eb-9c81-0d832403eae6.PNG" ></a>
 </p>
<hr>
<div align="center">
   <h1>Ekran Çıktısı
</h1> 
</div>
<p align='center'>
<a href="">
    <img  src="https://user-images.githubusercontent.com/34273337/115796650-e085df80-a3da-11eb-9d14-c0e845e2609e.PNG" ></a>
 </p>
