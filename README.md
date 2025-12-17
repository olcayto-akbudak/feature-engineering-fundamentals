# Feature Engineering Fundamentals

Bu repository, Feature Engineering (Özellik Mühendisliği) kavramlarını **teorik + uygulamalı** olarak ele alan, aynı zamanda **yeniden kullanılabilir bir otomasyon scripti** içeren bir öğrenme ve portföy projesidir.

Proje; veri ön işleme, feature engineering teknikleri ve bu tekniklerin model performansına etkisini gerçek veri setleri üzerinden göstermeyi amaçlar.

---

## 🎯 Projenin Amacı

* Feature Engineering temellerini öğrenmek ve pekiştirmek
* Encoding, scaling ve eksik değer doldurma tekniklerini uygulamak
* Feature engineering ile model accuracy artışını vaka analiziyle göstermek
* Tek fonksiyonla çalışabilen bir feature engineering otomasyon scripti geliştirmek
* GitHub ve portföy paylaşımına uygun, temiz ve profesyonel bir yapı oluşturmak

---

## 📁 Proje Klasör Yapısı

```text
feature-engineering-fundamentals/
│
├── notebooks/
│   └── feature_engineering_fundamentals.ipynb
│
├── scripts/
│   └── feature_engineering.py
│
├── data/
│   ├── titanic.csv
│   ├── house_prices.csv
│   └── customer_churn.csv
│
├── README.md
└── requirements.txt
```

---

## 📘 Notebook İçeriği

`feature_engineering_fundamentals.ipynb` aşağıdaki bölümlerden oluşur:

1. Feature Engineering Temelleri
2. Encoding Teknikleri

   * Label Encoding
   * One-Hot Encoding
3. Scaling Yöntemleri

   * StandardScaler
   * MinMaxScaler
4. Eksik Değer Doldurma Teknikleri

   * Mean / Median / Mode
   * KNN Imputer
5. 3 Farklı Veri Seti Üzerinde Uygulama

   * Titanic (Classification)
   * House Prices (Regression)
   * Customer Churn (Business Case)
6. Vaka Analizi: Feature Engineering ile Accuracy Artırma
7. Feature Engineering Otomasyon Tasarımı
8. Gün Sonu Notları ve Özet

Notebook, hem öğrenme hem de referans amacıyla markdown açıklamalar ve kod hücreleri birlikte olacak şekilde hazırlanmıştır.

---

## ⚙️ Feature Engineering Automation Script

`scripts/feature_engineering.py` dosyası, tekrar kullanılabilir bir feature engineering pipeline sunar.

Temel özellikler:

* Kategorik ve sayısal değişkenleri otomatik ayırma
* Eksik değer doldurma
* Encoding (Label / One-Hot)
* Scaling (Standard / MinMax)
* Parametreli ve genişletilebilir yapı

Bu script, gerçek projelerde hızlı ve tutarlı feature engineering uygulamak amacıyla tasarlanmıştır.

---

## 📊 Vaka Analizi – Accuracy Artışı

Projede, Titanic veri seti kullanılarak aşağıdaki karşılaştırma yapılır:

* Feature engineering öncesi model performansı
* Feature engineering sonrası model performansı

Bu analiz ile hangi feature engineering adımlarının model başarısına katkı sağladığı değerlendirilir.

---

## 🧰 Kullanılan Teknolojiler

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Jupyter Notebook

---

## 🚀 Kurulum

```bash
pip install -r requirements.txt
```

Notebook’u çalıştırmak için:

```bash
jupyter notebook
```

---

## 📝 Notlar

* Feature engineering adımları **train-test ayrımı dikkate alınarak** uygulanmıştır
* Data leakage riskine karşı gerekli önlemler açıklamalarla birlikte verilmiştir
* Proje, öğrenme amaçlı olduğu kadar **portföy ve mülakat sunumu** için de uygundur

---

## 📌 Geliştirme Fikirleri

* Pipeline yapısının `sklearn.Pipeline` ile genişletilmesi
* Feature selection eklenmesi
* Model karşılaştırmaları (Logistic, RandomForest, XGBoost)

---

Bu repository, feature engineering konusunda sağlam bir temel oluşturmak isteyen herkes için referans niteliğindedir.
