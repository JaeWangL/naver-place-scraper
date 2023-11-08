from base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from place_listing_enums import PlaceInfoClassnamesEnum
from place_listing_models import PlaceListingModel
import time
import re
from typing import List


class PlaceListingScraper(BaseScraper[List[PlaceListingModel]]):
    def scrape(self) -> List[PlaceListingModel]:
        # 검색결과 페이지 이동후 iframe(searchIframe) 컨텐츠가 로딩될때까지 wait
        self.wait_for_element(By.ID, "searchIframe")
        self.driver.switch_to.frame("searchIframe")
        time.sleep(1)

        results_listing: List[PlaceListingModel] = []
        # 한 페이지 당 존재하는 결과 수는 50개로 고정되어 있음
        for i in range(50):
            place = self.driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[2]/div[1]/ul/li[{str(i + 1)}]')
            if place is None:
                # 더 이상의 결과물이 없을시 loop 종료
                break
            place_name = place.find_element(By.CLASS_NAME, PlaceInfoClassnamesEnum.PLACE_NAME.value).text
            thumbnail_container = place.find_element(By.CLASS_NAME, PlaceInfoClassnamesEnum.THUMBNAIL_CONTAINER.value)
            if thumbnail_container is None:
                continue
            thumbnail_tag = thumbnail_container.find_element(By.TAG_NAME, "img")
            thumbnail_url = thumbnail_tag.get_attribute('src')
            self.driver.execute_script("arguments[0].scrollIntoView(true);", place)

            place.click()
            time.sleep(3)

            current_url = self.driver.current_url
            place_id = re.findall(r"place/(\d+)", current_url)
            final_url = 'https://pcmap.place.naver.com/place/' + place_id[0] + '/home'

            results_listing.append(PlaceListingModel(
                place_name=place_name,
                thumbnail_url=thumbnail_url,
                place_id=place_id[0],
                info_url=final_url
            ))

        return results_listing
