from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

T = TypeVar('T')


class BaseScraper(ABC, Generic[T]):
    def __init__(self, headless=True, wait_time=10) -> None:
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("start-maximized") # 숨겨진 HTML 요소들이 있을수도 있기 때문에 maximized 로 사용
        service = ChromeService(executable_path=ChromeDriverManager().install())

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait_time = wait_time

    @abstractmethod
    def scrape(self) -> T:
        pass

    def main(self, page_url: str) -> None:
        try:
            self.driver.get(page_url)
            self.scrape()
        except WebDriverException as e:
            print(f"Error during scraping: {e}")
            self.driver.get_screenshot_as_file("error_screenshot.png")
            with open("error_page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
        finally:
            self.close()

    def open(self, url) -> None:
        self.driver.get(url)

    def close(self) -> None:
        self.driver.quit()

    def wait_for_element(self, by, value):
        try:
            element_present = EC.visibility_of_element_located((by, value))
            WebDriverWait(self.driver, self.wait_time).until(element_present)
        except TimeoutException:
            print(f"Timed out waiting for page to load at {value}")
