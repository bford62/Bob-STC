Feature: Test Ping Functionality
  @demo @XT-141
  Scenario: PING_EXPECTED_TRUE
    Given Spirent config built
    When I try to ping "10.88.48.31"
    Then I expect response "true"
