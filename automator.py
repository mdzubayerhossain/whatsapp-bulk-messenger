import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os

def setup_chrome_options():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--profile-directory=Default")
    options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
    return options

def read_file(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        return f.read()

def get_numbers(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.read().splitlines() if line.strip()]

def send_messages(message, numbers, delay):
    os.system("")
    os.environ["WDM_LOG_LEVEL"] = "0"

    class style:
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

    print(style.BLUE)
    print("**********************************************************")
    print("**********************************************************")
    print("*****                                               ******")
    print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
    print("*****      This tool was built by Anirudh Bagri     ******")
    print("*****           www.github.com/mdzubayerhossain     ******")
    print("*****                                               ******")
    print("**********************************************************")
    print("**********************************************************")
    print(style.RESET)

    print(style.YELLOW + '\nThis is your message-')
    print(style.GREEN + message)
    print("\n" + style.RESET)
    message = quote(message)

    total_number = len(numbers)
    print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)

    options = setup_chrome_options()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    print('Once your browser opens up sign in to web whatsapp')
    driver.get('https://web.whatsapp.com')
    input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)

    for idx, number in enumerate(numbers):
        print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
        try:
            url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
            sent = False
            for i in range(3):
                if not sent:
                    driver.get(url)
                    try:
                        click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                    except Exception as e:
                        print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
                        print("Make sure your phone and computer is connected to the internet.")
                        print("If there is an alert, please dismiss it." + style.RESET)
                    else:
                        sleep(1)
                        click_btn.click()
                        sent = True
                        sleep(3)
                        print(style.GREEN + 'Message sent to: ' + number + style.RESET)
        except Exception as e:
            print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)

    driver.close()

def main():
    parser = argparse.ArgumentParser(description="WhatsApp Bulk Messenger")
    parser.add_argument("message_file", help="Path to the message file")
    parser.add_argument("numbers_file", help="Path to the numbers file")
    parser.add_argument("--delay", type=int, default=30, help="Delay in seconds for waiting elements")

    args = parser.parse_args()

    message = read_file(args.message_file)
    numbers = get_numbers(args.numbers_file)

    send_messages(message, numbers, args.delay)

if __name__ == "__main__":
    main()
