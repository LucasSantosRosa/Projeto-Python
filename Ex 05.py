from datetime import datetime # importando a biblioteca datetime para trabalhar com data e hora
usuario = "visitante" # variável para armazenar um valor padrão para o nome que será substituído por um novo valor. Assim não perdendo a interação caso saia do submenu sem ter escolhido a opção 1. 
while True:
    inicio =input (f"Oi!!! vamos fazer o seguinte, escolha a opção \n1 - Saudações \n2 - Data e hora atual \n3 - Sair \nDigite aqui a opção escolhida:")
    if inicio == "1":
        print("Opa! Então, queria te conhecer mais! Me diga seu nome:")
        nome = input()
        print(f'Então olá {nome}! Agora quero saber qual comida você mais gosta! Fala pra mim aqui:')
        comida = input()
        usuario = nome + comida # nome de usuário personalizado.
        print(f'hmmm, então é {comida} agora que eu sei, que tal eu te chamar de {usuario}!')
        while True: # loop para ativar um submenu, assim deixando o programa mais fluído, sem a necessidade de reinicar todo o looping fa linha 3.
            inicio2 = input(f'Então {usuario}, o que você gostaria de fazer agora? \n1 - Saber a data e hora atual \n2 - Sair do submenu \nDigite aqui a opção escolhida:')
            if inicio2 == "1":
                data = datetime.now() # obtendo a data e hora atual do S.O
                print (data.strftime(f'Então {usuario}, a data e hora atual é: {"%d/%m/%Y %H:%M:%S"}')) # método "srtftime" para personalizar exibição de data e hora.
            elif inicio2 == "2":
                print(f"Então adeus meu querido usuário {usuario}!")
                break
            else:             
                print("Opção inválida, por favor escolha uma das opções acima já ditas.")            
    elif inicio == "2":
       data = datetime.now() # obtendo a data e hora do S.O
       print (data.strftime(f'Então {usuario}, a data e hora atual é: {"%d/%m/%Y %H:%M:%S"}')) # método "srtftime" para personalizar exibição de data e hora.
    elif inicio == "3":
        print(f"Então adeus meu querido usuário {usuario}!")
        exit() # finaliza o programa caso a opção 3 seja escolhida.         
    else:
        print("Opção inválida, por favor escolha uma das opções acima já ditas.")  