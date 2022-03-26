from selenium import webdriver
# from selenium.webdriver.common.kwarg import kwarg

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    options=options
)
# desired_capabilitiesはSelenium 4で非推奨になったため削除。

# Selenium 経由でブラウザを操作する
driver.get('https://qiita.com')
print(driver.current_url)

# ブラウザを終了する
driver.quit()
