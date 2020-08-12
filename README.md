# Projeto Django

### Projeto criado para treinar os conceitos aprendidos sobre Django

**Será um sistema de controle de aprendizagem, onde o usuário poderá cadastrar várias matérias que estuda e escreverá na forma de um blog seu aprendizado sobre cada matéria.**

## Objetivos:

**Criar um sistema com 3 páginas HTML sendo:**
- Uma página *base.html* que servirá de base para as demais páginas. Esta deverá conter um cabeçalho e um rodapé com informações sobre o projeto.
- Página inicial contendo um formulário onde o usuário seleciona a matéria que já foi pré-cadastrada, seleciona a data, e escreve em uma caixa de texto o que foi aprendido. Abaixo do formulário, as postagens antigas devem ser apresentadas exibindo as informações passadas em sua criação (matéria, data e registro da aprendizagem).
- Página para cadastro de matérias com um formulário com um único input e um botão.

**Objetivos Específicos:**
- O código deverá ser escrito unicamente em português, evitando-se sempre o uso de acentuações
- As views deverão ser documentadas, mesmo que sejam simples
- Desenvolver uma interface amigável ao usuário, pensando também na responsividade para dispositivos móveis
- Usar views baseadas em funções
- Usar o banco de dados SQLite3
- Cada matéria cadastrada deverá ser uma chave estrangeira dentro do modelo de registro de aprendizagem

**Requisitos para versões de bibliotecas:**
Em projetos anteriores, usei as seguintes libs abaixo, então peço que mantenham-se as seguintes versões caso seja necessário o uso:

```
    beautifulsoup4==4.8.2
    django==2.2.11
    django-bootstrap4==1.1.1
    pytz==2019.3
    soupsieve==2.0
    sqlparse==0.3.1
```