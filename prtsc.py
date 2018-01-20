from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'請輸入路徑')
driver.get('http://www.pixiv.net/')
driver.save_screenshot('儲存位置/檔案名稱.png')  # 保存截圖
driver.close()