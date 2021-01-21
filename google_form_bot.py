import pyautogui
import time
import webbrowser
import csv
import google_form_bot_config as config


def browse_form():
    webbrowser.open(config.FORM_LINK)
    time.sleep(5)


def fill_form():
    with open(config.CSV_FILE, 'r') as data:
        for line in csv.DictReader(data):
            browse_form()
            for question_name, answer in line.items():
                question = next((q for q in config.QUESTION_LIST if q.name == question_name), None)
                if question is not None:
                    answer_question([question.mousePositionX,question.mousePositionY], question.inputType, question.name, answer)


def get_position(input_type, position, answer=''):
    if input_type == config.InputType.RADIOBUTTON:
        return position[0], position[1][int(answer)]
    else:
        return position[0], position[1]


def answer_question(position, input_type, question, answer ='', mouse_speeding=0.5, typing_speed=0.1):

    x, y = get_position(input_type, position, answer)

    if question in [i[0] for i in config.SCROLL_AT_QUESTION]:
        pyautogui.scroll(-650)
        time.sleep(1)

    if input_type == config.InputType.CHECKBOX:
        if int(answer) == 1:
            pyautogui.moveTo(x, y, duration=mouse_speeding)
            pyautogui.click()

    elif input_type == config.InputType.RADIOBUTTON:
        pyautogui.moveTo(x, y, duration=mouse_speeding)
        pyautogui.click()

    elif input_type == config.InputType.TEXTBOX:
        pyautogui.moveTo(x, y, duration=mouse_speeding)
        pyautogui.click()

        if answer != '':
            pyautogui.typewrite(answer, typing_speed)
    elif input_type == config.InputType.BUTTON:
        pyautogui.moveTo(x, y, duration=mouse_speeding)
        # pyautogui.click()

    else:
        pyautogui.moveTo(x, y, duration=mouse_speeding)


def main():
    print('Google Form Bot is started.')
    print('Start filling Form....')

    fill_form()

    print('Complete!')


if __name__ == "__main__":
    main()
