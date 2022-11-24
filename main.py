import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np
import schedule

id = 'your id'
password = 'password'

all_problem = {}

def solve_homework():
    # select first homework
    homework_btn = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(4) > a')
    homework_btn.click()

    # do homework
    problem_cnt = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > table:nth-child(5) > tbody > tr:nth-child(1) > td:nth-child(2)')
    problem_cnt = int(problem_cnt.text)

    i = 1
    while i <= problem_cnt:
        problem = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > form > table:nth-child(' + str(i * 2 - 1) + ') > tbody > tr > td:nth-child(2)').text

        answer_list = []
        wrong_list = []
        if len(all_problem) > 0:
            answer_list = all_problem[problem]['answer']
            wrong_list = all_problem[problem]['wrong']

        print(answer_list)
        print(wrong_list)

        examples = []
        radio_btns = []
        print(i)

        is_horizontal = False
        try:
            temp = browser.find_element(By.CSS_SELECTOR,  'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > form > table:nth-child('+ str (i * 2) + ') > tbody > tr:nth-child(4)')
            is_horizontal = False
        except:
            is_horizontal = True

        if not is_horizontal:
            for t in range(1, 5):
                examples.append(browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > form > table:nth-child('+ str (i * 2) + ') > tbody > tr:nth-child(' + str(t) + ') > td:nth-child(4)').text)
                radio_btns.append(browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > form > table:nth-child('+ str (i * 2) + ') > tbody > tr:nth-child(' + str(t) + ') > td:nth-child(2) > input[type=radio]'))
        else:
            for t in range(1, 5):
                examples.append(browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > form > table:nth-child(' + str(i * 2) + ') > tbody > tr:nth-child(1) > td:nth-child(' + str(t * 4) + ')').text)
                radio_btns.append(browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > form > table:nth-child(' + str(i * 2) + ') > tbody > tr:nth-child(1) > td:nth-child(' + str(t * 4 - 2) + ') > input[type=radio]'))

        is_find_answer = False
        for radio_btn, example in zip(radio_btns, examples):
            if example in answer_list:
                radio_btn.click()
                is_find_answer = True
                i += 1
                break

        if not is_find_answer:
            for radio_btn, example in zip(radio_btns, examples):
                if example not in wrong_list:
                    radio_btn.click()
                    break
            i += 1

    # while(True):
    # 	pass

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > form > table.normalfont > tbody > tr > td > input[type=submit]')
    submit_btn.click()

    browser.back()

def check_answer():
    past_submissions_btn = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(5) > a')
    past_submissions_btn.click()

    i = 2
    is_submission = True

    while(is_submission):
        try:
            submission_btn = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(3) > b > a')
            submission_btn.click()
        except:
            print('no submission')
            is_submission = False
            break

        problem_cnt = browser.find_element(By.CSS_SELECTOR,'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > table:nth-child(8) > tbody > tr:nth-child(1) > td:nth-child(2)')
        problem_cnt = int(problem_cnt.text)

        j = 1
        num = 16
        problem_list = []
        while j <= problem_cnt:
            problem_info = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > table:nth-child(' + str(num) + ') > tbody > tr > td:nth-child(2)')
            problem_info = problem_info.text

            answer_info = []
            for t in range(1, 5):
                answer_info.append(browser.find_element(By.CSS_SELECTOR,
                                                  'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > table:nth-child(' + str(
                                                      num + 1) + ') > tbody > tr:nth-child(' + str(t) + ') > td:nth-child(3)').text)

            your_answer_info = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > table:nth-child(' + str(num + 2) + ') > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td').text
            answer_list = ['a)', 'b)', 'c)', 'd)']
            ans_cnt = -1
            for k, answer in enumerate(answer_list):
                if answer in your_answer_info:
                    ans_cnt = k

            real_answer_info = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > table:nth-child(3) > tbody > tr > td:nth-child(2) > table:nth-child(' + str(num + 2) + ') > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(3) > td').text
            problem_list.append([problem_info, answer_info[ans_cnt], real_answer_info])

            num = num + 6
            j += 1
        i += 1
        problem_list = np.array(problem_list)

        for problem in problem_list:
            answer = []
            wrong = []
            if problem[2] == 'You have answered the question correctly.':
                answer.append(problem[1])
            elif problem[2] == 'Your answer is incorrect.':
                wrong.append(problem[1])

            try:
                all_problem[problem[0]] = {'answer': answer + all_problem[problem[0]]['answer'],
                                           'wrong': wrong + all_problem[problem[0]]['wrong']}
            except:
                all_problem[problem[0]] = {'answer': answer,
                                           'wrong': wrong}

        browser.back()
    browser.back()

def Process():
    # login process
    global browser
    browser = webdriver.Chrome()
    browser.get("https://www.newgradiance.com/services/servlet/COTC")

    id_input = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > input[type=text]')
    password_input = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input[type=password]')
    login_btn = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td > form > table > tbody > tr:nth-child(6) > td > input[type=image]:nth-child(1)')

    id_input.send_keys(id)
    password_input.send_keys(password)

    login_btn.click()

    # select class
    class_btn = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td.lightbackgroundwithnormalfont > form > table.normalfont > tbody > tr > td:nth-child(1) > a')
    class_btn.click()

    # select homework menu
    homework_menu_btn = browser.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(10) > td > a')
    homework_menu_btn.click()

    check_answer()
    solve_homework()

schedule.every(3).seconds.do(Process)#10분 6초마다 실행 반복
while True:#이벤트 대기
    schedule.run_pending()
    time.sleep(1)