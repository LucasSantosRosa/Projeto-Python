#   SOFTWARE EDUCACIONAL DE NÚMEROS PARES
#   OBJETIVO: APRESENTAR NÚMEROS PARES DE FORMA SIMPLES E INTERATIVA PARA CRIANÇAS
#   AUTOR: LUCAS SANTOS ROSA
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
 # SAUDAÇÕES INTERATIVAS
print("Opa! Então, vamos aprender o que são números pares hoje né? Queria te conhecer mais! Me diga seu nome:")
nome = input()
print(f'Então olá {nome}! Agora quero saber qual comida você mais gosta! Fala pra mim aqui:')
comida = input()
junto = nome + comida
print(f'hmmm, {comida} agora que eu sei, que tal eu vou chamar de {junto}. Bora aprender os números pares juntos {junto}!')

 # VARIÁVEL PARA VERIFICAR SE O NÚMERO É VÁLIDO
# ------------
valido = False
# ------------

 # LEITURA DE NÚMEROS INTEIROS COM TRATAMENTO DE ERRO
while not valido:
 try:
   numero = int(input(f'Me diga um número que seja inteiro (sem nada depois da vírgula) {junto}:'))
   print(f'Legal, agora temos um número inteiro!')
   valido = True
   break 
 except ValueError:  
    print(f'oooopa, este número ta errado {junto}! Ele não é inteiro. Números inteiros são aqueles que não tem nada depois da vírgula, como 1, 2, 3, 4, 5, 18, 20, 100... Vamos tentar de novo {junto}, me diga um número inteiro:')

  
if numero % 2 == 0:
 print(f'Parabéns {junto}! O {numero} é par! Mas... Antes de eu te contar o que é um número par, posso te mostrar algo legal? Responde eu com "sim" ou "não"') 
 
while True:  
  interacao = input().lower()
  if interacao in ["sim", "s", "si", "yes"]:
    print(f'Então {junto}, você gosta de feijão encima ou em baixo?')
    print('Digita "em cima" ou "embaixo" e se for muito diferentão "DO LADOKKK"')  
    resposta = input()
    # VERIFICAR TODOS OS BREAKS PARA VER SE ESTÃO FUNCIONANDO CORRETAMENTE
    if resposta.lower() == "em cima":
       print(f'{junto}, você é, definitivamente, doido... TODOS SABEM QUE EMBAIXO É MELHOR! Mas ta né... Cada um é cada um... Vamo voltar para os pares senão vou explodir minha CPU!')
       break  
    elif resposta.lower() == "embaixo":
       print(f'{junto}, EU TE AMO! Finalmente alguém por aqui que entende que feijão em cima é simplesmente BIZARRO! Você é 10/10, talvez eu te de um prêmio depois, talvez... Bora pro número par')
       break
    # ARRUMAR POIS NÃO APARECEU O PRINT ------------------------------------------------------
    elif resposta.upper() == "do ladokk":
       print(f'Tá... {junto}, você é uma pessoinha diferente... Mas eu acho você um GÊNIO também, porque só um gênio para gostar de feijão do lado... Brincadeira eu também gosto kkkk. Bora pro assunto de principal!')
       break 
    # ---------------------------------------------------------------------------------------
  elif interacao in ["não", "nao" , "n", "no", "not", "nop"]:   
    print(f'Poxa {junto}, seria legal... NEM QUERIA MESMO. Vamos continuar com os pares... aff...')
  else:
    print('Opa... Eu num entendi não, tente de novo ok? Responde só com "sim" ou "não" ai eu te mostro algo legal!')     
#IMPLEMENTAR "ELSE" DE ÍMPAR COM EXPLICAÇÃO!   
  