
from botcity.core import DesktopBot
import time
import pyautogui








class Bot(DesktopBot):
    def action(self, execution=None):
       
        mes=input('Digite o mes da competencia:')
        ano=input('Digite o ano:')
        pyautogui.hotkey('win','d')
        pyautogui.hotkey("win",'r')
        time.sleep(1)
        pyautogui.write(r"C:\Users\TI2\AppData\Roaming\Microsoft\Windows\Start Menu\CORPORATIVO.lnk")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(8)
        while True:
            if self.find("resources/Benner", matching=0.97, waiting_time=10000):
                
                break  
            else:
                self.not_found("resources/Benner")
        pyautogui.click(1166,355)
        time.sleep(2)
        self.kb_type('jefferson.leite')
        self.tab()
        self.kb_type('Edv2110281091@')
        self.enter()
        time.sleep(7)
        if not self.find( "Grupo_Relatorio", matching=0.97, waiting_time=10000):
          self.not_found("Grupo_Relatorio")
        self.double_click()
        time.sleep(1)
        if not self.find( "Comercial_Gerencial", matching=0.97, waiting_time=10000):
           self.not_found("Comercial_Gerencial")
        self.double_click()
        time.sleep(1)
        if not self.find( "Relatorio", matching=0.97, waiting_time=10000):
           self.not_found("Relatorio")
        self.double_click()
        time.sleep(1)
        if not self.find( "FaturamentoxDevolucao", matching=0.97, waiting_time=10000):
           self.not_found("FaturamentoxDevolucao")
        self.click()
        time.sleep(1)
        pyautogui.hotkey('ctrl','r')
        time.sleep(2)
        pyautogui.write(mes)
        pyautogui.write(ano)
        time.sleep(1)
        if not self.find( "Prever", matching=0.97, waiting_time=10000):
            self.not_found("Prever")
        self.click()
        time.sleep(5)
        if not self.find( "Save", matching=0.97, waiting_time=10000):
            self.not_found("Save")
        self.click()
     
        time.sleep(0.8)
        pyautogui.click(291,506)
        time.sleep(1)
        if not self.find( "ok", matching=0.97, waiting_time=10000):
            self.not_found("ok")
        self.click()
        time.sleep(1)
        self.enter()
        time.sleep(2)
        
        pyautogui.hotkey('win','d')
        time.sleep(1)
        self.browse('https://web.whatsapp.com/')
        time.sleep(6)
        if not self.find( "PesquisarConversa", matching=0.97, waiting_time=10000):
           self.not_found("PesquisarConversa")
        self.click()
        self.kb_type('Jefferson Pessoal')
        time.sleep(1)
        self.enter()
        time.sleep(1)
        if not self.find( "Mais", matching=0.97, waiting_time=10000):
            self.not_found("Mais")
        self.click()
        
        if not self.find( "AbriNovoDocumento", matching=0.97, waiting_time=10000):
            self.not_found("AbriNovoDocumento")
        self.click()
        
        time.sleep(1)        
        if not self.find( "AreaTrabalho", matching=0.97, waiting_time=10000):
            self.not_found("AreaTrabalho")
        self.click()
        time.sleep(1)
        if not self.find( "Analise_AreaTrabalho", matching=0.97, waiting_time=10000):
            self.not_found("Analise_AreaTrabalho")
        self.click()
        time.sleep(1)
        self.enter()
        time.sleep(1)
        self.kb_type('Teste do Robo BOT-CAISP')
        time.sleep(1)
        self.enter()
        time.sleep(3)
        pyautogui.hotkey('alt','f4')
        
        
        

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

