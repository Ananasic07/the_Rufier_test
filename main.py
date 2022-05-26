# Создание и запуск приложения, программирование интерфейса экранов и действий на них

# Здесь должен быть твой код
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class MainScr(Screen):
    def __init__ (self, name='main'):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(size_hint=[0.9,.1])
        layout3 = BoxLayout(size_hint=[0.9,.1])
        layout4 = BoxLayout(size_hint=[1,.7], padding=25)
        txt = 'Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику'+'\n'+ 'вашего здоровья сердечно-сосудистой системы.'
        txt = Label(text= txt, markup = True)
        txt1=Label(text='Введите имя:          ')
        txt2 = Label(text= 'Введите возраст:          ')
        btn = ScrButton(self, direction = 'down', goal = 'two', text='Начать')
        TI = TextInput(text='')
        TI2 = TextInput(text='')
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(txt)
        layout.add_widget(layout4)
        layout2.add_widget(txt1)
        layout3.add_widget(txt2)
        layout2.add_widget(TI)
        layout3.add_widget(TI2)
        layout4.add_widget(btn)
        self.add_widget(layout)

class TwoScr(Screen):
     def __init__ (self, name='two'):
        super().__init__(name=name)
        layout=  BoxLayout(orientation='vertical')
        layout2 = BoxLayout(size_hint=[0.009,.1])
        layout3 = BoxLayout(size_hint=[0.9, .1])
        txt = 'Замерьте пульс в течении 15 секунд.' + '\n' +'Результат запишите в соответствующее поле.'
        txt = Label(text=txt, markup=True)
        txt1 = Label(text='Введите результат:')
        btn = ScrButton(self, direction='left', goal='three', text='Продолжить')
        TI=TextInput(text='')
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(txt)
        layout3.add_widget(txt1)
        layout3.add_widget(TI)
        layout.add_widget(btn)
        self.add_widget(layout)

class ThreeScr(Screen):
    def __init__ (self, name='three'):
        super().__init__(name=name)
        layout =  BoxLayout(orientation='vertical')
        layout2 = BoxLayout(size_hint=[0.09,.1])
        layout3 = BoxLayout(size_hint=[0.9,.1])
        txt=Label(text='Выполните 30 пресиданий за 45 секунд',markup=True)
        btn = ScrButton(self, direction='left',goal='four', text='Продолжить')
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(txt)
        layout.add_widget(btn)
        self.add_widget(layout)

class FourScr(Screen):
    def __init__ (self, name='four'):
        super().__init__(name=name)
        layout =  BoxLayout(orientation='vertical')
        layout2 = BoxLayout(size_hint=[0.9,.1])
        layout3 = BoxLayout(size_hint=[0.9,.1])
        layout4 = BoxLayout(size_hint=[1,.7],padding = 27)
        txt='В течении минуты замерьте пульс 2 раза:\n за первые 15 секунд минуты, затем за последнии 15 секунд.\n Результаты запишите в соответствующие поля'
        txt = Label(text=txt, markup=True )
        txt1 = Label(text= 'Результат:         ')
        txt2 = Label(text= 'Результат после отдыха:         ')
        btn = ScrButton(self, direction='left', goal='five', text='Завершить')
        TI=TextInput(text='')
        TI2=TextInput(text='')
        layout.add_widget(txt)
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(layout4)
        layout2.add_widget(txt1)
        layout3.add_widget(txt2)
        layout2.add_widget(TI)
        layout3.add_widget(TI2)
        layout4.add_widget(btn)
        self.add_widget(layout)

class FiveScr(Screen):
    def __init__ (self, name='five'):
        super().__init__(name=name)
        layout =  BoxLayout(orientation='vertical')
        #txt = Label(text='', markup=True )


        self.add_widget(layout)

class ScrButton(Button):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MyApp(App):
    def build(self):
        sm =ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(TwoScr())
        sm.add_widget(ThreeScr())
        sm.add_widget(FourScr())
        sm.add_widget(FiveScr())
        return sm
app = MyApp()
app.run()

# P=(4*(P1+P2+P3))/10
# if old == 7 or old == 8:
#   if P>=21:
#       print('Низкий')
#   if 20.9>=P>=17:
#       print('Удовлетворительный')


