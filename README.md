# Research_about_Skill_Mining

A small project about skill mining of the Github users. This project is part of a scientific initiation of the University Federal of Minas Gerais.

==============================================================================

**Proposta de estudo semanal:** 

1 Definir 3 perfis-alvo:

  * first user: hitcode47 - Bruno dos Santos Lopes (perfil de pequeno porte - *para testes iniciais*)

  * second user: jesimonbarreto - Amigo (perfil de porte médio - *Adaptação pacotes maiores de dados*)
  
  * third user: CViniciusSDias - Professor do Alura (perfil de grande porte - verificação de desempenho para grandes quantidades de dados)


2 Colher os seguintes dados: 

  * Dados do usuário ****ok****
  * Quantidade de repositórios ****ok****
  * Numero de Commit em cada repositório ...
  * tipos de linguagem usadas ****ok****
  * Quantidade de bytes commitado por linguagem usadas ****ok****
  * Percentual de atividade para cada linguagem ****ok****
  * quantidade de Commit por linguagem ...
  * Horário de cada commit ...
 
4 Objetivos:

  * Definir Liguagem de programação predominante no perfil analisado ****ok****
  * Horário de atuação predominante
  * Salvar os dodos em arquivos separados por nome ****ok****

5 Elaborar documentação:
 
  * PEP 8 – Style Guide for Python Code
  * PEP 257 – Convenções Docstring

6 Problemas:

  * Marcações hexadecimais no arquivo de retorno
  * Arquivo gerador de commits não gera valores

*Relatório de estudo semanal*

questões abertas:
  * Como acessar APIs do github em seu potencial total de informação?
  * Como requisitar em camadas mais profundas dentro das APIs?
  * Como selecionar dados?
  

  #Respostas:

  * As requisções aos serviços de APIs possuem um limite de acordo com as definições estabelecidas pelo servidores. Para aumentar o limite de requisições, uma alternativa é criar um token de acesso. Além disso, APIs estão sujeitas a critérios de privacidade do servidor. Logo, o potencial de acesso é tão grande quanto o servidor permite ou o quanto os usuários disponibilizam ao público.

  * Aparentemente a API rest do github funciona em uma estrutura de camadas de link http. Muito provavelmente seja possível realizar localização de dados por requisição em cadeia.


Uso do Sonarlint
{
  1° Exigiu alterações de nomes de variáveis{
    snake_case --> variáveis e métodos
    CamelCase --> classes 

  }
}