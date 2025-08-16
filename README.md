# URL Harmonizer

`URL Harmonizer`, verilen domain veya URL listesini alarak hem **HTTP** hem de **HTTPS** versiyonlarını üretir.  
Girdi dosyasındaki her satırda bulunan domain veya URL işlenir, protokol olsa dahi temizlenip hem `http://` hem de `https://` versiyonları oluşturulur.

---

## 🚀 Özellikler
- Domain veya tam URL girebilirsiniz.
- Hem `http://` hem de `https://` sürümleri otomatik üretilir.
- Komut satırından **--input** ve **--output** parametreleriyle çalışır.
- Ekstra kütüphane gerektirmez (sadece `argparse` kullanır, Python ile birlikte gelir).

---

## 📦 Kurulum

1. Depoyu klonlayın veya `url_harmonizer.py` dosyasını indirin.
2. Python 3 kurulu olduğundan emin olun.
3. Girdi dosyanızı (`input.txt`) oluşturun.

---

## 💻 Kullanım

### Komut
```bash
python url_harmonizer.py --input input.txt --output output.txt
```

- `--input` : Domain/URL listesinin bulunduğu dosya.  
- `--output`: Sonuçların yazdırılacağı dosya.  

---

## 📂 Örnek Dosyalar

### input.txt
```
example.com
http://google.com
https://yandex.ru
medium.com
```

### Çalıştırma
```bash
python url_harmonizer.py --input input.txt --output output.txt
```

### output.txt
```
http://example.com
https://example.com
http://google.com
https://google.com
http://yandex.ru
https://yandex.ru
http://medium.com
https://medium.com
```

---

## 🛠 Katkıda Bulunma
- Hata bulursanız veya yeni özellik eklemek isterseniz issue açabilir ya da PR gönderebilirsiniz. 🚀

---

## 📄 Lisans
Bu proje MIT lisansı ile dağıtılmaktadır.
