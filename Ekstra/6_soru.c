int indis_al(int i, int *dizi)
{
  int j = 0;
  while(dizi != NULL){
    dizi = dizi->next;
    j++;
    if (i != dizi->dugum){
      continue;
    }else{
      return j-1;
    }
  }
}
//Varsayılan bir bağlı dizi yapısından verilen elemanın indisini arayan koddur.
//Arama işlemi liste uzunluğu kadar sürebileceği için N defa yapılacaktır ve 
//En kötü durumda başarımı O(n) olacaktır.
