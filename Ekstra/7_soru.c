typedef struct Dugum
{
	int veri;
	struct Dugum *baglanti;
}Dugum;
 
node *bas = NULL;

void degistir(Dugum *p1, Dugum*p2)
{
	int gecici = p1->veri;
	p1->veri = p2->veri;
	p2->veri = gecici;
}

void secmeSiralamasi(Dugum *bas)
{
	Dugum *baslangic = head;
	Dugum *capraz;
	Dugum *enKucuk;
	
	while(baslangic->baglanti)
	{
		enKucuk = baslangic;
		capraz = baslangic->baglanti;
		
		while(capraz)
		{
			/* En kücük elemanı bulma*/ 
			if( enKucuk->veri > capraz->veri )
			{
				enKucuk = capraz;
			}
			
			capraz = capraz->baglanti;
		}
		degistir(baslangic,enKucuk);			// En kucuk elemanı baslangica koyma
		baslangic = baslangic->baglanti;
	}
}


//Bu yapıda geçerli olan algoritma ilk elemanı tutup daha kucugu yoksa basa alma seklinde calisir
//En kotu durumda ters siralı olacak ve her seferinde diziyi gezecek ve n^2 islem yapacaktır.
//En kotu durumda basarimi O(n^2) olacaktır.
//En iyi durumda da aynı islemi tekrar edeceği için O(n^2) olacaktır.
