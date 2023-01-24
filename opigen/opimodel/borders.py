class BorderStyle:
    NONE = 0
    LINE = 1
    RAISED = 2
    LOWERED = 3
    ETCHED = 4
    RIDGED = 5
    BUTTON_RAISED = 6
    BUTTON_PRESSED = 7
    DOT = 8
    DASH = 9
    DASH_DOT = 10
    DASH_DOT_DOT = 11
    TITLE_BAR = 12
    GROUP_BOX = 13
    ROUND_RECTANGLE_BACKGROUND = 14
    EMPTY = 15


class Border(object):

    def __init__(self, style, width, color, alarm):
        self.alarm = alarm
        self.color = color
        self.style = style
        self.width = width