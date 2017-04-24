typedef struct {
  int *dizi;
  size_t kullanilan;
  size_t boyut;
} Dizi;

void diziTanimla(Dizi *a, size_t baslangicBoyutu) {
  a->dizi = (int *)malloc(baslangicBoyutu * sizeof(int));
  a->kullanilan = 0;
  a->boyut = baslangicBoyutu;
}

void diziEkle(Dizi *a, int eleman) {
  //Eger dizi boyutu doldu ise dizi boyutu burada buyutuluyor ve O(1) olan cost'a ek geliyor
  //fakat Amortized analiz kullanılarak burada belli bir seferde 1 kere olusan bu exception indirgeniyor.
  if (a->kullanilan == a->boyut) {
    a->boyut *= 2;
    a->dizi = (int *)realloc(a->dizi, a->boyut * sizeof(int));
  }
  a->dizi[a->kullanilan++] = eleman;
}

void diziYoket(Dizi *a) {
  free(a->dizi);
  a->dizi = NULL;
  a->kullanilan = a->boyut = 0;
}

int main(){
  Dizi a;
  int i;

  diziTanimla(&a, 5);  // Baslangicta 5 eleman ekleniyor.
  for (i = 0; i < 100; i++)
    diziEkle(&a, i);  // Bu noktada otomatik olarak boyut arttırılıyor ve karmasiklik tekrar yer ayırılmasıyla artıyor.
  freeArray(&a);
}

//Karmasiklik dizi boyutu büyümediği durumda O(1)'dir 
//Dizi boyutu büyür ise büyütme işleminde tekrar yer tahsisi işlemi O(n) kadar bir karmaşıklık artımına sebep olur
//fakat bu artım bir istisna olduğu için n+2n/n gibi bir fonksiyonla O(2) olur ve buradan amortized analiz ile O(1) hesaplanır
