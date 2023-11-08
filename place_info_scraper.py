from base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from place_info_enums import PlaceInfoClassnamesEnum, PlaceInfoXPathsEnum
from place_info_models import PlaceInfoModel


class PlaceInfoScraper(BaseScraper[PlaceInfoModel]):
    def scrape(self) -> PlaceInfoModel:
        # "장소명" 가 나올때까지 wait (상점이름정보가 가장 중요하며, 최상단에 위치하기때문)
        self.wait_for_element(By.XPATH, PlaceInfoXPathsEnum.PLACE_NAME.value)

        place_name = self.driver.find_element(By.XPATH, PlaceInfoXPathsEnum.PLACE_NAME.value).text
        address = self.driver.find_element(By.CLASS_NAME, PlaceInfoClassnamesEnum.ADDRESS.value).text

        open_time = ""
        open_time_more = self.driver.find_element(By.CLASS_NAME, PlaceInfoClassnamesEnum.OPEN_TIME_MORE.value)
        self.driver.execute_script("arguments[0].click();", open_time_more)
        open_time_list = self.driver.find_elements(By.CLASS_NAME, PlaceInfoClassnamesEnum.OPEN_TIME_LIST.value)[1:]
        for w in open_time_list:
            open_time = open_time + w.text + '\n'

        tel_number = self.driver.find_element(By.CLASS_NAME, PlaceInfoClassnamesEnum.TEL_NUMBER.value).text
        description_preview = self.driver.find_element(By.CLASS_NAME, PlaceInfoClassnamesEnum.DESCRIPTION_PREVIEW.value).text
        link_instagram = ""
        external_links_container_el = self.driver.find_element(By.CLASS_NAME, PlaceInfoClassnamesEnum.EXTERNAL_LINKS_CONTAINER.value)
        if external_links_container_el is not None:
            external_links = external_links_container_el.find_elements(By.TAG_NAME, 'a')
            for external_link in external_links:
                if '인스타' in external_link.text:
                    link_instagram = external_link.get_attribute('href')
                    break

        return PlaceInfoModel(
            place_name=place_name,
            address=address,
            open_time=open_time,
            tel_number=tel_number,
            description_preview=description_preview,
            link_instagram=link_instagram,
        )
