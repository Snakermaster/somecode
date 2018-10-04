import time
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
browser.set_window_size(1200,800)
wait = WebDriverWait(browser,10)

TELL = '18781374080'
PASSWD = 'sx252916..'






def login(tell,passwd):
    try:
        # 获取登录页面地址
        browser.get('https://www.zhihu.com/signup?next=%2F')
        # 获取登录按钮
        login_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                     '#root main.App-main div.SignContainer-switch span')))
        # 点击登录按钮切换至登录
        login_btn.click()
        # 获取电话输入框
        input_tell = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#root main.App-main div.SignFlow-account input' )))
        # 传入电话
        input_tell.send_keys(tell)
        time.sleep(5)
        # 获取密码输入框
        input_passwd = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#root main.App-main div.SignFlow-password input')))
        # 传入密码
        input_passwd.send_keys(passwd)
        time.sleep(5)
        # 获取登录按钮
        login = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#root main.App-main button.SignFlow-submitButton')))
        # 点击登录
        time.sleep(5)
        login.click()

        # 获取网页资源
        page_source = browser.page_source
        html = etree.HTML(page_source)
        try:
            s = html.xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/img/@src')
        except:
            s = html.xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[3]/div/span/div/img/@src')

        print(s)


        # 获取验证码图片地址
        # captcha =
        # # 获取验证码
        # captcha = wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR,'')))


    except TimeoutException:
        print('失败')
    # page_source = browser.page_source
    # return page_source
    print('跳转成功')

def main():

    login(TELL,PASSWD)



if __name__ == '__main__':
    main()







