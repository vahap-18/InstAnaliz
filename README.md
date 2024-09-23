# Instagram İstatistik Toplayıcı Programı

Bu Python programı, belirtilen bir Instagram kullanıcısına ait çeşitli istatistikleri toplar ve kullanıcıya tablo formatında gösterir. Program, kullanıcının takipçi sayısından beğeni ve yorum oranlarına kadar geniş bir yelpazede bilgi sağlar. Eğer hedef hesap gizli bir hesapsa, toplanamayan veriler kullanıcıya bildirilir.

## Özellikler

- **Takipçi Sayısı**: Belirtilen Instagram hesabının takipçi sayısını görüntüler.
- **Gönderi Sayısı**: Hesabın toplam gönderi sayısını gösterir.
- **Beğeni Sayısı** (Gizli Hesap Değilse): Hesabın gönderilerindeki toplam beğeni sayısını toplar.
- **Yorum Sayısı** (Gizli Hesap Değilse): Gönderilerdeki toplam yorum sayısını hesaplar.
- **Katılım Oranı (Etkileşim Yüzdesi)**: Beğeni ve yorum sayısına göre hesaplanan etkileşim oranını gösterir.
- **En Çok Beğenilen Gönderi**: Hesabın en fazla beğeni alan gönderisini bulur.
- **En Çok Yorum Alan Gönderi**: Hesabın en çok yorum alan gönderisini gösterir.
- **Ortalama Gönderi Etkileşimi**: Gönderi başına ortalama beğeni ve yorum sayısını hesaplar.
- **Gizli Hesap Uyarısı**: Gizli hesaplar için alınamayan veriler hakkında kullanıcıya bilgi verir.

## Gereksinimler

Programın çalışabilmesi için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- `instaloader`: Instagram verilerini toplamak için.
- `rich`: Verilerin renkli ve düzenli bir şekilde terminalde gösterilmesi için.
- `tqdm`: İşlem ilerlemesini göstermek için.

Gerekli kütüphaneleri yüklemek için:

```bash
pip install instaloader rich tqdm

```

## Kullanım

1. **Programı çalıştırın**:
Terminalde aşağıdaki komut ile programı başlatın:
    
    ```bash
    python instagram_analyzer.py
    
    ```
    
2. **Instagram Kullanıcı Adı Girin**:
Program çalıştığında, analiz edilmesini istediğiniz Instagram kullanıcısının adını girmeniz istenecek. Kullanıcı adını girdikten sonra program hesap verilerini toplamaya başlayacaktır.
3. **Sonuçları Görün**:
İstatistikler toplanıp analiz edildikten sonra tablo formatında ekrana yazdırılacaktır. Eğer analiz edilen hesap gizliyse, hangi verilerin alınamadığı kullanıcıya bildirilir.

### Örnek Kullanım

Aşağıdaki örnekte, `example_user` adında bir Instagram hesabı için topladığımız verileri görüyorsunuz:

```
Lütfen bir Instagram kullanıcı adı girin: example_user

```

Program çıktısı:

```
╒═══════════════════════════════════════╤═════════════╕
│ Bilgi                                 │ Değer       │
╞═══════════════════════════════════════╪═════════════╡
│ Takipçi Sayısı                        │ 500         │
├───────────────────────────────────────┼─────────────┤
│ Gönderi Sayısı                        │ 120         │
├───────────────────────────────────────┼─────────────┤
│ Beğeni Sayısı                         │ 1500        │
├───────────────────────────────────────┼─────────────┤
│ Yorum Sayısı                          │ 300         │
├───────────────────────────────────────┼─────────────┤
│ Katılım Oranı (%)                     │ 15.00%      │
├───────────────────────────────────────┼─────────────┤
│ En Çok Beğenilen Gönderi              │ Gönderi #23 │
├───────────────────────────────────────┼─────────────┤
│ En Çok Yorum Alan Gönderi             │ Gönderi #45 │
├───────────────────────────────────────┼─────────────┤
│ Ortalama Etkileşim                    │ 166.67      │
╘═══════════════════════════════════════╧═════════════╛

```

Eğer analiz edilen hesap **gizli** ise, şu şekilde bir çıktı alırsınız:

```
Bu hesap gizli olduğu için aşağıdaki verilere ulaşılamadı:

- Beğeni Sayısı
- Yorum Sayısı
- En Çok Beğenilen Gönderi
- En Çok Yorum Alan Gönderi

```

## Olası Hatalar ve Çözümleri

- **Giriş Yapma Hatası**:
    - **Hata Mesajı**: `Giriş yapılamadı. Lütfen kullanıcı adınızı ve şifrenizi kontrol edin.`
    - **Çözüm**: Instagram kullanıcı adı veya şifre hatalı olabilir. Doğru bilgileri girdiğinizden emin olun. Ayrıca, çok sık oturum açma denemesi yaptıysanız, Instagram hesabınız geçici olarak engellenmiş olabilir.
- **Profil Bulunamıyor Hatası**:
    - **Hata Mesajı**: `Girilen kullanıcı adı geçerli değil veya kullanıcı hesabı gizli.`
    - **Çözüm**: Instagram hesabının doğru olduğundan ve herkese açık olduğundan emin olun.
- **Ağ Bağlantısı Sorunu**:
    - **Hata Mesajı**: `Instagram'a bağlanılamıyor. Lütfen internet bağlantınızı kontrol edin.`
    - **Çözüm**: İnternet bağlantınızı kontrol edin ve tekrar deneyin.
- **Rate Limit Hatası**:
    - **Hata Mesajı**: `Instagram API talep limitine ulaşıldı.`
    - **Çözüm**: Instagram, API taleplerinde belirli limitler koyar. Bu hatayı alırsanız bir süre bekleyip tekrar deneyin.
- **Gizli Hesap Uyarısı**:
    - **Hata Mesajı**: `Bu hesap gizlidir ve bazı verilere ulaşılamıyor.`
    - **Çözüm**: Gizli hesaplarda beğeni, yorum ve diğer etkileşim verilerine ulaşmak mümkün değildir.

## Programı Geliştirirken Dikkat Edilecekler

- **Hesap Limiti**: Instagram, anonim veya sık talepler sonucunda API limitine ulaşabilir. Çok fazla istek gönderiyorsanız ara vermek gerekebilir.
- **Kütüphane Uyumluluğu**: Programın düzgün çalışması için kullanılan Python kütüphanelerinin güncel olduğundan emin olun.
- **Gizli Hesaplar**: Instagram API, gizli hesaplardan belirli verileri toplamanıza izin vermez. Bu nedenle gizli hesaplar için programda belirli veriler eksik olacaktır.

## İletişim

Programla ilgili herhangi bir sorunuz veya öneriniz varsa, projenin geliştiricisi ile iletişime geçmekten çekinmeyin:

- E-posta: rtoor6660@gmail.com
- Instagram: [vahap_dogann](https://www.instagram.com/vahap_dogann/)
