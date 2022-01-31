#!/usr/bin/env python3

__version__  =  'v1.0.0-rc2'

dene :
    ithalat  sistemi
     colorama  import  Fore , Style'dan _
    ithalat  _
    bağımsız değişkeni içe  aktar
     rastgele içe aktar
 KeyboardInterrupt hariç :
    print ( '[!] Çıkılıyor.' )
    sistem _ çıkış ()
hariç :
    print ( '[!] Eksik gereksinimler. python3 -m pip install -r gereksinimleri.txt'yi çalıştırmayı deneyin' )
    sistem _ çıkış ()

tanımlı  başlık ():
    yazdır ( " ___ _ _____ __ " )
    yazdır ( " / _ \ |__ ___ _ __ ___ \_ \_ __ / _| ___ __ _ __ _ " )
    yazdır ( " / /_)/ '_ \ / _ \| '_ \ / _ \ / /\/ '_ \| |_ / _ \ / _` |/ _` |" )
    yazdır ( " / ___/| | | | (_) | | | | __/\/ /_ | | | | _| (_) | (_| | (_| |" ) )
    print ( " \/ |_| |_|\___/|_| |_|\___\____/ |_| |_|_| \___/ \__, |\__,_|" )
    yazdır ( " |___/ " )
    print ( " PhoneInfoga Ver. {}" .format ( __version__ ) )
    print ( "Charon IV tarafından kodlanmıştır" )
    yazdır ( " \n " )

afiş ()

eğer  sys . version_info [ 0 ] <  3 :
    print ( " \033 [1m \033 [93m(!) Lütfen aracı Python 3"  +  Stil kullanarak çalıştırın . RESET_ALL )
    sistem _ çıkış ()

ayrıştırıcı  =  argparse . ArgumentParser ( açıklama =
    "Telefon numaraları için gelişmiş bilgi toplama aracı (https://github.com/sundowndev/PhoneInfoga) sürüm {}" . biçim ( __versiyon__ ),
                                 kullanım = '%(prog)s -n <sayı> [seçenekler]' )

ayrıştırıcı _ add_argument ( '-n' , '--sayı' , metavar = 'sayı' , tür = str ,
                    help = 'Taranacak telefon numarası (E164 veya uluslararası format)' )

ayrıştırıcı _ add_argument ( '-i' , '--input' , metavar = "input_file" , type = argparse . FileType ( 'r' ),
                    help = 'Taranacak telefon numarası listesi (her satıra bir tane)' )

ayrıştırıcı _ add_argument ( '-o' , '--output' , metavar = "output_file" , type = argparse . FileType ( 'w' ),
                    help = 'Tarama sonuçlarını kaydetmek için çıktı' )

ayrıştırıcı _ add_argument ( '-s' , '--scanner' , metavar = "tarayıcı" , default = "all" , type = str ,
                    help = 'Kullanılacak tarayıcı' )

ayrıştırıcı _ add_argument ( '--osint' , action = 'store_true' ,
                    help = 'OSINT keşif kullan' )

ayrıştırıcı _ add_argument ( '-u' , '--update' , action = 'store_true' ,
                    help = 'Projeyi güncelle' )

args  =  ayrıştırıcı . parse_args ()

def  resetColors ():
     arg değilse . _  çıktı :
        yazdır ( Stil . RESET_ALL )

# Çıkışta metin rengini sıfırla
atexit . kayıt ol ( resetColors )

# Herhangi bir parametre geçilirse yardım komutunu çalıştırın
 len ( sys . argv ) > 1 değilse : _  
    ayrıştırıcı _ print_help ()
    sistem _ çıkış ()

dene :
    ithalat  zamanı
    ithalat  hashlib
     json'u içe aktar
     yeniden içe aktar
    içe aktarma  istekleri
     urllib3'ü içe aktar
    bs4'ten  BeautifulSoup'u içe  aktarın 
     html5lib'i içe aktar
    telefon numaralarını içe  aktar
     telefon numaralarından  ithalat operatörü 
     telefon numaralarından  coğrafi kodlayıcıyı içe aktar 
     telefon numaralarından  içe aktarma  saat dilimi
 KeyboardInterrupt hariç :
    print ( ' \033 [91m[!] Çıkılıyor.' )
    sistem _ çıkış ()
