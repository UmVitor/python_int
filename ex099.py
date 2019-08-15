#Faça um programa que tenha uma função chamada maior(), que receba varios
#parametros com valores inteiros
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(* num):
   print('-='*40)
   print ('Analizando os valores passados...')
   print(f'Foram passados {len(num)} valores ao todo.')
   if (len(num) == 0):
       print('O maior valor informado foi 0')
   else:
        m = num[0]   
        for c in range(0,len(num)):
            print(num[c] , end=' ')
            if (num[c] > m):
                    m = num[c]
        print(f'O maior valor informado foi {m}.')
   print('-='*40) 


maior(10,1,0,1)
maior(0,1,1,1,1100,1,1,0)
maior(1,2)
maior()