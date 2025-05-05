📝📊 Öğrenci Not Sistemi (Grade Report System)
Bu Python projesi, öğrencilerin puanlarını harf notlarına çevirir, rapor kartları oluşturur ve öğrenci notlarını bir dosyaya yazar. 📚👨‍🏫

🎯 Projenin Amacı
Öğrencilerin puanlarını değerlendirmek

Notlara göre rapor kartları oluşturmak

Eksik öğrenciler için özel durumları yönetmek

Sonuçları .txt dosyalarına yazmak

🧠 Kullanılan Python Özellikleri
if-elif-else yapıları ile not hesaplama

try-except ile dosya kontrolü ve hata yönetimi

open(), write(), read() işlemleri ile dosya yazma/okuma

for döngüsü ile öğrenci listesinin işlenmesi

🔤 Harf Notu Dönüşümü
Puan	Harf Notu
70 ve üzeri	A
50-69	B
30-49	C
0-29	F

💡 Örnek Fonksiyon
python
Kopyala
Düzenle
def compute_grade(points):
    if points >= 70:
        return 'A'
    elif points >= 50:
        return 'B'
    elif points >= 30:
        return 'C'
    else:
        return 'F'
🧪 Örnek Çıktı
less
Kopyala
Düzenle
Zach scored 51/100 points in Chemistry and got the letter B  
There is an existing report card for Sophie  
Oğuzhan:A  
Zach:B  
Sophie:A  
Fred:F  
Belina was missing during the exam.  
Markus was missing during the exam.  
📁 Oluşturulan Dosyalar
zach_report.txt : Zach’in not dökümü

sophie_report.txt : Sophie’nin mevcut not dökümünü kontrol eder

grades.txt : Tüm öğrencilerin notlarının bulunduğu liste

🚀 Nasıl Çalıştırılır?
Kodları .py uzantılı bir dosyaya yapıştır

Terminalden çalıştır:

bash
Kopyala
Düzenle
python your_script_name.py
📌 Geliştirme Fikirleri
Her ders için ayrı not sistemi

Notları JSON veya CSV formatında saklama

Kullanıcı arayüzü (GUI) ile geliştirme

👨‍🏫 Python ile öğrencilerin notlarını yönetmek artık çok daha kolay!
