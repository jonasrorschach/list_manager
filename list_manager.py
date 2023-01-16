from os import system
from time import sleep



print('Selecione uma opção')




def syscln(tempo):

    sleep(tempo)
    try:
        system('clear')
    except:
        system('cls')



lista = []




while True:

    opcao = input('[I]nserir, [A]pagar ou [L]istar valores da sua lista: ')
    any_lista = any(lista)
    syscln(0)

    
    while True:

        if opcao.upper() == 'I':
            

            n_inserido = input('Quantos itens serão inseridos na lista?[Apenas números são tolerados]: ')

            try:    
                for i in range(0, int(n_inserido)):
                    syscln(0)
                    item = input('Digite o nome do ' + str(i + 1) + 'º Item: ')
                    lista.append(item)
                    
            except:
                print('Não é permitido digitar letras, caracteres especiais ou números com vírgula.')
                break

            print(f'Esses são os itens na sua lista agora {lista}')
            syscln(3)
            break


       
       
        elif opcao.upper() == 'A':

            if any_lista: # se houver algo dentro da lista vai rodar
                apagar = input('Quantos itens serão apagados da lista? ')
                apagar_num = apagar.isnumeric() # se apagar for número será truthy

        
            else:       # se não houver nada dentro da lista vai rodar
                print('Não há nada dentro da lista para ser apagado.') 
                sleep(3)
                break
            
            # try: # coloquei try caso any_lista e apagar_num seja truthy

            if apagar_num:
                apagar_int = int(apagar)
                tamanho_toleravel = len(lista) >= apagar_int
                tamanho_nao_toleravel = len(lista) < apagar_int
                
                if tamanho_toleravel:
                    # · Vou ter que ver qual é o número do iterator dentro da lista para passar para apagar
                    # · A quantidade de itens tem que ser certa, se não o limitador pergunta
                    try:
                        
                        for i in range(0, apagar_int):
                            iter_apagar = input(f'Insira o nome do {i + 1}º que deve ser apagado: ')
                            lista.remove(iter_apagar)
                        print('Todos itens selecionados foram removidos')
                        syscln(2)
                        break
                    
                    except:
                        print('O nome do objeto a ser apagador foi digitado errado. Tente novamente.')


                elif tamanho_nao_toleravel:
                    print('O número que você digitou é maior do que o número de itens dentro da lista. Tente novamente.')
                    syscln(2)
                    break
            
            else:
                print('O valor digitado não é um número. Tente novamente.')
                break


            

            # except:
            #     ...
            


        elif opcao.upper() == 'L':
            
            if any_lista:
                print(f'Esses são todos os itens da sua lista: {lista}')
                syscln(2)

                msg = 'Fim da lista'
                
                for j in range(0, 3):
                    print(msg)
                    msg += '.'
                    syscln(1)
                break



            else:
                print('Ainda não há nada na lista')
                break
            
        else:
            print('Por favor apenas insira uma letra de acordo com o comando.')



    question = input('Quer fazer mais alguma alteração?[S]im ou [N]ão ')
    if question.upper() == 'S':
        syscln(3)
        continue
    
    elif question.upper() == 'N':
        msg = 'Terminando programa'
        
        for i in range(0, 4):
            syscln(1)
            print(msg)
            msg += '.'
        break
    
    else:
        print('Só é permitido "S" para "sim" e "N" para "não". Tente novamente. ')