hariç :
    print ( ' \033 [91m[!] Eksik gereksinimler. python3 -m pip install -r gereksinimleri.txt'yi çalıştırmayı deneyin' )
    sistem _ çıkış ()
istekler . paketler . urllib3 . disable_warnings ()
istekler . paketler . urllib3 . kullan . ssl_ . DEFAULT_CIPHERS  +=  'YÜKSEK:!DH:!aNULL'
dene :
    istekler . paketler . urllib3 . katkıda bulunmak . pyopenssl . DEFAULT_SSL_CIPHER_LIST  +=  'YÜKSEK:!DH:!aNULL'
 AttributeError hariç :
    # pyopenssl desteği kullanılmadı / gerekli / mevcut
    geçmek

eğer  args . güncelleme :
    def  download_file ( url , target_path ):
        yanıt  =  istekler . get ( url , akış = Doğru )
        tanıtıcı  =  açık ( target_path , "wb" )
         yanıt olarak öbek  için . iter_content ( stack_size = 512 ): 
            if  yığın :   # canlı tut yeni parçaları filtrele
                işlemek . yazmak ( parça )

    print ( 'PhoneInfoga güncelleniyor...' )
    print ( 'Gerçek sürüm: {}' .format ( __version__ ) )

    # Son github etiketi alınıyor
    new_version  =  json . yükler ( istekler . get ( 'https://api.github.com/repos/sundowndev/PhoneInfoga/tags' ) içerik )[ 0 ][ 'ad' ]
    print ( 'Son sürüm: {}' .format ( new_version ) )

    osintFiles  = [ 'disposable_num_providers.json' , 'individuals.json' , 'reputation.json' , 'social_medias.json' ]

    dene :
        print ( '[*] OSINT dosyalarının güncellenmesi' )

         osintFiles içindeki dosya  için : 
            url  =  'https://raw.githubusercontent.com/sundowndev/PhoneInfoga/master/osint/{}' . biçim ( dosya )
            çıktı_dizini  =  'osint/{}' . biçim ( dosya )
            download_file ( url , çıktı_dizini )

        print ( '[*] Python betiği güncelleniyor' )
        url  =  'https://raw.githubusercontent.com/sundowndev/PhoneInfoga/master/phoneinfoga.py'
        output_directory  =  'phoneinfoga.py'
        download_file ( url , çıktı_dizini )
    hariç :
        print ( 'Güncelleme başarısız oldu. git pull kullanmayı deneyin.' )
        sistem _ çıkış ()

    print ( 'Araç başarıyla güncellendi.' )
    sistem _ çıkış ()

tarayıcılar  = [ 'herhangi bir' , 'tümü' , 'numverify' , 'ovh' ]

ajan  = []
uagent . ekleme ( "Mozilla/5.0 (uyumlu; MSIE 9.0; Windows NT 6.0) Opera 12.14" )
uagent . ekleme ( "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0" )
uagent . ekleme ( "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3" )
uagent . ekleme ( "Mozilla/5.0 (Windows; U; Windows NT 6.1; tr; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)" )
uagent . ekleme ( "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, Gecko gibi) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7" )
uagent . ekleme ( "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)" )
uagent . ekleme ( "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1" )
uagent . ekleme ( "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0" )

sayı  =  ''  # Tam sayı biçimi
localNumber  =  ''  # Yerel sayı biçimi
InternationalNumber  =  ''  # Uluslararası sayı biçimi
numberCountryCode  =  ''  # Çevirme kodu; örneğin:"+33"
sayıÜlke  =  ''  # Ülke; örneğin: Fransa

googleAbuseToken  =  ''
customFormatting  =  ''

def  search ( req , stop ):
    küresel  google Kötüye Kullanım Simgesi
    küresel  etken

    seçilenUserAgent  =  rastgele . seçim ( agent )
    s  =  istekler . Oturum ()
    başlıklar  = {
        'Kullanıcı Aracısı' : seçilenKullanıcı Aracısı ,
        'Kabul Et' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' ,
        'Accept-Language' : 'en-us, en; q = 0,5' ,
        'Kabul Et-Kodlama' : 'gzip,deflate' ,
        'Kabul Edilen Karakter Seti' : 'ISO-8859-1,utf-8;q=0.7,*;q=0.7' ,
        'Canlı Tut' : '115' ,
        'Bağlantı' : 'canlı tutma' ,
        'Çerez' : 'Çerez: CGIC=Ij90ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjg; ONAY=EVET+RE.fr+20150809-08-0; 1P_JAR=2018-11-28-14; NID = 148 = aSdSHJz71rufCokaUC93nH3H7lOb8E7BNezDWV-PyyiHTXqWK5Y5hsvj7IAzhZAK04-QNTXjYoLXVu_eiAJkiE46DlNn6JjjgCtY-7Fr0I4JaH-PZRb7WFgSTjiFqh0fw2cCWyN69DeP92dzMd572tQW2Z1gPwno3xuPrYC1T64wOud1DjZDhVAZkpk6UkBrU0PBcnLWL7YdL6IbEaCQlAI9BwaxoH_eywPVyS9V; SID=uAYeu3gT23GCz-ktdGInQuOSf-5SSzl3Plw11-CwsEYY0mqJLSiv7tFKeRpB_5iz8SH5lg.; HSID=AZmH_ctAfs0XbWOCJ; SSID=A0PcRJSylWIxJYTq_; APISID=HHB2bKfJ-2ZUL5-R/Ac0GK3qtM8EHkloNw; SAPISID=wQoxetHBpyo4pJKE/A2P6DUM9zGnStpIVt; SIDCC=ABtHo-EhFAa2AJrJIUgRGtRooWyVK0bAwiQ4UgDmKamfe88xOYBXM47FoL5oZaTxR3H-eOp7-rE; OTZ=4671861_52_52_123900_48_436380; OGPC=873035776-8:; OGP=-873035776:;'
    }

    dene :
        URL  =  'https://www.google.com/search?tbs=li:1&q={}&gws_rd=ssl' . biçim ( gereksinim )
        r  =  s . get ( URL  +  googleAbuseToken , başlıklar = başlıklar )

         r iken _ durum_kodu  ==  503 :
            print ( code_warning  +  'Google arama tarafından geçici olarak kara listeye alındınız. Aşağıdaki URL'deki captcha'yı tamamlayın ve GOOGLE_ABUSE_EXEMPTION çerezinin içeriğini kopyalayın/yapıştırın: {}' . format ( URL ))
            print ( ' \n '  +  code_info  +  'Yardıma mı ihtiyacınız var? https://github.com/sundowndev/PhoneInfoga#dealing-with-google-captcha'yı okuyun )
            belirteç  =  giriş ( ' \n GOOGLE_ABUSE_EXEMPTION=' )
            googleAbuseToken  =  '&google_abuse='  +  simge
            r  =  s . get ( URL  +  googleAbuseToken , başlıklar = başlıklar )

        çorba  =  GüzelSoup ( r . içerik , 'html.parser' )
        sonuç  =  çorba . bul ( "div" , id = "arama" ). find_all ( "div" , class_ = "g" )

        bağlantılar  = []
        sayaç  =  0

         sonuçlarda  sonuç için : _ 
            sayaç  +=  1

            if  int ( sayaç ) >  int ( dur ):
                kırmak

            url  =  sonuç . bul ( "a" ). almak ( 'href' )
            url  =  yeniden . alt ( r'(?:\/url\?q\=)' , '' , url )
            url  =  yeniden . alt ( r'(?:\/url\?url\=)' , '' , url )
            url  =  yeniden . alt ( r'(?:\&sa\=)(?:.*)' , '' , url )
            url  =  yeniden . alt ( r'(?:\&rct\=)(?:.*)' , '' , url )

            eğer  yeniden . eşleşme ( r"^(? : \/search\?q\=)" , url ) Yok değil  : 
                url  =  'https://google.com'  +  url

            bağlantılar . ekle ( url )

        dönüş  bağlantıları
    hariç :
        print ( code_error  +  'İstek başarısız oldu. Lütfen yeniden deneyin veya GitHub'da bir sorun açın.' )

def  formatNumber ( InputNumber ):
    geri  dön . sub ( "(?:\+)?(?:[^[0-9]*)" , "" , InputNumber )

def  localScan ( InputNumber ):
    küresel  sayı
    küresel  yerelNumara
    küresel  uluslararasıNumara
    küresel  numaraÜlkeKodu
    küresel  numaraÜlke

    print ( code_info  +  'Yerel tarama çalıştırılıyor...' )

    FormattedPhoneNumber  =  "+"  +  formatNumber ( InputNumber )

    dene :
        PhoneNumberObject  =  telefon numaraları . ayrıştırma ( FormattedPhoneNumber , Yok )
    hariç :
        dönüş  Yanlış
    başka :
         telefon numaraları  değilse . is_valid_number ( PhoneNumberObject ):
            dönüş  Yanlış

        sayı  =  telefon numaraları . format_number ( PhoneNumberObject , telefon numaraları . PhoneNumberFormat . E164 ). değiştir ( '+' , '' )
        numberCountryCode  =  telefon numaraları . format_number ( PhoneNumberObject , telefon numaraları . PhoneNumberFormat . ULUSLARARASI ). böl ( ' ' )[ 0 ]

        countryRequest  =  json . yükler ( request . request ( 'GET' , 'https://restcountries.eu/rest/v2/callingcode/{}' .format ( numberCountryCode . replace ( ' +' , '' ))) içerik )
        numberCountry  =  countryRequest [ 0 ][ 'alpha2Code' ]

        localNumber  =  telefon numaraları . format_number ( PhoneNumberObject , telefon numaraları . PhoneNumberFormat . E164 ). değiştir ( numberCountryCode , '' )
        InternationalNumber  =  telefon numaraları . format_number ( PhoneNumberObject , phonenumbers . PhoneNumberFormat . ULUSLARARASI )

        print ( code_result  +  'Uluslararası biçim: {}' . biçim ( internationalNumber ))
        print ( code_result  +  'Yerel biçim: 0{}' . biçim ( localNumber ))
        print ( code_result  +  'Ülke kodu: {}' .format ( numberCountryCode ) )
        print ( code_result  +  'Location: {}' .format ( geocoder . description_for_number ( PhoneNumberObject , " tr" )))
        print ( code_result  +  'Taşıyıcı: {}' .format ( taşıyıcı . name_for_number ( PhoneNumberObject , ' en ' ) ) )
        print ( code_result  +  'Alan: {}' .format ( geocoder . description_for_number ( PhoneNumberObject , ' en' )))
         timezoneResult  için timezone . _  time_zones_for_number ( PhoneNumberObject ):
           eğer  telefon numaraları . is_possible_number ( PhoneNumberObject ):
            print ( code_info  +  'Sayı geçerli ve mümkün.' )
        başka :
            print ( code_warning  +  'Sayı geçerli ancak mümkün olmayabilir.' )

 tanım numverifyScan ( ):
    küresel  sayı

     arg değilse . _  tarayıcı == 'numverify' ve args değil . tarayıcı == 'tümü' :       
        dönüş  - 1

    yazdır ( code_info  +  'Numverify.com taraması çalıştırılıyor...' )

    requestSecret  =  ''
    cevap  =  istekler . al ( 'https://numverify.com/' )
    çorba  =  BeautifulSoup ( karşılık . metin , "html5lib" )
     Çorbada etiket  için . _  find_all ( "input" , type = "gizli" ):
        if  etiketi [ 'ad' ] ==  "scl_request_secret" :
            requestSecret  =  etiket [ 'değer' ]
            kırmak

    apiKey  =  hashlib . md5 (( sayı  +  requestSecret ). kodlayın ( 'utf-8' )). altılı özet ()

    başlıklar  = {
        'ana bilgisayar' : "numverify.com" ,
        'bağlantı' : "canlı tutma" ,
        'içerik uzunluğu' : "49" ,
        'kabul' : "uygulama/json" ,
        'origin' : "https://numverify.com" ,
        'x-requested-with' : "XMLHttpRequest" ,
        'user-agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, Gecko gibi) Chrome/67.0.3396.99 Safari/537.36" ,
        'content-type' : "multipart/form-data; border=----WebKitFormBoundary7MA4YWxkTrZu0gW" ,
        'yönlendiren' : "https://numverify.com/" ,
        'kabul-kodlama' : "gzip, deflate, br" ,
        'kabul-dil' : "en-US,en;q=0.9,fr;q=0.8,la;q=0.7,es;q=0.6,zh-CN;q=0.5,zh;q=0.4" ,
        'önbellek kontrolü' : "önbellek yok"
    }

    yanıt  =  istekler . request ( "GET" , "https://numverify.com/php_helper_scripts/phone_api.php?secret_key={}&number={}" . biçim ( apiKey , sayı ), veri = "" , başlıklar = başlıklar )

    eğer  cevap . içerik  ==  "Yetkisiz"  veya  yanıt . durum_kodu  !=  200 :
        print (( code_error  +  "API çağrılırken bir hata oluştu (hatalı istek veya yanlış api anahtarı)." ))
        dönüş  - 1

    veri  =  json . yükler ( yanıt . içerik )

    if  data [ "geçerli" ] ==  Yanlış :
        print (( code_error  +  "Hata: Lütfen geçerli bir telefon numarası belirtin. Örnek: +6464806649" ))
        sistem _ çıkış ()

    InternationalNumber  =  '({}){}' . biçim ( veri [ "ülke_ön eki " ], veri [ "yerel_biçim" ])

    print (( code_result  +  "Number: ({}) {}" ) ) format ( data [ "country_prefix" ], data [ "local_format" ]))
    print (( code_result  +  "Ülke: {} ({})" )) format ( data [ "country_name" ], data [ "country_code" ]))
    print (( code_result  +  "Konum: {}" ). format ( data [ "konum" ]))
    yazdır (( code_result  +  "Taşıyıcı: {}" ). biçim ( veri [ "taşıyıcı" ]))
    print (( code_result  +  "Satır tipi: {}" ) .format ( data [ "line_type" ]))
         print ( code_result  +  'Timezone: {}' .format ( timezoneResult ) )

    if  data [ "line_type" ] ==  'sabit hat' :
        print (( code_warning  +  "Bu büyük olasılıkla bir sabit hat, ancak yine de sabit bir VoIP numarası olabilir." ))
    elif  data [ "line_type" ] ==  'mobil' :
        print (( code_warning  +  "Bu büyük olasılıkla bir cep telefonu numarasıdır, ancak yine de bir VoIP numarası olabilir." ))

