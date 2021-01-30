from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send message to multiple Moodle users from a group.')
    parser.add_argument('-u', '--username', required=True, help='Moodle username')
    parser.add_argument('-p', '--password', required=True, help='Moodle password')
    parser.add_argument('-l', '--login', required=True, help='Moodle login URL')
    parser.add_argument('-c', '--course', required=True, type=int, help='Moodle course ID')
    parser.add_argument('-g', '--group', required=True, type=int, help='Moodle users group ID')
    parser.add_argument('-m', '--message', required=True, help='Message to send to the users')
    args = parser.parse_args()
    driver = webdriver.Chrome()
    driver.get(args.login)
    element = driver.find_element_by_id('username')
    element.send_keys(args.username)
    element = driver.find_element_by_id('password')
    element.send_keys(args.password)
    element.send_keys(Keys.RETURN)
    driver.get(f'{args.login}/grade/report/grader/index.php?id={args.course}&group={args.group}')
    user_rows = driver.find_elements_by_css_selector('tr.userrow')
    user_ids = [int(user_row.get_attribute('data-uid')) for user_row in user_rows]
    print(user_ids)
    for user_id in user_ids:
        driver.get(f'{args.login}/message/index.php?id={user_id}')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea')))
        driver.execute_script(f'$("textarea")[0].value = "{args.message}"')
        driver.find_element_by_css_selector('button[data-action=send-message]').click()

