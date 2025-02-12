Feature: Regras de cancelamento de pedidos

  Scenario: Bloqueio de cancelamento para pedidos acima de R$ 1.000
    Given um pedido no valor de R$ 1.001 foi realizado
    When o usuário tenta cancelar o pedido
    Then o sistema deve bloquear o cancelamento
    And deve exibir uma mensagem informando que o pedido não pode ser cancelado

  Scenario: Cobrança de taxa para cancelamentos após saída para entrega
    Given um pedido foi enviado para entrega
    When o usuário solicita o cancelamento do pedido
    Then o sistema deve aplicar uma taxa de cancelamento
    And deve exibir o valor da taxa ao usuário

  Scenario: Cancelamento permitido para pedidos abaixo de R$ 1.000 antes da saída para entrega
    Given um pedido no valor de R$ 500 foi realizado
    And o pedido ainda não saiu para entrega
    When o usuário solicita o cancelamento
    Then o sistema deve permitir o cancelamento sem taxa
