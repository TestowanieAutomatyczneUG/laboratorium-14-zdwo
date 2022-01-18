Feature: FizzBuzz

  Scenario Outline: FizzBuzz game
    Given FizzBuzz game
    When <number>
    Then <result>

    Examples:
      | number | result |
      |     5 |     Buzz |
      |     7 |     7 |
      |     15 |     FizzBuzz |
      |     20 |      Buzz |
      |     3 |     Fizz |