def  ovhScan ():
    küresel  yerelNumara
    küresel  numaraÜlke

     arg değilse . _  tarayıcı == 'ovh' ve args değil . tarayıcı == 'tümü' :       
        dönüş  - 1

    yazdır ( code_info  +  'OVH taraması çalıştırılıyor...' )

    sorgu dizesi  = { "ülke" : sayıÜlke . alt () }

    başlıklar  = {
        'kabul' : "uygulama/json" ,
        'önbellek kontrolü' : "önbellek yok"
    }

    yanıt  =  istekler . request ( "GET" , "https://api.ovh.com/1.0/telephony/number/detailedZones" , veri = "" , başlıklar = başlıklar , params = sorgu dizesi )

    veri  =  json . yükler ( yanıt . içerik )

     isinstance ise ( veri , liste ):
        requestNumber  =  "0"  +  localNumber . değiştirin ( localNumber [ - 4 :], 'xxxx' )

         verilerdeki voip_number  için : _ 
            if  voip_number [ 'number' ] ==  requestNumber :
                yazdır (( code_info  +  "OVH veritabanında 1 sonuç bulundu" ))
                print (( code_result  +  "Sayı aralığı: {}" .format ( voip_number [ ' sayı' ])))
                print (( code_result  +  "Şehir: {}" .format ( voip_number [ ' şehir' ])))
                print (( code_result  +  "Posta kodu: {}" .format ( voip_number [ ' zipCode' ] ise  voip_number [ 'zipCode' ] Başka Hiçbiri ' ' )  ) )   
                askForExit ()

