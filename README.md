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

5 - Criando templates que precisam ser parametrizados

Poucos templates vão nascer sem a necessidade de nenhum parâmetro. Nesta explicação é demonstrado como definir tais parâmetros e também como utilizar cada um para atender a necessidade do template.
 - [Criando templates que precisam de informações extras do usuário(a)](https://www.youtube.com/watch?v=EO4jCWhaVLA&ab_channel=4Zuppers)
 ```bash
 stk create app teste-aplicacao2 -p /home/stk/workspace/stack-exemplo-explicacao/template-exemplo
 ```

6 - Computando inputs para facilitar a utilização de variáveis e evitar duplicação de lógica

Vão existir situações onde mais de um arquivo precisa da utilização de uma combinação de variáveis de input definidas no template. Sem o devido cuidado isso pode virar duplicação de código dentro do template dificultando sua futura manutenção. Acompanhe uma explicação sobre como isso pode ser resolvido através dos computed_inputs
- [Utilizando computed inputs para evitar duplicação de lógica dentro dos itens do template](https://www.youtube.com/watch?v=pm9_N1t6guM&ab_channel=4Zuppers)
```bash
stk create app teste-aplicacao -p /home/stk/workspace/stack-exemplo-explicacao/template-exemplo
```

7 - Criando templates que exigem instalação de artefatos na máquina como prereq

Para algumas stacks de tecnologias é comum a instalação de artefatos na máquina. Isso acontece muito no mundo Javascript, por exemplo. Alguns projetos sugerem a instalação de binários globais, como o NextJS e o NestJS. A mesma coisa pode acontecer para outros ambientes.
Para que você fique mais preparado(a) criamos uma explicação de como é possível resolver essa necessidade através de hooks.
- [Possibilitando a execução de comandos de setup na máquina durante a materialização do template](https://www.youtube.com/watch?v=oUbEWhKC1Ek&ab_channel=4Zuppers)

8 - Especificando comandos por sistema operacional para os hooks do tipo "run" do template.

Aqui temos uma explicação rápida sobre como indicar comandos equivalentes para sistemas operacionais diferentes na hora de executar um hook do tipo "run".
- [Explicação sobre como especificar a execução de comandos em função do Sistema Operacional](https://www.youtube.com/watch?v=iIvOB1KOeWE&ab_channel=4Zuppers)

9 - Passando por alguns erros que podem acontecer no dia a dia e já ficando mais preparado(a).

A vida não é feita só de acertos e vai ser mais do que normal cometer alguns errinhos durante a execução de comandos, definição de arquivos de templates e utilização de variáveis. Para te deixar um pouquinho mais preparado(a), foi criada uma explicação demonstrando um pouco dos problemas.

- [Passando por alguns erros comuns durante a utilização da CLI](https://www.youtube.com/watch?v=RrFZzF1GTcU&ab_channel=4Zuppers)


```bash
docker run -v $PWD:/root/workdir -it --entrypoint /bin/bash -w /root/workdir  stackspot/stk-cli-ubuntu

docker run -v $PWD:/home/stk -it --entrypoint /bin/bash  stackspot/stk-cli-ubuntu

apt update
apt install curl
apt install git
apt install links

# fonte: https://github.com/stack-spot/stk-cli-action/blob/main/action.yml
curl -fsSL https://stk.stackspot.com/install.sh | bash
mv /home/runner/.stk/bin/* /usr/local/bin
stk -v
stk login <EMAIL_ADDRESS>
```

### Atividades Preparatórias
**Acompanhe a construção de um template para facilitar a construção de novos projetos utilizando Spring Boot.**

O objetivo desta atividade é que você fique mais próximo(a) de conseguir construir seus próprios templates adequados as necessidades do seu contexto.
Para isso você vai acompanhar um passo a passo de criação de uma nova stack voltada para o mundo Spring e de um template que permite criar novos projetos web básicos com Spring Boot. No passo a passo vamos usar a parte de parâmetros, aplicação de tais parâmetros no template e também vamos trabalhar com os computed_inputs para evitar duplicação de lógica.

Ao final deste vídeo você vai precisar responder uma avaliação para verificar se de fato absorveu o que era esperado para dar os próximos passos.

- [Passo a passo criando um template que facilita a criação de projetos com Spring Boot](https://www.youtube.com/watch?v=-e4gireEB-Q&ab_channel=4Zuppers)

**Acompanhe a construção de um template para facilitar a criação de projetos que querem usar o NextJS.**
O objetivo desta atividade é que você fique mais próximo(a) de conseguir construir seus próprios templates adequados as necessidades do seu contexto. Neste caso, explorando a execução de comandos na máquina que são necessários para que o projeto seja criado corretamente.

Em termos de funcionalidades da StackSpot, o passo a passo que vai ser demonstrado usa menos features do que o que foi criado para construir um template para geração de projetos com Spring Boot. Por outro lado vamos explorar o hook do tipo run e executar o comando de criação de aplicações NextJS direto pela CLI da StackSpot.

Ao final deste vídeo você vai precisar responder uma avaliação para verificar se de fato absorveu o que era esperado para dar os próximos passos.
- [Passo a passo criando um template com hook para facilitar a criação de projetos com NextJS](https://www.youtube.com/watch?v=LUvkn91lj50&ab_channel=4Zuppers)

### Atividades Obrigatórias
**Baseado no contexto de um projeto que simula um marketplace, identifique e crie templates que possam ajudar as equipes de engenharia daquele contexto**

[Leia a descrição do contexto](https://github.com/zup-academy/materiais-publicos-treinamentos/blob/main/treinamento-criadores-stacks-stackspot/contextos-trabalho.md) e crie os templates que você entender que fazem sentido.

Após exercitar e criar seus templates, você vai precisar responder uma avaliação para nos contar um pouco dos detalhes do seu processo.

[Resposta do Especialista]

Stack: Spring Boot + Java para apis
Inputs: group id, artifact id, versao(valor default), versao spring boot(valor default) para passar aplicar os valores no pom.xml
ComputedInputs: Pacote e pasta para que eu pudesse usar na geração da estrutura de pastas e também na definição dos pacotes
Hooks: Não foi necessário.


Stack: NextJS para construção de frontends com React
Inputs: apenas usei o nome da app que estava sendo criada
ComputedInputs: Não foi necessário
Hooks: Criei para executar o npx create-next-app para materializar o projeto

**Baseado no contexto de documentações, crie templates que possam ajudar pessoas que utilizam alguma das tecnologias citadas.**
[Leia a descrição do contexto](https://github.com/zup-academy/materiais-publicos-treinamentos/blob/main/treinamento-criadores-stacks-stackspot/contextos-documentacoes.md) e crie os templates que você entender que fazem sentido.

Após exercitar e criar seus templates que facilitam o consumo de uma documentaeção, você vai precisar responder uma avaliação para nos contar um pouco dos detalhes do seu processo.

[Resposta do Especialista]

Documentação: Spring Framework e toda sua stack.

Template padrão: Projeto web padrão
Inputs: descricao do projeto, group id, artifact id e versão. Preciso especificar as informações no pom.xml
ComputedInputs: Criei as variáveis pacote e pasta para materializar corretamente sem precisar de duplicação
Hooks: Não foi necessário

Template padrão: Projeto reativo
Inputs: descricao do projeto, group id, artifact id,versão, lista de opções de servidores possíveis. Preciso especificar as informações no pom.xml. O servidor entra para dar a opção de usar o netty.
ComputedInputs: Criei as variáveis pacote e pasta para materializar corretamente sem precisar de duplicação
Hooks: Não foi necessário

## Identificando e construindo plugins para facilitar configurações iniciais de uma aplicação
Uma situação recorrente em qualquer momento do ciclo de vida de uma aplicação é a necessidade de realizar uma configuração pela primeira vez. Algumas vezes isso acontece no começo do ciclo de vida, como por exemplo realizar a configuração de acesso a um banco de dados. Outras vezes acontece no meio do projeto, por exemplo realizar uma configuração de um determinado sistema de mensageria que passou a ser necessário naquele contexto. Independente do momento citado, a funcionalidade de criação de plugins da StackSpot cai como uma luva para facilitar a realização deste setup. Este grupo de atividades tem o objetivo de exercitar justamente sua capacidade de construir plugins utilizando a stackspot para facilitar criações de configurações extras em cima de projetos sejam eles construídos via templates de stacks da StackSpot ou não. Abaixo você encontra o resumo dos objetivos de aprendizagem da seção.

- Em função do olhar analítico sobre um contexto a pessoa tem que ser capaz de criar plugins que facilitem configurações de tecnologias dentro dos projetos
- Ser capaz de parametrizar o plugin atendendo as necessidades das tecnologias do contexto
- Ser capaz de isolar eventuais tratamentos de inputs em computed inputs para reaproveitá-los dentro das pastas e arquivos do plugin.
- Ser capaz de criar hooks que permitam a execução de comandos necessários para criação e setups necessários dos plugins.

### Teorias Necessárias
1 - Relembrando o conceito de um plugin

Vamos apenas relembrar o conceito original de um plugin dentro da StackSpot. Só que também já precisamos deixar em mente que nem sempre o objetivo original é seguido pelas pessoas que usam seu produto. Confira um pouco mais sobre essa visão nesta explicação.
- [Relembrando o conceito de um plugin](https://www.youtube.com/watch?v=pm5-hMn-1Bc&ab_channel=4Zuppers)

2 - Uma rápida introdução a criação de um plugin

Acompanhe a explicação onde é demonstrada a criação de um plugin bem básico. A ideia é apresentar o comando de criação e a estrutura básica gerada, além das opções iniciais de utilização.
- [Uma rápida introdução a criação de um plugin](https://youtu.be/tLd-7c7TP4E)
```bash
stk create plugin plugin-exemplo
cd teste-aplicacao/
# deve ser utilizado dentro da aplicação
stk apply plugin -p /home/stk/workspace/stack-exemplo-explicacao/plugin-exemplo
```

3 - Expandindo o entendimento sobre hooks. Tipos suportados, momentos de aplicação e os tipos que vamos estudar.

Agora é hora de ter um olhar mais profundo sobre as possibilidades dessa feature que vai acompanhar muito dos plugins que você vai criar, os Hooks. Temos alguns tipos, possibilidades de uso e tudo mais. Acompanhe a explicação com o máximo de atenção, talvez ela seja meio densa.
- [Hooks: Tipos suportados, momentos de aplicação e os tipos que vamos estudar](https://www.youtube.com/watch?v=njEqiBusQtE&ab_channel=4Zuppers)

4 - Demonstrando a criação de hooks em cenários variados

Agora temos mais uma explicação densa, você vai poder ver vários hooks que foram criados utilizando muitas das possibilidades disponíveis.

Vamos explorar os parâmetros, computedInputs, tipos de hooks diferentes etc.

Além disso também é explicado que nem sempre da para fazer um hook que faça 100% do trabalho necessário e talvez nem seja preciso, se você conseguir entregar uns 80% do caminho, já ajuda demais a pessoa que está do outro lado querendo adiantar a vida.

Acompanhe o vídeo para ter uma visão ainda mais clara do que você vai poder fazer.
- [Demonstrando a criação de hooks em cenários variados](https://www.youtube.com/watch?v=f1QQBwPaD7E&ab_channel=4Zuppers)

## Links
- [Bloom’s Revised Taxonomy](https://www.coloradocollege.edu/other/assessment/how-to-assess-learning/learning-outcomes/blooms-revised-taxonomy.html)
- [Template](https://docs.stackspot.com/docs/getting-started/glossary/#template)
- [Plugin](https://docs.stackspot.com/docs/getting-started/glossary/#plugin)

- [Templates com Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/)
