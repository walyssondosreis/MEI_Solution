# coding: utf-8

# PROJECT: WALLBASE
# MODULE: tableframe
# DESCRIPTION: MÓDULO DA TABELA DE FILME (TARANTINO)
# AUTHOR: WALYSSON P. DOS REIS
# EMAIL: walyssondosreis@email.com

import tkinter as tk
import tkinter.ttk as ttk
import time

# ===================================================================================================================
# CLASSE TABLE: CLIENTE
# ===================================================================================================================
class TableCliente(tk.Frame):


    def __init__(self, TopLevel, cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self, TopLevel)
        # ---------------------------------------------------------------------------------------------------------------
        # CONFIGURAÇÔES DO TABLE FRAME
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #---------------------------------------------------------------------------------------------------------------
        self.Parent = TopLevel
        self.manipdb=cxAtributoComum['db']
        self.widthDefaultTopLevel = cxAtributoComum[0]
        self.heightDefaultTopLevel = cxAtributoComum[1]
        self.callbuscarClientePorCodigo=cxMetodoComum[6]
        # ---------------------------------------------------------------------------------------------------------------
        self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
        self.updateTable()
        #self.tv.selection_set('I001')
        #self.tv.state(statespec=['disabled','pressed'])
        #self.tv.focus_force()


    def criarTabela(self):

        # SCROLLS DA TABELA
        self.yScroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.yScroll.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.xScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.xScroll.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.tv = ttk.Treeview(self)
        self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
        self.tv['height']=int(round(self.heightDefaultTopLevel*0.051)) # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA

        self.tv['columns'] = ('nome','cpfcnpj', 'telefone', 'logradouro','cidade','estado','cep')
        self.tv.heading('#0', text='COD')
        width50=int(self.widthDefaultTopLevel*0.03472)
        width100=int(self.widthDefaultTopLevel*0.0694)
        self.tv.column('#0',minwidth=width50,width=width50,stretch=0)
        self.tv.heading('nome', text='NOME DO CLIENTE') #0
        self.tv.column('nome', anchor=tk.W,minwidth=width50*3,width=width100*3,stretch=0)
        self.tv.heading('cpfcnpj', text='CPF/CNPJ')
        self.tv.column('cpfcnpj', anchor=tk.W,minwidth=width50, width=int(width100*1.1),stretch=0)
        self.tv.heading('telefone', text='TELEFONE')
        self.tv.column('telefone', anchor=tk.W,minwidth=width50, width=width100,stretch=0)
        self.tv.heading('logradouro', text='ENDEREÇO')
        self.tv.column('logradouro', anchor=tk.W,minwidth=width50*3, width=int(width100*3.6),stretch=0)
        self.tv.heading('cidade',text='CIDADE')
        self.tv.column('cidade',anchor=tk.W,minwidth=int(self.widthDefaultTopLevel*0.06458), width=int(self.widthDefaultTopLevel*0.1319),stretch=0)
        self.tv.heading('estado', text='ESTADO')
        self.tv.column('estado', anchor=tk.CENTER, minwidth=int(self.widthDefaultTopLevel*0.02083), width=int(self.widthDefaultTopLevel*0.0416), stretch=0)
        self.tv.heading('cep', text='CEP')
        self.tv.column('cep', anchor=tk.W, minwidth=int(self.widthDefaultTopLevel*0.0243), width=int(self.widthDefaultTopLevel*0.0486), stretch=0)

        self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))

        self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
        self.tv.bind('<Return>',self.eventKeyEnter)
        self.tv.bind('<Double-Button-1>', self.eventKeyEnter)
        self.tv['xscrollcommand']=self.xScroll.set
        self.tv['yscrollcommand']=self.yScroll.set
        # ---------------------------------------------------------------------------------------------------------------
        # ! BINDING DOS SCROOLS
        self.yScroll['command'] =self.tv.yview  # EVENTO BINDING DA BARRA DE ROLAGEM VERTICAL (y)
        # ! TANTO O xviw() QUANTO O yview() SÃO METODOS DE COORDENADAS DO LISTBOX
        self.xScroll['command'] = self.tv.xview  # EVENTO BINDING DA BARRA DE ROLAGEM HORIZONTAL (x)
        #---------------------------------------------------------------------------------------------------------------
        #tuplateste=['1713','Walysson Pereira dos Reis','187.698.589-89','(38)992461716',
                          # 'Rua J 79 Dona Gregória','Montes Claros','MG','39403045']
        #self.InsertInTable(tuplateste)

    def InsertInTable(self,tupValuesIN):
        tupValues=[]
        for x in range(len(tupValuesIN)):
            if tupValuesIN[x]==None: tupValues.append('[VAZIO]')
            else: tupValues.append(tupValuesIN[x])

        self.tv.insert('', 'end', text='%s'%tupValues[0], tags=('REGISTRO'),
                             values=(tupValues[1],tupValues[2],tupValues[3],tupValues[4],tupValues[5],tupValues[6],tupValues[7]))

        self.tv.tag_configure('REGISTRO',background='white',font=('Trebuchet',int(round(self.widthDefaultTopLevel*0.00594)))) #testar fonte 11
        #int(round(self.widthDefaultTopLevel*0.00594))


    def deleteAllInTable(self):
        for x in self.tv.tag_has('REGISTRO'):
            self.tv.delete(x)
            #print(x)

    def updateTable(self):
        self.deleteAllInTable()
        consulta=self.manipdb.listarCliente()
        for tup in range(len(consulta)):
            self.InsertInTable(consulta[tup])

    def eventSelect(self,event=None):
        iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
        #mv=self.tv.item(iid,option='values')
        cod=self.tv.item(iid,option='text')
        mv=self.tv.item(iid,option='values')
        #print(self.tv.focus())
        #print(mv)
        return [cod,mv]

    def eventKeyEnter(self,event=None):
        try:
            #print('TA AQUI KEY ENTER')
            iid = self.tv.focus()  # RETORNA A iid DO ITEM EM FOCO
            # mv=self.tv.item(iid,option='values')
            cod = self.tv.item(iid, option='text')
            #print(cod)
            self.callbuscarClientePorCodigo(cod=cod)
            self.winfo_toplevel().destroy()
        except: pass #print('AQUI NÃO FUNFA')