def  replaceVariables ( string ):
    küresel  sayı
    küresel  uluslararasıNumara
    küresel  yerelNumara

    dizi  =  dizi . değiştir ( '$n' , sayı )
    dizi  =  dizi . replace ( '$i' , InternationalNumber )
    dizi  =  dizi . değiştir ( '$l' , localNumber )

    dönüş  dizesi

def  osintIndividualScan ():
    küresel  sayı
    küresel  uluslararasıNumara
    küresel  numaraÜlkeKodu
    küresel  özelBiçimlendirme

    dorklar  =  json . yükle ( açık ( 'osint/individuals.json' ))

     dork  in  dork için :
         dork [ 'dialCode' ]  Yok ise  veya dork  [ ' dialCode' ] ==  numberCountryCode :
             customFormatting ise :
                dorkRequest  =  replaceVariables ( dork [ 'istek' ]) +  ' | metin:"{}"' . biçim ( özelBiçimlendirme )
            başka :
                dorkRequest  =  replaceVariables ( dork [ 'istek' ])

            print (( code_info  +  "{} ..." üzerinde ayak izleri aranıyor .format ( dork [ 'site' ])))
             arama sonucu  için ( dorkRequest ,  stop = dork [ ' stop' ]):
                eğer  sonuç :
                    yazdır (( code_result  +  "URL: "  +  sonuç ))
        başka :
            dönüş  - 1

