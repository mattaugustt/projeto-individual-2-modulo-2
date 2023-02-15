#Matheus Augusto
#Projeto individual 2 - Módulo 2


#Desenvolver um projeto (usando dicionários) que vai gravar
#a quantidade de currículos para aquela vaga e quantas
#pessoas têm as palavras-chave necessárias no currículo. 

#Para isso, nosso código Python vai checar para qual vaga a
#pessoa se inscreveu e o resumo que a pessoa enviou em
#busca dessas informações.


vagas = {1 : ('Python', 'Programação', 'Desenvolvimento', 'python', 'programação','desenvolvimento'),
         2 : ('Análise de dados', 'Dados', 'SQL', 'análise de dados', 'dados', 'sql')}
         #chaves com as variações em minusculo e maiusculo.
         
candidatos = [] #armazenamento dos usuários cadastrados
perf_nec1 = [] #usuarios que possuem o perfil necessário para a vaga 1
perf_nec2 = [] #usuarios que possuem o perfil necessário para a vaga 2

def contratar():
  '''Função que recebe o arquivo txt da minibio do candidato para o processo seletivo.'''
  print('~'*80)
  print('Vaga 1 - necessário: \nPython, Programação e Desenvolvimento. \n\nVaga 2 - necessário: \nAnálise de dados, Dados e SQL\n')
  print('~'*80)
  vaga = input('Para qual vaga deseja se candidatar? (ex: Vaga 1 - digite 1)\n') #vaga pretendida pelo primeiro a ser inserido
  print('~'*80)
  nome = input('Diga qual seu nome:\n')  #nome do primeiro a ser inserido
  print('~'*80)
  while int(vaga) != 0:
    cont1 = 0 #contador de habilidades necessárias à vaga 1
    cont2 = 0 #contador de habilidades necessárias à vaga 2
    candidato = [] #armazenamento do usuário em questão
    print('~'*80)
    curriculo = input('Diga quais são suas experiencias com as palavras-chave necessárias:\n')
    print('~'*80)
    x = curriculo.split(',')
    for i in x:
      if (vaga == '1') and (i in vagas[1]) and (x.index(i) == 0): #observa a primeira habilidade do candidato
        cont1 += 1
      if (vaga == '1') and (x.index(i) != 0) and (i[1:] in vagas[1]): #observa as outras habilidades do candidato
        cont1 += 1
    
      if cont1 == 3:
        perf_nec1.append(nome) #adiciona o candidato com o perfil necessário na lista com todos os usuários que 
                                #cumprem os requisitos da vaga 1
      
    for i in x:
      if (vaga == '2') and (i in vagas[2]) and (x.index(i) == 0): #observa a primeira habilidade do candidato
        cont2 += 1
      if (vaga == '2') and (x.index(i) != 0) and (i[1:] in vagas[2]): #observa as outras habilidades do candidato
        cont2 += 1
    
      if cont2 == 3:
        perf_nec2.append(nome) #adiciona o candidato com o perfil necessário na lista com todos os usuários que 
                                #cumprem os requisitos da vaga 2
      
    candidato.append(nome)
    candidato.append(vaga)
    candidato.append(curriculo) #adicionam as informações individuais na lista com as informações do candidato
    candidatos.append(candidato) #adiciona as informações do candidato na lista com as informações de todos os candidatos

    
    print('Vaga 1 - necessário: \nPython, Programação e Desenvolvimento. \n\nVaga 2 - necessário: \nAnálise de dados, Dados e SQL\n')
    print('~'*80)
    vaga = input('Para qual vaga deseja se candidatar? (ex: Vaga 1 - digite 1)\n') #atualiza variavel 
    print('~'*80)
    nome = input('Diga qual seu nome:\n') #atualiza variavel
    print('~'*80)
  
  '''
  #para leitura do arquivo
  minibio = open(arq, 'r')
  conta = 0
  if (vaga == 1) and ('python' in minibio) and ('programação' in minibio) and ('desenvolvimento' in minibio):
    conta += 1
  
  if (vaga == 2) and ('analise de dados' in minibio) and ('dados' in minibio) and ()


'''


#quantos candidatos tem o perfil necessário.
def perf_nec():
  '''Função que conta a quantidade de candidatos que possuem o perfil necessário.'''
  print('Para a vaga 1,', len(perf_nec1), 'pessoa(s) possue(em) o perfil necessário. Sendo ela(s): \n', perf_nec1)
  print('Para a vaga 2,', len(perf_nec2), 'pessoa(s) possue(em) o perfil necessário. Sendo ela(s): \n', perf_nec2)


#quantos candidatos estão concorrendo a cada vaga específica.
def conta_cand(lista):
  '''Função que conta a quantidade de candidatos para cada vaga.'''
  conta1 = 0
  conta2 = 0
  for i in lista:
    for j in i:
      if j == '1':
        conta1 += 1
      if j == '2':
        conta2 +=1
  print('Vaga 1:', conta1, 'inscritos.')
  print('Vaga 2:', conta2, 'inscritos.')




