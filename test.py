import tkinter as tk
from tkinter import *

# Cores
cor0 = '#ffffff'  # branco
cor1 = '#111111'  # preto
cor2 = '#ffa500'  # laranja

# Criação da janela principal
janela = tk.Tk()
janela.title('Calculadora IMC')
janela.geometry("480x350")
janela.configure(bg=cor0)

#Funçao para salvar os dados digitados
def salvar_dados():
    nome = e_nome.get()
    peso = e_peso.get()
    altura = e_altura.get()
    resultado = l_resultado['text']
    descricao = l_resultado_texto['text']

    with open("Informacoes_imc.txt", "a") as file:
            file.write(f"Nome: {nome}, Peso: {peso}, Altura: {altura}, Resultado: {resultado}\n")

def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    resultado = imc

    if resultado <= 18.5:
        l_resultado_texto['text'] = 'Seu IMC é: Abaixo do peso'

    elif resultado > 18.5 and resultado <= 24.9:
        l_resultado_texto['text'] = 'Seu IMC é: Peso Normal'

    elif resultado > 24.9 and resultado <= 29.9:
        l_resultado_texto['text'] = 'Seu IMC é: Acima do peso'

    elif resultado >= 30 and resultado < 35:
        l_resultado_texto['text'] = 'Seu IMC é: OBESIDADE!'

    else:
        l_resultado_texto['text'] = 'Seu IMC é: OBESIDADE EXTREMA!!'

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)

#funçao para limpar campos
def limpar():
    e_nome.delete(0, END)
    e_peso.delete(0, END)
    e_altura.delete(0, END)
    l_resultado['text'] = '---'
    l_resultado_texto['text'] = 'O seu IMC é: abaixo do peso'
# funçao para atualização dos dados
def atualizar():
    nome = e_nome.get()
    peso = e_peso.get()
    altura = e_altura.get()
    resultado = l_resultado['text']

    # Ler os dados do arquivo
    with open("Informacoes_imc.txt", "r") as file:
        linhas = file.readlines()

    # Atualizar os dados
    for i, linha in enumerate(linhas):
        if nome in linha:
            linhas[i] = f"Nome: {nome}, Peso: {peso}, Altura: {altura}, Resultado: {resultado}\n"
            break

    # Escrever os dados atualizados de volta para o arquivo
    with open("Informacoes_imc", "w") as file:
        file.writelines(linhas)

    # Limpar os campos após a atualização
    limpar()

def buscar():
    nome = e_nome.get()

    # Ler os dados do arquivo
    with open("Informacoes_imc.txt", "r") as file:
        linhas = file.readlines()

    # Buscar os dados da entrada selecionada
    for linha in linhas:
        if nome in linha:
            # Extrair os dados da linha encontrada
            dados = linha.split(", ")
            for dado in dados:
                if "Nome" in dado:
                    e_nome.delete(0, END)
                    e_nome.insert(0, dado.split(": ")[1])
                elif "Peso" in dado:
                    e_peso.delete(0, END)
                    e_peso.insert(0, dado.split(": ")[1])
                elif "Altura" in dado:
                    e_altura.delete(0, END)
                    e_altura.insert(0, dado.split(": ")[1])

# Divisão da janela
frame_up = Frame(janela, width=500, height=50, bg='white', pady=0, padx=0, relief='flat')
frame_up.grid(row=0, column=0, sticky=NSEW)

frame_down = Frame(janela, width=500, height=180, bg=cor0, pady=0, padx=0, relief='flat')
frame_down.grid(row=1, column=0, sticky=NSEW)

# Configuração do frame superior
app_nome = Label(frame_up, text='Calculadora IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Roboto', 16, 'bold'), bg=cor0, fg=cor1)
app_nome.place(x=105, y=0)

app_linha = Label(frame_up, text='', width=500, height=1, padx=0, relief='flat', anchor='center', font=('Roboto', 1), bg=cor1, fg=cor1)
app_linha.place(x=0, y=35)

# Configuração do frame inferior
l_nome = Label(frame_down, text='Insira o seu nome:', height=1, padx=0, relief='flat', anchor='center', font=('Roboto', 9, 'bold'), bg=cor0, fg=cor1)
l_nome.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_nome = Entry(frame_down, width=10, relief='solid', font=('Roboto', 9, 'bold'), justify='center')
e_nome.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


l_peso = Label(frame_down, text='Insira o seu peso:', height=1, padx=0, relief='flat', anchor='center', font=('Roboto', 9, 'bold'), bg=cor0, fg=cor1)
l_peso.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_down, width=10, relief='solid', font=('Roboto', 9, 'bold'), justify='center')
e_peso.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_down, text='Insira a sua altura:', height=1, padx=0, relief='flat', anchor='center', font=('Roboto', 9, 'bold'), bg=cor0, fg=cor1)
l_altura.grid(row=2, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(frame_down, width=10, relief='solid', font=('Roboto', 9, 'bold'), justify='center')
e_altura.grid(row=2, column=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_down, text='---', width=15, height=2, padx=6, pady=12, relief='flat', anchor='center', font=('Roboto', 12, 'bold'), bg=cor2, fg=cor0)
l_resultado.place(x=300, y=30)

l_resultado_texto = Label(frame_down, text='O seu IMC é: abaixo do peso', width=37, height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Roboto', 10 , 'bold'), bg=cor0, fg=cor1)
l_resultado_texto.place(x=230, y=130)

# Criação do botão de calculo
b_calcular = Button(frame_down, text='Calcular', width=34, height=1, overrelief=SOLID, padx=0, pady=12, relief='raised', anchor='center', font=('Roboto', 10 , 'bold'), bg=cor2, fg=cor1, command=calcular)
b_calcular.grid(row=4, column=0, columnspan=30, sticky=NSEW, pady=60, padx=5)

# Criação do botão de limpar campos
b_limpar = Button(frame_down, text='Limpar', width=7, height=1, overrelief=SOLID, padx=0, pady=12, relief='raised', anchor='center', font=('Roboto', 10 , 'bold'), bg=cor2, fg=cor1, command=limpar)
b_limpar.grid(row=4, column=1, columnspan=30, sticky=NSEW, pady=60, padx=5)
b_limpar.place(x=380, y=183)

#Crição do botao para salvar os dados
b_salvar_dados = Button(frame_down, text='Salvar', width=7, height=1, overrelief=SOLID, padx=0, pady=12, relief='raised', anchor='center', font=('Roboto', 10 , 'bold'), bg=cor2, fg=cor1, command=salvar_dados)
b_salvar_dados.grid(row=4, column=1, sticky=NSEW, pady=60, padx=5)
b_salvar_dados.place(x=300, y=183)

# Criação do botão de atualizar dados
b_atualizar_dados = Button(frame_down, text='Atualizar', width=7, height=1, overrelief=SOLID, padx=0, pady=12, relief='raised', anchor='center', font=('Roboto', 10 , 'bold'), bg=cor2, fg=cor1, command=atualizar)
b_atualizar_dados.grid(row=4, column=1, sticky=NSEW, pady=60, padx=5)
b_atualizar_dados.place(x=220, y=183)

# Criação do botão de buscar dados para atualização
b_buscar_dados = Button(frame_down, text='Buscar', width=7, height=1, overrelief=SOLID, padx=0, pady=12, relief='raised', anchor='center', font=('Roboto', 10 , 'bold'), bg=cor2, fg=cor1, command=buscar)
b_buscar_dados.grid(row=4, column=1, sticky=NSEW, pady=60, padx=5)
b_buscar_dados.place(x=200, y=120)



# Iniciando o loop principal
janela.mainloop()
