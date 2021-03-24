
#coding: utf-8

from PIL import Image,ImageTk
from tkinter import  messagebox
from tableframe import *

# ===================================================================================================================
# CLASSE VIEW: LOGIN
# ===================================================================================================================
class ViewLogin(tk.Frame):

    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS + METODOS E ATRIBUTOS COMPARTILHADOS ENTRE CLASSES
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.enabledWidgetsMainFrame=cxMetodoComum[0] # PERMITE ACESSO AO METODO MAINFRAME QUE ABILITA OS BOTÕES AO LOGAR
        self.selectViewHome=cxMetodoComum[10]
        self.corFundo = 'SystemWindow'
        self.fonttypeComum=['Trebuchet', int(round(self.widthDefaultTopLevel*0.006729))]
        self.fontfgComum= 'seagreen'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        # --------------------------------------------------------------------------------------------------------------
        self.grid_columnconfigure(0,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # FRAME INTERNO
        # --------------------------------------------------------------------------------------------------------------
        self.interFrameLogin=tk.Frame(self,padx=int(self.widthDefaultTopLevel*0.01388),
                                      pady=int(self.heightDefaultTopLevel*0.0222),bd=2,relief=tk.GROOVE,bg=self.corFundo)
        self.interFrameLogin.grid(row=1,column=0)
        self.rowconfigure(1,pad=int(self.heightDefaultTopLevel*0.185185))
        # --------------------------------------------------------------------------------------------------------------
        # METODOS PARA CONSTRUÇÃO DE WIDGETS
        self.widgetsLogoIcon()
        self.widgetsLogin()
        # --------------------------------------------------------------------------------------------------------------

    def widgetsLogoIcon(self):
        self.img_logoMei = Image.open(r".\images\meilogo3.png").\
            resize((int(self.widthDefaultTopLevel * 1.2),int(self.heightDefaultTopLevel * 0.462962)),Image.ANTIALIAS)
        self.img_logoMei = ImageTk.PhotoImage(self.img_logoMei)
        self.lb_logoMei = tk.Label(self, image=self.img_logoMei, width=int(self.widthDefaultTopLevel * 0.934895),
                                   height=int(self.heightDefaultTopLevel * 0.362962), bg='white')
        self.lb_logoMei.image = self.img_logoMei
        self.lb_logoMei.grid(row=0,column=0)

    def widgetsLogin(self):

        # CAMPO USUARIO
        self.tx1 = tk.Label(self.interFrameLogin, text='Usuário:', font=self.fonttypeComum,bg=self.corFundo, fg=self.fontfgComum, pady='0')
        self.tx1.grid(row=1,column=0)
        self.entNome = tk.Entry(self.interFrameLogin, width='30', font=self.fonttypeComum,bd=2,relief=tk.GROOVE)  # Entry É O objeto sem. jtexfield
        # NÃO É POSSIVEL DEFINIR O HEIDTH POIS NO ENTRY O MAX É O TAMANHO DA LINHA
        self.entNome['justify'] = 'center'  # Justifica o Texto Digitado
        self.entNome.focus_force()
        self.entNome.grid(row=1, column=1)
        self.entNome.bind('<Return>',self.passarFocoEnNome)

        # CAMPO SENHA
        self.tx2 = tk.Label(self.interFrameLogin, text='Senha:', font=self.fonttypeComum,bg=self.corFundo, fg=self.fontfgComum,
                            pady=int(self.heightDefaultTopLevel * 0.0166))
        self.tx2.grid(row=2,column=0)
        self.entPass = tk.Entry(self.interFrameLogin, width='30', font=self.fonttypeComum, show='*', justify='center',bd=2,relief=tk.GROOVE)
        self.entPass.bind('<Return>', self.validaLogin)
        self.entPass.grid(row=2, column=1)

        # BOTAO LOGIN
        self.btlogin = tk.Button(self.interFrameLogin, text='Entrar',bg=self.corFundo,fg=self.fontfgComum,
                                 font=self.fonttypeComum,padx=int(self.widthDefaultTopLevel * 0.0138), relief=tk.GROOVE,highlightthickness=2)
        self.btlogin['command'] = self.validaLogin
        self.btlogin.bind('<Return>', self.validaLogin)
        self.btlogin.grid(row=3, column=1)

    def validaLogin(self,event=None):
        if self.entNome.get()=='mei' and self.entPass.get()=='123':
            messagebox.showinfo('OK', 'Login Efetuado com Sucesso!')
            self.enabledWidgetsMainFrame()
            self.selectViewHome()
        else:
            messagebox.showwarning('Login Inválido','Usuário e/ou Senha Inválidos\nPor Favor, Digite Novamente Suas Credenciais')
            self.entNome.delete(0, 'end')
            self.entPass.delete(0, 'end')
            self.entNome.focus_force()

    def passarFocoEnNome(self,event=None):
        self.entPass.focus_force()
# ===================================================================================================================
# CLASSE VIEW: INICIO HOME
# ===================================================================================================================
class ViewHome(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callCadCliente=cxMetodoComum[2]
        self.corFundo ='SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        #self.grid_columnconfigure(0,weight=1)
        #self.grid_columnconfigure(1,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.manipdb=cxAtributoComum['db']
        # --------------------------------------------------------------------------------------------------------------
        # FRAMES INTERNOS
        # --------------------------------------------------------------------------------------------------------------

        self.tableFrameTotalVendas=TableHomeTotalVendas(self, cxAtributoComum, cxMetodoComum)
        self.tableFrameTotalVendas.grid(row=2, column=0)#,sticky=tk.N+tk.W)

        self.tableFrameTotalCompras = TableHomeTotalCompras(self, cxAtributoComum, cxMetodoComum)
        self.tableFrameTotalCompras.grid(row=4, column=0)#,sticky=tk.N+tk.E)

        self.tableFrameTotalLucro = TableHomeTotalLucro(self, cxAtributoComum, cxMetodoComum)
        self.tableFrameTotalLucro.grid(row=6, column=0,columnspan=1)

        #self.interViewFrame = tk.Frame(self,bg='orange')#, padx=int(self.widthDefaultTopLevel * 0.01004),
                                      #pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        #self.interViewFrame.grid(row=0, column=0)

        # --------------------------------------------------------------------------------------------------------------
        # CHAMADA DE MÉTODOS DE CONSTRUÇÃO DE WIDGETS
        # --------------------------------------------------------------------------------------------------------------
        self.widgetsViewFrame()
        # --------------------------------------------------------------------------------------------------------------

    def widgetsViewFrame(self):
        lb_vendas = tk.Label(self, text='VENDAS MENSAL',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        lb_vendas.grid(row=1)
        lb_compras=tk.Label(self,text='COMPRAS MENSAL',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        lb_compras.grid(row=3)
        lb_lucro=tk.Label(self,text='LUCRO MENSAL',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        lb_lucro.grid(row=5)
        # --------------------------------------------------------------------------------------------------------------
        self.img_logoMei2 = Image.open(r".\images\financial.png"). \
            resize((int(self.widthDefaultTopLevel * 0.224895), int(self.heightDefaultTopLevel * 0.432962)),
                   Image.ANTIALIAS)
        self.img_logoMei2 = ImageTk.PhotoImage(self.img_logoMei2)
        self.lb_logoMei2 = tk.Label(self, image=self.img_logoMei2,
                                   width=int(self.widthDefaultTopLevel * 0.224895),
                                   height=int(self.heightDefaultTopLevel * 0.462962), bg='white')
        self.lb_logoMei2.image = self.img_logoMei2
        self.lb_logoMei2.grid(row=0)

    def setEstiloTreeview(self, fgTreeview, font, rowheight): # DEFINE ESTILO PARA QUALQUER TREEVIEW
         style=ttk.Style()
         style.configure("Treeview", foreground=fgTreeview,rowheight=rowheight) # DEFINE STYLO PARA A TREEVIEW
         style.configure("Treeview.Heading", foreground='black',font=font) # DEFINE ESTILO PARA OS INDICES DA TREEVIEW

# ===================================================================================================================
# CLASSE VIEW: CLIENTE
# ===================================================================================================================
class ViewCliente(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callCadCliente=cxMetodoComum[2]
        self.corFundo ='SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.manipdb=cxAtributoComum['db']
        # --------------------------------------------------------------------------------------------------------------
        # FRAMES INTERNOS
        # --------------------------------------------------------------------------------------------------------------
        self.tableFrame=TableCliente(self,cxAtributoComum,cxMetodoComum)

        self.tableFrame.grid(row=0,column=0,sticky=tk.N)

        self.interViewFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.01004),
                                       pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interViewFrame.grid(row=0, column=1,sticky=tk.N+tk.S)

        # --------------------------------------------------------------------------------------------------------------
        # CHAMADA DE MÉTODOS DE CONSTRUÇÃO DE WIDGETS
        # --------------------------------------------------------------------------------------------------------------
        #self.widgetsViewFrame()
        # --------------------------------------------------------------------------------------------------------------

    def widgetsViewFrame(self):
        width9=int(round(self.widthDefaultTopLevel*0.00468))
        width80=int(round(self.widthDefaultTopLevel*0.04166))
        self.bt_historico=tk.Button(self.interViewFrame, text='Histórico', font=self.fonttypeComum, width=width9,
                                    height=2,relief=tk.GROOVE, bg=self.corFundo,state=tk.DISABLED)
        self.bt_historico.grid(row=0, column=0)
        self.bt_buscar = tk.Button(self.interViewFrame, text='Buscar', font=self.fonttypeComum, width=width9,
                                   height=2, relief=tk.GROOVE, bg=self.corFundo,state=tk.DISABLED)
        self.bt_buscar.grid(row=1, column=0)
        self.bt_editar = tk.Button(self.interViewFrame, text='Editar', font=self.fonttypeComum, width=width9, height=2,
                                   relief=tk.GROOVE, bg=self.corFundo,command=self.editar)
        self.bt_editar.grid(row=2, column=0)
        self.bt_excluir = tk.Button(self.interViewFrame, text='Excluir', font=self.fonttypeComum, width=width9, height=2,
                                    relief=tk.GROOVE, bg=self.corFundo, command=self.excluir)
        self.bt_excluir.grid(row=3, column=0)

        self.img_meilogo = Image.open(r".\images\bussIcon.png").resize((width9 * 10, int(round(self.heightDefaultTopLevel*0.0833))), Image.ANTIALIAS)
        self.img_meilogo = ImageTk.PhotoImage(self.img_meilogo)
        self.lb_meilogo = tk.Label(self.interViewFrame, image=self.img_meilogo, width=width9 * 10, height=int(round(self.heightDefaultTopLevel*0.0833)),
                                   relief=tk.FLAT,
                                   bg=self.corFundo, takefocus=0)
        self.lb_meilogo.image = self.img_meilogo
        self.lb_meilogo.grid(row=4, column=0, sticky=tk.S)

        self.interViewFrame.grid_rowconfigure(0, pad=width80)
        self.interViewFrame.grid_rowconfigure(1, pad=width80)
        self.interViewFrame.grid_rowconfigure(2, pad=width80)
        self.interViewFrame.grid_rowconfigure(3, pad=width80)
        self.interViewFrame.grid_rowconfigure(4, pad=width80 * 2.6)

    def setEstiloTreeview(self, fgTreeview, font, rowheight): # DEFINE ESTILO PARA QUALQUER TREEVIEW
         style=ttk.Style()
         style.configure("Treeview", foreground=fgTreeview,rowheight=rowheight) # DEFINE STYLO PARA A TREEVIEW
         style.configure("Treeview.Heading", foreground='black',font=font) # DEFINE ESTILO PARA OS INDICES DA TREEVIEW

    def editar(self):
        # --------------------------------------------------------------------------------------------------------------
        # SELECIONA E TRATA DADOS PARA OS ENTRYS DO EDITAR
        # --------------------------------------------------------------------------------------------------------------
        cod = self.tableFrame.eventSelect()
        listEditar=[cod[0],cod[1][0]]

        sttemp=''
        for c in cod[1][1]: # CPF/CNPJ
            if(c in ['.','-','/']): pass
            else: sttemp+=c
        listEditar.append(sttemp)

        if cod[1][2]!='[VAZIO]': # TELEFONE
            sttemp = ''
            for c in cod[1][2]:
                if (c in ['(', ')', '-']):
                    pass
                else:
                    sttemp += c
            listEditar.append(sttemp)
        else: listEditar.append('')

        if cod[1][3] != '[VAZIO]': # LOGRADOURO
            listEditar.append(cod[1][3])
        else:
            listEditar.append('')
        if cod[1][4] != '[VAZIO]': # CIDADE
            listEditar.append(cod[1][4])
        else:
            listEditar.append('')

        if cod[1][5] != '[VAZIO]': # ESTADO
            listEditar.append(cod[1][5])
        else:
            listEditar.append('')

        if cod[1][6] != '[VAZIO]': # CEP
            sttemp=''
            for c in cod[1][6]:
                if (c =='-'):pass
                else: sttemp += c
            listEditar.append(sttemp)
        else:
            listEditar.append('')
        self.callCadCliente(listEditar)

        # --------------------------------------------------------------------------------------------------------------

    def excluir(self):
        if messagebox.askokcancel('EXCLUIR','Esta Ação Será Permanente.\nDeseja Realmente Excluir?'):
            cod=self.tableFrame.eventSelect()[0]
            msg=self.manipdb.excluirCliente(cod)
            if(msg=='OK'):
                self.tableFrame.updateTable()
                messagebox.showinfo('OK','Excluido Com Sucesso!')
            else: messagebox.showinfo('ERRO','Erro Ao Remover')
# ===================================================================================================================
# CLASSE VIEW: FORNECEDOR
# ===================================================================================================================
class ViewFornecedor(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callCadFornecedor=cxMetodoComum[5]
        self.corFundo ='SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.manipdb=cxAtributoComum['db']
        # --------------------------------------------------------------------------------------------------------------
        # FRAMES INTERNOS
        # --------------------------------------------------------------------------------------------------------------
        self.tableFrame=TableFornecedor(self,cxAtributoComum,cxMetodoComum)
        self.tableFrame.grid(row=0,column=0,sticky=tk.N)

        self.interViewFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.01004),
                                       pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interViewFrame.grid(row=0, column=1,sticky=tk.N+tk.S)

        # --------------------------------------------------------------------------------------------------------------
        # CHAMADA DE MÉTODOS DE CONSTRUÇÃO DE WIDGETS
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------

    def widgetsViewFrame(self):
        width9=int(round(self.widthDefaultTopLevel*0.00468))
        width80=int(round(self.widthDefaultTopLevel*0.04166))
        self.bt_historico=tk.Button(self.interViewFrame, text='Histórico', font=self.fonttypeComum, width=width9, height=2,
                                    relief=tk.GROOVE, bg=self.corFundo,state=tk.DISABLED)
        self.bt_historico.grid(row=0, column=0)
        self.bt_buscar = tk.Button(self.interViewFrame, text='Buscar', font=self.fonttypeComum, width=width9, height=2,
                                   relief=tk.GROOVE, bg=self.corFundo,state=tk.DISABLED)
        self.bt_buscar.grid(row=1, column=0)
        self.bt_editar = tk.Button(self.interViewFrame, text='Editar', font=self.fonttypeComum, width=width9, height=2,
                                   relief=tk.GROOVE, bg=self.corFundo,command=self.editar)
        self.bt_editar.grid(row=2, column=0)
        self.bt_excluir = tk.Button(self.interViewFrame, text='Excluir', font=self.fonttypeComum, width=width9, height=2,
                                    relief=tk.GROOVE, bg=self.corFundo, command=self.excluir)
        self.bt_excluir.grid(row=3, column=0)

        self.img_meilogo = Image.open(r".\images\bussIcon.png").resize((width9 * 10, int(round(self.heightDefaultTopLevel*0.0833))), Image.ANTIALIAS)
        self.img_meilogo = ImageTk.PhotoImage(self.img_meilogo)
        self.lb_meilogo = tk.Label(self.interViewFrame, image=self.img_meilogo, width=width9 * 10, height=int(round(self.heightDefaultTopLevel*0.0833)),
                                   relief=tk.FLAT,
                                   bg=self.corFundo, takefocus=0)
        self.lb_meilogo.image = self.img_meilogo
        self.lb_meilogo.grid(row=4, column=0, sticky=tk.S)

        self.interViewFrame.grid_rowconfigure(0, pad=width80)
        self.interViewFrame.grid_rowconfigure(1, pad=width80)
        self.interViewFrame.grid_rowconfigure(2, pad=width80)
        self.interViewFrame.grid_rowconfigure(3, pad=width80)
        self.interViewFrame.grid_rowconfigure(4, pad=width80 * 2.6)

    def setEstiloTreeview(self, fgTreeview, font, rowheight): # DEFINE ESTILO PARA QUALQUER TREEVIEW
         style=ttk.Style()
         style.configure("Treeview", foreground=fgTreeview,rowheight=rowheight) # DEFINE STYLO PARA A TREEVIEW
         style.configure("Treeview.Heading", foreground='black',font=font) # DEFINE ESTILO PARA OS INDICES DA TREEVIEW

    def editar(self):
        # --------------------------------------------------------------------------------------------------------------
        # SELECIONA E TRATA DADOS PARA OS ENTRYS DO EDITAR
        # --------------------------------------------------------------------------------------------------------------
        cod = self.tableFrame.eventSelect()
        listEditar=[cod[0],cod[1][0]]

        sttemp=''
        for c in cod[1][1]: # CNPJ
            if(c in ['.','-','/']): pass
            else: sttemp+=c
        listEditar.append(sttemp)

        if cod[1][2]!='[VAZIO]': # TELEFONE
            sttemp = ''
            for c in cod[1][2]:
                if (c in ['(', ')', '-']):
                    pass
                else:
                    sttemp += c
            listEditar.append(sttemp)
        else: listEditar.append('')

        if cod[1][3] != '[VAZIO]': # LOGRADOURO
            listEditar.append(cod[1][3])
        else:
            listEditar.append('')
        if cod[1][4] != '[VAZIO]': # CIDADE
            listEditar.append(cod[1][4])
        else:
            listEditar.append('')

        if cod[1][5] != '[VAZIO]': # ESTADO
            listEditar.append(cod[1][5])
        else:
            listEditar.append('')

        if cod[1][6] != '[VAZIO]': # CEP
            sttemp=''
            for c in cod[1][6]:
                if (c =='-'):pass
                else: sttemp += c
            listEditar.append(sttemp)
        else:
            listEditar.append('')
        self.callCadFornecedor(listEditar)

        # --------------------------------------------------------------------------------------------------------------

    def excluir(self):
        if messagebox.askokcancel('EXCLUIR','Esta Ação Será Permanente.\nDeseja Realmente Excluir?'):
            cod=self.tableFrame.eventSelect()[0]
            msg=self.manipdb.excluirFornecedor(cod)
            if(msg=='OK'):
                self.tableFrame.updateTable()
                messagebox.showinfo('OK','Excluido Com Sucesso!')
            else: messagebox.showinfo('ERRO','Erro Ao Remover')
# ===================================================================================================================
# CLASSE VIEW: PRODUTO
# ===================================================================================================================
class ViewProduto(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callCadProduto=cxMetodoComum[7]
        self.corFundo ='SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.manipdb=cxAtributoComum['db']
        # --------------------------------------------------------------------------------------------------------------
        # FRAMES INTERNOS
        # --------------------------------------------------------------------------------------------------------------
        self.tableFrame=TableProduto(self,cxAtributoComum,cxMetodoComum)

        self.tableFrame.grid(row=0,column=0,sticky=tk.N)

        self.interViewFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.01004),
                                       pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interViewFrame.grid(row=0, column=1,sticky=tk.N+tk.S)

        # --------------------------------------------------------------------------------------------------------------
        # CHAMADA DE MÉTODOS DE CONSTRUÇÃO DE WIDGETS
        # --------------------------------------------------------------------------------------------------------------
        #self.widgetsViewFrame()
        # --------------------------------------------------------------------------------------------------------------

    def widgetsViewFrame(self):
        width9=int(round(self.widthDefaultTopLevel*0.00468))
        width80=int(round(self.widthDefaultTopLevel*0.04166))

        self.bt_buscar = tk.Button(self.interViewFrame, text='Buscar', font=self.fonttypeComum, width=width9,
                                   height=2, relief=tk.GROOVE, bg=self.corFundo,state=tk.DISABLED)
        self.bt_buscar.grid(row=0, column=0)
        self.bt_editar = tk.Button(self.interViewFrame, text='Editar', font=self.fonttypeComum, width=width9, height=2,
                                   relief=tk.GROOVE, bg=self.corFundo,command=self.editar)
        self.bt_editar.grid(row=1, column=0)
        self.bt_excluir = tk.Button(self.interViewFrame, text='Excluir', font=self.fonttypeComum, width=width9, height=2,
                                    relief=tk.GROOVE, bg=self.corFundo, command=self.excluir)
        self.bt_excluir.grid(row=2, column=0)

        self.img_meilogo = Image.open(r".\images\bussIcon.png").resize((width9 * 10, int(round(self.heightDefaultTopLevel*0.0833))), Image.ANTIALIAS)
        self.img_meilogo = ImageTk.PhotoImage(self.img_meilogo)
        self.lb_meilogo = tk.Label(self.interViewFrame, image=self.img_meilogo, width=width9 * 10, height=int(round(self.heightDefaultTopLevel*0.0833)),
                                   relief=tk.FLAT,
                                   bg=self.corFundo, takefocus=0)
        self.lb_meilogo.image = self.img_meilogo
        self.lb_meilogo.grid(row=3, column=0, sticky=tk.S)

        self.interViewFrame.grid_rowconfigure(0, pad=width80)
        self.interViewFrame.grid_rowconfigure(1, pad=width80)
        self.interViewFrame.grid_rowconfigure(2, pad=width80)
        self.interViewFrame.grid_rowconfigure(3, pad=width80 * 4.3)

    def setEstiloTreeview(self, fgTreeview, font, rowheight): # DEFINE ESTILO PARA QUALQUER TREEVIEW
         style=ttk.Style()
         style.configure("Treeview", foreground=fgTreeview,rowheight=rowheight) # DEFINE STYLO PARA A TREEVIEW
         style.configure("Treeview.Heading", foreground='black',font=font) # DEFINE ESTILO PARA OS INDICES DA TREEVIEW

    def editar(self):
        # --------------------------------------------------------------------------------------------------------------
        # SELECIONA E TRATA DADOS PARA OS ENTRYS DO EDITAR
        # --------------------------------------------------------------------------------------------------------------
        cod = self.tableFrame.eventSelect()
        listEditar=[cod[0],cod[1][0]] # COD E NOME

        sttemp=''
        for c in cod[1][1]: # PREÇO
            if(c == '.'): sttemp+=','
            else: sttemp+=c
        listEditar.append(sttemp)

        sttemp = ''
        for c in cod[1][2]:  # DESCRICAO
            if (c == '|'):
                sttemp += '\n'
            else:
                sttemp += c
        listEditar.append(sttemp)

        listEditar.append(cod[1][2]) # DESCRICAO

        self.callCadProduto(listEditar)

        # --------------------------------------------------------------------------------------------------------------

    def excluir(self):
        if messagebox.askokcancel('EXCLUIR','Esta Ação Será Permanente.\nDeseja Realmente Excluir?'):
            cod=self.tableFrame.eventSelect()[0]
            msg=self.manipdb.excluirProduto(cod)
            if(msg=='OK'):
                self.tableFrame.updateTable()
                messagebox.showinfo('OK','Excluido Com Sucesso!')
            else: messagebox.showwarning('ERROR','Produto não pode ser removido.\nProvalmente o produto consta nos registros de compra e venda'
                                                        ' não podendo assim ser removido.')
# ===================================================================================================================
# CLASSE VIEW: VENDA
# ===================================================================================================================
class ViewVenda(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        #self.callCadCliente=cxMetodoComum[2]
        self.corFundo ='SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.manipdb=cxAtributoComum['db']
        # --------------------------------------------------------------------------------------------------------------
        # FRAMES INTERNOS
        # --------------------------------------------------------------------------------------------------------------
        self.tableProdutos = TableCarrinho(self, [int(self.widthDefaultTopLevel*0.6197), int(self.heightDefaultTopLevel*0.9852), self.manipdb])
        self.tableProdutos.grid(row=0, column=1, sticky=tk.N + tk.W)

        self.tableFrame=TableVenda(self,cxAtributoComum,[self.tableProdutos.InsertInTable,self.tableProdutos.deleteAllInTable])
        self.tableFrame.grid(row=0,column=0,sticky=tk.N)


        self.interViewFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.01004),
                                       pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interViewFrame.grid(row=0, column=2,sticky=tk.N+tk.S)

        # --------------------------------------------------------------------------------------------------------------
        # CHAMADA DE MÉTODOS DE CONSTRUÇÃO DE WIDGETS
        # --------------------------------------------------------------------------------------------------------------
        #self.widgetsViewFrame()

        # --------------------------------------------------------------------------------------------------------------

    def widgetsViewFrame(self):
        width9=int(round(self.widthDefaultTopLevel*0.00468))
        width80=int(round(self.widthDefaultTopLevel*0.04166))
        self.bt_historico=tk.Button(self.interViewFrame, text='Histórico', font=self.fonttypeComum, width=width9,
                                    height=2,relief=tk.GROOVE, bg=self.corFundo,state=tk.DISABLED)
        self.bt_historico.grid(row=0, column=0)
        self.bt_buscar = tk.Button(self.interViewFrame, text='Buscar', font=self.fonttypeComum, width=width9,
                                   height=2, relief=tk.GROOVE, bg=self.corFundo,state=tk.DISABLED)
        self.bt_buscar.grid(row=1, column=0)

        self.bt_excluir = tk.Button(self.interViewFrame, text='Excluir', font=self.fonttypeComum, width=width9, height=2,
                                    relief=tk.GROOVE, bg=self.corFundo, command=self.excluir)
        self.bt_excluir.grid(row=2, column=0)

        self.img_meilogo = Image.open(r".\images\bussIcon.png").resize((width9 * 10, int(round(self.heightDefaultTopLevel*0.0833))), Image.ANTIALIAS)
        self.img_meilogo = ImageTk.PhotoImage(self.img_meilogo)
        self.lb_meilogo = tk.Label(self.interViewFrame, image=self.img_meilogo, width=width9 * 10, height=int(round(self.heightDefaultTopLevel*0.0833)),
                                   relief=tk.FLAT,
                                   bg=self.corFundo, takefocus=0)
        self.lb_meilogo.image = self.img_meilogo
        self.lb_meilogo.grid(row=3, column=0, sticky=tk.S)

        self.interViewFrame.grid_rowconfigure(0, pad=width80)
        self.interViewFrame.grid_rowconfigure(1, pad=width80)
        self.interViewFrame.grid_rowconfigure(2, pad=width80)
        self.interViewFrame.grid_rowconfigure(3, pad=width80*4.3)



    def setEstiloTreeview(self, fgTreeview, font, rowheight): # DEFINE ESTILO PARA QUALQUER TREEVIEW
         style=ttk.Style()
         style.configure("Treeview", foreground=fgTreeview,rowheight=rowheight) # DEFINE STYLO PARA A TREEVIEW
         style.configure("Treeview.Heading", foreground='black',font=font) # DEFINE ESTILO PARA OS INDICES DA TREEVIEW



    def excluir(self):
        if self.tableFrame.eventSelect()==None:
            return

        if messagebox.askokcancel('EXCLUIR?','Esta Ação Será Permanente.\nDeseja Realmente Excluir?'):
            if messagebox.askokcancel('EXCLUIR?', 'Todos Os Produtos Desta Venda Serão Devolvidos Ao Estoque\n'
                                                  'Fazendo-Se Necessário Uma Nova Venda Para Liberação dos Mesmos.\n'
                                                  'Deseja Realmente Excluir?'): pass
            else: return 0
            cod=self.tableFrame.eventSelect()[0]
            msg=self.manipdb.excluirVenda(cod)
            if(msg=='OK'):
                self.tableFrame.updateTable()
                messagebox.showinfo('OK','Excluido Com Sucesso!')
            else: messagebox.showinfo('ERRO','Erro Ao Remover')
# ===================================================================================================================
# CLASSE VIEW: COMPRA
# ===================================================================================================================
class ViewCompra(tk.Frame):
            def __init__(self, TopLevel, cxAtributoComum, cxMetodoComum):
                tk.Frame.__init__(self, TopLevel)
                # --------------------------------------------------------------------------------------------------------------
                # PROPRIEDADES COMUNS
                # --------------------------------------------------------------------------------------------------------------
                self.widthDefaultTopLevel = cxAtributoComum[0]  # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
                self.heightDefaultTopLevel = cxAtributoComum[1]  # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
                #self.callCadCliente = cxMetodoComum[2]
                self.corFundo = 'SystemWindow'
                self.fonttypeComum = ['Trebuchet', int(self.heightDefaultTopLevel * 0.0111)]
                self.fontfgComum = 'DodgerBlue4'
                # --------------------------------------------------------------------------------------------------------------
                # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
                self.grid_columnconfigure(0, weight=1)
                self.grid_columnconfigure(1, weight=1)
                self['bg'] = self.corFundo
                # --------------------------------------------------------------------------------------------------------------
                # OBJETOS/VARIÁVEIS COMUNS
                # --------------------------------------------------------------------------------------------------------------
                self.manipdb = cxAtributoComum['db']
                # --------------------------------------------------------------------------------------------------------------
                # FRAMES INTERNOS
                # --------------------------------------------------------------------------------------------------------------
                self.tableProdutos = TableCarrinho(self, [int(self.widthDefaultTopLevel * 0.6197),
                                                          int(self.heightDefaultTopLevel * 0.9852), self.manipdb])
                self.tableProdutos.grid(row=0, column=1, sticky=tk.N + tk.W)

                self.tableFrame = TableCompra(self, cxAtributoComum,
                                             [self.tableProdutos.InsertInTable, self.tableProdutos.deleteAllInTable])
                self.tableFrame.grid(row=0, column=0,sticky=tk.N)

                self.interViewFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.01004),
                                               pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE,
                                               bg=self.corFundo)
                self.interViewFrame.grid(row=0, column=2, sticky=tk.N + tk.S)

                # --------------------------------------------------------------------------------------------------------------
                # CHAMADA DE MÉTODOS DE CONSTRUÇÃO DE WIDGETS
                # --------------------------------------------------------------------------------------------------------------
                # self.widgetsViewFrame()

                # --------------------------------------------------------------------------------------------------------------

            def widgetsViewFrame(self):
                width9 = int(round(self.widthDefaultTopLevel * 0.00468))
                width80 = int(round(self.widthDefaultTopLevel * 0.04166))
                self.bt_historico = tk.Button(self.interViewFrame, text='Histórico', font=self.fonttypeComum,
                                              width=width9,
                                              height=2, relief=tk.GROOVE, bg=self.corFundo, state=tk.DISABLED)
                self.bt_historico.grid(row=0, column=0)
                self.bt_buscar = tk.Button(self.interViewFrame, text='Buscar', font=self.fonttypeComum, width=width9,
                                           height=2, relief=tk.GROOVE, bg=self.corFundo, state=tk.DISABLED)
                self.bt_buscar.grid(row=1, column=0)

                self.bt_excluir = tk.Button(self.interViewFrame, text='Excluir', font=self.fonttypeComum, width=width9,
                                            height=2,
                                            relief=tk.GROOVE, bg=self.corFundo, command=self.excluir)
                self.bt_excluir.grid(row=2, column=0)

                self.img_meilogo = Image.open(r".\images\bussIcon.png").resize(
                    (width9 * 10, int(round(self.heightDefaultTopLevel * 0.0833))), Image.ANTIALIAS)
                self.img_meilogo = ImageTk.PhotoImage(self.img_meilogo)
                self.lb_meilogo = tk.Label(self.interViewFrame, image=self.img_meilogo, width=width9 * 10,
                                           height=int(round(self.heightDefaultTopLevel * 0.0833)),
                                           relief=tk.FLAT,
                                           bg=self.corFundo, takefocus=0)
                self.lb_meilogo.image = self.img_meilogo
                self.lb_meilogo.grid(row=3, column=0, sticky=tk.S)

                self.interViewFrame.grid_rowconfigure(0, pad=width80)
                self.interViewFrame.grid_rowconfigure(1, pad=width80)
                self.interViewFrame.grid_rowconfigure(2, pad=width80)
                self.interViewFrame.grid_rowconfigure(3, pad=width80 * 4.3)

            def setEstiloTreeview(self, fgTreeview, font, rowheight):  # DEFINE ESTILO PARA QUALQUER TREEVIEW
                style = ttk.Style()
                style.configure("Treeview", foreground=fgTreeview, rowheight=rowheight)  # DEFINE STYLO PARA A TREEVIEW
                style.configure("Treeview.Heading", foreground='black',
                                font=font)  # DEFINE ESTILO PARA OS INDICES DA TREEVIEW

            def excluir(self):
                if self.tableFrame.eventSelect() == None:
                    return

                if messagebox.askokcancel('EXCLUIR?', 'Esta Ação Será Permanente.\nDeseja Realmente Excluir?'):
                    if messagebox.askokcancel('EXCLUIR?', 'Todos Os Produtos Desta Venda Serão Devolvidos Ao Estoque\n'
                                                          'Fazendo-Se Necessário Uma Nova Venda Para Liberação dos Mesmos.\n'
                                                          'Deseja Realmente Excluir?'):
                        pass
                    else:
                        return 0
                    cod = self.tableFrame.eventSelect()[0]
                    msg = self.manipdb.excluirCompra(cod)
                    if (msg == 'OK'):
                        self.tableFrame.updateTable()
                        messagebox.showinfo('OK', 'Excluido Com Sucesso!')
                    else:
                        messagebox.showinfo('ERROR','Produto não pode ser removido.\nProvalmente consta nos registros que ja foram vendidos produtos'
                                                    ' desta compra, não podendo assim ser removido.')
# ===================================================================================================================
# CLASSE VIEW: ESTOQUE
# ===================================================================================================================
class ViewEstoque(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callCadProduto=cxMetodoComum[7]
        self.corFundo ='SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.manipdb=cxAtributoComum['db']
        # --------------------------------------------------------------------------------------------------------------
        # FRAMES INTERNOS
        # --------------------------------------------------------------------------------------------------------------
        self.tableFrame=TableEstoque(self,cxAtributoComum,cxMetodoComum)

        self.tableFrame.grid(row=0,column=0)

        self.interViewFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.01004),
                                       pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interViewFrame.grid(row=0, column=1,sticky=tk.N+tk.S)

        # --------------------------------------------------------------------------------------------------------------
        # CHAMADA DE MÉTODOS DE CONSTRUÇÃO DE WIDGETS
        # --------------------------------------------------------------------------------------------------------------
        #self.widgetsViewFrame()
        # --------------------------------------------------------------------------------------------------------------

    def widgetsViewFrame(self):
        width9=int(round(self.widthDefaultTopLevel*0.00468))
        width80=int(round(self.widthDefaultTopLevel*0.04166))

        self.bt_buscar = tk.Button(self.interViewFrame, text='Buscar', font=self.fonttypeComum, width=width9,
                                   height=2, relief=tk.GROOVE, bg=self.corFundo,state=tk.DISABLED)
        self.bt_buscar.grid(row=0, column=0)
        self.bt_editar = tk.Button(self.interViewFrame, text='Editar', font=self.fonttypeComum, width=width9, height=2,
                                   relief=tk.GROOVE, bg=self.corFundo,command=self.editar)
        self.bt_editar.grid(row=1, column=0)
        self.bt_excluir = tk.Button(self.interViewFrame, text='Excluir', font=self.fonttypeComum, width=width9, height=2,
                                    relief=tk.GROOVE, bg=self.corFundo, command=self.excluir)
        self.bt_excluir.grid(row=2, column=0)
        self.interViewFrame.grid_rowconfigure(0, pad=width80)
        self.interViewFrame.grid_rowconfigure(1, pad=width80)
        self.interViewFrame.grid_rowconfigure(2, pad=width80)
        self.interViewFrame.grid_rowconfigure(3, pad=width80)

    def setEstiloTreeview(self, fgTreeview, font, rowheight): # DEFINE ESTILO PARA QUALQUER TREEVIEW
         style=ttk.Style()
         style.configure("Treeview", foreground=fgTreeview,rowheight=rowheight) # DEFINE STYLO PARA A TREEVIEW
         style.configure("Treeview.Heading", foreground='black',font=font) # DEFINE ESTILO PARA OS INDICES DA TREEVIEW

    def editar(self):
        # --------------------------------------------------------------------------------------------------------------
        # SELECIONA E TRATA DADOS PARA OS ENTRYS DO EDITAR
        # --------------------------------------------------------------------------------------------------------------
        cod = self.tableFrame.eventSelect()
        listEditar=[cod[0],cod[1][0]] # COD E NOME

        sttemp=''
        for c in cod[1][1]: # PREÇO
            if(c == '.'): sttemp+=','
            else: sttemp+=c
        listEditar.append(sttemp)

        sttemp = ''
        for c in cod[1][2]:  # DESCRICAO
            if (c == '|'):
                sttemp += '\n'
            else:
                sttemp += c
        listEditar.append(sttemp)

        listEditar.append(cod[1][2]) # DESCRICAO

        self.callCadProduto(listEditar)

        # --------------------------------------------------------------------------------------------------------------

    def excluir(self):
        if messagebox.askokcancel('EXCLUIR','Esta Ação Será Permanente.\nDeseja Realmente Excluir?'):
            cod=self.tableFrame.eventSelect()[0]
            msg=self.manipdb.excluirProduto(cod)
            if(msg=='OK'):
                self.tableFrame.updateTable()
                messagebox.showinfo('OK','Excluido Com Sucesso!')
            else: messagebox.showinfo('ERRO','Erro Ao Remover')
# ===================================================================================================================
# ===================================================================================================================