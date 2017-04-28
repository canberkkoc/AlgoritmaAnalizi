def fib(n):
 if n==1 or n==2:
  return 1
 return fib(n-1)+fib(n-2)

#Her değer için iki koldan n işlem yapılacağı için karmaşıklığı O(2^n)

 
def bellekAra(fn, parametre):
 bellekDizisi = {}
 if parametre not in bellekDizisi:
  bellekDizisi[parametre] = fn(parametre)
  return bellekDizisi[parametre]
  
#Burada bulunan değer tekrar aranmayacağı için her değer için n işlem yapılır
#Böylece karmaşıklığı O(n)

print(bellekAra(fib,10))

# 3x3 matrix
girdi1 = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
girdi2 = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
carpimSonucu = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]



def matrisCarp(a,b,sonuc):
  for i in range(len(a)):
   # iterate through columns of Y
   for j in range(len(b[0])):
       # iterate through rows of Y
       for k in range(len(b)):
           sonuc[i][j] += a[i][k] * b[k][j]
  return sonuc  
#Carpim icin n defa ilk liste n defa 2. liste ve n defa çarpım sonucu dönülecek
#karmaşıklık n.n.n yani O(n^3)'tür
           
print(matrisCarp(girdi1,girdi2,carpimSonucu))
