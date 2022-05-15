import requests
from bs4 import BeautifulSoup

MENU_URL = "https://www.w-tokyodo.com/neostall/space/lunch/?lunch=%E6%9D%B1%E5%A4%A7%E6%9C%AC%E9%83%B7%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%91%E3%82%B9%E6%9D%91"

r = requests.get(MENU_URL)
soup = BeautifulSoup(r.text, "html.parser")
data = soup.select(selector=".cnt_tabs_inner li")
todays_data = data[0]

truck_places = [place.getText() for place in todays_data.find_all(name="h4", class_="cnt_ttl02")]
truck_restarants = [restarant.getText() for restarant in todays_data.find_all(name="h4", class_="cnt_archive_lists_ttl")]

menus = todays_data.find_all(name="p")
for menu in menus:
    menu.find(name="span").decompose()

truck_menus = [menu.getText() for menu in menus]