def  osintReputationScan ():
    küresel  sayı
    küresel  uluslararasıNumara
    küresel  özelBiçimlendirme

    dorklar  =  json . yükle ( açık ( 'osint/reputation.json' ))

     dork  in  dork için :
         customFormatting ise :
            dorkRequest  =  replaceVariables ( dork [ 'istek' ]) +  ' | metin:"{}"' . biçim ( özelBiçimlendirme )
        başka :
            dorkRequest  =  replaceVariables ( dork [ 'istek' ])

        print (( code_info  +  "Arıyor {}..." .format ( dork [ ' başlık' ])))
         arama sonucu  için ( dorkRequest ,  stop = dork [ ' stop' ]):
            eğer  sonuç :
                yazdır (( code_result  +  "URL: "  +  sonuç ))

def  osintSocialMediaScan ():
    küresel  sayı
    küresel  uluslararasıNumara
    küresel  özelBiçimlendirme

    dorklar  =  json . yükle ( aç ( 'osint/social_medias.json' ))

     dork  in  dork için :
         customFormatting ise :
            dorkRequest  =  replaceVariables ( dork [ 'istek' ]) +  ' | metin:"{}"' . biçim ( özelBiçimlendirme )
        başka :
            dorkRequest  =  replaceVariables ( dork [ 'istek' ])

        print (( code_info  +  "{} ..." üzerinde ayak izleri aranıyor .format ( dork [ 'site' ])))
         arama sonucu  için ( dorkRequest ,  stop = dork [ ' stop' ]):
            eğer  sonuç :
                yazdır (( code_result  +  "URL: "  +  sonuç ))

