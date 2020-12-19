from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from logger import LOG


class NoIp:
    def __init__(self, config: dict):
        self.options = self._init_options()
        self.service = self._start_service()
        self.driver = self._connect_driver()
        self.username = config["username"]
        self.password = config["password"]

    def __del__(self):
        if self.driver:
            self.driver.quit()

    def _init_options(self):
        try:
            options = Options()
            options.binary_location = '/usr/bin/chromium-browser'
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--window-size=1200x600')
            return options
        except Exception as e:
            LOG.error(f'failed to init options. {e}')

    def _start_service(self):
        LOG.debug('start chromium-service ...')
        try:
            chromedriver_path = '/usr/lib/chromium/chromedriver'
            service = Service(executable_path=chromedriver_path)
            service.start()
            LOG.debug('started')
            return service
        except Exception as e:
            LOG.error(f'failed to start chromium-service. {e}')

    def _connect_driver(self):
        LOG.debug('connect to webdriver ...')
        try:
            driver = webdriver.Remote(
                self.service.service_url,
                desired_capabilities=self.options.to_capabilities())
            LOG.debug('connected')
            return driver
        except Exception as e:
            LOG.error(f'failed to connect webdriver. {e}')
            return None

    def login(self) -> bool:
        LOG.debug('start login()')
        try:
            self.driver.get('https://www.noip.com/login')

            username_txt = self.driver.find_element_by_name('username')
            username_txt.send_keys(self.username)
            password_txt = self.driver.find_element_by_name('password')
            password_txt.send_keys(self.password)

            login_btn = self.driver.find_element_by_name('Login')
            login_btn.submit()

            LOG.debug('end login()')
            return True
        except Exception as e:
            LOG.error(f'failed to login. {e}')
            return False

    def confirm(self) -> bool:
        LOG.debug('start confirm()')
        try:
            self.driver.get('https://my.noip.com/#!/dynamic-dns')
            # self.browser.save_screenshot('ddns.png')
            try:
                confirm_btn = self.driver.find_element_by_class_name('btn.btn-labeled.btn-confirm')
            except Exception:
                confirm_btn = None

            if confirm_btn:
                confirm_btn.click()
                # self.browser.save_screenshot('confirm.png')
                LOG.info("clicked 'Confirm' button.")
                return True
            else:
                LOG.info("'Confirm' button not found.")
                return True
        except Exception as e:
            LOG.error(f'failed to confirm. {e}')
            return False
