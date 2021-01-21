class Question:
    name = ''
    inputType = ''
    mousePositionX = 0
    mousePositionY = 0
    answerAction = ''
    answer = ''

    def __init__(self, name, mouse_x, mouse_y, input_type):
        self.name = name
        self.mousePositionX = mouse_x
        self.mousePositionY = mouse_y
        self.inputType = input_type


class MouseAction:
    MOVE = 'move'
    SCROLL = 'scroll'


class InputType:
    TEXTBOX = 'textbox'
    CHECKBOX = 'checkbox'
    RADIOBUTTON = 'radiobutton'
    BUTTON = 'button'


class QuestionName:
    Q1_EMAIL = 'email'

    Q2_1_MON_MORNING = 'mon_morning'
    Q2_2_MON_MIDDAY = 'mon_midday'
    Q2_3_MON_AFTERNOON = 'mon_afternoon'
    Q2_4_MON_EVENING = 'mon_evening'

    Q3_1_TUE_MORNING = 'tue_morning'
    Q3_2_TUE_MIDDAY = 'tue_midday'
    Q3_3_TUE_AFTERNOON = 'tue_afternoon'
    Q3_4_TUE_EVENING = 'tue_evening'

    Q4_1_WED_MORNING = 'wed_morning'
    Q4_2_WED_MIDDAY = 'wed_midday'
    Q4_3_WED_AFTERNOON = 'wed_afternoon'
    Q4_4_WED_EVENING = 'wed_evening'

    Q5_1_THU_MORNING = 'thu_morning'
    Q5_2_THU_MIDDAY = 'thu_midday'
    Q5_3_THU_AFTERNOON = 'thu_afternoon'
    Q5_4_THU_EVENING = 'thu_evening'

    Q6_1_FRI_MORNING = 'fri_morning'
    Q6_2_FRI_MIDDAY = 'fri_midday'
    Q6_3_FRI_AFTERNOON = 'fri_afternoon'
    Q6_4_FRI_EVENING = 'fri_evening'

    Q7_DISCUSSION = 'discussion'

    Q8_ALLERGY = 'allergy'
    Q8_1_ALLERGY_OTHER = 'allergy_other'

    Q9_COMMENT = 'comment'
    Q10_SUBMIT = 'submit'


class MousePosition:
    EMAIL = (664, 586)
    MONDAY = 266
    TUESDAY = 320
    WEDNESDAY = 377
    THURSDAY = 430
    FRIDAY = 484
    MORNING = 837
    MIDDAY = 951
    AFTERNOON = 1070
    EVENING = 1190
    DISCUSS = (664, 270)
    ALLERGY = (664, (416, 457, 496, 533, 575, 617, 655))
    OTHER = (775, 655)
    COMMENT = (664, 836)
    SUBMIT_BTN = (683, 912)


FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSdtL38Ah8vqo9uYLVhraDA4xvGL-5ZhiO2oxHMMtW-QX_0hmg/viewform?usp=sf_link '

CSV_FILE = 'C:\\Users\\1000277417\\PycharmProjects\\HelloWorld\\google_form_path\\find_a_time_list.csv'
WEEKDAYS = ('mon', 'tue', 'wed', 'thu', 'fri')
SESSIONS = ('midday', 'afternoon', 'evening', 'afternoon')
SCROLL_AT_QUESTION = (('mon_morning', -650), ('discussion', -500))

QUESTION_LIST = [
    Question(QuestionName.Q1_EMAIL, MousePosition.EMAIL[0], MousePosition.EMAIL[1], InputType.TEXTBOX),
    Question(QuestionName.Q2_1_MON_MORNING, MousePosition.MORNING, MousePosition.MONDAY, InputType.CHECKBOX),
    Question(QuestionName.Q2_2_MON_MIDDAY, MousePosition.MIDDAY, MousePosition.MONDAY, InputType.CHECKBOX),
    Question(QuestionName.Q2_3_MON_AFTERNOON, MousePosition.AFTERNOON, MousePosition.MONDAY, InputType.CHECKBOX),
    Question(QuestionName.Q2_4_MON_EVENING, MousePosition.EVENING, MousePosition.MONDAY, InputType.CHECKBOX),
    Question(QuestionName.Q3_1_TUE_MORNING, MousePosition.MORNING, MousePosition.TUESDAY, InputType.CHECKBOX),
    Question(QuestionName.Q3_2_TUE_MIDDAY, MousePosition.MIDDAY, MousePosition.TUESDAY, InputType.CHECKBOX),
    Question(QuestionName.Q3_3_TUE_AFTERNOON, MousePosition.AFTERNOON, MousePosition.TUESDAY, InputType.CHECKBOX),
    Question(QuestionName.Q3_4_TUE_EVENING, MousePosition.EVENING, MousePosition.TUESDAY, InputType.CHECKBOX),
    Question(QuestionName.Q4_1_WED_MORNING, MousePosition.MORNING, MousePosition.WEDNESDAY, InputType.CHECKBOX),
    Question(QuestionName.Q4_2_WED_MIDDAY, MousePosition.MIDDAY, MousePosition.WEDNESDAY, InputType.CHECKBOX),
    Question(QuestionName.Q4_3_WED_AFTERNOON, MousePosition.AFTERNOON, MousePosition.WEDNESDAY, InputType.CHECKBOX),
    Question(QuestionName.Q4_4_WED_EVENING, MousePosition.EVENING, MousePosition.WEDNESDAY, InputType.CHECKBOX),
    Question(QuestionName.Q5_1_THU_MORNING, MousePosition.MORNING, MousePosition.THURSDAY, InputType.CHECKBOX),
    Question(QuestionName.Q5_2_THU_MIDDAY, MousePosition.MIDDAY, MousePosition.THURSDAY, InputType.CHECKBOX),
    Question(QuestionName.Q5_3_THU_AFTERNOON, MousePosition.AFTERNOON, MousePosition.THURSDAY, InputType.CHECKBOX),
    Question(QuestionName.Q5_4_THU_EVENING, MousePosition.EVENING, MousePosition.THURSDAY, InputType.CHECKBOX),
    Question(QuestionName.Q6_1_FRI_MORNING, MousePosition.MORNING, MousePosition.FRIDAY, InputType.CHECKBOX),
    Question(QuestionName.Q6_2_FRI_MIDDAY, MousePosition.MIDDAY, MousePosition.FRIDAY, InputType.CHECKBOX),
    Question(QuestionName.Q6_3_FRI_AFTERNOON, MousePosition.AFTERNOON, MousePosition.FRIDAY, InputType.CHECKBOX),
    Question(QuestionName.Q6_4_FRI_EVENING, MousePosition.EVENING, MousePosition.FRIDAY, InputType.CHECKBOX),
    Question(QuestionName.Q7_DISCUSSION, MousePosition.DISCUSS[0], MousePosition.DISCUSS[1], InputType.TEXTBOX),
    Question(QuestionName.Q8_ALLERGY, MousePosition.ALLERGY[0], MousePosition.ALLERGY[1], InputType.RADIOBUTTON),
    Question(QuestionName.Q8_1_ALLERGY_OTHER, MousePosition.OTHER[0], MousePosition.OTHER[1], InputType.TEXTBOX),
    Question(QuestionName.Q9_COMMENT, MousePosition.COMMENT[0], MousePosition.COMMENT[1], InputType.TEXTBOX),
    Question(QuestionName.Q10_SUBMIT, MousePosition.SUBMIT_BTN[0], MousePosition.SUBMIT_BTN[1], InputType.BUTTON)
]
