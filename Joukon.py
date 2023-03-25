from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup
class pg(GridLayout):
    def soma(self, instance):
        try:
            num1 = float(self.number1.text)
            num2 = float(self.number2.text)
            resultado = num1 + num2
            self.show_result(resultado)
        except ValueError:
            self.show_error_message("Digite apenas números nos campos ou digite alguma coisa!")
        
    def subtracao(self, instance):
        try:
            num1 = float(self.number1.text)
            num2 = float(self.number2.text)
            resultado = num1 - num2
            self.show_result(resultado)
        except ValueError:
            self.show_error_message("Digite apenas números nos campos!")
        
    def multiplicacao(self, instance):
        try:
            num1 = float(self.number1.text)
            num2 = float(self.number2.text)
            resultado = num1 * num2
            self.show_result(resultado)
        except ValueError:
            self.show_error_message("Digite apenas números nos campos!")
        
    def divisao(self, instance):
        try:
            num1 = float(self.number1.text)
            num2 = float(self.number2.text)
            resultado = num1 / num2
            self.show_result(resultado)
        except ZeroDivisionError:
            self.show_error_message("Não é possível dividir por zero!")
        except ValueError:
            self.show_error_message("Digite apenas números nos campos!")
    
    def show_result(self, resultado):
        popup = Popup(title='Resultado',
                      content=Label(text=str(resultado)),
                      size_hint=(None, None), size=(200, 100))
        popup.open()
    def show_error_message(self, mensagem):#função do pop up de erro
        popup = Popup(title='Erro',#criação do pop up e definindo o mesmo
                      content=Label(text=mensagem),
                      size_hint=(None, None), size=(500, 100))
        popup.open()    



    def __init__(self, **kwargs):
        super(pg, self).__init__(**kwargs)
        Window.size = (700, 150)# definindo o tamanho da janela
        self.cols = 2 #colunas
        self.rows = 4# numero de linas
        #1 Input e label
        _N1 = Label(text="Digite o primeiro número ->")
        _N1.color = (220, 20, 60, 1)#Crimson
        self.add_widget(_N1)
        self.number1 = TextInput(multiline=False)
        self.add_widget(self.number1)
        #2 Input e label
        _N2 = Label(text="Digite o segundo número ->")
        _N2.color = (220, 20, 60, 1)#Crimson
        self.add_widget(_N2)
        self.number2 = TextInput(multiline=False)
        self.add_widget(self.number2)
        #butoes das operações.
        btn = Button(text="Soma", on_press=self.soma)
        self.add_widget(btn)
        btn2 = Button(text="Subtração", on_press=self.subtracao)
        self.add_widget(btn2)
        btn3 = Button(text="Multiplicação", on_press=self.multiplicacao)
        self.add_widget(btn3)
        btn4 = Button(text="Divisão", on_press=self.divisao)
        self.add_widget(btn4)
        
class MyApp(App):
    #classe do app quando instanciar vai chamar outra classe
    def build(self):
        return pg()


if __name__ == '__main__':
    MyApp().run()# instanciando o app