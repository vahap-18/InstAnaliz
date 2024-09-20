# Instagram İstatistik Toplayıcı Programı

Bu Python programı, belirlenen bir Instagram kullanıcısına ait temel istatistikleri toplar ve kullanıcıya gösterir. Program, açık Instagram hesaplarından çeşitli metrikler sunar ve bu bilgileri tablo halinde gösterir. Eğer kullanıcı gizli bir hesapsa, hangi verilerin alınamadığı açıkça belirtilir.

## Özellikler

- **Takipçi Sayısı**: Belirtilen hesabın takipçi sayısını görüntüler.
- **Gönderi Sayısı**: Hesabın toplam gönderi sayısını gösterir.
- **Beğeni Sayısı** (Gizli Hesap Değilse): Gönderilerdeki toplam beğeni sayısını toplar.
- **Yorum Sayısı** (Gizli Hesap Değilse): Gönderilerdeki toplam yorum sayısını toplar.
- **Katılım Oranı** (Gizli Hesap Değilse): Beğeni ve yorumların toplamını kullanarak takipçi sayısına oranla etkileşim yüzdesini hesaplar.
- **En Çok Beğenilen Video** (Gizli Hesap Değilse): Hesabın en çok beğeni alan videosunu bulur.
- **En Çok İzlenen Video** (Gizli Hesap Değilse): Hesabın en çok görüntülenen videosunu bulur.
- **Ortalama Etkileşim** (Gizli Hesap Değilse): Gönderi başına ortalama beğeni, yorum ve izlenme sayılarını hesaplar.
- **Gizli Hesaplar İçin Uyarı**: Gizli hesaplar için veriler alınamazsa, kullanıcıya hangi verilerin alınamayacağı belirtilir.

## Gereksinimler

Bu programı çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

- `instaloader`
- `tabulate`
- `collections`
- `time`

Gerekli kütüphaneleri yüklemek için:

```bash
pip install instaloader tabulate
```

## Kullanım

1. **Programı çalıştırın**:
   Programı başlatmak için terminalde aşağıdaki komutu çalıştırın:

   ```bash
   python instagram_stats.py
   ```

2. **Kullanıcı Adı Girin**:
   Program çalıştırıldığında sizden bir Instagram kullanıcı adı girmeniz istenecek.

3. **Sonuçları Görün**:
   Program belirtilen kullanıcıya ait istatistikleri toplayacak ve tablo halinde ekrana yazdıracaktır.

   - Eğer kullanıcı **gizli bir hesap** ise, program hangi verilerin alınamadığını bildirecektir.

## Örnek Kullanım

Programı çalıştırdıktan sonra bir Instagram kullanıcı adı girin:

```
Lütfen bir Instagram kullanıcı adı girin: example_user
```

Program daha sonra istatistikleri tablo formatında gösterecektir:

```
╒═══════════════════════════════════════╤═════════════╕
│ Bilgi                                 │ Değer       │
╞═══════════════════════════════════════╪═════════════╡
│ Takipçi Sayısı                        │ 5000        │
├───────────────────────────────────────┼─────────────┤
│ Gönderi Sayısı                        │ 120         │
├───────────────────────────────────────┼─────────────┤
│ Beğeni Sayısı                         │ 15000       │
├───────────────────────────────────────┼─────────────┤
│ Yorum Sayısı                          │ 3000        │
├───────────────────────────────────────┼─────────────┤
│ Katılım Oranı (%)                     │ 25.00%      │
├───────────────────────────────────────┼─────────────┤
│ Toplam İzlenme Sayısı                 │ 90000       │
├───────────────────────────────────────┼─────────────┤
│ En Çok Beğenilen Video Beğeni Sayısı  │ 9500        │
├───────────────────────────────────────┼─────────────┤
│ En Çok İzlenen Video İzlenme Sayısı   │ 50000       │
├───────────────────────────────────────┼─────────────┤
│ Ortalama Görüntüleme Sayısı           │ 166.67      │
├───────────────────────────────────────┼─────────────┤
│ Ortalama Beğeni Sayısı                │ 12.50       │
├───────────────────────────────────────┼─────────────┤
│ Ortalama Yorum Sayısı                 │ 2.50        │
╘═══════════════════════════════════════╧═════════════╛
```

Eğer kullanıcı gizli bir hesapsa, alınamayan veriler belirtilir:

```
Hesap gizli olduğu için aşağıdaki veriler alınamıyor:

- Beğeni Sayısı
- Yorum Sayısı
- Video Görüntüleme Sayısı
- Gönderi Etkile

```
