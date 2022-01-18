Feature: ISBN

  Scenario Outline: ISBN control number
    Given Algorithm
    When <number>
    Then <result>

    Examples:
      | number | result |
      |     '978-3-16-148410-0' |     0 |
      |     '978-92-95055-02-5' |     5 |
      |     '978-3-16-148410-0' |     0 |
      |     '978-83-7181-510-2' |     2 |
      |     '9781861972712'     |     2 |