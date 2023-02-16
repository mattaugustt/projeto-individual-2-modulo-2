#Matheus Augusto
#Projeto individual 2 - Módulo 2
#Contratando! 


vagas = {1 : ('Python', 'Programação', 'Desenvolvimento', 'python', 'programação','desenvolvimento'),
         2 : ('Análise de dados', 'Dados', 'SQL', 'análise de dados', 'dados', 'sql')}
         #chaves com as habilidades necessárias com as variações em minusculo e maiusculo.
         
candidatos = {} #armazenamento dos usuários cadastrados
perf_nec1 = {} #usuarios que possuem o perfil necessário para a vaga 1
perf_nec2 = {} #usuarios que possuem o perfil necessário para a vaga 2


#função que faz a adição do curriculo
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
    curriculo = input('Diga quais são suas experiencias/habilidades com as palavras-chave necessárias:\n')
    print('~'*80)
    x = curriculo.split(',')
    for i in x:
      if (vaga == '1') and (i in vagas[1]) and (x.index(i) == 0): #observa a primeira habilidade do candidato
        cont1 += 1
      if (vaga == '1') and (x.index(i) != 0) and (i[1:] in vagas[1]): #observa as outras habilidades do candidato
        cont1 += 1
    
      if cont1 == 3:
        perf_nec1[nome] = (curriculo) #adiciona o candidato com o perfil necessário no dicionário com todos os usuários que 
                                      #cumprem os requisitos da vaga 1
      
    for i in x:
      if (vaga == '2') and (i in vagas[2]) and (x.index(i) == 0): #observa a primeira habilidade do candidato
        cont2 += 1
      if (vaga == '2') and (x.index(i) != 0) and (i[1:] in vagas[2]): #observa as outras habilidades do candidato
        cont2 += 1
    
      if cont2 == 3:
        perf_nec2[nome] = (curriculo) #adiciona o candidato com o perfil necessário no dicionário com todos os usuários que 
                                      #cumprem os requisitos da vaga 2
      
    candidatos[nome] = (vaga, curriculo)
    #adicionam as informações individuais no par chave-valores com as informações do candidato


    
    print('Vaga 1 - necessário: \nPython, Programação e Desenvolvimento. \n\nVaga 2 - necessário: \nAnálise de dados, Dados e SQL\n')
    print('~'*80)
    vaga = input('Para qual vaga deseja se candidatar? (ex: Vaga 1 - digite 1)\n') #atualiza variavel 
    print('~'*80)
    nome = input('Diga qual seu nome:\n') #atualiza variavel
    print('~'*80)



#função que mostra usuários com o perfil necessário para cada vaga
def perf_nec():
  '''Função que conta a quantidade de candidatos que possuem o perfil necessário.'''
  print('Para a vaga 1,', len(perf_nec1.keys()), 'pessoa(s) possue(em) o perfil necessário. Sendo ela(s): \n', perf_nec1)
  print('Para a vaga 2,', len(perf_nec2.keys()), 'pessoa(s) possue(em) o perfil necessário. Sendo ela(s): \n', perf_nec2)



#função que mostra a quantidade de candidatos pra cada vaga
def conta_cand(dicio):
  '''Função que conta a quantidade de candidatos para cada vaga.'''
  conta1 = 0
  conta2 = 0
  for chave,i in dicio.items():
    if '1' in i:
      conta1 += 1
    if '2' in i:
      conta2 +=1
  print('Vaga 1:', conta1, 'inscritos.')
  print('Vaga 2:', conta2, 'inscritos.')


#print(candidatos)   #dicionário com os candidatos e suas informações
#print(perf_nec1)   #dicionário com os candidatos com o perfil necessário na vaga 1
#print(perf_nec2)   #dicionário com os candidatos com o perfil necessário na vaga 2
#conta_cand(candidatos)   #mostra a quantidade de candidatos inscritos em cada uma das vagas
#perf_nec()   #mostra a quantidade de candidatos com o perfil necessário, bem como os candidatos e suas habilidades, para cada vaga
