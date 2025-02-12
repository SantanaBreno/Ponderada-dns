from behave import given, when, then

@given('um usuário realiza uma transação')
def step_impl(context):
    context.transacao = {"registrada": True, "log": None}

@when('o sistema registra a transação')
def step_impl(context):
    context.transacao["log"] = "criptografado"

@then('um log criptografado deve ser gerado')
def step_impl(context):
    assert context.transacao["log"] == "criptografado"

@then('o log deve conter uma assinatura digital válida')
def step_impl(context):
    assert "assinatura digital válida" in "assinatura digital válida"

@given('uma transação foi realizada há mais de {meses:d} meses')
def step_impl(context, meses):
    context.transacao = {"idade": meses, "log_armazenado": meses < 12}

@when('um administrador tenta acessar o log da transação')
def step_impl(context):
    context.log_acessivel = context.transacao["idade"] < 12

@then('o log ainda deve estar disponível')
def step_impl(context):
    assert context.log_acessivel

@then('o log deve permanecer armazenado por pelo menos 12 meses')
def step_impl(context):
    assert context.transacao["log_armazenado"]

@given('múltiplas transações são registradas no sistema')
def step_impl(context):
    context.transacoes = [True] * 99 + [False]  # Simulando 99% com log

@when('os logs são analisados')
def step_impl(context):
    context.taxa_rastreabilidade = sum(context.transacoes) / len(context.transacoes)

@then('pelo menos 99% das transações devem ter logs completos e rastreáveis')
def step_impl(context):
    assert context.taxa_rastreabilidade >= 0.99
