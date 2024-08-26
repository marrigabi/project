Feature: Autenticação de usuário

  Background:
    Given que o sistema está inicializado

  Scenario: Registrar um novo usuário com sucesso
    When o usuário se registra com o nome "Gabrieli" e senha "senha123"
    Then o sistema deve criar uma conta para "Gabrieli"

  Scenario: Login com credenciais válidas
    Given que o usuário "Gabrieli" está registrado no sistema com a senha "senha123"
    When o usuário faz login com o nome "Gabrieli" e a senha "senha123"
    Then o login deve ser bem-sucedido

  Scenario: Login com credenciais inválidas
    Given que o usuário "Gabrieli" está registrado no sistema com a senha "senha123"
    When o usuário tenta fazer login com o nome "Alice" e a senha "senhaerrada"
    Then o login deve falhar com uma mensagem de erro

  Scenario: Logout de um usuário autenticado
    Given que o usuário "Gabrieli" está autenticado no sistema
    When o usuário faz logout
    Then o usuário deve ser desconectado com sucesso
