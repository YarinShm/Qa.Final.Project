# pip3 install requests
import pytest

from mainApi import*



def test_1_banana():
    assert Check_status_code(code_site('https://fruityvice.com/api/fruit/banana')) == True

def test_2_mazda():
    assert Check_status_code(code_site('https://fruityvice.com/api/fruit/Mazda')) == False

def test_3_Kiwi():
    assert Does_it_contain_number('https://fruityvice.com/api/fruit/kiwi', 66, "id") == True

def test_4_kiwi():
    assert Does_it_contain_number('https://fruityvice.com/api/fruit/kiwi', 5, "id") == True

def test_5_Kiwi():
    assert Does_it_contain_value('https://fruityvice.com/api/fruit/kiwi','Solanaceae', 'family')

def test_6_all_fruits():
    assert Check_how_many_Jsons('https://fruityvice.com/api/fruit/all') > 7

def test_7_mango():
    assert Check_status_code(code_site('https://fruityvice.com/api/fruit/mango')) == True

def test_8_strawberry_id():
    assert Does_it_contain_number('https://fruityvice.com/api/fruit/strawberry', 3, "id") == True

def test_9_strawberry_name():
    assert Does_it_contain_value('https://fruityvice.com/api/fruit/strawberry', 'Strawberry', 'name') == True


def test_10_tomato_fat():
    assert How_many_nut_values('https://fruityvice.com/api/fruit/tomato','fat') == 0.2


def test_11_kiwi_fat():
    assert How_many_nut_values('https://fruityvice.com/api/fruit/kiwi', 'fat') == 0.5

def test_12_mango_calories():
    assert How_many_nut_values('https://fruityvice.com/api/fruit/mango', 'calories') == 60


