---
marp: true
theme: default
class: 
  - lead
backgroundImage:

paginate: true
---

# Testes de Especificação com Behave e Gherkin
### Prof. Dr. Valério Gutemberg
#### :pencil: 
#### :pencil: Testes de Software
:pencil2: Curso de Sistemas para Internet

---

# O que são Testes de Especificação?

Testes de Especificação são uma abordagem de teste que se concentra na verificação do comportamento do
sistema em conformidade com a especificação definida. Utilizando a linguagem Gherkin, esses testes permitem que
casos de uso sejam escritos em uma linguagem simples e compreensível, facilitando a comunicação entre as equipes técnicas e não técnicas.

---

# Vantagens dos Testes de Especificação

- **Clareza na comunicação**: Uso de uma linguagem comum (Gherkin) entre desenvolvedores, testers e stakeholders.
- **Facilita a colaboração**: Requisitos são definidos de forma que todos possam entender e contribuir.
- **Documentação viva**: O código dos testes serve como documentação contínua do sistema.
- **Integração com BDD**: Promove a prática de desenvolvimento orientado a comportamento (Behavior-Driven Development).

---

# Desvantagens dos Testes de Especificação

- **Manutenção dos testes**: Pode ser necessário esforço contínuo para manter os testes atualizados conforme o sistema evolui.
- **Curva de aprendizado**: Ferramentas como Behave e a sintaxe Gherkin podem exigir um período de adaptação.
- **Possível complexidade**: Em sistemas muito grandes, a quantidade de cenários pode se tornar difícil de gerenciar.

---

# Quando Usar Testes de Especificação?

- **Requisitos bem definidos**: Ideal quando os requisitos são claros e podem ser descritos de forma precisa.
- **Desenvolvimento Ágil**: Útil em ambientes que seguem práticas de BDD, onde o comportamento do sistema é fundamental.
- **Equipes multidisciplinares**: Quando é essencial que todos, desde desenvolvedores até stakeholders, entendam os testes.

---

# Quando Não Usar Testes de Especificação?

- **Projetos pequenos ou simples**: Pode não valer a pena o esforço para projetos com poucos requisitos.
- **Falta de clareza nos requisitos**: Se os requisitos ainda estão sendo definidos, os testes podem se tornar obsoletos rapidamente.
- **Pouca familiaridade com BDD**: Se a equipe não está familiarizada com BDD, pode ser melhor começar com testes mais tradicionais.

---

# Ferramentas para Testes de Especificação

## Gherkin

Gherkin é uma linguagem de domínio específico para descrever cenários de teste de uma forma que qualquer pessoa possa entender. Utiliza uma estrutura 
de frases chave como "Dado", "Quando", "Então" para definir as condições do teste.

## Behave

Behave é uma biblioteca Python que permite a execução de testes escritos em Gherkin. 
Ele interpreta os arquivos `.feature` e executa os cenários definidos,
conectando o texto escrito com código Python.

---

# Exemplo de Uso do Behave com Gherkin

1. **Definição de Cenário**: 
   ```gherkin
   Funcionalidade: Buscar Contatos
     Cenário: Usuário busca um contato existente
       Dado que o contato "João" está na lista de contatos
       Quando o usuário busca por "João"
       Então o contato "João" deve ser exibido

Implementação no Behave:


xoxoxoox

2. **Conclusão**
   
Os Testes de Especificação, especialmente com ferramentas como Behave e Gherkin,
 são uma abordagem poderosa para garantir que o software se comporte conforme especificado, promovendo uma colaboração mais efetiva entre todos os envolvidos no projeto.
 Apesar das desvantagens, sua aplicação pode ser crucial em ambientes ágeis e em projetos onde a comunicação clara e a documentação contínua são essenciais.