# ===================================================================================================================
# CLASSE TABLE: FORNECEDOR
# ===================================================================================================================
class TableFornecedor(tk.Frame):


    def __init__(self, TopLevel, cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self, TopLevel)
        # ---------------------------------------------------------------------------------------------------------------
        # CONFIGURAÇÔES DO TABLE FRAME
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #---------------------------------------------------------------------------------------------------------------
        self.Parent = TopLevel
        self.manipdb=cxAtributoComum['db']
        self.widthDefaultTopLevel = cxAtributoComum[0]
        self.heightDefaultTopLevel = cxAtributoComum[1]
        self.callbuscarFornecedorPorCodigo = cxMetodoComum[6]
        # ---------------------------------------------------------------------------------------------------------------
        self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
        self.updateTable()

    def criarTabela(self):

        # SCROLLS DA TABELA
        self.yScroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.yScroll.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.xScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.xScroll.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.tv = ttk.Treeview(self)
        self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
        self.tv['height']=int(round(self.heightDefaultTopLevel*0.051)) # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA

        self.tv['columns'] = ('nome','cnpj', 'telefone', 'logradouro','cidade','estado','cep')
        self.tv.heading('#0', text='COD')
        width50=int(self.widthDefaultTopLevel*0.03472)
        width100=int(self.widthDefaultTopLevel*0.0694)
        self.tv.column('#0',anchor=tk.CENTER,minwidth=width50,width=width50,stretch=0)
        self.tv.heading('nome', text='RAZÃO SOCIAL') #0
        self.tv.column('nome', anchor=tk.W,minwidth=width50*3,width=width100*3,stretch=0)
        self.tv.heading('cnpj', text='CNPJ')
        self.tv.column('cnpj', anchor=tk.W,minwidth=width50, width=int(width100*1.1),stretch=0)
        self.tv.heading('telefone', text='TELEFONE')
        self.tv.column('telefone', anchor=tk.W,minwidth=width50, width=width100,stretch=0)
        self.tv.heading('logradouro', text='ENDEREÇO')
        self.tv.column('logradouro', anchor=tk.W,minwidth=width50*3, width=int(width100*3.6),stretch=0)
        self.tv.heading('cidade',text='CIDADE')
        self.tv.column('cidade',anchor=tk.W,minwidth=int(self.widthDefaultTopLevel*0.06458), width=int(self.widthDefaultTopLevel*0.1319),stretch=0)
        self.tv.heading('estado', text='ESTADO')
        self.tv.column('estado', anchor=tk.CENTER, minwidth=int(self.widthDefaultTopLevel*0.02083), width=int(self.widthDefaultTopLevel*0.0416), stretch=0)
        self.tv.heading('cep', text='CEP')
        self.tv.column('cep', anchor=tk.W, minwidth=int(self.widthDefaultTopLevel*0.0243), width=int(self.widthDefaultTopLevel*0.0486), stretch=0)

        self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))

        self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
        self.tv.bind('<Return>', self.eventKeyEnter)
        self.tv.bind('<Double-Button-1>', self.eventKeyEnter)
        self.tv['xscrollcommand']=self.xScroll.set
        self.tv['yscrollcommand']=self.yScroll.set
        # ---------------------------------------------------------------------------------------------------------------
        # ! BINDING DOS SCROOLS
        self.yScroll['command'] =self.tv.yview  # EVENTO BINDING DA BARRA DE ROLAGEM VERTICAL (y)
        # ! TANTO O xviw() QUANTO O yview() SÃO METODOS DE COORDENADAS DO LISTBOX
        self.xScroll['command'] = self.tv.xview  # EVENTO BINDING DA BARRA DE ROLAGEM HORIZONTAL (x)
        #---------------------------------------------------------------------------------------------------------------
        #tuplateste=['1713','Walysson Pereira dos Reis','187.698.589-89','(38)992461716',
                          # 'Rua J 79 Dona Gregória','Montes Claros','MG','39403045']
        #self.InsertInTable(tuplateste)

    def InsertInTable(self,tupValuesIN):
        tupValues=[]
        for x in range(len(tupValuesIN)):
            if tupValuesIN[x]==None: tupValues.append('[VAZIO]')
            else: tupValues.append(tupValuesIN[x])

        self.tv.insert('', 'end', text='%s'%tupValues[0], tags=('REGISTRO'),
                             values=(tupValues[1],tupValues[2],tupValues[3],tupValues[4],tupValues[5],tupValues[6],tupValues[7]))

        self.tv.tag_configure('REGISTRO',background='white',font=('Trebuchet',int(round(self.widthDefaultTopLevel*0.00594))))



    def deleteAllInTable(self):
        for x in self.tv.tag_has('REGISTRO'):
            self.tv.delete(x)
            #print(x)

    def updateTable(self):
        self.deleteAllInTable()
        consulta=self.manipdb.listarFornecedor()
        for tup in range(len(consulta)):
            self.InsertInTable(consulta[tup])

    def eventSelect(self,event=None):
        iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
        #mv=self.tv.item(iid,option='values')
        cod=self.tv.item(iid,option='text')
        mv=self.tv.item(iid,option='values')
        #print(mv)
        return [cod,mv]

    def eventKeyEnter(self,event=None):
        try:
            #print('TA AQUI KEY ENTER')
            iid = self.tv.focus()  # RETORNA A iid DO ITEM EM FOCO
            # mv=self.tv.item(iid,option='values')
            cod = self.tv.item(iid, option='text')
            #print(cod)
            self.callbuscarFornecedorPorCodigo(cod=cod)
            self.winfo_toplevel().destroy()
        except: pass #print('AQUI NÃO FUNFA')
