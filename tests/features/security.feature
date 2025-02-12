Feature: Segurança e rastreabilidade das transações

  Scenario: Transações devem ser registradas com logs criptografados
    Given um usuário realiza uma transação
    When o sistema registra a transação
    Then um log criptografado deve ser gerado
    And o log deve conter uma assinatura digital válida

  Scenario: Retenção de logs por no mínimo 12 meses
    Given uma transação foi realizada há mais de 11 meses
    When um administrador tenta acessar o log da transação
    Then o log ainda deve estar disponível
    And o log deve permanecer armazenado por pelo menos 12 meses

  Scenario: Garantia de rastreabilidade em 99% das transações
    Given múltiplas transações são registradas no sistema
    When os logs são analisados
    Then pelo menos 99% das transações devem ter logs completos e rastreáveis
