    # DEF
def ler_numeros ():
  while True:
    try:
      dados = [float(x)for x in input().split()]
      if len(dados) != 2:
        print("Ops! Vamos começar apenas com dois números ok?")
      else:
        return dados
    except ValueError:
      print("Ops! Apenas números, não vamos fazer equações hoje haha!")

     # Saudações e escolhas
Nome = input("Olá, para começarmos, digite seu nome:")
print (f"Olá, {Nome} agora podemos iniciar nossas contas básicas")

while True:
 print("\nMas antes eu preciso de saber qual das opções abaixo você gostaria de ver. Escolha uma destas:")
 print("1 - soma")
 print("2 - subtração")
 print("3 - multiplicar")
 print("4 - dividir")
 print("5 - sair")
 opcao = (input("Qual?:"))
 if opcao == "1":    
    # APRESENTAÇÃO DA OPERAÇÃO DE SOMA
  print("Beleza, quer começar pelas fáceis. Então me diga dois números:")
  numeros = ler_numeros()
  soma = numeros[0] + numeros[1] 
  print(f"Muito bem, a conta ja está feita! Veja só: quando juntamos {numeros[0]} palitos com {numeros[1]} palitos, temos exatamente {soma} palitos! Fácil né?") 
    # APRESENTAÇÃO DA OPERAÇÃO DE SUBTRAÇÃO
 elif opcao == "2":
  print("Muito bem... Essa da medo... Medo de acontecer no banco... vamos para a SUBTRAÇÃO! Me diga dois números:")
  numeros = ler_numeros()
  subtracao = numeros[0] - numeros[1]
  print(f"Bem, a subtração já está feita! Veja só: quando tiramos {numeros[0]} palitos de {numeros[1]} palitos, temos {subtracao} palitos! Tranquilo né? O problema é quando acontece com o dinheiro...")

    # APRESENTAÇÃO DA OPERAÇÃO DE MULTIPLICAÇÃO 
 elif opcao == "3":
    print("Essa é um pouco mais difícil, mas se você entendeu as duas primeiras, vai dar certo! oração e dedicação é o segredo. Vamos para a multiplicação! Me diga dois números:")
    numeros = ler_numeros()
    multiplicacao = numeros[0] * numeros[1]
    print(f"Então, aqui já temos a multiplicação prontinha! Olhe aqui: Quando temos {numeros[0]} palitos e contamos estes mesmos palitos {numeros[1]} vezes vamos acabar transformando os palitos em {multiplicacao} palitos!")
    # APRESENTAÇÃO DA OPERAÇÃO DE DIVISÃO
 elif opcao == "4":
   print("Agora sim, aqui a gente vai misturar tudo o que aprendemos! Vamos para a divisão! Me diga dois números:")
   numeros = ler_numeros()
   # ARRUMAR DIVISÃO POR ZERO
   if numeros[0] == 0 or numeros[1] == 0:
     print("EPA EPA!!! Você quer me explodir? Não tem como dividir por zero, se eu tenho 2 palitos e 0 pessoas, eu não posso dividir com ninguém. Vamos tentar de novo, me diga dois números:")
     continue  
   else:
     divisao = numeros [0] / numeros[1]
     print(f"UFA, conseguimos dividir! Mas vai, não foi tão dificil assim né? Olha aqui: se temos {numeros[0]} palitos e queremos dividir estes palitos com {numeros[1]} de amigos, então cada um irá ter {divisao} palitos!")
   # IMPLEMENTAR SAÍDA/"TEM CERTEZA?"  