# ===================================================================================================================
# CLASSE TABLE: PRODUTO
# ===================================================================================================================
class TableProduto(tk.Frame):


    def __init__(self, TopLevel, cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self, TopLevel)
        # ---------------------------------------------------------------------------------------------------------------
        # CONFIGURAÇÔES DO TABLE FRAME
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #---------------------------------------------------------------------------------------------------------------
        self.Parent = TopLevel
        self.manipdb=cxAtributoComum['db']
        self.widthDefaultTopLevel = cxAtributoComum[0]
        self.heightDefaultTopLevel = cxAtributoComum[1]
        self.callbuscarProdutoPorCodigo=cxMetodoComum[9]
        # ---------------------------------------------------------------------------------------------------------------
        self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
        self.updateTable()

    def criarTabela(self):

        # SCROLLS DA TABELA
        self.yScroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.yScroll.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.xScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.xScroll.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.tv = ttk.Treeview(self)
        self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
        self.tv['height']=int(round(self.heightDefaultTopLevel*0.051)) # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA

        self.tv['columns'] = ('nome','preco', 'descricao')
        self.tv.heading('#0', text='COD')
        width50=int(self.widthDefaultTopLevel*0.03472)
        width100=int(self.widthDefaultTopLevel*0.0694)
        self.tv.column('#0',minwidth=width50,width=width50,stretch=0)
        self.tv.heading('nome', text='NOME DO PRODUTO') #0
        self.tv.column('nome', anchor=tk.W,minwidth=width50*3,width=width100*4,stretch=0)
        self.tv.heading('preco', text='PREÇO (R$)')
        self.tv.column('preco', anchor=tk.CENTER,minwidth=width50, width=int(width100*1.0),stretch=0)
        self.tv.heading('descricao', text='DESCRIÇÃO')
        self.tv.column('descricao', anchor=tk.W,minwidth=width50, width=int(width100*7),stretch=0)


        self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))

        self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
        self.tv.bind('<Return>',self.eventKeyEnter)
        self.tv.bind('<Double-Button-1>',self.eventKeyEnter)
        self.tv['xscrollcommand']=self.xScroll.set
        self.tv['yscrollcommand']=self.yScroll.set
        # ---------------------------------------------------------------------------------------------------------------
        # ! BINDING DOS SCROOLS
        self.yScroll['command'] =self.tv.yview  # EVENTO BINDING DA BARRA DE ROLAGEM VERTICAL (y)
        # ! TANTO O xviw() QUANTO O yview() SÃO METODOS DE COORDENADAS DO LISTBOX
        self.xScroll['command'] = self.tv.xview  # EVENTO BINDING DA BARRA DE ROLAGEM HORIZONTAL (x)
        #---------------------------------------------------------------------------------------------------------------
        #tuplateste=['1713','Walysson Pereira dos Reis','187.698.589-89','(38)992461716',
                          # 'Rua J 79 Dona Gregória','Montes Claros','MG','39403045']
        #self.InsertInTable(tuplateste)

    def InsertInTable(self,tupValuesIN):
        tupValues=[]
        #print('TRATAR AQUI:',tupValuesIN[3])
        for x in range(len(tupValuesIN)-1):
            if tupValuesIN[x]==None: tupValues.append('[VAZIO]')
            else: tupValues.append(tupValuesIN[x])

        descIN=tupValuesIN[3]
        if descIN!=None:
            descOUT=''
            for p in range(len(descIN)):
                #print('DESCSUM:', descIN[p] + descIN[p + 1])
                #if descIN[p]=='\t': print('CHAR: O BARRA T')
                #if descIN[p] == '\n': print('CHAR: O BARRA N')
                #print('CHAR:',descIN[p])
                if descIN[p]=='\n': descOUT+='|'
                else: descOUT+=descIN[p]
            tupValues.append(descOUT)
        else: tupValues.append('')
        self.tv.insert('', 'end', text='%s'%tupValues[0], tags=('REGISTRO'),
                             values=(tupValues[1],tupValues[2],tupValues[3]))

        self.tv.tag_configure('REGISTRO',background='white',font=('Trebuchet',int(round(self.widthDefaultTopLevel*0.00594)))) #testar fonte 11
        #int(round(self.widthDefaultTopLevel*0.00594))


    def deleteAllInTable(self):
        for x in self.tv.tag_has('REGISTRO'):
            self.tv.delete(x)
            #print(x)

    def updateTable(self):
        self.deleteAllInTable()
        consulta=self.manipdb.listarProduto()
        #print(consulta)
        for tup in range(len(consulta)):
            self.InsertInTable(consulta[tup])

    def eventSelect(self,event=None):
        iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
        #mv=self.tv.item(iid,option='values')
        cod=self.tv.item(iid,option='text')
        mv=self.tv.item(iid,option='values')
        #print(mv)
        return [cod,mv]

    def eventKeyEnter(self,event=None):
        try:
            cod = self.eventSelect()[0]
            #print(cod)
        except:
            #print('NADA SELECIONADO NA TABELA!')
            return 0
        try:
            self.callbuscarProdutoPorCodigo(cod=cod)
            self.winfo_toplevel().destroy()
        except:
            pass
            #print('Este Evento Não É Chamado Por este Frame!')
# ===================================================================================================================
# CLASSE TABLE: CARRINHO DE COMPRAS E VENDAS
# ===================================================================================================================
class TableCarrinho(tk.Frame):


    def __init__(self, TopLevel, cxAtributoComum):
        tk.Frame.__init__(self, TopLevel)
        # ---------------------------------------------------------------------------------------------------------------
        # CONFIGURAÇÔES DO TABLE FRAME
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #---------------------------------------------------------------------------------------------------------------
        self.Parent = TopLevel
        self.manipdb=cxAtributoComum[2]
        self.widthDefaultTopLevel = cxAtributoComum[0]
        self.heightDefaultTopLevel = cxAtributoComum[1]
        # ---------------------------------------------------------------------------------------------------------------
        self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA


    def criarTabela(self):

        # SCROLLS DA TABELA
        self.yScroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.yScroll.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.xScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.xScroll.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.tv = ttk.Treeview(self)
        self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
        self.tv['height']=int(round(self.heightDefaultTopLevel*0.03825)) # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA


        style=ttk.Style()
        style.configure("Treeview", foreground='blue',rowheight=int(self.heightDefaultTopLevel*0.092)) # DEFINE STYLO PARA A TREEVIEW #int(self.heightDefaultTopLevel*0.092)
        style.configure("Treeview.Heading", foreground='black',
                        font=('Trebuchet',8,'bold')) # DEFINE ESTILO PARA OS INDICES DA TREEVIEW


        #self.tv['style'] = style
        self.tv['columns'] = ('produto','preco','qtd','total')
        self.tv.heading('#0', text='COD')
        width50=int(self.widthDefaultTopLevel*0.03472)
        width100=int(self.widthDefaultTopLevel*0.0694)
        self.tv.column('#0',minwidth=width50,width=int(width50*1.2),stretch=0,anchor=tk.CENTER)
        self.tv.heading('produto', text='Produto') #0
        self.tv.column('produto', anchor=tk.W,minwidth=width50*3,width=int(width100*5),stretch=0)
        self.tv.heading('preco', text='Preço UN')
        self.tv.column('preco', anchor=tk.CENTER,minwidth=width50, width=int(width100*1.0),stretch=0)
        self.tv.heading('qtd', text='QTD')
        self.tv.column('qtd', anchor=tk.CENTER,minwidth=width50, width=int(width100*1.5),stretch=0)
        self.tv.heading('total', text='Total')
        self.tv.column('total', anchor=tk.CENTER,minwidth=width50, width=int(width100*1.2),stretch=0)

        self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))

        self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
        self.tv['xscrollcommand']=self.xScroll.set
        self.tv['yscrollcommand']=self.yScroll.set
        # ---------------------------------------------------------------------------------------------------------------
        # ! BINDING DOS SCROOLS
        self.yScroll['command'] =self.tv.yview  # EVENTO BINDING DA BARRA DE ROLAGEM VERTICAL (y)
        # ! TANTO O xviw() QUANTO O yview() SÃO METODOS DE COORDENADAS DO LISTBOX
        self.xScroll['command'] = self.tv.xview  # EVENTO BINDING DA BARRA DE ROLAGEM HORIZONTAL (x)
        #---------------------------------------------------------------------------------------------------------------


    def InsertInTable(self,tupValues):

        self.tv.insert('', 'end', text='%s'%tupValues[0], tags=('REGISTRO'),
                             values=(tupValues[1],tupValues[2],tupValues[3],tupValues[4]))

        self.tv.tag_configure('REGISTRO',font=('Trebuchet',9))

    def deleteAllInTable(self):
        for x in self.tv.tag_has('REGISTRO'):
            self.tv.delete(x)
            #print(x)

    def deletePorIID(self,iid):
        self.tv.delete(iid)

    def capturaCodigosDaLista(self):
        rows = []
        for iid in self.tv.tag_has('REGISTRO'):
            cod = self.tv.item(iid, option='text')
            mv = self.tv.item(iid, option='values')
            rows.append([cod,mv[1],mv[2]])
        return rows


    def eventSelect(self,event=None):
        try:
            iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
            mv=self.tv.item(iid,option='values')
            return (iid, mv[3])
        except:
            return None
