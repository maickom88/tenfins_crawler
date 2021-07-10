import logging
import os
from models.event_details_model import EventDetailsModel
from models.event_model import EventModel
from enums.crawler_force import CrawlerForce
from models import Event
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from typing import List
from webdriver_manager.chrome import ChromeDriverManager
import time


class CrawlerRepository:
    def __init__(self, url: str):
        self.url = url

    def getEvents(self, force: CrawlerForce) -> List[EventModel]:
        try:
            driver = configure_set_up_driver()
            driver.get(self.url)
            driver.find_element_by_class_name('-GsjxiNEo_N3LzPTWTZch').click()
            driver = page_down(driver)
            if(force == CrawlerForce.MINIMUM):
                driver = get216(driver)
            if(force == CrawlerForce.MEDIUM):
                driver = get216(driver)
                driver = get216(driver)
            if(force == CrawlerForce.MAX):
                driver = get216(driver)
                driver = get216(driver)
                driver = get216(driver)

            events = driver.find_elements_by_class_name(
                '_2gFU0t87uCmml36Fna9lZu')
            list_events: List[EventModel] = []
            for event in events:
                url = event.find_element_by_class_name(
                    '_3UX9sLQPbNUbfbaigy35li').get_attribute("href")
                title = event.find_element_by_class_name(
                    '_30guAjxdBy0Pk99zTF_aFt').text
                local = event.find_element_by_class_name(
                    '_1iWvR5fnY_ZywNOmtcS95E').text
                hours = event.find_element_by_class_name(
                    '_3RH1_pJ5HhrUeNswZyf8r5').text
                month = event.find_element_by_class_name(
                    '_3kalOIVEhJHQXgHatFoDeJ').text
                day = event.find_element_by_class_name(
                    '_1XNZaAvcDTPpSbzcoV0W3n').text
                image = event.find_element_by_tag_name(
                    'img').get_attribute("src")
                event_model = EventModel(
                    title=title, url=url, local=local, hours=hours, month=month, day=day, image=image)
                list_events.append(event_model)
            return list_events
        except Exception as error:
            logging.exception(
                f"Failed to retrieve details on scraping: {error}")
            raise Exception
        finally:
            driver.quit()

    def getDetailsEvent(self) -> EventDetailsModel:
        try:
            driver = configure_set_up_driver()
            driver.get(self.url)
            try:
                title = driver.find_element_by_class_name(
                    '_2a7MPEB7nHW5q-0UQJsl6T').text
            except:
                title = None
            try:
                description = driver.find_element_by_class_name(
                    '_241_qbENUQasyRr7CHEJmo').text
            except:
                description = None
            try:
                date = driver.find_element_by_class_name(
                    '_1uSR2i2AbCWQwvNtGHdKnz').text
            except:
                date = None
            try:
                address = driver.find_element_by_class_name(
                    '_36ZCsgOz77AokAEvfUegFS').text
            except:
                address = None
            try:
                local = driver.find_element_by_class_name(
                    '_1QjPq2P_9FMrK_-ZPAEgzQ').text
            except:
                local = None
            try:
                hours = driver.find_element_by_class_name(
                    '_1iK6x88EqsupILFxTvC9ip').text
            except:
                hours = None
            try:
                about = driver.find_element_by_class_name(
                    'Wla7qETMG4RlwfQQMTIqx').text
            except:
                about = None
            try:
                image = driver.find_element_by_class_name(
                    '_1tHUGDRLiXm3qKqo5etU7i').find_element_by_tag_name('img').get_attribute('src')
            except:
                image = None
            details = EventDetailsModel(image=image, about=about, hours=hours, local=local,
                                        address=address, date=date, description=description, title=title)
            return details
        except Exception as error:
            logging.debug(
                f"Failed to retrieve details on scraping: {error}")
            raise Exception
        finally:
            driver.quit()


# def configure_set_up_driver() -> WebDriver:
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('window-size=1920x1080')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument('--no-sandbox')
#     return webdriver.Chrome(
#         ChromeDriverManager().install(), options=chrome_options)

#for production
def configure_set_up_driver() -> WebDriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    return webdriver.Chrome(
        executable_path=os.environ.get("CHROMEDRIVER_PATH"),
        options=chrome_options
    )

def get216(driver):
    time.sleep(3)
    driver = page_down(driver)
    time.sleep(3)
    driver = page_down(driver)
    time.sleep(3)
    return driver


def page_down(element):
    script = '''function doScrolling(elementY, duration){
    var startingY = window.pageYOffset;
    var diff = elementY - startingY;
    var start;
    window.requestAnimationFrame(function step(timestamp) {
        if (!start) start = timestamp;
        // Elapsed milliseconds since start of scrolling.
        var time = timestamp - start;
        // Get percent of completion in range [0, 1].
        var percent = Math.min(time / duration, 1);
        window.scrollTo(0, startingY + diff * percent);
        // Proceed with animation as long as we wanted it to.
        if (time < duration) {
        window.requestAnimationFrame(step);
        }
    })
    }
    doScrolling(document.body.scrollHeight, 3000)
    '''

    element.execute_script(script)
    return element