def  osintDisposableNumScan ():
    küresel  sayı

    dorklar  =  json . yükle ( açık ( 'osint/disposable_num_providers.json' ))

     dork  in  dork için :
        dorkRequest  =  replaceVariables ( dork [ 'istek' ])

        print (( code_info  +  "{} ..." üzerinde ayak izleri aranıyor .format ( dork [ 'site' ])))
         arama sonucu  için ( dorkRequest ,  stop = dork [ ' stop' ]):
            eğer  sonuç :
                print (( code_result  +  "Sonuç bulundu: {}" .format ( dork [ ' site' ])))
                yazdır (( code_result  +  "URL: "  +  sonuç ))
                askForExit ()

def  osintScan ():
    küresel  sayı
    küresel  yerelNumara
    küresel  uluslararasıNumara
    küresel  numaraÜlkeKodu
    küresel  numaraÜlke
    küresel  özelBiçimlendirme

     arg değilse . _  osint :
        dönüş  - 1
    print ( code_info  +  'OSINT ayak izi keşfi çalıştırılıyor...' )

    # Beyaz sayfalar
    print (( code_info  +  "411.com'da tarama URL'si oluşturuluyor..." ))
    print ( code_result  +  "URL'yi tara: https://www.411.com/phone/{}" .format ( internationalNumber . replace ( '+' , '' ). replace ( ' ' , '-' )))

    askCustomPayload  =  input ( code_info  +  'Bu numara için ek bir format kullanmak ister misiniz? (e/H)' )

    Eğer  soruyorCustomPayload  ==  'y'  veya  soruyorCustomPayload  ==  'evet' ise :
        customFormatting  =  input ( code_info  +  'Özel biçim:' )

    yazdır (( code_info  +  '---- Web sayfaları ayak izleri ----' ))

    print (( code_info  +  "Web sayfalarında ayak izleri aranıyor... (limit=5)" ))
     customFormatting ise :
        istek  =  '{} | metin:"{}" | metin:"{}" | metin:"{}"' . biçim ( sayı , sayı , uluslararasıSayı , özelBiçimlendirme )
    başka :
        istek  =  '{} | metin:"{}" | metin:"{}"' . biçim ( sayı , sayı , uluslararasıSayı )
     arama sonucu  için ( req ,  stop = 5 ) :
        eğer  sonuç :
            print (( code_result  +  "Sonuç bulundu: "  +  sonuç ))

    # Belgeler
    print (( code_info  +  "Belgeler aranıyor... (limit=10)" ))
     customFormatting ise :
        istek  =  'iç metin:"{}" | metin:"{}" | metin içi:"{}" dahili:doc | dahili:docx | dahili: odt | dahili:pdf | dahili:rtf | dahili:sxw | dahili:psw | dahili: ppt | dahili:pptx | dahili:pps | dahili: csv | dahili: txt' . biçim ( sayı , uluslararasıSayı , özelBiçimlendirme )
    başka :
        istek  =  'iç metin:"{}" | metin içi:"{}" dahili:doc | dahili:docx | dahili: odt | dahili:pdf | dahili:rtf | dahili:sxw | dahili:psw | dahili: ppt | dahili:pptx | dahili:pps | dahili: csv | dahili: txt' . biçim ( sayı , uluslararasıSayı )
     arama sonucu  için ( '  intext:"{}" | intext:"{}" ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:txt' .format ( sayı , uluslararasıNumber ) , dur = 10 ) :
        eğer  sonuç :
            print (( code_result  +  "Sonuç bulundu: "  +  sonuç ))

    print (( code_info  +  '---- İtibar ayak izleri ----' ))

    osintReputationScan ()

    print (( code_info  +  "scamcallfighters.com'da URL oluşturuluyor..." ))
    yazdır ( code_result  +  'http://www.scamcallfighters.com/search-phone-{}.html' . biçim ( sayı ))

    tmpNumAsk  =  input ( code_info  +  "Geçici numara sağlayıcıların ayak izlerini aramak ister misiniz? (E/n) " )

    eğer  tmpNumAsk . alt () !=  'n'  ve  tmpNumAsk . alt () !=  'hayır' :
        print (( code_info  +  '---- Geçici numara sağlayıcıların ayak izleri ----' ))

        print (( code_info  +  "Tempophone.com'da telefon numarası aranıyor..." ))
        yanıt  =  istekler . istek ( "GET" , "https://tempophone.com/api/v1/phones" )
        veri  =  json . yükler ( yanıt . içerik )
         [ 'nesneler' ] verisindeki voip_number için  : 
            if  voip_number [ 'telefon' ] ==  formatNumber ( sayı ):
                print (( code_result  +  "Geçici bir numara sağlayıcı bulundu: tempophone.com" ) ))
                askForExit ()

        osintDisposableNumScan ()

    print (( code_info  +  '---- Sosyal medya ayak izleri ----' ))

    osintSocialMediaScan ()

    yazdır (( code_info  +  '---- Telefon rehberi ayak izleri ----' ))

    eğer  numberCountryCode  ==  '+1' :
        print (( code_info  +  "Gerçek İnsanlarda URL Oluşturuluyor... " ))
        print ( code_result  +  'https://www.truepeoplesearch.com/results?phoneno={}' .format ( internationalNumber . replace ( ' ' , '' )))

    osintIndividualScan ()