# ===================================================================================================================
# CLASSE TABLE: VENDA
# ===================================================================================================================
class TableVenda(tk.Frame):


    def __init__(self, TopLevel, cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self, TopLevel)
        # ---------------------------------------------------------------------------------------------------------------
        # CONFIGURAÇÔES DO TABLE FRAME
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #---------------------------------------------------------------------------------------------------------------
        self.Parent = TopLevel
        self.manipdb=cxAtributoComum['db']
        self.widthDefaultTopLevel = cxAtributoComum[0]
        self.heightDefaultTopLevel = cxAtributoComum[1]
        self.callInsertProdutosVenda=cxMetodoComum[0]
        self.callDeleteProdutosVenda=cxMetodoComum[1]
        # ---------------------------------------------------------------------------------------------------------------
        self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
        self.updateTable()
        #self.tv.selection_set('I001')
        #self.tv.state(statespec=['disabled','pressed'])
        #self.tv.focus_force()


    def criarTabela(self):

        # SCROLLS DA TABELA
        self.yScroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.yScroll.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.xScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.xScroll.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.tv = ttk.Treeview(self)
        self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
        self.tv['height']=int(round(self.heightDefaultTopLevel*0.051)) # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA

        self.tv['columns'] = ('data','nome', 'valor')
        self.tv.heading('#0', text='COD')
        width50=int(self.widthDefaultTopLevel*0.03472)
        width100=int(self.widthDefaultTopLevel*0.0694)
        self.tv.column('#0',minwidth=width50,width=width50,stretch=0)
        self.tv.heading('data', text='DATA') #0
        self.tv.column('data', anchor=tk.W,minwidth=width50*3,width=width100*1,stretch=0)
        self.tv.heading('nome', text='NOME DO CLIENTE')
        self.tv.column('nome', anchor=tk.W,minwidth=width50, width=int(width100*3.5),stretch=0)
        self.tv.heading('valor', text='VALOR')
        self.tv.column('valor', anchor=tk.W,minwidth=width50, width=width100,stretch=0)

        self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))

        self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
        self.tv['xscrollcommand']=self.xScroll.set
        self.tv['yscrollcommand']=self.yScroll.set
        # ---------------------------------------------------------------------------------------------------------------
        # ! BINDING DOS SCROOLS
        self.yScroll['command'] =self.tv.yview  # EVENTO BINDING DA BARRA DE ROLAGEM VERTICAL (y)
        # ! TANTO O xviw() QUANTO O yview() SÃO METODOS DE COORDENADAS DO LISTBOX
        self.xScroll['command'] = self.tv.xview  # EVENTO BINDING DA BARRA DE ROLAGEM HORIZONTAL (x)
        #---------------------------------------------------------------------------------------------------------------
        #tuplateste=['1713','Walysson Pereira dos Reis','187.698.589-89','(38)992461716',
                          # 'Rua J 79 Dona Gregória','Montes Claros','MG','39403045']
        #self.InsertInTable(tuplateste)

    def InsertInTable(self, tupValues):
        #print(tupValues)

        totaldevenda=0
        for vd in range(len(tupValues)-3):
            rowvd=tupValues[vd+3]
            totaldevenda+=int(rowvd[1])*float(rowvd[2])

        self.tv.insert('', 'end', text='%s'%tupValues[0], tags=('REGISTRO'),
                             values=(tupValues[1],tupValues[2],'%.2f'%totaldevenda))

        self.tv.tag_configure('REGISTRO',background='white',font=('Trebuchet',int(round(self.widthDefaultTopLevel*0.00594)))) #testar fonte 11
        #int(round(self.widthDefaultTopLevel*0.00594))


    def deleteAllInTable(self):
        for x in self.tv.tag_has('REGISTRO'):
            self.tv.delete(x)
            #print(x)

    def updateTable(self):
        self.deleteAllInTable()
        consulta=self.manipdb.listarVenda()
        print(consulta)
        for tup in range(len(consulta)):
            self.InsertInTable(consulta[tup])

    def eventSelect(self,event=None):
        iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
        mv=self.tv.item(iid,option='values')
        cod=self.tv.item(iid,option='text')
        self.callDeleteProdutosVenda()
        listaprodutoscompra=self.manipdb.buscarProdutosDaVendaPorCOD(cod)
        for produto in listaprodutoscompra:
            self.callInsertProdutosVenda(produto)
        #print(self.tv.focus())
        #print(mv)
        return [cod,mv]
