def ikiliArama(liste,eleman):  
    ilk = 0  
    son = len(liste)-1  
    bulundu = False  
    while( ilk<=son and not found):  
        orta = (ilk + son)//2  
        if liste[orta] == eleman :  
            bulundu = True  
        else:  
            if eleman < liste[orta]:  
                ilk = orta - 1  
            else:  
                son = orta + 1   
    return bulundu
    
// Arama işlemini ikiye bölerek yaptığı için ilk başta n/2 daha sonra n/4 daha sonra n/8 şeklinde 
// devam edeceği için başarımı O(logn) olacaktır.
