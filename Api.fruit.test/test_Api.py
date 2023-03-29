# pip3 install requests
import pytest

from mainApi import*

class TestAPI:


    def test_6_all_fruits(self):
        assert Check_how_many_Jsons('https://fruityvice.com/api/fruit/all') > 7

    def test_10_tomato_fat(self):
        assert How_many_nut_values('https://fruityvice.com/api/fruit/tomato','fat') == 0.2

#class TestOther:

    #
    # def test_1_banana(self):
    #     assert Check_status_code(code_site('https://fruityvice.com/api/fruit/banana')) == True
    #
    # def test_2_mazda(self):
    #     assert Check_status_code(code_site('https://fruityvice.com/api/fruit/Mazda')) == False
    #
    # def test_3_Kiwi(self):
    #     assert Does_it_contain_number('https://fruityvice.com/api/fruit/kiwi', 66, "id") == True
    #
    # def test_4_kiwi(self):
    #     assert Does_it_contain_number('https://fruityvice.com/api/fruit/kiwi', 5, "id") == True
    #
    # def test_5_Kiwi(self):
    #     assert Does_it_contain_value('https://fruityvice.com/api/fruit/kiwi','Solanaceae', 'family')
    #
    # def test_7_mango(self):
    #     assert Check_status_code(code_site('https://fruityvice.com/api/fruit/mango')) == True
    #
    # def test_8_strawberry_id(self):
    #     assert Does_it_contain_number('https://fruityvice.com/api/fruit/strawberry', 3, "id") == True
    #
    # def test_9_strawberry_name(self):
    #     assert Does_it_contain_value('https://fruityvice.com/api/fruit/strawberry', 'Strawberry', 'name') == True
    #
    #
    # def test_11_kiwi_fat(self):
    #     assert How_many_nut_values('https://fruityvice.com/api/fruit/kiwi', 'fat') == 0.5
    #
    # def test_12_mango_calories(self):
    #     assert How_many_nut_values('https://fruityvice.com/api/fruit/mango', 'calories') == 60