# ===================================================================================================================
# CLASSE TABLE: COMPRA
# ===================================================================================================================
class TableCompra(tk.Frame):

        def __init__(self, TopLevel, cxAtributoComum, cxMetodoComum):
            tk.Frame.__init__(self, TopLevel)
            # ---------------------------------------------------------------------------------------------------------------
            # CONFIGURAÇÔES DO TABLE FRAME
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            # ---------------------------------------------------------------------------------------------------------------
            self.Parent = TopLevel
            self.manipdb = cxAtributoComum['db']
            self.widthDefaultTopLevel = cxAtributoComum[0]
            self.heightDefaultTopLevel = cxAtributoComum[1]
            self.callInsertProdutosCompra = cxMetodoComum[0]
            self.callDeleteProdutosVenda = cxMetodoComum[1]
            # ---------------------------------------------------------------------------------------------------------------
            self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
            self.updateTable()
            # self.tv.selection_set('I001')
            # self.tv.state(statespec=['disabled','pressed'])
            # self.tv.focus_force()

        def criarTabela(self):

            # SCROLLS DA TABELA
            self.yScroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
            self.yScroll.grid(row=0, column=1, sticky=tk.N + tk.S)
            self.xScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
            self.xScroll.grid(row=1, column=0, sticky=tk.E + tk.W)

            self.tv = ttk.Treeview(self)
            self.tv['selectmode'] = tk.BROWSE  # DEFINE O MODO DE SELEÇÃO DA TABELA
            self.tv['height'] = int(
                round(self.heightDefaultTopLevel * 0.051))  # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA

            self.tv['columns'] = ('data', 'nome', 'valor')
            self.tv.heading('#0', text='COD')
            width50 = int(self.widthDefaultTopLevel * 0.03472)
            width100 = int(self.widthDefaultTopLevel * 0.0694)
            self.tv.column('#0', minwidth=width50, width=width50, stretch=0)
            self.tv.heading('data', text='DATA')  # 0
            self.tv.column('data', anchor=tk.W, minwidth=width50 * 3, width=width100 * 1, stretch=0)
            self.tv.heading('nome', text='NOME DO FORNECEDOR')
            self.tv.column('nome', anchor=tk.W, minwidth=width50, width=int(width100 * 3.5), stretch=0)
            self.tv.heading('valor', text='VALOR')
            self.tv.column('valor', anchor=tk.W, minwidth=width50, width=width100, stretch=0)

            self.tv.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))

            self.tv.bind('<<TreeviewSelect>>', self.eventSelect)
            self.tv['xscrollcommand'] = self.xScroll.set
            self.tv['yscrollcommand'] = self.yScroll.set
            # ---------------------------------------------------------------------------------------------------------------
            # ! BINDING DOS SCROOLS
            self.yScroll['command'] = self.tv.yview  # EVENTO BINDING DA BARRA DE ROLAGEM VERTICAL (y)
            # ! TANTO O xviw() QUANTO O yview() SÃO METODOS DE COORDENADAS DO LISTBOX
            self.xScroll['command'] = self.tv.xview  # EVENTO BINDING DA BARRA DE ROLAGEM HORIZONTAL (x)
            # ---------------------------------------------------------------------------------------------------------------
            # tuplateste=['1713','Walysson Pereira dos Reis','187.698.589-89','(38)992461716',
            # 'Rua J 79 Dona Gregória','Montes Claros','MG','39403045']
            # self.InsertInTable(tuplateste)

        def InsertInTable(self, tupValues):
            # print(tupValues)

            totaldecompra = 0
            for vd in range(len(tupValues) - 3):
                rowvd = tupValues[vd + 3]
                totaldecompra += int(rowvd[1]) * float(rowvd[2])

            self.tv.insert('', 'end', text='%s' % tupValues[0], tags=('REGISTRO'),
                           values=(tupValues[1], tupValues[2], '%.2f' % totaldecompra))

            self.tv.tag_configure('REGISTRO', background='white', font=(
            'Trebuchet', int(round(self.widthDefaultTopLevel * 0.00594))))  # testar fonte 11
            # int(round(self.widthDefaultTopLevel*0.00594))

        def deleteAllInTable(self):
            for x in self.tv.tag_has('REGISTRO'):
                self.tv.delete(x)
                # print(x)

        def updateTable(self):
            self.deleteAllInTable()
            consulta = self.manipdb.listarCompra()
            print(consulta)
            for tup in range(len(consulta)):
                self.InsertInTable(consulta[tup])

        def eventSelect(self, event=None):
            iid = self.tv.focus()  # RETORNA A iid DO ITEM EM FOCO
            mv = self.tv.item(iid, option='values')
            cod = self.tv.item(iid, option='text')
            self.callDeleteProdutosVenda()
            listaprodutoscompra = self.manipdb.buscarProdutosDaCompraPorCOD(cod)
            for produto in listaprodutoscompra:
                self.callInsertProdutosCompra(produto)
            # print(self.tv.focus())
            # print(mv)
            return [cod, mv]
# ===================================================================================================================
# CLASSE TABLE: ESTOQUE
# ===================================================================================================================
class TableEstoque(tk.Frame):


    def __init__(self, TopLevel, cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self, TopLevel)
        # ---------------------------------------------------------------------------------------------------------------
        # CONFIGURAÇÔES DO TABLE FRAME
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #---------------------------------------------------------------------------------------------------------------
        self.Parent = TopLevel
        self.manipdb=cxAtributoComum['db']
        self.widthDefaultTopLevel = cxAtributoComum[0]
        self.heightDefaultTopLevel = cxAtributoComum[1]
        self.callbuscarProdutoPorCodigo=cxMetodoComum[9]
        # ---------------------------------------------------------------------------------------------------------------
        self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
        self.updateTable()

    def criarTabela(self):

        # SCROLLS DA TABELA
        self.yScroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.yScroll.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.xScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.xScroll.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.tv = ttk.Treeview(self)
        self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
        self.tv['height']=int(round(self.heightDefaultTopLevel*0.051)) # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA

        self.tv['columns'] = ('nome','qtd_comprado','qtd_vendido','qtd_estoque',
                              'preco_compra','preco_venda','per_lucro')
        self.tv.heading('#0', text='COD')
        width50=int(self.widthDefaultTopLevel*0.03472)
        width100=int(self.widthDefaultTopLevel*0.0694)
        self.tv.column('#0',anchor=tk.CENTER,minwidth=width50,width=int(width50+10),stretch=0)
        self.tv.heading('nome', text='NOME DO PRODUTO') #0
        self.tv.column('nome', anchor=tk.W,minwidth=width50*3,width=int(width100*5.7),stretch=0)
        self.tv.heading('qtd_comprado', text='QTD COMPRADO')
        self.tv.column('qtd_comprado', anchor=tk.CENTER,minwidth=width50, width=int(width100*1.2),stretch=0)
        self.tv.heading('qtd_vendido', text='QTD VENDIDO')
        self.tv.column('qtd_vendido', anchor=tk.CENTER,minwidth=width50, width=int(width100*1.2),stretch=0)
        self.tv.heading('qtd_estoque', text='QTD EM ESTOQUE')
        self.tv.column('qtd_estoque', anchor=tk.CENTER, minwidth=width50, width=int(width100 * 1.2), stretch=0)
        self.tv.heading('preco_compra', text='PREÇO DE COMPRA')
        self.tv.column('preco_compra', anchor=tk.E, minwidth=width50, width=int(width100 * 1.2), stretch=0)
        self.tv.heading('preco_venda', text='PREÇO DE VENDA')
        self.tv.column('preco_venda', anchor=tk.E, minwidth=width50, width=int(width100 * 1.2), stretch=0)
        self.tv.heading('per_lucro', text='LUCRO ATUAL')
        self.tv.column('per_lucro', anchor=tk.CENTER, minwidth=width50, width=int(width100 * 1.2), stretch=0)


        self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))

        self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
        self.tv.bind('<Return>',self.eventKeyEnter)
        self.tv.bind('<Double-Button-1>',self.eventKeyEnter)
        self.tv['xscrollcommand']=self.xScroll.set
        self.tv['yscrollcommand']=self.yScroll.set
        # ---------------------------------------------------------------------------------------------------------------
        # ! BINDING DOS SCROOLS
        self.yScroll['command'] =self.tv.yview  # EVENTO BINDING DA BARRA DE ROLAGEM VERTICAL (y)
        # ! TANTO O xviw() QUANTO O yview() SÃO METODOS DE COORDENADAS DO LISTBOX
        self.xScroll['command'] = self.tv.xview  # EVENTO BINDING DA BARRA DE ROLAGEM HORIZONTAL (x)
        #---------------------------------------------------------------------------------------------------------------
        #tuplateste=['1713','Walysson Pereira dos Reis','187.698.589-89','(38)992461716',
                          # 'Rua J 79 Dona Gregória','Montes Claros','MG','39403045']
        #self.InsertInTable(tuplateste)

    def InsertInTable(self, tupValues):


        self.tv.insert('', 'end', text='%s'%tupValues[0], tags=('REGISTRO'),
                             values=(tupValues[1],tupValues[2],tupValues[3],tupValues[4]
                                     , tupValues[5],tupValues[6],tupValues[7]))

        self.tv.tag_configure('REGISTRO',background='white',font=('Trebuchet',int(round(self.widthDefaultTopLevel*0.00594)))) #testar fonte 11
        #int(round(self.widthDefaultTopLevel*0.00594))


    def deleteAllInTable(self):
        for x in self.tv.tag_has('REGISTRO'):
            self.tv.delete(x)
            #print(x)

    def updateTable(self):
        self.deleteAllInTable()
        consulta=self.manipdb.listarEstoque()
        #['cod_produto','nome_produto','qtd_comprado','qtd_vendido','qtd_estoque','preco_compra','preco_venda',*'lucro_per']
        #print(consulta[0])
        for tup in range(len(consulta)):
            self.InsertInTable(consulta[tup])

    def eventSelect(self,event=None):
        iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
        #mv=self.tv.item(iid,option='values')
        cod=self.tv.item(iid,option='text')
        mv=self.tv.item(iid,option='values')
        #print(mv)
        return [cod,mv]

    def eventKeyEnter(self,event=None):
        try:
            cod = self.eventSelect()[0]
            #print(cod)
        except:
            #print('NADA SELECIONADO NA TABELA!')
            return 0
        try:
            self.callbuscarProdutoPorCodigo(cod=cod)
            self.winfo_toplevel().destroy()
        except:
            pass
            #print('Este Evento Não É Chamado Por este Frame!')
