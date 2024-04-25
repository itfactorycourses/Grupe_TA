
# un feature reprezinta o colectie de teste care acopera in general acelasi modul
#  dupa cuvantul cheie Feature: vom scrie o scurta descriere, free text, a ceea ce vrem sa testam

Feature: If the user searches for a product, proper results must be returned according
      to the search criteria and filters

#  atunci cand vrem sa facem un test case scriem cuvantul cheie Scenario: urmat de o scurta descriere
#    a testului pe care urmeaza sa il facem (test condition)

#  Pasii de reproducere se descriu folosind urmatoarele cuvinte cheie:
#  Given = contextul in care se desfasoara actiunea
#  When = pasul de reproducere pe care trebuie sa il executam (putem avea atatea when-uri cate avem nevoie)
#  Then = rezultatul pe care ne asteptam sa il primim atunci cand executam pasii de reproducere

  @T1 @search
  Scenario: Verify that when the user searches for a keyword, the search returns results according to that keyword
    Given I am on magento software testing homepage
    When I click on the search input and I enter "capri" text
    When I click "ENTER"
    Then I should have at least "1" results returned
    Then The search results should have "capri" in the product title




