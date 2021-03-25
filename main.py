#TITLE: MEI SOLUTION
# AUTOR: Walysson dos Reis
# coding: utf-8

from cadframe import *
from viewframe import *
from meidb import *


class App():
    #===================================================================================================================
    # MÉTODO CONTRUTOR DO MAINFRAME
    #===================================================================================================================
    def __init__(self,toplevel):
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.corFundo='SystemWindow'
        self.widthDefaultTopLevel = toplevel.winfo_screenwidth() # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel = toplevel.winfo_screenheight() # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        #print(self.widthDefaultTopLevel, type(self.widthDefaultTopLevel))
        #print(self.heightDefaultTopLevel, type(self.heightDefaultTopLevel))
        # --------------------------------------------------------------------------------------------------------------
        # PARAMETROS DE LIGAÇÃO DE FRAMES
        # --------------------------------------------------------------------------------------------------------------
        self.cxAtributoComum = {'db':db(),0: self.widthDefaultTopLevel, 1: self.heightDefaultTopLevel}
        self.cxMetodoComum={0:self.enabledWidgetsBlock,1:self.selectLoginHome,2:self.selectCadCliente,3:self.selectViewCliente,
                            4:self.selectViewFornecedor,5:self.selectCadFornecedor,6:None,7:self.selectCadProduto,8:self.selectViewProduto,
                            9:None,10:self.selectViewHome}
        #---------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DA JANELA (TOPLEVEL)
        #---------------------------------------------------------------------------------------------------------------
        self.__topTk = toplevel # CRIA UMA VARIÁVEL DE ACESSO PARA OS METODOS DA CLASSE
        self.__topTk.resizable(width=True,height=True) # MET. QUE DETERMINA QUAIS EIXOS PODEM SER REDIMENSIONADOS AO MAXIMIZAR
        # toplevel.grid_rowconfigure(0, weight=1) # CENTRALIZA O GRID NAS LINHAS DA JANELA
        self.__topTk.grid_columnconfigure(0, weight=1)  # CENTRALIZA O GRID NAS colunas DA JANELA
        #toplevel.maxsize(400,350) # METODO QUE DEFINE O TAMANHO MAX DA JANELA
        self.__topTk.minsize(int(self.widthDefaultTopLevel*0.78125),int(self.heightDefaultTopLevel*0.925925)) # METODO QUE DEFINE O TAMANHO MIN DA JANELA
        self.__topTk.title('MEI SOLUTION') # MET. QUE DEFINE O TITULO DA JANELA
        #self.__topTk.wm_attributes("-alpha",0.95) # regula o nivel de opacidade da janela 0 - 1
        try: self.__topTk.wm_iconbitmap("bussIcon.ico") # TROCA ICONE DA JANELA PADRÃO TK
        except: self.__topTk.wm_iconbitmap(r".\images\bussIcon.ico")  # TROCA ICONE DA JANELA PADRÃO TK
        self.__topTk['bg']=self.corFundo
        self.__topTk.state('zoom')
        # --------------------------------------------------------------------------------------------------------------
        # FRAMES DA JANELA PRINCIPAL
        # --------------------------------------------------------------------------------------------------------------
        self.TopMenuBar = tk.Frame(self.__topTk) # FRAME DA BARRA DE MENU DO TOPO
        self.ExtFrame = tk.Frame(self.__topTk) # FRAME BARRA LATERAL (ACESSO RAPIDO) + FRAME DE TROCA

        # --------------------------------------------------------------------------------------------------------------
        self.TopMenuBar.grid(row=0,column=0,sticky=tk.W+tk.E)
        self.ExtFrame.grid(row=1, column=0,sticky=tk.W+tk.S+tk.N+tk.E)
        self.ExtFrame.grid_columnconfigure(1, weight=1) # FAZ O FRAME DE TROCA EXPANDIR
        #self.callAlterFrame() # METODO ESPECIAL PARA A CRIAÇÃO DA TELA QUE IRÁ ALTERNAR
        # --------------------------------------------------------------------------------------------------------------
        # MÉTODOS E ROTINAS PARA CONSTRUÇÃO DE WIDGETS E FRAMES
        # --------------------------------------------------------------------------------------------------------------
        self.__widgetsTopMenuBar()
        self.__widgetsLeftSideBar()
        self.selectLoginHome()
        #self.selectTransCadVenda()
        #self.selectCadCompra()
        #self.selectViewCompra()
        #self.selectViewHome()
        #self.selectViewProduto()
        #self.selectViewEstoque()
        #self.selectCadVenda()

        # --------------------------------------------------------------------------------------------------------------
    #===================================================================================================================
    # MÉTODOS PARA CRIAÇÃO DE WIDGETS DO MAINFRAME
    #===================================================================================================================
    def callAlterFrame(self):
        self.AlterFrame = tk.Frame(self.ExtFrame)
        self.AlterFrame.grid(row=0, column=1, sticky=tk.S + tk.N + tk.W + tk.E)
        self.AlterFrame.grid_rowconfigure(0, weight=1)  # FAZ O FRAME EXPANDIR LINHAS EM RELAÇÃO AO FRAME PAI
        self.AlterFrame.grid_columnconfigure(0, weight=1)  # FAZ O FRAME EXPANDIR COLUNAS EM RELAÇÃO AO FRAME PAI

    def __widgetsTopMenuBar(self):
        # MENU BUTTON (OPÇÕES PRINCIPAIS)
        self.topmenu_home = tk.Menubutton(self.TopMenuBar, text=('Inicio'), relief=tk.FLAT, padx=10)
        self.topmenu_home.grid(row=0, column=0)
        self.topmenu_home.bind('<Button-1>', self.selectViewHome)
        self.topmenu_transacao = tk.Menubutton(self.TopMenuBar, text=('Transação'), relief=tk.FLAT, padx=10)
        self.topmenu_transacao.grid(row=0, column=2)
        self.topmenu_view = tk.Menubutton(self.TopMenuBar, text=('Exibir'), relief=tk.FLAT,padx=10)
        self.topmenu_view.grid(row=0, column=3)
        self.topmenu_cadastrar = tk.Menubutton(self.TopMenuBar, text=('Cadastrar'), relief=tk.FLAT,padx=10)
        self.topmenu_cadastrar.grid(row=0, column=4)
        self.topmenu_relatorio = tk.Menubutton(self.TopMenuBar, text=('Relatório'), relief=tk.FLAT,padx=10)
        self.topmenu_relatorio.grid(row=0, column=5)
        self.topmenu_config = tk.Menubutton(self.TopMenuBar, text=('Configurações'), relief=tk.FLAT,padx=10)
        self.topmenu_config.grid(row=0, column=6)
        self.topmenu_ajuda = tk.Menubutton(self.TopMenuBar, text=('Ajuda'), relief=tk.FLAT,padx=10)
        self.topmenu_ajuda.grid(row=0, column=7)
        self.topmenu_sobre = tk.Menubutton(self.TopMenuBar, text=('Sobre'), relief=tk.FLAT, padx=10)
        self.topmenu_sobre.grid(row=0, column=8)
        self.topmenu_logout = tk.Menubutton(self.TopMenuBar, text=('Bloquear'), relief=tk.FLAT,padx=10)
        self.topmenu_logout.grid(row=0, column=9)
        self.topmenu_logout.bind('<Button-1>', self.selectLoginHome)
        self.topmenu_close = tk.Menubutton(self.TopMenuBar, text=('Sair'), relief=tk.FLAT,padx=10)
        self.topmenu_close.grid(row=0, column=10)
        self.topmenu_close.bind('<Button-1>',self.confirmClose)

        # ---------------------------------------------------------------------------------------------------------------
        self.menu_transacao = tk.Menu(self.topmenu_transacao, tearoff=0)
        self.menu_transacao.add_command(label='Realizar Venda', command=self.selectCadVenda)
        self.menu_transacao.add_separator()
        self.menu_transacao.add_command(label='Registrar Compra',command=self.selectCadCompra)
        self.menu_transacao.add_separator()
        self.menu_transacao.add_command(label='Registrar Despesa',state=tk.DISABLED)
        self.menu_transacao.add_separator()
        self.menu_transacao.add_command(label='Registrar Credito (à Receber)',state=tk.DISABLED)
        self.menu_transacao.add_separator()
        self.menu_transacao.add_command(label='Registrar Debito (à Pagar)',state=tk.DISABLED)
        self.topmenu_transacao['menu'] = self.menu_transacao
        # ---------------------------------------------------------------------------------------------------------------
        self.menu_view = tk.Menu(self.topmenu_view,tearoff=0)
        self.menu_view.add_command(label='Relação de Clientes',command=self.selectViewCliente)
        self.menu_view.add_separator()
        self.menu_view.add_command(label='Relação de Estoque',command=self.selectViewEstoque)
        self.menu_view.add_separator()
        self.menu_view.add_command(label='Relação de Fornecedores',command=self.selectViewFornecedor)
        self.menu_view.add_separator()
        self.menu_view.add_command(label='Relação de Produtos',command=self.selectViewProduto)
        self.menu_view.add_separator()
        self.menu_view.add_command(label='Relação de Compras',command=self.selectViewCompra)
        self.menu_view.add_separator()
        self.menu_view.add_command(label='Relação de Vendas', command=self.selectViewVenda)
        self.menu_view.add_separator()
        self.menu_view.add_command(label='Relação de Devedores',state=tk.DISABLED)
        self.menu_view.add_separator()
        self.menu_view.add_command(label='Relação de Credores',state=tk.DISABLED)
        self.topmenu_view['menu'] = self.menu_view

        # ---------------------------------------------------------------------------------------------------------------
        self.menu_cadastrar = tk.Menu(self.topmenu_cadastrar, tearoff=0)
        self.menu_cadastrar.add_command(label=' Cadastro de Cliente', command=self.selectCadCliente)
        self.menu_cadastrar.add_separator()
        self.menu_cadastrar.add_command(label='Cadastro de Fornecedor', command=self.selectCadFornecedor)
        self.menu_cadastrar.add_separator()
        self.menu_cadastrar.add_command(label='Cadastro de Produto', command=self.selectCadProduto)
        self.menu_cadastrar.add_separator()
        self.menu_cadastrar.add_command(label='Cadastro de Devedor', command=self.selectCadDevedor,state=tk.DISABLED)
        self.menu_cadastrar.add_separator()
        self.menu_cadastrar.add_command(label='Cadastro de Credor', command=self.selectCadCredor,state=tk.DISABLED)
        self.topmenu_cadastrar['menu'] = self.menu_cadastrar
        # ---------------------------------------------------------------------------------------------------------------
        self.menu_relatorio = tk.Menu(self.topmenu_relatorio, tearoff=0)
        self.menu_relatorio.add_command(label='Relatório de Vendas',state=tk.DISABLED)
        self.menu_relatorio.add_separator()
        self.menu_relatorio.add_command(label='Relatório de Compras',state=tk.DISABLED)
        self.menu_relatorio.add_separator()
        self.menu_relatorio.add_command(label='Relatório Contas à Receber',state=tk.DISABLED)
        self.menu_relatorio.add_separator()
        self.menu_relatorio.add_command(label='Relatório Contas à Pagar',state=tk.DISABLED)
        self.menu_relatorio.add_separator()
        self.menu_relatorio.add_command(label='Relatório Balanço Mensal',state=tk.DISABLED)
        self.topmenu_relatorio['menu'] = self.menu_relatorio
        # ---------------------------------------------------------------------------------------------------------------
        self.menu_config= tk.Menu(self.topmenu_config,tearoff=0)
        self.menu_config.add_command(label='Alterar Usuário',state=tk.DISABLED)
        self.menu_config.add_separator()
        self.menu_config.add_command(label='Alterar Senha',state=tk.DISABLED)
        self.topmenu_config['menu']=self.menu_config
        # ---------------------------------------------------------------------------------------------------------------

    def __widgetsLeftSideBar(self):
        # --------------------------------------------------------------------------------------------------------------
        # IMAGENS DOS BOTÕES
        # --------------------------------------------------------------------------------------------------------------
        sizeico=int(self.heightDefaultTopLevel*0.0641)
        self.img_refresh = Image.open(r".\images\home.png").resize((sizeico, sizeico), Image.ANTIALIAS)
        self.img_refresh = ImageTk.PhotoImage(self.img_refresh)
        self.img_vender = Image.open(r".\images\dollar.png").resize((sizeico, sizeico), Image.ANTIALIAS)
        self.img_vender = ImageTk.PhotoImage(self.img_vender)
        self.img_comprar = Image.open(r".\images\buy.png").resize((sizeico, sizeico), Image.ANTIALIAS)
        self.img_comprar = ImageTk.PhotoImage(self.img_comprar)
        self.img_cliente = Image.open(r".\images\useradd2.png").resize((sizeico, sizeico), Image.ANTIALIAS)
        self.img_cliente = ImageTk.PhotoImage(self.img_cliente)
        self.img_estoque = Image.open(r".\images\box2.png").resize((sizeico, sizeico), Image.ANTIALIAS)
        self.img_estoque = ImageTk.PhotoImage(self.img_estoque)
        self.img_logout = Image.open(r".\images\padlock3.png").resize((sizeico, sizeico), Image.ANTIALIAS)
        self.img_logout = ImageTk.PhotoImage(self.img_logout)
        self.img_close = Image.open(r".\images\close.png").resize((sizeico, sizeico), Image.ANTIALIAS)
        self.img_close = ImageTk.PhotoImage(self.img_close)
        # --------------------------------------------------------------------------------------------------------------
        # CANVAS BACKGROUND
        # --------------------------------------------------------------------------------------------------------------
        self.canvas_background=tk.Canvas(self.ExtFrame, width=self.widthDefaultTopLevel*0.0521,
                                         height=self.heightDefaultTopLevel * 0.9074, bg=self.corFundo,relief=tk.FLAT)
        self.canvas_background.grid(row=0,column=0,sticky=tk.N)
        # --------------------------------------------------------------------------------------------------------------
        # BOTÕES
        # --------------------------------------------------------------------------------------------------------------
        self.bt_refresh=tk.Button (image=self.img_refresh,height=sizeico, width=sizeico,relief=tk.FLAT,bg=self.corFundo,takefocus=0)
        self.bt_refresh.image=self.img_refresh
        self.bt_refresh['command'] = self.selectViewHome
        self.bt_vender = tk.Button(image=self.img_vender, height=sizeico, width=sizeico,relief=tk.FLAT,bg=self.corFundo,takefocus=0)
        self.bt_vender['command']=self.selectCadVenda
        self.bt_vender.image=self.img_vender
        self.bt_comprar = tk.Button(image=self.img_comprar, height=sizeico, width=sizeico, relief=tk.FLAT,bg=self.corFundo, takefocus=0)
        self.bt_comprar['command'] = self.selectCadCompra
        self.bt_comprar.image = self.img_comprar
        self.bt_cad = tk.Button(image=self.img_cliente, height=sizeico, width=sizeico,relief=tk.FLAT,bg=self.corFundo,takefocus=0)
        self.bt_cad.image=self.img_cliente
        self.bt_cad['command']=self.selectCadCliente
        self.bt_estoque = tk.Button(image=self.img_estoque, height=sizeico, width=sizeico,relief=tk.FLAT,bg=self.corFundo,takefocus=0)
        self.bt_estoque.image=self.img_estoque
        self.bt_estoque['command']=self.selectViewEstoque
        self.bt_logout = tk.Button(image=self.img_logout, height=sizeico, width=sizeico,relief=tk.FLAT,bg=self.corFundo,takefocus=0)
        self.bt_logout.image=self.img_logout
        self.bt_logout['command']=self.selectLoginHome
        self.bt_close = tk.Button(image=self.img_close, height=sizeico, width=sizeico,relief=tk.FLAT,bg=self.corFundo,takefocus=0)
        self.bt_close.image=self.img_close
        self.bt_close['command']=self.confirmClose
        # --------------------------------------------------------------------------------------------------------------
        # ATRIBUIÇÕES DOS BOTÕES NO CANVAS
        # --------------------------------------------------------------------------------------------------------------
        sizebtx=self.widthDefaultTopLevel*0.001166
        sizebty=self.heightDefaultTopLevel*0.046296
        self.canvas_background.create_window(sizebtx+5, sizebty, anchor=tk.W, window=self.bt_refresh)
        self.canvas_background.create_window(sizebtx+5, sizebty*3, anchor=tk.W, window=self.bt_vender)
        self.canvas_background.create_window(sizebtx + 5, sizebty * 5, anchor=tk.W, window=self.bt_comprar)
        self.canvas_background.create_window(sizebtx+5, sizebty*7, anchor=tk.W, window=self.bt_cad)
        self.canvas_background.create_window(sizebtx+5, sizebty*9, anchor=tk.W, window=self.bt_estoque)
        self.canvas_background.create_window(sizebtx+5, sizebty*11, anchor=tk.W, window=self.bt_logout)
        self.canvas_background.create_window(sizebtx+5, sizebty*13, anchor=tk.W, window=self.bt_close)
    #===================================================================================================================
    # MÉTODOS DE AÇÂO DO MAINFRAME
    #===================================================================================================================
    def enabledWidgetsBlock(self):

        self.topmenu_cadastrar['state'] = tk.NORMAL
        self.topmenu_home['state'] = tk.NORMAL
        self.topmenu_view['state'] = tk.ACTIVE
        self.topmenu_relatorio['state'] = tk.NORMAL
        self.topmenu_transacao['state'] = tk.NORMAL
        self.topmenu_config['state'] = tk.NORMAL
        self.topmenu_logout['state'] = tk.NORMAL
        self.bt_refresh['state'] = tk.NORMAL
        self.bt_vender['state'] = tk.NORMAL
        self.bt_comprar['state'] = tk.NORMAL
        self.bt_cad['state'] = tk.NORMAL
        self.bt_estoque['state'] = tk.NORMAL
        self.bt_logout['state'] = tk.NORMAL
    #===================================================================================================================
    # MÉTODOS PARA AS TELAS DE HOME/LOGIN/*CLOSE
    #===================================================================================================================
    def selectLoginHome(self,event=None):
        try: self.AlterFrame.destroy()
        except: pass
        # --------------------------------------------------------------------------------------------------------------
        # DESABILITA BOTÕES
        #-------------------------------------------------------------------------------------------------------------
        self.topmenu_cadastrar['state'] = tk.DISABLED
        self.topmenu_home['state'] = tk.DISABLED
        self.topmenu_view['state'] = tk.DISABLED
        self.topmenu_relatorio['state'] = tk.DISABLED
        self.topmenu_transacao['state'] = tk.DISABLED
        self.topmenu_config['state'] = tk.DISABLED
        self.topmenu_logout['state'] = tk.DISABLED
        self.bt_refresh['state'] = tk.DISABLED
        self.bt_vender['state'] = tk.DISABLED
        self.bt_comprar['state'] = tk.DISABLED
        self.bt_cad['state'] = tk.DISABLED
        self.bt_estoque['state'] = tk.DISABLED
        self.bt_logout['state'] = tk.DISABLED
        #-------------------------------------------------------------------------------------------------------------
        self.callAlterFrame()
        fr_LoginHome=ViewLogin(self.AlterFrame, self.cxAtributoComum, self.cxMetodoComum)
        fr_LoginHome.grid(row=0,column=0,sticky=tk.S+tk.N+tk.W+tk.E)

    def confirmClose(self,event=None):
        if messagebox.askokcancel('ENCERRAR','Deseja Realmente Encerrar O Programa?'):
            self.cxAtributoComum['db'].disconnect()
            self.__topTk.destroy()
    # ===================================================================================================================
    # MÉTODOS PARA AS TELAS DE TRANSAÇÃO
    # ===================================================================================================================
    def selectCadVenda(self, listaUpdate=''):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_cadVenda = CadVenda(self.AlterFrame, self.cxAtributoComum, self.cxMetodoComum)
        fr_cadVenda.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_cadVenda.grid_columnconfigure(0,weight=1)

    def selectCadCompra(self, listaUpdate=''):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_cadCompra = CadCompra(self.AlterFrame, self.cxAtributoComum, self.cxMetodoComum)
        fr_cadCompra.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_cadCompra.grid_columnconfigure(0,weight=1)

    def selectViewVenda(self):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_viewVenda = ViewVenda(self.AlterFrame, self.cxAtributoComum, self.cxMetodoComum)
        fr_viewVenda.widgetsViewFrame()
        fr_viewVenda.setEstiloTreeview('blue', ('Trebuchet', int(round(self.widthDefaultTopLevel* 0.00525)), 'bold'),
                                         int(self.heightDefaultTopLevel * 0.022))
        fr_viewVenda.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_viewVenda.grid_columnconfigure(0,weight=1)

    def selectViewCompra(self):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_viewCompra = ViewCompra(self.AlterFrame, self.cxAtributoComum, self.cxMetodoComum)
        fr_viewCompra.widgetsViewFrame()
        fr_viewCompra.setEstiloTreeview('blue', ('Trebuchet', int(round(self.widthDefaultTopLevel* 0.00525)), 'bold'),
                                         int(self.heightDefaultTopLevel * 0.022))
        fr_viewCompra.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_viewCompra.grid_columnconfigure(0,weight=1)
    #===================================================================================================================
    # MÉTODOS PARA AS TELAS DE CADASTRO
    #===================================================================================================================
    def selectCadCliente(self,listaUpdate=''):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_cadCliente = CadCliente(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        fr_cadCliente.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_cadCliente.grid_columnconfigure(0,weight=1)
        if listaUpdate!='': fr_cadCliente.updateCliente(listaUpdate)

    def selectCadFornecedor(self,listaUpdate=''):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_cadFornecedor = CadFornecedor(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        fr_cadFornecedor.grid(row=0, column=0, sticky=tk.S + tk.N + tk.W + tk.E)
        if listaUpdate != '': fr_cadFornecedor.updateFornecedor(listaUpdate)

    def selectCadProduto(self,listaUpdate=''):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_cadProduto = CadProduto(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        fr_cadProduto.grid(row=0, column=0, sticky=tk.S + tk.N + tk.W + tk.E)
        if listaUpdate != '': fr_cadProduto.updateProduto(listaUpdate)

    def selectCadDevedor(self):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_cadDevedor = CadDevedor(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        fr_cadDevedor.grid(row=0, column=0, sticky=tk.S + tk.N + tk.W + tk.E)

    def selectCadCredor(self):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_cadCredor = CadCredor(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        fr_cadCredor.grid(row=0, column=0, sticky=tk.S + tk.N + tk.W + tk.E)
    #===================================================================================================================
    # MÉTODOS PARA AS TELAS DE EXIBIÇÃO (VIEW)
    #===================================================================================================================
    def selectViewHome(self,event=None):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_viewHome = ViewHome(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        fr_viewHome.setEstiloTreeview('blue', ('Trebuchet', int(round(self.widthDefaultTopLevel* 0.00525)), 'bold'),
                                         int(self.heightDefaultTopLevel * 0.022))
        fr_viewHome.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_viewHome.grid_columnconfigure(0,weight=1)

    def selectViewCliente(self):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_viewCliente = ViewCliente(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        fr_viewCliente.widgetsViewFrame()
        fr_viewCliente.setEstiloTreeview('blue', ('Trebuchet', int(round(self.widthDefaultTopLevel* 0.00525)), 'bold'),
                                         int(self.heightDefaultTopLevel * 0.022))
        fr_viewCliente.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_viewCliente.grid_columnconfigure(0,weight=1)

    def selectViewFornecedor(self):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_viewFornecedor = ViewFornecedor(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        fr_viewFornecedor.widgetsViewFrame()
        fr_viewFornecedor.setEstiloTreeview('blue', ('Trebuchet', int(round(self.widthDefaultTopLevel * 0.00525)), 'bold'),
                                         int(self.heightDefaultTopLevel * 0.022))
        fr_viewFornecedor.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_viewFornecedor.grid_columnconfigure(0,weight=1)

    def selectViewProduto(self):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_viewProduto = ViewProduto(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        fr_viewProduto.widgetsViewFrame()
        fr_viewProduto.setEstiloTreeview('blue', ('Trebuchet', int(round(self.widthDefaultTopLevel * 0.00525)), 'bold'),
                                         int(self.heightDefaultTopLevel * 0.022))
        fr_viewProduto.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_viewProduto.grid_columnconfigure(0,weight=1)

    def selectViewEstoque(self):
        try: self.AlterFrame.destroy()
        except: pass
        self.callAlterFrame()
        fr_viewEstoque = ViewEstoque(self.AlterFrame,self.cxAtributoComum,self.cxMetodoComum)
        #fr_viewEstoque.widgetsViewFrame()
        fr_viewEstoque.setEstiloTreeview('blue', ('Trebuchet', int(round(self.widthDefaultTopLevel * 0.00525)), 'bold'),
                                         int(self.heightDefaultTopLevel * 0.022))
        fr_viewEstoque.grid(row=0, column=0,sticky=tk.S + tk.N + tk.W + tk.E)
        fr_viewEstoque.grid_columnconfigure(0,weight=1)

def closeApp():
    if messagebox.askokcancel('ENCERRAR',' Deseja realmente encerrar o programa?'):
        db().stopDBService()
        window.destroy() # ENCERRA A JANELA PRINCIPAL

window=tk.Tk()
App(window)
window.protocol("WM_DELETE_WINDOW",closeApp)
window.mainloop()

