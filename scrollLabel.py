# Модуль с классом-наследником ScrollView для создания инструкции, у которой при необходимости включается полоса прокрутки

# Здесь должен быть твой код
class ScrollLable(ScrollView):
    def __init__(self, ltext, **kwargs):
        super(). __init__(**kwargs)
        self.lable = Lable(text=ltext, marcup= True, size_hint_y = None, font_size='18sp', halign = 'left', valign='top')
        self.add_widget(self.lable)
        self.lable.bind
