from behave import given, when, then

# Simulação de banco de dados de usuários
users_db = {
    "gabrieli": "senha123",
    "bob": "password456"
}

@given('que o sistema está inicializado')
def step_given_system_initialized(context):
    users_db.clear()  # Limpa o "banco de dados" de usuários para garantir um estado inicial limpo
    # Adiciona alguns usuários iniciais com senha incorreta para "Gabrieli"
    users_db.update({
        "Gabrieli": "wrongpassword",  # Senha errada
    })

@when('o usuário se registra com o nome "{username}" e senha "{password}"')
def step_when_user_registers(context, username, password):
    if username not in users_db:
        users_db[username] = password
        context.registration_success = True
    else:
        context.registration_success = False

@then('o sistema deve criar uma conta para "{username}"')
def step_then_system_creates_account(context, username):
    assert context.registration_success, f"Falha ao registrar o usuário '{username}'"

@given('que o usuário "{username}" está registrado no sistema com a senha "{password}"')
def step_given_user_registered(context, username, password):
    users_db[username] = password

@when('o usuário faz login com o nome "{username}" e a senha "{password}"')
def step_when_user_logs_in(context, username, password):
    stored_password = users_db.get(username)
    if stored_password == password:
        context.login_success = True
        context.authenticated_user = username
    else:
        context.login_success = False

@then('o login deve ser bem-sucedido')
def step_then_login_successful(context):
    assert context.login_success, "Falha no login"

@when('o usuário tenta fazer login com o nome "{username}" e a senha "{password}"')
def step_when_user_attempts_login(context, username, password):
    stored_password = users_db.get(username)
    if stored_password == password:
        context.login_success = True
    else:
        context.login_success = False
        context.error_message = "Credenciais inválidas"

@then('o login deve falhar com uma mensagem de erro')
def step_then_login_fails_with_error(context):
    assert not context.login_success, "Login inesperadamente bem-sucedido"
    assert context.error_message == "Credenciais inválidas", "Mensagem de erro incorreta"

@given('que o usuário "{username}" está autenticado no sistema')
def step_given_user_authenticated(context, username):
    context.authenticated_user = username
    context.login_success = True

@when('o usuário faz logout')
def step_when_user_logs_out(context):
    if hasattr(context, 'authenticated_user'):
        del context.authenticated_user
        context.logout_success = True
    else:
        context.logout_success = False

@then('o usuário deve ser desconectado com sucesso')
def step_then_logout_successful(context):
    assert context.logout_success, "Falha ao desconectar o usuário"
    assert not hasattr(context, 'authenticated_user'), "Usuário ainda está autenticado"
