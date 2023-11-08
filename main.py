from place_info_scraper import PlaceInfoScraper
from place_listing_scraper import PlaceListingScraper


scraper_info = PlaceInfoScraper(headless=False)
scraper_info.main("https://pcmap.place.naver.com/place/1378910547/home")


scraper_listing = PlaceListingScraper(headless=False)
scraper_listing.main("https://map.naver.com/p/search/%EC%84%9C%EB%A9%B4%20%EA%B3%B5%EB%B0%A9")
