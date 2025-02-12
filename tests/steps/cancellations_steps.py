# cancellations_steps.py
from behave import given, when, then

# @given('um pedido no valor de R$ {valor} foi realizado')
# def step_pedido_realizado(context, valor):
#     context.pedido = {"valor": valor, "status": "Saiu para entrega"}

# @when('usuário tenta cancelar o pedido')
# def step_cancelamento_pedido(context):
#     if 

@given('um pedido no valor de {valor:d} foi realizado')
def step_impl(context, valor):
    context.pedido = {"valor": valor, "status": "realizado"}

@given('o pedido ainda não saiu para entrega')
def step_impl(context):
    context.pedido["status"] = "pendente"

@given('um pedido foi enviado para entrega')
def step_impl(context):
    context.pedido = {"status": "em entrega"}

@when('o usuário tenta cancelar o pedido')
@when('o usuário solicita o cancelamento do pedido')
def step_impl(context):
    if context.pedido["status"] == "em entrega":
        context.cancelamento = "taxa aplicada"
    elif context.pedido["valor"] > 1000 and context.pedido["status"] == "em entrega":
        context.cancelamento = "bloqueado"
    else:
        context.cancelamento = "permitido"

@then('o sistema deve bloquear o cancelamento')
def step_impl(context):
    assert context.cancelamento == "bloqueado"

@then('deve exibir uma mensagem informando que o pedido não pode ser cancelado')
def step_impl(context):
    assert context.cancelamento == "bloqueado"

@then('o sistema deve aplicar uma taxa de cancelamento')
def step_impl(context):
    assert context.cancelamento == "taxa aplicada"

@then('deve exibir o valor da taxa ao usuário')
def step_impl(context):
    assert context.cancelamento == "taxa aplicada"

@then('o sistema deve permitir o cancelamento sem taxa')
def step_impl(context):
    assert context.cancelamento == "permitido"

@given(u'um pedido no valor de R$ 500 foi realizado')
def step_impl(context):
    context.pedido = {"valor": 500, "status": "realizado"}

@given(u'o pedido esperando para para entrega')
def step_impl(context):
    context.pedido["status"] = "pedente" 

@when(u'o usuário solicita o cancelamento')
def step_impl(context):
    if context.pedido["valor"] <= 1000 and context.pedido["status"] == "pedente":
        context.cancelamento = "permitido"
    else:
        context.cancelamento = "bloqueado"

@then(u'o sistema deve permitir o cancelamento sem a taxa')
def step_impl(context):
    assert context.cancelamento == "permitido"