def arayaSokmaSiralamasi(k):
    for i in range(1,len(k)):    #ilk elemandan bakmaya başlıyoruz
        j = i                    #ilk elemanı kopyalayarak sonrakilere bakacağız cünkü ilk elemanla işlem yaparsak döngü bozuluyor.
        while j > 0 and k[j] < k[j-1]: #solundaki elemanların kücük olacağı şekilde yer değiştirilecek.
            k[j], k[j-1] = k[j-1], k[j] #sağda kalan eleman kücük ise yer değiştirme yapılacak.
            j=j-1 #dizi basina dönülünce döngü kırılacak.
    return k
    
#En iyi durumda başarım n-1 karşılaştırma olacağı için O(n) olacak. (Dizi sıralı ise)
#En kötü durumda O(n^2) olacaktır çünkü tekrar tekrar dizi gezilecek döngü içinde döngü olacaktır.
#Ortalama başarım O(n^2) O(n)'i kapsadığı için O(n^2) olacaktır.
