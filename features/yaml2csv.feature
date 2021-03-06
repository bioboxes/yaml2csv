Feature:

  Scenario: Converting a single YAML key-value pair to CSV
    Given I create the file "input.yaml" with the contents:
      """
      ---
      KEY: value
      """
    When I run the command:
      """
      yaml2csv --input input.yaml --output output.csv
      """
    Then the stderr should be empty
    And the exit code should be 0
    And the file "output.csv" should exist
    And the file "output.csv" should contain:
      """
      KEY,value

      """


  Scenario: Converting a multiple YAML key-value pairs to CSV
    Given I create the file "input.yaml" with the contents:
      """
      ---
      key_1: value_1
      key_2: value_2
      """
    When I run the command:
      """
      yaml2csv --input input.yaml --output output.csv
      """
    Then the stderr should be empty
    And the exit code should be 0
    And the file "output.csv" should exist
    And the file "output.csv" should contain:
      """
      key_1,value_1
      key_2,value_2

      """

  Scenario: Converting a single nested YAML key-value pair to CSV
    Given I create the file "input.yaml" with the contents:
      """
      ---
      key_1:
        key_2: value_1
      """
    When I run the command:
      """
      yaml2csv --input input.yaml --output output.csv
      """
    Then the stderr should be empty
    And the exit code should be 0
    And the file "output.csv" should exist
    And the file "output.csv" should contain:
      """
      key_1.key_2,value_1

      """


  Scenario: Downcasing the generated output
    Given I create the file "input.yaml" with the contents:
      """
      ---
      Key_1:
        KEY_2: value_1
      """
    When I run the command:
      """
      yaml2csv --input input.yaml --output output.csv --downcase
      """
    Then the stderr should be empty
    And the exit code should be 0
    And the file "output.csv" should exist
    And the file "output.csv" should contain:
      """
      key_1.key_2,value_1

      """

  Scenario: Converting a single YAML key-value pair with spaces
    Given I create the file "input.yaml" with the contents:
      """
      ---
      has  space: value
      """
    When I run the command:
      """
      yaml2csv --input input.yaml --output output.csv --strict-keys
      """
    Then the stderr should be empty
    And the exit code should be 0
    And the file "output.csv" should exist
    And the file "output.csv" should contain:
      """
      has_space,value

      """

  Scenario: Converting a single YAML key-value pair with the '--convert-bools' flag
    Given I create the file "input.yaml" with the contents:
      """
      ---
      key_1: true
      key_2: false
      """
    When I run the command:
      """
      yaml2csv --input input.yaml --output output.csv --convert-bools
      """
    Then the stderr should be empty
    And the exit code should be 0
    And the file "output.csv" should exist
    And the file "output.csv" should contain:
      """
      key_1,1
      key_2,0

      """

  Scenario: Sorting the output
    Given I create the file "input.yaml" with the contents:
      """
      ---
      c: 3
      a: 1
      b: 2
      """
    When I run the command:
      """
      yaml2csv --input input.yaml --output output.csv --sort
      """
    Then the stderr should be empty
    And the exit code should be 0
    And the file "output.csv" should exist
    And the file "output.csv" should contain:
      """
      a,1
      b,2
      c,3

      """
