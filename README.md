

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
 <p>Çok fazla terim olduğu için sınırlama koyulur ve  vektör boyutları böylece daha küçük  tutulur.
    <b>vect = TfidfVectorizer(min_df = 2,ngram_range=(1,2)).fit(X_train)</b>
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
