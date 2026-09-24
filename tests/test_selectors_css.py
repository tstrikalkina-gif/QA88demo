import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



def hide_footer(driver):
    driver.execute_script("document.querySelector('footer').style.display='none'")


def scroll_down(driver, steps: int = 10, pixels: int = 500, pause: float = 0.5) -> None:
    for _ in range(steps):
        ActionChains(driver).scroll_by_amount(0, pixels).perform()
        time.sleep(pause)

class TestSelectorsCSS:
    def test_selectors_css(self, driver):
        time.sleep(2)
        footer = driver.find_element(By.TAG_NAME, 'footer')
        print(footer.tag_name)

# поиск по имени элемента и его атрибуту By.CSS_SELECTOR
        tools = driver.find_element(By.CSS_SELECTOR, "img[src='/assets/Toolsqa-DZdwt2ul.jpg']")
        print(tools.get_attribute('src'))


        driver.find_element(By.CSS_SELECTOR,"a[href='/elements']").click()
        time.sleep(2)

        driver.back()

        #по атрибуту
        driver.find_element(By.CSS_SELECTOR, "[href='/elements']").click()

        #поиск по id
        driver.find_element(By.ID, "item-0").click()
        time.sleep(2)


        driver.find_element(By.CSS_SELECTOR, "#item-0").click()
        time.sleep(2)

        # "item-0"
        # "#item-0"
        # "li#item-0"
        # "li[id='item-0']"
        # "[id='item-0']"

        driver.find_element(By.CSS_SELECTOR, "a[class='router-link']").click()
        time.sleep(2)

        driver.back()

        driver.find_element(By.CSS_SELECTOR, "[class='router-link']").click()
        time.sleep(2)

        driver.back()
        driver.find_element(By.CLASS_NAME, "router-link").click()
        # driver.find_element(By.CLASS_NAME, "btn btn-light ").click() не правильно!! 2 класса
        # driver.find_element(By.CLASS_NAME, "btn").click()  правильно!! 1 класс
        time.sleep(2)

        driver.back()
        #поиск по css по классу сокращение форма записи'.'
        driver.find_element(By.CSS_SELECTOR, ".router-link").click()
        # "router-link"  By.CLASS_NAME
        # ".router-link" By.CSS_SELECTOR через сокращенную форму '.'
        # "a.router-link" By.CSS_SELECTOR tagname и через сокращенную форму '.'
        # "a[class='router-link']" By.CSS_SELECTOR  по  tagname и по аттрибуту
        # "[class='router-link']" By.CSS_SELECTOR  по аттрибуту
        time.sleep(2)

        # input#userName.mr-sm-2.form-control
        driver.find_element(By.CSS_SELECTOR, "input#userName.mr-sm-2.form-control").send_keys("Tamara")
        time.sleep(2)
        driver.back()

        #"div.element-list li:nth-child(5) a"     поиск по пятому ребенку у div

        driver.find_element(By.CSS_SELECTOR, "div.element-list li:nth-child(5) a").click()
        time.sleep(2)
        hide_footer(driver)
        scroll_down(driver)

        driver.find_element(By.CSS_SELECTOR, "div.element-list li:last-child a").click()
        time.sleep(2)


    def test_selectors_css_parts(self, driver):
        time.sleep(2)
        # поиск по части аттрибута By.CSS_SELECTOR
        #div.category-cards>a:nth-child(2)
        driver.find_element(By.CSS_SELECTOR, "div[class*='ory-card']>a:nth-child(2)").click()
        time.sleep(2)
        driver.back()

        # поиск по части аттрибута начинается с  By.CSS_SELECTOR

        driver.find_element(By.CSS_SELECTOR, "div[class^='category']>a:nth-child(2)").click()
        time.sleep(2)
        driver.back()

        # поиск по части аттрибута заканчивается на  By.CSS_SELECTOR
        driver.find_element(By.CSS_SELECTOR, "div[class$='-cards']>a:nth-child(2)").click()
        time.sleep(2)
        # //a[@class='router-link'] By.Xpath
        # a[class='router-link']    By.CSS
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@href='/automation-practice-form']").click()

    def test_selectors_xpath(self, driver):
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@href='/elements']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@href='/text-box']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys("Monkey")
  #//*[@placeholder='Full Name']

 #//form/div[1]/div[2]/input
 #//form/div[2]/div[2]/input

        driver.find_element(By.XPATH, "//form/div[2]/div[2]/input").send_keys("monkey234@gmail.com")
        time.sleep(2)

        #// *[text() = 'Current Address'] /../..// textarea

        driver.find_element(By.XPATH, "//*[text()='Current Address']/../..//textarea").send_keys("Address1")
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id='permanentAddress-wrapper']/div[2]/textarea").send_keys("Address 2")

        driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        div_output = driver.find_element(By.XPATH, "//div[@id='output']")

        assert "Monkey" in div_output.text