# zupedu-empacote-stack-stackpot

## Analisando o cenário para encontrar oportunidades de uso da stackspot
Analisando o cenário para encontrar oportunidades de uso da stackspot

Este grupo de atividades tem como objetivo treinar o seu olhar analítico em cima de um contexto para encontrar oportunidades de uso da StackSpot que possama dar mais padrão e velocidade para o dia a dia de trabalho. Abaixo você encontra o resumo dos objetivos de aprendizagem da seção.

Ser capaz de identificar a necessidade de criação de templates, plugins e stackfiles para um determinado contexto

### Teorias Necessárias
- Visão geral da StackSpot

- Facilitando o entendimento do seu nível de conhecimento dado o contexto que você vive

- O que é e como eu identifico a necessidade de um template?
  - [1.3 O que é um template?](https://www.youtube.com/watch?v=nTxxH2a5nb4&ab_channel=4Zuppers)

- O que é e como eu identifico a necessidade de um plugin?
  - [O que é um plugin?](https://www.youtube.com/watch?v=p8q0-LdrSZ0&ab_channel=4Zuppers)

- O que é e como eu identifico a necessidade de um stackfile?
  - [O que é um stackfile?](https://www.youtube.com/watch?v=pZrKo1JWzzc&ab_channel=4Zuppers)

- E o que é de fato uma stack?
  - [O que é uma stack?](https://www.youtube.com/watch?v=AmikJ8Zx9d8&ab_channel=4Zuppers)

### Atividades Preparatórias
#### Acompanhe a análise das oportunidades de alguém que já domina a StackSpot

Nessa atividade você vai acompanhar o análise feita em cima de uma aplicação web voltada para educação. Ela é uma aplicação escrita em Java e que utiliza o ecossistema do Spring para dar mais velocidade para a implementação das funcionalidaes.

Não fique preocupado(a) com a stack de tecnologias em si, acompanhe a linha de raciocínio e fique bem atento(a) a tudo que for demonstrado durante o vídeo.

Um detalhe importante, uma vez que você decidiu realizar esta atividade, recomendamos fortemente que você também preencha a avaliação que foi preparada para testar o seu nível de entendimento sobre o que foi explorado.

[Assista agora ao passo ao passo da análise](https://youtu.be/FsSaLtwx_0k)

[Assista agora ao passo ao passo mostrando que pode ser template, plugin e stackfile.](https://youtu.be/FuKpv4ivsAM)

### Atividades Obrigatórias

#### Analise o contexto de um projeto que simula um marketplace e descubra oportunidades de criação de templates, plugins e stackfiles.

Leia a descrição do contexto e identifique o que pode virar template, plugins e stackfiles. Quando tiver clareza, responda a avaliação.

- [https://github.com/zup-academy/materiais-publicos-treinamentos/blob/main/treinamento-criadores-stacks-stackspot/contextos-trabalho.md](https://github.com/zup-academy/materiais-publicos-treinamentos/blob/main/treinamento-criadores-stacks-stackspot/contextos-trabalho.md)

Templates:
- Spring Boot + Java para apis
- Micronaut + Java para apis
- ASP.NET Core + C#
- NextJS para construção de frontends com React
- NestJS para construção de BFFs

Plugins:
- Projeto precisa falar com um postgresql
- Projeto precisa mandar mensagem para nosso kafka.
- Projeto precisa receber mensagem de uma ou mais filas do kafka
- Projeto precisa mandar e consumir informação do cache. No caso utilizamos o redis.
- Projeto precisa seguir a arquitetura de software sugerida pela Clean Architecture
- Projeto precisa habilitar autenticar e autorização usando o que é recomendado internamente.
- De vez em quando tem projeto que precisa falar com o SNS da AWS.

Stackfile:
- Default com Spring Boot + Java
- Default + Postgres
- Default + kafka
- Default + Postgres + Kafka + clean Architecture

#### Analise o contexto de uma documentação relativa a um determinado projeto e descubra as oportunidades de criação de templates, plugins e stackfiles.

Leia a descrição do contexto e identifique o que pode virar template, plugins e stackfiles. Quando tiver clareza, responda a avaliação.
- [https://github.com/zup-academy/materiais-publicos-treinamentos/blob/main/treinamento-criadores-stacks-stackspot/contextos-documentacoes.md](https://github.com/zup-academy/materiais-publicos-treinamentos/blob/main/treinamento-criadores-stacks-stackspot/contextos-documentacoes.md)

## Identificando e construindo templates para facilitar começo de novos projetos
Este grupo de atividades tem o objetivo de exercitar sua capacidade de construir templates utilizando a stackspot para criar estruturas básicas de partidas para novos projetos. Vai ser praticada principalmente a construção de templates parametrizados, que é o caso da vida real mais comum. Além disso, também vamos explorar a criação de templates que precisam executar comandos de setup na máquina em si. Abaixo você encontra o resumo dos objetivos de aprendizagem da seção.

- Em função do olhar analítico sobre um contexto a pessoa tem que ser capaz de criar templates que facilitem o começo de novos projetos
- Ser capaz de parametrizar o template atendendo as necessidades das tecnologias do contexto
- Ser capaz de isolar eventuais tratamentos de inputs em computed inputs para reaproveitá-los dentro das pastas e arquivos do template.
- Ser capaz de criar hooks que permitam a execução de comandos necessários para criação e setups necessários de templates.

### Teorias Necessárias

**1 - Instalação da stackspot**

Para instalar o CLI(command line interface) da StackSpot e deixar seu ambiente preparado(a) para acompanhar as explicações e exercícios é sugerido que você até o site oficial e realize o download. O endereço de acesso é stackspot.com.

[Você também pode acompanhar o passo a passo de download através do vídeo](https://youtu.be/vT9Tll20ZSU)

2 - O que eu preciso saber do Jinja, engine de templates usada pelo CLI da StackSpot

O Jinja é uma engine de templates escrita em Python e foi escolhida para ser a engine de materialização de templates dinâmicos dentro da CLI da StackSpot. É importante descobrir o nível que precisamos saber sobre essa tecnologia de modo a criarmos nossos templates.
- [2.9 - Explicando o nível de entendimento necessário sobre o Jinja, a engine de template da CLI](https://www.youtube.com/watch?v=ltIE6Q2D3fQ&ab_channel=4Zuppers)

3 - Uma leve navegada pelos comandos essenciais para criação de stacks com seus templates, plugins e stackfiles.
- [Navegando pelos comandos da CLI da StackSpot voltados para criação de stacks de aplicações](https://www.youtube.com/watch?v=m9Muu5zRpg8&ab_channel=4Zuppers)

Acompanhe uma explicação sobre os comandos básicos da CLI da StackSpot voltados para a criação de stacks de aplicações.

4 - Como criar e adicionar numa stack o primeiro template
Acompanhe uma explicação sobre como podemos criar templates e adicioná-los a uma stack.
- [Explicação básica sobre como criar um template](https://www.youtube.com/watch?v=JpZhbET8dK4&ab_channel=4Zuppers)
```bash
stk create stack stack-exemplo-explicacao
cd stack-exemplo-explicacao
stk create template template-exemplo
stk create app test-app -p /home/stk/workspace/stack-exemplo-explicacao/template-exemplo
```


## Links
- [Bloom’s Revised Taxonomy](https://www.coloradocollege.edu/other/assessment/how-to-assess-learning/learning-outcomes/blooms-revised-taxonomy.html)
- [Template](https://docs.stackspot.com/docs/getting-started/glossary/#template)
- [Plugin](https://docs.stackspot.com/docs/getting-started/glossary/#plugin)

