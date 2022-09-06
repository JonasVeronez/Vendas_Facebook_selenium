from time import sleep
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint

import pyautogui
 

from cProfile import label
from tkinter import *

from setuptools import Command

lista = []
janela = Tk()

def logar():
    l = Login.get()
    s = Senha.get() 
    janela.destroy()
    lista_anuncios = []


    anuncios1 = {'imagem': r'C:\Users\Jonas Veronez\Pictures\magazine', 'Título': 'Os Melhores Preços Magazine Luiza de NoteBooks!', 'Preço': '0', 'Condição': 'Novo','link':'https://www.magazinevoce.com.br/magazinevendasveronez/l/veronez-notbooks/16948953/','Descrição': 'Confira as ofertas de NoteBooks da Magazine Luiza! '}
    anuncios2 = {'imagem': r'C:\Users\Jonas Veronez\Pictures\magazine1', 'Título': 'Os Melhores Preços Magazine Luiza de Celulares!', 'Preço': '0', 'Condição': 'Novo','link':'https://www.magazinevoce.com.br/magazinevendasveronez/l/jonas-veronez-silva/16948841/','Descrição': 'Confira as ofertas de Celulares da Magazine Luiza! '}
    anuncios3 = {'imagem': r'C:\Users\Jonas Veronez\Pictures\magazine2', 'Título': 'Os Melhores Preços Magazine Luiza para sua cozinha!', 'Preço': '0', 'Condição': 'Novo','link':'https://www.magazinevoce.com.br/magazinevendasveronez/l/veronez-itens-de-cozinha/16949157/','Descrição': 'Confira as ofertas de itens para sua cozinha da Magazine Luiza!'}
    anuncios4 = {'imagem': r'C:\Users\Jonas Veronez\Pictures\magazine3', 'Título': 'Os Melhores Preços Magazine Luiza para sua sala!', 'Preço': '0', 'Condição': 'Novo','link':'https://www.magazinevoce.com.br/magazinevendasveronez/l/veronez-sua-cozinha/16949246/','Descrição': 'Confira as ofertas de itens para sua sala da Magazine Luiza! '}
    anuncios5 = {'imagem': r'C:\Users\Jonas Veronez\Pictures\magazine4', 'Título': 'Os Melhores Preços  de Calçados Feminino Magazine Luiza!', 'Preço': '0', 'Condição': 'Novo','link':'https://www.magazinevoce.com.br/magazinevendasveronez/l/veronez-calcados/16950660/','Descrição': 'Confira o preço desses calçados na Magazine Luiza! \n Corra pois há poucos produtos em estoque! '}



    lista_anuncios.append(anuncios1)
    lista_anuncios.append(anuncios2)
    lista_anuncios.append(anuncios3)
    lista_anuncios.append(anuncios4)
    lista_anuncios.append(anuncios5)


    navegador = webdriver.Chrome()
    navegador.get("https://www.facebook.com/") 

    try:
        element = WebDriverWait(navegador,2 , poll_frequency= 0.5).until(
                    EC._element_if_visible((By.ID, "email")) #------------------verify COOK 5 seconds----------------------
                                                        )
    except:
        print('------------------Login----------------------')
        navegador.find_element_by_name('email').send_keys(l)#------------user,
        navegador.find_element_by_name('pass').send_keys(s)#------------password,
        sleep(0.1)
        usuario = navegador.find_element_by_name('login').click()#------------enter

        for anuncios in lista_anuncios:


            sleep(3)
            navegador.get("https://www.facebook.com/groups/rendaextraoummn/")
            print('---ESPERANDO---')
            sleep(2)

            usuario = navegador.find_element(By.CSS_SELECTOR, ("[aria-label='Vender algo']")).click()
            sleep(6)

            navegador.find_element(By.CSS_SELECTOR, ("[class='a8c37x1j buofh1pr']")).click()
            sleep(4)

            usuario = navegador.find_element(By.CSS_SELECTOR, ("[class='bi6gxh9e aov4n071 l9j0dhe7']")).click()


            #--------------------------------------sales-------------------------------------------------


            sleep(0.1)
            pyautogui.write(anuncios['imagem'])
            sleep(0.01)
            pyautogui.press('enter')
            print(usuario)
            sleep(8)

            navegador.find_element(By.CSS_SELECTOR, ("[aria-label='Título']")).send_keys(anuncios['Título'])
            sleep(0.2)
            navegador.find_element(By.CSS_SELECTOR, ("[aria-label='Preço']")).send_keys(anuncios['Preço'])
            sleep(0.2)
            navegador.find_element(By.CSS_SELECTOR, ("[aria-label='Condição']")).send_keys(anuncios['Condição'])
            sleep(0.2)
            navegador.find_element(By.CSS_SELECTOR, ("[aria-label='Descrição']")).send_keys(anuncios['Descrição']+'\
            \n Link de acesso:\n'+anuncios['link'])
            sleep(3)
            navegador.find_element(By.CSS_SELECTOR, ("[aria-label='Avançar']")).click()
            sleep(1)
            tamanho1 = len(navegador.find_elements(By.CSS_SELECTOR, ("[class='n851cfcs ozuftl9m n1l5q3vz l9j0dhe7 o8rfisnq']")))
        
            
            item = 0 
            while tamanho1 != item:
                navegador.find_elements(By.CSS_SELECTOR, ("[class='n851cfcs ozuftl9m n1l5q3vz l9j0dhe7 o8rfisnq']"))[item].click()
                item = item + 1

            sleep(1)

            navegador.find_element(By.CSS_SELECTOR, ("[aria-label='Publicar']")).click()
            sleep(8)
            print('------------------------RESTART------------------')

    else:
        pprint('não acho')
    

janela.title("jonassilva@gea.inatel.br")
janela.geometry("350x150")

label =  Label(janela, text="Login")
label.grid(row=0,column=0)
Login = Entry(janela, width=25)
Login.grid(row=0, column=1)

label =  Label(janela, text="Senha")
label.grid(row=1,column=0)
Senha = Entry(janela, width=25, show='*')
Senha.grid(row=2, column=1)


botao = Button(janela, text="Iniciar",width=15, bg="green", command=logar)
botao.grid(row=3, column=1, padx=0, pady=10)


janela.mainloop()    