# ===================================================================================================================

# ===================================================================================================================
# CLASSE TABLES: HOME
# ===================================================================================================================
# class TableHomeTotalVendas(tk.Frame):
#
#
#     def __init__(self, TopLevel, cxAtributoComum,cxMetodoComum):
#         tk.Frame.__init__(self, TopLevel)
#         # ---------------------------------------------------------------------------------------------------------------
#         # CONFIGURAÇÔES DO TABLE FRAME
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight=1)
#         #---------------------------------------------------------------------------------------------------------------
#         self.Parent = TopLevel
#         self.manipdb=cxAtributoComum['db']
#         self.widthDefaultTopLevel = cxAtributoComum[0]
#         self.heightDefaultTopLevel = cxAtributoComum[1]
#         self.callbuscarProdutoPorCodigo=cxMetodoComum[9]
#         # ---------------------------------------------------------------------------------------------------------------
#         self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
#         self.updateTable()
#
#     def criarTabela(self):
#
#         self.tv = ttk.Treeview(self)
#         self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
#         self.tv['height']=13 # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA
#
#         self.tv['columns'] = ('totalmes')
#         self.tv.heading('#0', text='%d'%(time.localtime().tm_year))
#         width50=int(self.widthDefaultTopLevel*0.05472)
#         self.tv.column('#0',anchor=tk.CENTER,minwidth=width50,width=width50,stretch=0)
#         self.tv.heading('totalmes', text='VENDAS') #0
#         self.tv.column('totalmes', anchor=tk.E,minwidth=int(width50),width=width50,stretch=0)
#
#         self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))
#
#         self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
#         self.tv.bind('<Return>',self.eventKeyEnter)
#         self.tv.bind('<Double-Button-1>',self.eventKeyEnter)
#
#     def InsertInTable(self,tupValuesIN):
#         print(tupValuesIN)
#         tupValues=[]
#         if(tupValuesIN[0]==1):
#             tupValues.append('JAN')
#         elif (tupValuesIN[0]==2):
#             tupValues.append('FEV')
#         elif (tupValuesIN[0]==3):
#             tupValues.append('MAR')
#         elif (tupValuesIN[0]==4):
#             tupValues.append('ABR')
#         elif (tupValuesIN[0]==5):
#             tupValues.append('MAI')
#         elif (tupValuesIN[0]==6):
#             tupValues.append('JUN')
#         elif (tupValuesIN[0]==7):
#             tupValues.append('JUL')
#         elif (tupValuesIN[0]==8):
#             tupValues.append('AGO')
#         elif (tupValuesIN[0]==9):
#             tupValues.append('SET')
#         elif (tupValuesIN[0]==10):
#             tupValues.append('OUT')
#         elif (tupValuesIN[0]==11):
#             tupValues.append('NOV')
#         elif (tupValuesIN[0]==12):
#             tupValues.append('DEZ')
#
#
#         tupValues.append(tupValuesIN[1])
#         self.tv.insert('', 'end', text='%s'%tupValues[0], tags=('REGISTRO'),values=(tupValues[1]))
#
#         self.tv.tag_configure('REGISTRO',background='white',font=('Trebuchet',int(round(self.widthDefaultTopLevel*0.00594))))
#
#     def deleteAllInTable(self):
#         for x in self.tv.tag_has('REGISTRO'):
#             self.tv.delete(x)
#             #print(x)
#
#     def updateTable(self):
#         self.deleteAllInTable()
#         consulta=self.manipdb.totalVendasMensal()
#         #print(consulta)
#         for tup in range(len(consulta)):
#             self.InsertInTable(consulta[tup])
#
#     def eventSelect(self,event=None):
#         iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
#         #mv=self.tv.item(iid,option='values')
#         cod=self.tv.item(iid,option='text')
#         mv=self.tv.item(iid,option='values')
#         #print(mv)
#         return [cod,mv]
#
#     def eventKeyEnter(self,event=None):
#         try:
#             cod = self.eventSelect()[0]
#             #print(cod)
#         except:
#             #print('NADA SELECIONADO NA TABELA!')
#             return 0
#         try:
#             self.callbuscarProdutoPorCodigo(cod=cod)
#             self.winfo_toplevel().destroy()
#         except:
#             pass
#             #print('Este Evento Não É Chamado Por este Frame!')

