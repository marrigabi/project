def before_scenario(context, scenario):
    context.authenticated_user = None  # Reseta o estado do usuário autenticado antes de cada cenário

def after_scenario(context, scenario):
    context.authenticated_user = None  # Limpa o estado após cada cenário
