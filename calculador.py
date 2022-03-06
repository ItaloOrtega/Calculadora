from tkinter import *
#Função Botão, para que o valor seja alocado corretamente nos botões de número e ligar as teclas a botões
def botao(tela, lbl, x, i, j): #Cria o botão ligado a tela
  btt = Button(tela,text=str(x), padx=15, pady=15, bg="#666666", fg="#FFFFFF", command=lambda:colocar(lbl,x))
  tela.bind(f'<KP_{x}>',lambda event:colocar(lbl_entrada,x)) #Aloca o teclado númerico aos valores
  tela.bind(f'<Mod2-KeyPress-{x}>',lambda event:colocar(lbl_entrada,x)) #Aloca os números na parte principal do teclado aos valores
  if x != 0: #Caso o número a ser alocado seja diferente de zero
    btt.grid(row=i, column=j) #Ocorre a alocação normalmente
  else:
    btt.config(padx=37) #Caso seja o 0, será um botão maior
    btt.grid(row=i, column=j, columnspan=2)
  return btt

def colocar(lbl,x): #Função para colocar os valores digitados ou clicados na label de entrada
  linha = lbl.cget('text')+str(x) 
  lbl.config(text=str(linha))

def igual(lbl): #Função que pega os valores escritos na lbl de entrada e transforma em uma equação matematica
  linha = lbl.cget('text')
  linha = linha.replace("x","*") #Subistui todos os x para *, assim funciona a multiplicação
  try: #Tenta transformar a linha string em uma eq mat por meio da função eval()
    resp = eval(linha)
    lbl.config(text=str(resp))
  except: #Não sendo possivel mostra erro na lbl
    lbl.config(text="ERRO")

def limpar(lbl): #Função limpa totalmente a lbl de entrada
  lbl.config(text="")

def deletar(lbl): #Função deleta o ultimo valor digitado da lbl de entrada
  linha = lbl.cget('text')
  linha = linha[0:len(linha)-1]
  lbl.config(text=linha)

tela = Tk() #Tela principal
tela.configure(bg= "#CCCCCC")
tela.title("Calculadora")
#Largura e altura da tela
larg = 315
alt = 300
#Calcula as dimensões da tela que esta sendo usado pelo usuario
larg_s = tela.winfo_screenwidth() # largura da tela do usuario
alt_s = tela.winfo_screenheight() # altura da tela do usuario
#calcaula as coordenadas para mostrar a tela da aplicação no meio do monitor
a = (larg_s/2) - (larg/2)
b = (alt_s/2) - (alt/2)
tela.geometry('%dx%d+%d+%d' % (larg, alt, a, b-50))
tela.resizable(False, False) #Desabilita a redimensão da janela

#Lbl_aux servem para dar um espaço das margens ou pular linhas, para melhor visualização da GUI
lbl_aux0 =  Label(tela, text="    ", bg= "#CCCCCC",font= "Calibri 10")
lbl_aux0.grid(row=0, column=0, columnspan=20)
lbl_aux1 =  Label(tela, text="    ", bg= "#CCCCCC",font= "Calibri 10")
lbl_aux1.grid(row=2, column=0, columnspan=20)
lbl_aux2 =  Label(tela, text="    ", bg= "#CCCCCC",font= "Calibri 10")
lbl_aux2.grid(row=3, column=0)

#Lbl_Entrada é a label onde os valores digitados/clicados aparecem para formar a equação matematica
lbl_entrada =  Label(tela, text="",width=33, bg= "#FFFFFF", fg="#000000",font= "Calibri 10")
lbl_entrada.grid(row=1, column=1, columnspan=20)

btts_num = {} #Dicionario que recebe os botões númericos da calculadora
x = 3 #X e Y são as posições iniciais da linha e da coluna respectivamente para alocar os botões
y = 1
for i in range(9,-1,-1): #For para criar os 10 botões de números
  btts_num["btt_"+str(i)] = botao(tela,lbl_entrada,i,x,y)
  y += 1 #Vai para a proxima coluna
  if y == 4: #Caso chegue na coluna 4, incrementa x e retorna y para 1
    x += 1
    y = 1