def  askForExit ():
     arg değilse . _  çıktı :
        user_input  =  input ( code_info  +  "Taramaya devam edilsin mi? (e/H) " )

        eğer  user_input . alt () ==  'y'  veya  user_input . alt () ==  'evet' :
            dönüş  - 1
        başka :
            print ( code_info  +  "Güle güle!" )
            sistem _ çıkış ()

def  scanNumber ( InputNumber ):
    print ( code_title  +  "[!] ---- {} ---- [!]" için bilgi alınıyor" .format ( formatNumber ( InputNumber )))

    localScan ( InputNumber )

    küresel  sayı
    küresel  yerelNumara
    küresel  uluslararasıNumara
    küresel  numaraÜlkeKodu
    küresel  numaraÜlke

     numara değilse : _ 
        print (( code_error  +  "Hata: {} sayısı geçerli değil. Atlanıyor." . format ( formatNumber ( InputNumber ))))
        sistem _ çıkış ()

    numverifyScan ()
    ovhScan ()
    osintScan ()

    print ( code_info  +  "Tarama tamamlandı." )

    print ( ' \n '  +  Stil . RESET_ALL )

dene :
    eğer  args . çıktı :
        code_info  =  '[*]'
        code_warning  =  '(!)'
        code_result  =  '[+]'
        code_error  =  '[!]'
        kod_başlığı  =  ''

        eğer  args . osint :
            print ( ' \033 [91m[!] OSINT tarayıcı çıktı seçeneğiyle kullanılamaz (üzgünüm).' )
            sistem _ çıkış ()

        sistem _ stdout  =  argümanlar . çıktı
        afiş ()
    başka :
        code_info  =  Ön . SIFIRLA  +  Stil . PARLAK  +  '[*]'
        code_warning  =  Ön . SARI  +  Stil . PARLAK  +  '(!)'
        code_result  =  Ön . YEŞİL  +  Stil . PARLAK  +  '[+]'
        code_error  =  Ön . KIRMIZI  +  Stil . PARLAK  +  '[!]'
        code_title  =  Ön . SARI  +  Stil . PARLAK

    # Tarayıcı seçeneğini doğrulayın
     arg değilse . _  tarayıcılarda tarayıcı : _  
        print (( code_error  +  "Hata: tarayıcı mevcut değil." ))
        sistem _ çıkış ()

    eğer  args . sayı :
        scanNumber ( bağımsız değişken numarası )
    elif  argo . giriş :
         args'deki satır  için . _  girdi . okuma satırları ():
            taramaNumarası ( satır )

    eğer  args . çıktı :
        arglar . çıktı . kapat ()
 KeyboardInterrupt hariç :
    print (( " \n "  +  code_error  +  "Tarama kesintiye uğradı. Hoşçakalın!" ))
    sistem _ çıkış ()
