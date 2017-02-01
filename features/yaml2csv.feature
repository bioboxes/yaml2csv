Feature:

  Scenario: Converting a single YAML key-value pair to CSV
    Given I create the file "input.yaml" with the contents:
      """
      ---
      key: value
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
      key,value

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