#Botão de separação decimal
btt_virg = Button(tela,text=",", padx=17, pady=15, bg="#666666", fg="#FFFFFF", command=lambda:colocar(lbl_entrada,"."))
btt_virg.grid(row=6, column=3)
#Liga as teclas de virgula, ponto e separador para adicionar . na lbl entrada
tela.bind('<KP_Separator>',lambda event:colocar(lbl_entrada,"."))
tela.bind('<period>',lambda event:colocar(lbl_entrada,"."))
tela.bind('<comma>',lambda event:colocar(lbl_entrada,"."))
#Cria os botões de operações numericas e liga suas teclas as mesmas funções
btt_add = Button(tela,text="+", padx=15, pady=15, bg="#666666", fg="#FFFFFF", command=lambda:colocar(lbl_entrada,"+"))
btt_add.grid(row=3, column=4)
tela.bind('<KP_Add>',lambda event:colocar(lbl_entrada,"+"))
btt_sub = Button(tela,text="-", padx=17, pady=15, bg="#666666", fg="#FFFFFF", command=lambda:colocar(lbl_entrada,"-"))
btt_sub.grid(row=4, column=4)
tela.bind('<KP_Subtract>',lambda event:colocar(lbl_entrada,"-"))
btt_mult = Button(tela,text="x", padx=15, pady=15, bg="#666666", fg="#FFFFFF", command=lambda:colocar(lbl_entrada,"x"))
btt_mult.grid(row=5, column=4)
tela.bind('<KP_Multiply>',lambda event:colocar(lbl_entrada,"x"))
btt_div = Button(tela,text="/", padx=17, pady=15, bg="#666666", fg="#FFFFFF", command=lambda:colocar(lbl_entrada,"/"))
btt_div.grid(row=6, column=4)
tela.bind('<KP_Divide>',lambda event:colocar(lbl_entrada,"/"))
#Botão de deletar o ultimo valor escrito
btt_delete = Button(tela,text="⌫", padx=10, pady=42, bg="#666666", fg="#FFFFFF", command=lambda:deletar(lbl_entrada))
btt_delete.grid(row=3, column=5, rowspan=2)
tela.bind('<BackSpace>',lambda event:deletar(lbl_entrada)) #liga a tela backspace na função deletar
#Aloca as teclas e cria os botões abre e fecha parentesis
btt_abre = Button(tela,text="(", padx=17, pady=15, bg="#666666", fg="#FFFFFF", command=lambda:colocar(lbl_entrada,"("))
btt_abre.grid(row=5, column=5)
tela.bind('<parenleft>',lambda event: colocar(lbl_entrada,"("))
btt_fecha = Button(tela,text=")", padx=17, pady=15, bg="#666666", fg="#FFFFFF", command=lambda:colocar(lbl_entrada,")"))
btt_fecha.grid(row=6, column=5)
tela.bind('<parenright>',lambda event: colocar(lbl_entrada,")"))
btt_clear = Button(tela,text="C", padx=15, pady=42, bg="#666666", fg="#FFFFFF", command=lambda:limpar(lbl_entrada))
btt_clear.grid(row=3, column=6, rowspan=2)
tela.bind('<Delete>',lambda event:limpar(lbl_entrada)) #Liga a tecla Delete na função limpar
btt_igual = Button(tela,text="=", padx=15, pady=41, bg="#666666", fg="#FFFFFF", command=lambda:igual(lbl_entrada))
btt_igual.grid(row=5, column=6, rowspan=2)
#liga a tecla Enter, do teclado normal e numerico, na função igual()
tela.bind('<Return>',lambda event:igual(lbl_entrada))
tela.bind('<KP_Enter>',lambda event:igual(lbl_entrada))
tela.bind('<Escape>',lambda event:tela.destroy()) #Aloca a tecla Esc para sair da calculadora
  
tela.mainloop() #Loop da tela
