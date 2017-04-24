def kabarcikSiralama(liste):  
    for sayi in range(len(liste)-1,0,-1):  
        for i in range(sayi):  
            if liste[i]>liste[i+1]:  
                gecici = liste[i]  
                liste[i] = liste[i+1]  
                liste[i+1] = gecici  
  
liste = [14,46,43,27,57,41,45,21,70]  
kabarcikSiralama(liste)  
print(liste)

//3. soruda en iyi durum O(n)'dir.
//Bubble sort ile bu durumu sağlamak mümkündür eğer liste sıralı gelirse n-1 karşılaştırma yapacağı için O(n) olacaktır.
//En kötü durumda ise O(n^2) olacaktır.Başta alacağı elemanı sürekli liste sonuna kadar karşılaştıracaktır.
