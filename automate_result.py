from selenium import webdriver
from tqdm import tqdm

print('------------------Bulk Result Checker (for RTMNU)------------------------')
start_roll_no = int(input("Enter first Roll No. :"))
end_roll_no = int(input("Enter Last Roll No. :"))

#chrome driver define
#browser = webdriver.Chrome("chromedriver.exe")
# browser.get('https://rtmnuresults.org/')
# time.sleep(2)
for roll_no in tqdm(range(start_roll_no,end_roll_no+1,1)):
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get('https://rtmnuresults.org/')
    browser.find_element_by_xpath("//select[@id='ddlselectfaculty']/option[text()='Faculty of Science & Technology']").click()
    browser.find_element_by_xpath("//select[@id='ddlselectexam']/option[text()='B.E. Third Semester (Computer Science & Engineering)[CBS]']").click()
    browser.find_element_by_xpath("//input[@id='txtrollno']").send_keys(roll_no)
    browser.find_element_by_xpath("//input[@id='imgbtnviewmarksheet']").click()

    try:
        alert = browser.switch_to_alert()
        alert.accept()

    except:
        browser.get_screenshot_as_file('result/'+ str(roll_no) + '.png')
    finally:
        browser.close()