class TableHomeTotalVendas(tk.Frame):


    def __init__(self, TopLevel, cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self, TopLevel)
        # ---------------------------------------------------------------------------------------------------------------
        # CONFIGURAÇÔES DO TABLE FRAME
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #---------------------------------------------------------------------------------------------------------------
        self.Parent = TopLevel
        self.manipdb=cxAtributoComum['db']
        self.widthDefaultTopLevel = cxAtributoComum[0]
        self.heightDefaultTopLevel = cxAtributoComum[1]
        self.callbuscarProdutoPorCodigo=cxMetodoComum[9]
        # ---------------------------------------------------------------------------------------------------------------
        self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
        self.updateTable()

    def criarTabela(self):

        self.tv = ttk.Treeview(self)
        self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
        self.tv['height']=2 # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA

        self.tv['columns'] = ('jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez')
        self.tv.heading('#0', text='')
        width50=int(self.widthDefaultTopLevel*0.05472)
        self.tv.column('#0',anchor=tk.CENTER,minwidth=width50,width=width50,stretch=0)
        self.tv.heading('jan', text='JAN') #0
        self.tv.column('jan', anchor=tk.CENTER,minwidth=int(width50),width=width50,stretch=0)
        self.tv.heading('fev', text='FEV')  # 0
        self.tv.column('fev', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('mar', text='MAR')  # 0
        self.tv.column('mar', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('abr', text='ABR')  # 0
        self.tv.column('abr', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('mai', text='MAI')  # 0
        self.tv.column('mai', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('jun', text='JUN')  # 0
        self.tv.column('jun', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('jul', text='JUL')  # 0
        self.tv.column('jul', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('ago', text='AGO')  # 0
        self.tv.column('ago', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('set', text='SET')  # 0
        self.tv.column('set', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('out', text='OUT')  # 0
        self.tv.column('out', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('nov', text='NOV')  # 0
        self.tv.column('nov', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('dez', text='DEZ')  # 0
        self.tv.column('dez', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)

        self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))

        self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
        self.tv.bind('<Return>',self.eventKeyEnter)
        self.tv.bind('<Double-Button-1>',self.eventKeyEnter)

    def InsertInTable(self,tupCon):
        #print(tupCon)
        tupValues={}
        for tupValuesIN in tupCon:
            if(tupValuesIN[0]==1):
                tupValues[1]=tupValuesIN[1]
            elif (tupValuesIN[0]==2):
                tupValues[2] = tupValuesIN[1]
            elif (tupValuesIN[0]==3):
                tupValues[3] = tupValuesIN[1]
            elif (tupValuesIN[0]==4):
                tupValues[4] = tupValuesIN[1]
            elif (tupValuesIN[0]==5):
                tupValues[5] = tupValuesIN[1]
            elif (tupValuesIN[0]==6):
                tupValues[6] = tupValuesIN[1]
            elif (tupValuesIN[0]==7):
                tupValues[7] = tupValuesIN[1]
            elif (tupValuesIN[0]==8):
                tupValues[8] = tupValuesIN[1]
            elif (tupValuesIN[0]==9):
                tupValues[9] = tupValuesIN[1]
            elif (tupValuesIN[0]==10):
                tupValues[10] = tupValuesIN[1]
            elif (tupValuesIN[0]==11):
                tupValues[11] = tupValuesIN[1]
            elif (tupValuesIN[0]==12):
                tupValues[12] = tupValuesIN[1]

        listAno=[]
        for x in range(1,13):
            try:
                listAno.append(tupValues[x])
            except:
                listAno.append('')
        #print(listAno)
        self.tv.insert('', 'end', text='%d'%(time.localtime().tm_year), tags=('REGISTRO'),values=(listAno[0],listAno[1],listAno[2],listAno[3],listAno[4],
                                                                           listAno[5],listAno[6],listAno[7],listAno[8],listAno[9],
                                                                           listAno[10],listAno[11],))

        self.tv.tag_configure('REGISTRO',background='white',font=('Trebuchet',int(round(self.widthDefaultTopLevel*0.00594))))

    def deleteAllInTable(self):
        for x in self.tv.tag_has('REGISTRO'):
            self.tv.delete(x)
            #print(x)

    def updateTable(self):
        self.deleteAllInTable()
        consulta=self.manipdb.totalVendasMensal()
        print(consulta)
        self.InsertInTable(consulta)

    def eventSelect(self,event=None):
        iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
        #mv=self.tv.item(iid,option='values')
        cod=self.tv.item(iid,option='text')
        mv=self.tv.item(iid,option='values')
        #print(mv)
        return [cod,mv]

    def eventKeyEnter(self,event=None):
        try:
            cod = self.eventSelect()[0]
            #print(cod)
        except:
            #print('NADA SELECIONADO NA TABELA!')
            return 0
        try:
            self.callbuscarProdutoPorCodigo(cod=cod)
            self.winfo_toplevel().destroy()
        except:
            pass
            #print('Este Evento Não É Chamado Por este Frame!')

class TableHomeTotalCompras(tk.Frame):


    def __init__(self, TopLevel, cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self, TopLevel)
        # ---------------------------------------------------------------------------------------------------------------
        # CONFIGURAÇÔES DO TABLE FRAME
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #---------------------------------------------------------------------------------------------------------------
        self.Parent = TopLevel
        self.manipdb=cxAtributoComum['db']
        self.widthDefaultTopLevel = cxAtributoComum[0]
        self.heightDefaultTopLevel = cxAtributoComum[1]
        self.callbuscarProdutoPorCodigo=cxMetodoComum[9]
        # ---------------------------------------------------------------------------------------------------------------
        self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
        self.updateTable()

    def criarTabela(self):

        self.tv = ttk.Treeview(self)
        self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
        self.tv['height']=2 # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA

        self.tv['columns'] = ('jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez')
        self.tv.heading('#0', text='')
        width50=int(self.widthDefaultTopLevel*0.05472)
        self.tv.column('#0',anchor=tk.CENTER,minwidth=width50,width=width50,stretch=0)
        self.tv.heading('jan', text='JAN') #0
        self.tv.column('jan', anchor=tk.CENTER,minwidth=int(width50),width=width50,stretch=0)
        self.tv.heading('fev', text='FEV')  # 0
        self.tv.column('fev', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('mar', text='MAR')  # 0
        self.tv.column('mar', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('abr', text='ABR')  # 0
        self.tv.column('abr', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('mai', text='MAI')  # 0
        self.tv.column('mai', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('jun', text='JUN')  # 0
        self.tv.column('jun', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('jul', text='JUL')  # 0
        self.tv.column('jul', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('ago', text='AGO')  # 0
        self.tv.column('ago', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('set', text='SET')  # 0
        self.tv.column('set', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('out', text='OUT')  # 0
        self.tv.column('out', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('nov', text='NOV')  # 0
        self.tv.column('nov', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('dez', text='DEZ')  # 0
        self.tv.column('dez', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)

        self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))

        self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
        self.tv.bind('<Return>',self.eventKeyEnter)
        self.tv.bind('<Double-Button-1>',self.eventKeyEnter)

    def InsertInTable(self,tupCon):
        #print(tupCon)
        tupValues={}
        for tupValuesIN in tupCon:
            if(tupValuesIN[0]==1):
                tupValues[1]=tupValuesIN[1]
            elif (tupValuesIN[0]==2):
                tupValues[2] = tupValuesIN[1]
            elif (tupValuesIN[0]==3):
                tupValues[3] = tupValuesIN[1]
            elif (tupValuesIN[0]==4):
                tupValues[4] = tupValuesIN[1]
            elif (tupValuesIN[0]==5):
                tupValues[5] = tupValuesIN[1]
            elif (tupValuesIN[0]==6):
                tupValues[6] = tupValuesIN[1]
            elif (tupValuesIN[0]==7):
                tupValues[7] = tupValuesIN[1]
            elif (tupValuesIN[0]==8):
                tupValues[8] = tupValuesIN[1]
            elif (tupValuesIN[0]==9):
                tupValues[9] = tupValuesIN[1]
            elif (tupValuesIN[0]==10):
                tupValues[10] = tupValuesIN[1]
            elif (tupValuesIN[0]==11):
                tupValues[11] = tupValuesIN[1]
            elif (tupValuesIN[0]==12):
                tupValues[12] = tupValuesIN[1]

        listAno=[]
        for x in range(1,13):
            try:
                listAno.append(tupValues[x])
            except:
                listAno.append('')
        #print(listAno)
        self.tv.insert('', 'end', text='%d'%(time.localtime().tm_year), tags=('REGISTRO'),values=(listAno[0],listAno[1],listAno[2],listAno[3],listAno[4],
                                                                           listAno[5],listAno[6],listAno[7],listAno[8],listAno[9],
                                                                           listAno[10],listAno[11],))

        self.tv.tag_configure('REGISTRO',background='white',font=('Trebuchet',int(round(self.widthDefaultTopLevel*0.00594))))

    def deleteAllInTable(self):
        for x in self.tv.tag_has('REGISTRO'):
            self.tv.delete(x)
            #print(x)

    def updateTable(self):
        self.deleteAllInTable()
        consulta=self.manipdb.totalComprasMensal()
        print(consulta)
        self.InsertInTable(consulta)

    def eventSelect(self,event=None):
        iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
        #mv=self.tv.item(iid,option='values')
        cod=self.tv.item(iid,option='text')
        mv=self.tv.item(iid,option='values')
        #print(mv)
        return [cod,mv]

    def eventKeyEnter(self,event=None):
        try:
            cod = self.eventSelect()[0]
            #print(cod)
        except:
            #print('NADA SELECIONADO NA TABELA!')
            return 0
        try:
            self.callbuscarProdutoPorCodigo(cod=cod)
            self.winfo_toplevel().destroy()
        except:
            pass
            #print('Este Evento Não É Chamado Por este Frame!')

class TableHomeTotalLucro(tk.Frame):


    def __init__(self, TopLevel, cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self, TopLevel)
        # ---------------------------------------------------------------------------------------------------------------
        # CONFIGURAÇÔES DO TABLE FRAME
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #---------------------------------------------------------------------------------------------------------------
        self.Parent = TopLevel
        self.manipdb=cxAtributoComum['db']
        self.widthDefaultTopLevel = cxAtributoComum[0]
        self.heightDefaultTopLevel = cxAtributoComum[1]
        self.callbuscarProdutoPorCodigo=cxMetodoComum[9]
        # ---------------------------------------------------------------------------------------------------------------
        self.criarTabela()  # METODO QUE IRÁ CRIAR A TABELA
        self.updateTable()

    def criarTabela(self):

        self.tv = ttk.Treeview(self)
        self.tv['selectmode']=tk.BROWSE # DEFINE O MODO DE SELEÇÃO DA TABELA
        self.tv['height']=2 # DEFINE A QUATIDADE DE LINHAS MOSTRADAS DA TABELA

        self.tv['columns'] = ('jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez')
        self.tv.heading('#0', text='')
        width50=int(self.widthDefaultTopLevel*0.05472)
        self.tv.column('#0',anchor=tk.CENTER,minwidth=width50,width=width50,stretch=0)
        self.tv.heading('jan', text='JAN') #0
        self.tv.column('jan', anchor=tk.CENTER,minwidth=int(width50),width=width50,stretch=0)
        self.tv.heading('fev', text='FEV')  # 0
        self.tv.column('fev', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('mar', text='MAR')  # 0
        self.tv.column('mar', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('abr', text='ABR')  # 0
        self.tv.column('abr', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('mai', text='MAI')  # 0
        self.tv.column('mai', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('jun', text='JUN')  # 0
        self.tv.column('jun', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('jul', text='JUL')  # 0
        self.tv.column('jul', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('ago', text='AGO')  # 0
        self.tv.column('ago', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('set', text='SET')  # 0
        self.tv.column('set', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('out', text='OUT')  # 0
        self.tv.column('out', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('nov', text='NOV')  # 0
        self.tv.column('nov', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)
        self.tv.heading('dez', text='DEZ')  # 0
        self.tv.column('dez', anchor=tk.CENTER, minwidth=int(width50), width=width50, stretch=0)

        self.tv.grid(row=0,column=0,sticky = (tk.N,tk.S,tk.W,tk.E))

        self.tv.bind('<<TreeviewSelect>>',self.eventSelect)
        self.tv.bind('<Return>',self.eventKeyEnter)
        self.tv.bind('<Double-Button-1>',self.eventKeyEnter)

    def InsertInTable(self,tupCon):
        #print(tupCon)
        tupValues={}
        for tupValuesIN in tupCon:
            if(tupValuesIN[0]==1):
                tupValues[1]=tupValuesIN[1]
            elif (tupValuesIN[0]==2):
                tupValues[2] = tupValuesIN[1]
            elif (tupValuesIN[0]==3):
                tupValues[3] = tupValuesIN[1]
            elif (tupValuesIN[0]==4):
                tupValues[4] = tupValuesIN[1]
            elif (tupValuesIN[0]==5):
                tupValues[5] = tupValuesIN[1]
            elif (tupValuesIN[0]==6):
                tupValues[6] = tupValuesIN[1]
            elif (tupValuesIN[0]==7):
                tupValues[7] = tupValuesIN[1]
            elif (tupValuesIN[0]==8):
                tupValues[8] = tupValuesIN[1]
            elif (tupValuesIN[0]==9):
                tupValues[9] = tupValuesIN[1]
            elif (tupValuesIN[0]==10):
                tupValues[10] = tupValuesIN[1]
            elif (tupValuesIN[0]==11):
                tupValues[11] = tupValuesIN[1]
            elif (tupValuesIN[0]==12):
                tupValues[12] = tupValuesIN[1]

        listAno=[]
        for x in range(1,13):
            try:
                listAno.append(tupValues[x])
            except:
                listAno.append('')
        #print(listAno)
        self.tv.insert('', 'end', text='%d'%(time.localtime().tm_year), tags=('REGISTRO'),values=(listAno[0],listAno[1],listAno[2],listAno[3],listAno[4],
                                                                           listAno[5],listAno[6],listAno[7],listAno[8],listAno[9],
                                                                           listAno[10],listAno[11],))

        self.tv.tag_configure('REGISTRO',background='white',font=('Trebuchet',int(round(self.widthDefaultTopLevel*0.00594))))

    def deleteAllInTable(self):
        for x in self.tv.tag_has('REGISTRO'):
            self.tv.delete(x)
            #print(x)

    def updateTable(self):
        self.deleteAllInTable()
        #consulta=self.manipdb.totalComprasMensal()
        #print(consulta)
        #self.InsertInTable(consulta)

    def eventSelect(self,event=None):
        iid = self.tv.focus() # RETORNA A iid DO ITEM EM FOCO
        #mv=self.tv.item(iid,option='values')
        cod=self.tv.item(iid,option='text')
        mv=self.tv.item(iid,option='values')
        #print(mv)
        return [cod,mv]

    def eventKeyEnter(self,event=None):
        try:
            cod = self.eventSelect()[0]
            #print(cod)
        except:
            #print('NADA SELECIONADO NA TABELA!')
            return 0
        try:
            self.callbuscarProdutoPorCodigo(cod=cod)
            self.winfo_toplevel().destroy()
        except:
            pass
            #print('Este Evento Não É Chamado Por este Frame!')