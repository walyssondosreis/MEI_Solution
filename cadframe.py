#coding: utf-8

import datetime
from  viewframe import *

# ===================================================================================================================
# CLASSE CADASTRO: CLIENTE
# ===================================================================================================================
class CadCliente(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS ENTRE MODULOS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callHomeFrame=cxMetodoComum[10] # PERMITE O ACESSO AO MÉTODO selectLoginHome QUE BLOQUEIA O PROGRAMA
        self.callViewCliente=cxMetodoComum[3]
        self.corFundo = 'SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS ENTRE OS MÉTODOS DA CLASSE
        # --------------------------------------------------------------------------------------------------------------
        self.manip=cxAtributoComum['db']
        self.codCliente=''
        # --------------------------------------------------------------------------------------------------------------
        self.interCadFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.02604),
                                      pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interCadFrame.grid(row=0, column=0) # ,ipadx=int(self.widthDefaultTopLevel * 0.404),ipady=int(self.heightDefaultTopLevel * 0.3703)


        # METODOS PARA CONSTRUÇÃO DE WIDGETS
        self.widgets()
        # ------------------------------------------------------------------------------------------------------------

    def widgets(self):
        #---------------------------------------------------------------------------------------------------------------
        # LABELS
        #---------------------------------------------------------------------------------------------------------------
        self.lb_titulo=tk.Label(self.interCadFrame,text='CADASTRO DE CLIENTE',pady=10,bg=self.corFundo,
                                font=('REFSAN',int(self.heightDefaultTopLevel*0.014814),'bold','underline'),fg=self.fontfgComum)
        self.lb_nome=tk.Label(self.interCadFrame,text='Nome:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cpfORcnpj = tk.Label(self.interCadFrame, text='CPF/CNPJ:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_telefone = tk.Label(self.interCadFrame, text='Telefone:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_logradouro = tk.Label(self.interCadFrame, text='Rua Nº Bairro:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cidade = tk.Label(self.interCadFrame, text='Cidade:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_estado = tk.Label(self.interCadFrame, text='Estado:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cep = tk.Label(self.interCadFrame, text='CEP:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_status=tk.Label(self.interCadFrame, text='',pady=10,bg=self.corFundo,font=self.fonttypeComum+['bold'])
        #---------------------------------------------------------------------------------------------------------------
        order_lb=0; self.lb_titulo.grid(row=order_lb,column=0,columnspan=2)
        order_lb += 1; self.lb_nome.grid(row=order_lb,column=0,sticky=tk.W)
        order_lb+=1; self.lb_cpfORcnpj.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_telefone.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_logradouro.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_cidade.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_estado.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_cep.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1; self.lb_status.grid(row=order_lb, column=0, sticky=tk.W)
        #---------------------------------------------------------------------------------------------------------------
        # ENTRYS
        #---------------------------------------------------------------------------------------------------------------
        self.en_nome=tk.Entry(self.interCadFrame,width=60,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_nome.bind('<Key>', self.statusAction)
        self.en_cpfORcnpj = tk.Entry(self.interCadFrame, width=14,justify=tk.CENTER, bd=2, relief=tk.GROOVE, font=self.fonttypeComum,
                                     validate='key', validatecommand=(self.register(self.verificarCpf), '%P', '%d'))
        self.en_telefone = tk.Entry(self.interCadFrame, width=14, justify=tk.CENTER, bd=2, relief=tk.GROOVE, font=self.fonttypeComum,
                                    validate='key', validatecommand=(self.register(self.verificarTelefone), '%P', '%d'))
        self.en_logradouro = tk.Entry(self.interCadFrame, width=40,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_cidade = tk.Entry(self.interCadFrame, width=40,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_estado = tk.Entry(self.interCadFrame, width=9, justify=tk.CENTER, bd=2, relief=tk.GROOVE, font=self.fonttypeComum,
                                  validate='key', validatecommand=(self.register(self.verificarEstado), '%P', '%d'))
        self.en_cep = tk.Entry(self.interCadFrame, width=9,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum,
                                     validate='key', validatecommand=(self.register(self.verificarCEP), '%P', '%d'))
        # ---------------------------------------------------------------------------------------------------------------
        order_en=1; self.en_nome.grid(row=order_en,column=1)
        order_en+=1; self.en_cpfORcnpj.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_telefone.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_logradouro.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_cidade.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_estado.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_cep.grid(row=order_en, column=1,sticky=tk.W)
        # ---------------------------------------------------------------------------------------------------------------
        # BOTÕES DO FORMULÁRIO DE CADASTRO
        #---------------------------------------------------------------------------------------------------------------
        self.grdButton=tk.Frame(self.interCadFrame,bg=self.corFundo)
        self.grdButton.grid(row=order_lb + 1, column=1,sticky=tk.E+tk.W+tk.S+tk.N)
        self.grdButton.columnconfigure(0,weight=1)
        self.grdButton.columnconfigure(1, weight=1)
        self.grdButton.columnconfigure(2, weight=1)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar=tk.Button(self.grdButton,text='Salvar',width=10,font=self.fonttypeComum,command=self.salvar)
        self.bt_salvar.bind('<Return>',self.salvar)
        self.bt_cancelar=tk.Button(self.grdButton,text='Cancelar',width=10,font=self.fonttypeComum,command=self.cancelar)
        self.bt_sair=tk.Button(self.grdButton,text='Sair',width=10,font=self.fonttypeComum,command=self.sair)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar.grid(row=0,column=0)
        self.bt_cancelar.grid(row=0,column=1)
        self.bt_sair.grid(row=0,column=2)
        # ---------------------------------------------------------------------------------------------------------------

    def salvar(self,event=None):
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_nome.get() == '':
            messagebox.showwarning('AVISO', 'Nome Deve Ser Preenchido!')
            self.en_nome.focus_force()
            return 0
        elif self.somenteLetra(self.en_nome.get()):
            nome = self.en_nome.get().upper()
        else:
            messagebox.showwarning('AVISO', 'Nome Com Caracteres Inválidos!')
            self.en_nome.focus_force()
            return 0
        # ---------------------------------------------------------------------------------------------------------------
        if len(self.en_cpfORcnpj.get())==11:
            cpfcnpj=''
            for c in self.en_cpfORcnpj.get():
                if(len(cpfcnpj) in [3,7]): cpfcnpj+='.'
                if(len(cpfcnpj)==11): cpfcnpj+='-'
                cpfcnpj+=c

        elif len(self.en_cpfORcnpj.get())==14:
            cpfcnpj = ''
            for c in self.en_cpfORcnpj.get():
                if (len(cpfcnpj) in [2, 6]): cpfcnpj += '.'
                if (len(cpfcnpj) == 10): cpfcnpj += '/'
                if (len(cpfcnpj) == 15): cpfcnpj += '-'
                cpfcnpj += c
        else:
            messagebox.showwarning('AVISO', 'CPF/CNPJ Inválido!\nCPF Deve ter 11 Digitos\nCNPJ Deve ter 14 Digitos')
            self.en_cpfORcnpj.focus_force()
            return 0
        # ---------------------------------------------------------------------------------------------------------------
        if len(self.en_telefone.get()) == 10:
            telefone = ''
            for c in self.en_telefone.get():
                if (len(telefone) == 0): telefone += '('
                if (len(telefone) == 3): telefone += ')'
                if (len(telefone) == 8): telefone += '-'
                telefone += c

        elif len(self.en_telefone.get()) == 11:
            telefone =''
            for c in self.en_telefone.get():
                if (len(telefone) == 0): telefone += '('
                if (len(telefone) == 3): telefone += ')'
                if (len(telefone) == 9): telefone += '-'
                telefone += c
        elif self.en_telefone.get()=='':
            telefone = 'null'
        else:
            messagebox.showwarning('AVISO', 'Telefone Inválido!')
            self.en_telefone.focus_force()
            return 0
        # ---------------------------------------------------------------------------------------------------------------

        if self.en_logradouro.get() == '':
            logradouro = 'null'
        else:
            logradouro = self.en_logradouro.get().upper()
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_cidade.get() == '':
            cidade = 'null'
        elif self.somenteLetra(self.en_cidade.get()):
            cidade = self.en_cidade.get().upper()
        else:
            messagebox.showwarning('AVISO', 'Cidade Com Caracteres Inválidos!')
            self.en_cidade.focus_force()
            return 0
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_estado.get() == '':
            estado = 'null'
        else:
            estado = self.en_estado.get().upper()
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_cep.get() == '':
            cep = 'null'
        elif len(self.en_cep.get())<8:
            messagebox.showwarning('AVISO', 'CEP Inválido!\nCEP Deve ter 8 Digitos')
            self.en_cep.focus_force()
            return 0
        else:
            cep = ''
            for c in self.en_cep.get():
                if (len(cep) ==5): cep += '-'
                cep += c
        # ---------------------------------------------------------------------------------------------------------------
        if(self.codCliente!= ''):
            if messagebox.askokcancel('Alterar Dados', 'Esta Ação Será Permanente.\nDeseja Realmente Alterar?'):
                sts = self.manip.updateCliente(cod=self.codCliente, nome=nome, cpfcnpj=cpfcnpj, telefone=telefone,
                                         logradouro=logradouro, cidade=cidade, estado=estado, cep=cep)
            else: return 0
        else:
            sts = self.manip.gravarCliente(nome=nome, cpfcnpj=cpfcnpj, telefone=telefone,
                                 logradouro=logradouro, cidade=cidade, estado=estado, cep=cep)
        # ---------------------------------------------------------------------------------------------------------------
        self.lb_status['text'] = sts
        if (sts == 'SALVO!'):
            self.lb_status['fg'] = 'green'
            self.codCliente= ''
        else:
            self.lb_status['fg'] = 'red'
        # ---------------------------------------------------------------------------------------------------------------

    def updateCliente(self,listCliente):
        self.codCliente = listCliente[0]
        self.lb_titulo['text']='ATUALIZAR CLIENTE'
        self.en_nome.insert(0,listCliente[1])
        self.en_cpfORcnpj.insert(0, listCliente[2])
        self.en_telefone.insert(0, listCliente[3])
        self.en_logradouro.insert(0, listCliente[4])
        self.en_cidade.insert(0, listCliente[5])
        self.en_estado.insert(0, listCliente[6])
        self.en_cep.insert(0, listCliente[7])
        #print('ID NA CHAMADA UPDADE:', self.codCliente)

    def cancelar(self):
        self.en_nome.delete(0, tk.END)
        self.en_cpfORcnpj.delete(0, tk.END)
        self.en_telefone.delete(0, tk.END)
        self.en_logradouro.delete(0, tk.END)
        self.en_cidade.delete(0, tk.END)
        self.en_estado.delete(0, tk.END)
        self.en_cep.delete(0, tk.END)
        self.lb_status['text'] = ''
        self.codCliente= ''
        self.lb_titulo['text']='CADASTRO DE CLIENTE'

    def sair(self):
        if (self.lb_titulo['text']=='ATUALIZAR CLIENTE'):self.callViewCliente()
        else:self.callHomeFrame()

    def statusAction(self, event):
        if (self.lb_status['text'] != ''): self.cancelar()

    def verificarCpf(self, stgEntry, action):
       # try:
           # print('VALOR CHAR:',stgEntry)
       # except: pass

        #print('AÇÃO ENTRY:',action,type(action))
        if(action=='1'):
            if(len(stgEntry)>14):
                return False
            if(stgEntry[-1] in ('0','1','2','3','4','5','6','7','8','9')):
                return True
            else:
                messagebox.showwarning('AVISO!','Somente Números Por Favor!')
                return False

        elif action=='0':
            return True

    def verificarTelefone(self, stgEntry, action):
        #try:
           # print('VALOR CHAR:', stgEntry)
        #except:
            #pass

        #print('AÇÃO ENTRY:', action, type(action))
        if (action == '1'):
            if (len(stgEntry) > 11):
                return False
            if (stgEntry[-1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                return True
            else:
                messagebox.showwarning('AVISO!', 'Somente Números Por Favor!')
                return False

        elif action == '0':
            return True

    def verificarCEP(self, stgEntry, action):
        #try:
        #    print('VALOR CHAR:',stgEntry)
       # except: pass

       # print('AÇÃO ENTRY:',action,type(action))
        if(action=='1'):
            if(len(stgEntry)>8):
                return False
            if(stgEntry[-1] in ('0','1','2','3','4','5','6','7','8','9')):
                return True
            else:
                messagebox.showwarning('AVISO!','Somente Números Por Favor!')
                return False

        elif action=='0':
            return True

    def verificarEstado(self, stgEntry, action):
        #try:
            #print('VALOR CHAR:',stgEntry)
        #except: pass

        #print('AÇÃO ENTRY:',action,type(action))
        if(action=='1'):
            if(len(stgEntry)>2):
                return False
            if(stgEntry[-1].lower() in ('a','b','c','d','e','f','g','h','i','j','k','l','m',
                                'n','o','p','q','r','s','t','u','v','x','w','y','z','ç')):
                return True
            else:
                messagebox.showwarning('AVISO!','Somente Letras Por Favor!')
                return False

        elif action=='0':
            return True

    def somenteLetra(self,stgEntry):
        for c in stgEntry:
          #  print('VALOR DE C:',c)
            if(c.lower() in (' ','a','b','c','d','e','f','g','h','i','j','k','l','m',
                             'n','o','p','q','r','s','t','u','v','x','w','y','z','ç',
                             'ã','õ','â','ê','î','ô','û','à','è','ì','ò','ù','á','é','í','ó','ú',"'")):
                pass
            else: return False
        return True
# ===================================================================================================================
# CLASSE CADASTRO: FORNECEDOR
# ===================================================================================================================
class CadFornecedor(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callHomeFrame=cxMetodoComum[10] # PERMITE O ACESSO AO MÉTODO selectLoginHome QUE BLOQUEIA O PROGRAMA
        self.callViewFornecedor=cxMetodoComum[4]
        self.corFundo = 'SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.manip=cxAtributoComum['db']
        self.codFornecedor=''
        # --------------------------------------------------------------------------------------------------------------
        self.interCadFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.02604),
                                      pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interCadFrame.grid(row=0, column=0) # ,ipadx=int(self.widthDefaultTopLevel * 0.404),ipady=int(self.heightDefaultTopLevel * 0.3703)


        # METODOS PARA CONSTRUÇÃO DE WIDGETS
        self.widgets()
        # ------------------------------------------------------------------------------------------------------------

    def widgets(self):
        #---------------------------------------------------------------------------------------------------------------
        # LABELS
        #---------------------------------------------------------------------------------------------------------------
        self.lb_titulo=tk.Label(self.interCadFrame,text='CADASTRO DE FORNECEDOR',pady=10,bg=self.corFundo,
                                font=('REFSAN',int(self.heightDefaultTopLevel*0.014814),'bold','underline'),fg=self.fontfgComum)
        self.lb_nome=tk.Label(self.interCadFrame,text='Razão Social:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cnpj = tk.Label(self.interCadFrame, text='CNPJ:', pady=10, bg=self.corFundo, font=self.fonttypeComum)
        self.lb_telefone = tk.Label(self.interCadFrame, text='Telefone:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_logradouro = tk.Label(self.interCadFrame, text='Rua Nº Bairro:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cidade = tk.Label(self.interCadFrame, text='Cidade:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_estado = tk.Label(self.interCadFrame, text='Estado:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cep = tk.Label(self.interCadFrame, text='CEP:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_status=tk.Label(self.interCadFrame, text='',pady=10,bg=self.corFundo,font=self.fonttypeComum+['bold'])
        #---------------------------------------------------------------------------------------------------------------
        order_lb=0; self.lb_titulo.grid(row=order_lb,column=0,columnspan=2)
        order_lb += 1; self.lb_nome.grid(row=order_lb,column=0,sticky=tk.W)
        order_lb+=1; self.lb_cnpj.grid(row=order_lb, column=0, sticky=tk.W)
        order_lb += 1;self.lb_telefone.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_logradouro.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_cidade.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_estado.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_cep.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1; self.lb_status.grid(row=order_lb, column=0, sticky=tk.W)
        #---------------------------------------------------------------------------------------------------------------
        # ENTRYS
        #---------------------------------------------------------------------------------------------------------------
        self.en_nome=tk.Entry(self.interCadFrame,width=60,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_nome.bind('<Key>', self.statusAction)
        self.en_cnpj = tk.Entry(self.interCadFrame, width=14, justify=tk.CENTER, bd=2, relief=tk.GROOVE, font=self.fonttypeComum,
                                validate='key', validatecommand=(self.register(self.verificarCpf), '%P', '%d'))
        self.en_telefone = tk.Entry(self.interCadFrame, width=14, justify=tk.CENTER, bd=2, relief=tk.GROOVE, font=self.fonttypeComum,
                                    validate='key', validatecommand=(self.register(self.verificarTelefone), '%P', '%d'))
        self.en_logradouro = tk.Entry(self.interCadFrame, width=40,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_cidade = tk.Entry(self.interCadFrame, width=40,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_estado = tk.Entry(self.interCadFrame, width=9, justify=tk.CENTER, bd=2, relief=tk.GROOVE, font=self.fonttypeComum,
                                  validate='key', validatecommand=(self.register(self.verificarEstado), '%P', '%d'))
        self.en_cep = tk.Entry(self.interCadFrame, width=9,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum,
                                     validate='key', validatecommand=(self.register(self.verificarCEP), '%P', '%d'))
        # ---------------------------------------------------------------------------------------------------------------
        order_en=1; self.en_nome.grid(row=order_en,column=1)
        order_en+=1; self.en_cnpj.grid(row=order_en, column=1, sticky=tk.W)
        order_en += 1; self.en_telefone.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_logradouro.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_cidade.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_estado.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_cep.grid(row=order_en, column=1,sticky=tk.W)
        # ---------------------------------------------------------------------------------------------------------------
        # BOTÕES DO FORMULÁRIO DE CADASTRO
        #---------------------------------------------------------------------------------------------------------------
        self.grdButton=tk.Frame(self.interCadFrame,bg=self.corFundo)
        self.grdButton.grid(row=order_lb + 1, column=1,sticky=tk.E+tk.W+tk.S+tk.N)
        self.grdButton.columnconfigure(0,weight=1)
        self.grdButton.columnconfigure(1, weight=1)
        self.grdButton.columnconfigure(2, weight=1)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar=tk.Button(self.grdButton,text='Salvar',width=10,font=self.fonttypeComum,command=self.salvar)
        self.bt_salvar.bind('<Return>',self.salvar)
        self.bt_cancelar=tk.Button(self.grdButton,text='Cancelar',width=10,font=self.fonttypeComum,command=self.cancelar)
        self.bt_sair=tk.Button(self.grdButton,text='Sair',width=10,font=self.fonttypeComum,command=self.sair)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar.grid(row=0,column=0)
        self.bt_cancelar.grid(row=0,column=1)
        self.bt_sair.grid(row=0,column=2)
        # ---------------------------------------------------------------------------------------------------------------

    def salvar(self,event=None):
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_nome.get() == '':
            messagebox.showwarning('AVISO', 'Razão Social Deve Ser Preenchido!')
            self.en_nome.focus_force()
            return 0
        elif self.somenteLetra(self.en_nome.get()):
            nome = self.en_nome.get().upper()
        else:
            messagebox.showwarning('AVISO', 'Razão Social Com Caracteres Inválidos!')
            self.en_nome.focus_force()
            return 0
        # ---------------------------------------------------------------------------------------------------------------

        if len(self.en_cnpj.get())==14:
            cnpj = ''
            for c in self.en_cnpj.get():
                if (len(cnpj) in [2, 6]): cnpj += '.'
                if (len(cnpj) == 10): cnpj += '/'
                if (len(cnpj) == 15): cnpj += '-'
                cnpj += c
        else:
            messagebox.showwarning('AVISO', 'CNPJ Inválido!\nCNPJ Deve ter 14 Digitos')
            self.en_cnpj.focus_force()
            return 0
        # ---------------------------------------------------------------------------------------------------------------
        if len(self.en_telefone.get()) == 10:
            telefone = ''
            for c in self.en_telefone.get():
                if (len(telefone) == 0): telefone += '('
                if (len(telefone) == 3): telefone += ')'
                if (len(telefone) == 8): telefone += '-'
                telefone += c

        elif len(self.en_telefone.get()) == 11:
            telefone =''
            for c in self.en_telefone.get():
                if (len(telefone) == 0): telefone += '('
                if (len(telefone) == 3): telefone += ')'
                if (len(telefone) == 9): telefone += '-'
                telefone += c
        elif self.en_telefone.get()=='':
            telefone = 'null'
        else:
            messagebox.showwarning('AVISO', 'Telefone Inválido!')
            self.en_telefone.focus_force()
            return 0
        # ---------------------------------------------------------------------------------------------------------------

        if self.en_logradouro.get() == '':
            logradouro = 'null'
        else:
            logradouro = self.en_logradouro.get().upper()
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_cidade.get() == '':
            cidade = 'null'
        elif self.somenteLetra(self.en_cidade.get()):
            cidade = self.en_cidade.get().upper()
        else:
            messagebox.showwarning('AVISO', 'Cidade Com Caracteres Inválidos!')
            self.en_cidade.focus_force()
            return 0
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_estado.get() == '':
            estado = 'null'
        else:
            estado = self.en_estado.get().upper()
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_cep.get() == '':
            cep = 'null'
        elif len(self.en_cep.get())<8:
            messagebox.showwarning('AVISO', 'CEP Inválido!\nCEP Deve ter 8 Digitos')
            self.en_cep.focus_force()
            return 0
        else:
            cep = ''
            for c in self.en_cep.get():
                if (len(cep) ==5): cep += '-'
                cep += c
        # ---------------------------------------------------------------------------------------------------------------
        if(self.codFornecedor!= ''):
            if messagebox.askokcancel('Alterar Dados', 'Esta Ação Será Permanente.\nDeseja Realmente Alterar?'):
                sts = self.manip.updateFornecedor(cod=self.codFornecedor, nome=nome, cnpj=cnpj, telefone=telefone,
                                         logradouro=logradouro, cidade=cidade, estado=estado, cep=cep)
            else: return 0
        else:
            sts = self.manip.gravarFornecedor(nome=nome, cnpj=cnpj, telefone=telefone,
                                 logradouro=logradouro, cidade=cidade, estado=estado, cep=cep)
        # ---------------------------------------------------------------------------------------------------------------
        self.lb_status['text'] = sts
        if (sts == 'SALVO!'):
            self.lb_status['fg'] = 'green'
            self.codFornecedor= ''
        else:
            self.lb_status['fg'] = 'red'
        # ---------------------------------------------------------------------------------------------------------------

    def updateFornecedor(self, listFornecedor):
        self.codFornecedor = listFornecedor[0]
        self.lb_titulo['text']='ATUALIZAR FORNECEDOR'
        self.en_nome.insert(0, listFornecedor[1])
        self.en_cnpj.insert(0, listFornecedor[2])
        self.en_telefone.insert(0, listFornecedor[3])
        self.en_logradouro.insert(0, listFornecedor[4])
        self.en_cidade.insert(0, listFornecedor[5])
        self.en_estado.insert(0, listFornecedor[6])
        self.en_cep.insert(0, listFornecedor[7])
        #print('ID NA CHAMADA UPDADE:', self.codFornecedor)

    def cancelar(self):
        self.en_nome.delete(0, tk.END)
        self.en_cnpj.delete(0, tk.END)
        self.en_telefone.delete(0, tk.END)
        self.en_logradouro.delete(0, tk.END)
        self.en_cidade.delete(0, tk.END)
        self.en_estado.delete(0, tk.END)
        self.en_cep.delete(0, tk.END)
        self.lb_status['text'] = ''
        self.codFornecedor= ''
        self.lb_titulo['text']='CADASTRO DE CLIENTE'

    def sair(self):
        if (self.lb_titulo['text']=='ATUALIZAR FORNECEDOR'):self.callViewFornecedor()
        else:self.callHomeFrame()

    def statusAction(self, event):
        if (self.lb_status['text'] != ''): self.cancelar()

    def verificarCpf(self, stgEntry, action):
       # try:
           # print('VALOR CHAR:',stgEntry)
       # except: pass

        #print('AÇÃO ENTRY:',action,type(action))
        if(action=='1'):
            if(len(stgEntry)>14):
                return False
            if(stgEntry[-1] in ('0','1','2','3','4','5','6','7','8','9')):
                return True
            else:
                messagebox.showwarning('AVISO!','Somente Números Por Favor!')
                return False

        elif action=='0':
            return True

    def verificarTelefone(self, stgEntry, action):
        #try:
           # print('VALOR CHAR:', stgEntry)
        #except:
            #pass

        #print('AÇÃO ENTRY:', action, type(action))
        if (action == '1'):
            if (len(stgEntry) > 11):
                return False
            if (stgEntry[-1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                return True
            else:
                messagebox.showwarning('AVISO!', 'Somente Números Por Favor!')
                return False

        elif action == '0':
            return True

    def verificarCEP(self, stgEntry, action):
        #try:
        #    print('VALOR CHAR:',stgEntry)
       # except: pass

       # print('AÇÃO ENTRY:',action,type(action))
        if(action=='1'):
            if(len(stgEntry)>8):
                return False
            if(stgEntry[-1] in ('0','1','2','3','4','5','6','7','8','9')):
                return True
            else:
                messagebox.showwarning('AVISO!','Somente Números Por Favor!')
                return False

        elif action=='0':
            return True

    def verificarEstado(self, stgEntry, action):
        #try:
            #print('VALOR CHAR:',stgEntry)
        #except: pass

        #print('AÇÃO ENTRY:',action,type(action))
        if(action=='1'):
            if(len(stgEntry)>2):
                return False
            if(stgEntry[-1].lower() in ('a','b','c','d','e','f','g','h','i','j','k','l','m',
                                'n','o','p','q','r','s','t','u','v','x','w','y','z','ç')):
                return True
            else:
                messagebox.showwarning('AVISO!','Somente Letras Por Favor!')
                return False

        elif action=='0':
            return True

    def somenteLetra(self,stgEntry):
        for c in stgEntry:
          #  print('VALOR DE C:',c)
            if(c.lower() in (' ','a','b','c','d','e','f','g','h','i','j','k','l','m',
                             'n','o','p','q','r','s','t','u','v','x','w','y','z','ç',
                             'ã','õ','â','ê','î','ô','û','à','è','ì','ò','ù','á','é','í','ó','ú',"'",'-')):
                pass
            else: return False
        return True
# ===================================================================================================================
# CLASSE CADASTRO: PRODUTO
# ===================================================================================================================
class CadProduto(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callHomeFrame=cxMetodoComum[10] # PERMITE O ACESSO AO MÉTODO selectLoginHome QUE BLOQUEIA O PROGRAMA
        self.callViewProduto=cxMetodoComum[8]
        self.corFundo = 'SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.manip=cxAtributoComum['db']
        self.codProduto= ''
        # --------------------------------------------------------------------------------------------------------------
        self.interCadFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.02604),
                                      pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interCadFrame.grid(row=0, column=0) # ,ipadx=int(self.widthDefaultTopLevel * 0.404),ipady=int(self.heightDefaultTopLevel * 0.3703)


        # METODOS PARA CONSTRUÇÃO DE WIDGETS
        self.widgets()
        # ------------------------------------------------------------------------------------------------------------

    def widgets(self):
        #---------------------------------------------------------------------------------------------------------------
        # LABELS
        #---------------------------------------------------------------------------------------------------------------
        self.lb_titulo=tk.Label(self.interCadFrame,text='CADASTRO DE PRODUTO',pady=10,bg=self.corFundo,
                                font=('REFSAN',int(self.heightDefaultTopLevel*0.014814),'bold','underline'),fg=self.fontfgComum)
        self.lb_nome=tk.Label(self.interCadFrame,text='Nome:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_preco = tk.Label(self.interCadFrame, text='Preço de Venda:', pady=10, bg=self.corFundo, font=self.fonttypeComum)
        self.lb_descricao = tk.Label(self.interCadFrame, text='Descrição:', pady=10, bg=self.corFundo, font=self.fonttypeComum)
        self.lb_status=tk.Label(self.interCadFrame, text='',pady=10,bg=self.corFundo,font=self.fonttypeComum+['bold'])
        #---------------------------------------------------------------------------------------------------------------
        order_lb=0; self.lb_titulo.grid(row=order_lb,column=0,columnspan=2)
        order_lb += 1; self.lb_nome.grid(row=order_lb,column=0,sticky=tk.W)
        order_lb+=1; self.lb_preco.grid(row=order_lb, column=0, sticky=tk.W)
        order_lb += 1;self.lb_descricao.grid(row=order_lb, column=0, sticky=tk.W+tk.N)
        order_lb += 1; self.lb_status.grid(row=order_lb, column=0, sticky=tk.W)
        #---------------------------------------------------------------------------------------------------------------
        # ENTRYS E TEXTS
        #---------------------------------------------------------------------------------------------------------------
        self.en_nome=tk.Entry(self.interCadFrame,width=60,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_nome.bind('<Key>', self.statusAction)
        self.en_preco = tk.Entry(self.interCadFrame, width=14, justify=tk.CENTER, bd=2, relief=tk.GROOVE, font=self.fonttypeComum)
        # ---------------------------------------------------------------------------------------------------------------
        self.tx_descricao = tk.Text(self.interCadFrame, width=60,height=5, bd=2, relief=tk.GROOVE, font=self.fonttypeComum)

        # ---------------------------------------------------------------------------------------------------------------
        order_en=1; self.en_nome.grid(row=order_en,column=1)
        order_en+=1; self.en_preco.grid(row=order_en, column=1, sticky=tk.W)
        order_en += 1; self.tx_descricao.grid(row=order_en, column=1, sticky=tk.W)
        # ---------------------------------------------------------------------------------------------------------------
        # BOTÕES DO FORMULÁRIO DE CADASTRO
        #---------------------------------------------------------------------------------------------------------------
        self.grdButton=tk.Frame(self.interCadFrame,bg=self.corFundo)
        self.grdButton.grid(row=order_lb + 1, column=1,sticky=tk.E+tk.W+tk.S+tk.N)
        self.grdButton.columnconfigure(0,weight=1)
        self.grdButton.columnconfigure(1, weight=1)
        self.grdButton.columnconfigure(2, weight=1)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar=tk.Button(self.grdButton,text='Salvar',width=10,font=self.fonttypeComum,command=self.salvar)
        self.bt_salvar.bind('<Return>',self.salvar)
        self.bt_cancelar=tk.Button(self.grdButton,text='Cancelar',width=10,font=self.fonttypeComum,command=self.cancelar)
        self.bt_sair=tk.Button(self.grdButton,text='Sair',width=10,font=self.fonttypeComum,command=self.sair)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar.grid(row=0,column=0)
        self.bt_cancelar.grid(row=0,column=1)
        self.bt_sair.grid(row=0,column=2)
        # ---------------------------------------------------------------------------------------------------------------

    def salvar(self,event=None):
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_nome.get() == '':
            messagebox.showwarning('AVISO', 'Nome do Produto Deve Ser Informado!')
            self.en_nome.focus_force()
            return 0
        else:
            nome = self.en_nome.get().upper()
        # ---------------------------------------------------------------------------------------------------------------
        if self.en_preco.get()=='':
            messagebox.showwarning('AVISO', 'Preço Deve Ser Preenchido!')
            self.en_preco.focus_force()
            return 0
        elif self.verificarPreco(self.en_preco.get()):
            preco=''
            for c in self.en_preco.get():
                if c ==',': preco+='.'
                else: preco+=c
        else:
            messagebox.showwarning('AVISO', 'Preço Com Caracteres Inválidos!')
            self.en_preco.focus_force()
            return 0
        #print('PREÇO AQUI: ',preco)
        # ---------------------------------------------------------------------------------------------------------------
        if self.tx_descricao.get(0.0,tk.END)=='\n':
            descricao = 'null'
        else:
            descricao = self.tx_descricao.get(0.0, tk.END).upper()


        # ---------------------------------------------------------------------------------------------------------------
        if(self.codProduto!= ''):
            if messagebox.askokcancel('Alterar Dados', 'Esta Ação Será Permanente.\nDeseja Realmente Alterar?'):
                sts = self.manip.updateProduto(cod=self.codProduto, nome=nome, preco=preco,descricao=descricao)
            else: return 0
        elif self.lb_status['text']!='SALVO!':
            sts = self.manip.gravarProduto(nome=nome, preco=preco,descricao=descricao)
        else:
            messagebox.showwarning('AVISO','Produto JÁ Foi Salvo!')
        # ---------------------------------------------------------------------------------------------------------------
        self.lb_status['text'] = sts
        if (sts == 'SALVO!'):
            self.lb_status['fg'] = 'green'
            self.codProduto= ''
        else:
            self.lb_status['fg'] = 'red'
        # ---------------------------------------------------------------------------------------------------------------

    def updateProduto(self, listProduto):
        self.codProduto = listProduto[0]
        self.lb_titulo['text']='ATUALIZAR PRODUTO'
        self.en_nome.insert(0, listProduto[1])
        self.en_preco.insert(0, listProduto[2])
        self.tx_descricao.insert(0.0, listProduto[3])
        #print('ID NA CHAMADA UPDADE:', self.codProduto)

    def cancelar(self):
        self.en_nome.delete(0, tk.END)
        self.en_preco.delete(0, tk.END)
        self.tx_descricao.delete(0.0, tk.END)
        self.lb_status['text'] = ''
        self.codProduto= ''
        self.lb_titulo['text']='CADASTRO DE PRODUTO'

    def sair(self):
        if (self.lb_titulo['text']=='ATUALIZAR PRODUTO'):self.callViewProduto()
        else:self.callHomeFrame()

    def statusAction(self, event):
        if (self.lb_status['text'] != ''): self.cancelar()

    def verificarPreco(self, stgEntry):
        for c in stgEntry:
            #  print('VALOR DE C:',c)
            if (c.lower() in (' ', '0','1','2','3','4','5','6','7','8','9',',','.')):
                pass
            else:
                return False
        return True
# ===================================================================================================================
# CLASSE CADASTRO: DEVEDOR
# ===================================================================================================================
class CadDevedor(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.corFundo = 'SystemWindow'
        self.fonttypeComum = ('Trebuchet',int(self.heightDefaultTopLevel * 0.0111) )
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        self.interCadFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.02604),
                                      pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interCadFrame.grid(row=0, column=0) # ,ipadx=int(self.widthDefaultTopLevel * 0.404),ipady=int(self.heightDefaultTopLevel * 0.3703)


        # METODOS PARA CONSTRUÇÃO DE WIDGETS
        self.widgets()
        # ------------------------------------------------------------------------------------------------------------
    def widgets(self):
        #---------------------------------------------------------------------------------------------------------------
        # LABELS
        #---------------------------------------------------------------------------------------------------------------
        self.lb_titulo=tk.Label(self.interCadFrame,text='CADASTRO DE DEVEDOR',pady=10,bg=self.corFundo,
                                font=('REFSAN',int(self.heightDefaultTopLevel*0.014814),'bold','underline'),fg=self.fontfgComum)
        self.lb_nome=tk.Label(self.interCadFrame,text='Nome:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cpfORcnpj = tk.Label(self.interCadFrame, text='CPF/CNPJ:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_telefone = tk.Label(self.interCadFrame, text='Telefone:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_logradouro = tk.Label(self.interCadFrame, text='Rua Nº:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cidade = tk.Label(self.interCadFrame, text='Cidade:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_estado = tk.Label(self.interCadFrame, text='Estado:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cep = tk.Label(self.interCadFrame, text='CEP:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        #---------------------------------------------------------------------------------------------------------------
        order_lb=0; self.lb_titulo.grid(row=order_lb,column=0,columnspan=2)
        order_lb += 1; self.lb_nome.grid(row=order_lb,column=0,sticky=tk.W)
        order_lb+=1; self.lb_cpfORcnpj.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_telefone.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_logradouro.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_cidade.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_estado.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_cep.grid(row=order_lb, column=0,sticky=tk.W)
        #---------------------------------------------------------------------------------------------------------------
        # ENTRYS
        #---------------------------------------------------------------------------------------------------------------
        self.en_nome=tk.Entry(self.interCadFrame,width=60,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_cpfORcnpj = tk.Entry(self.interCadFrame, width=14,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_telefone = tk.Entry(self.interCadFrame, width=14,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_logradouro = tk.Entry(self.interCadFrame, width=40,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_cidade = tk.Entry(self.interCadFrame, width=40,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_estado = tk.Entry(self.interCadFrame, width=9,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_cep = tk.Entry(self.interCadFrame, width=9,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        # ---------------------------------------------------------------------------------------------------------------
        order_en=1; self.en_nome.grid(row=order_en,column=1)
        order_en+=1; self.en_cpfORcnpj.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_telefone.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_logradouro.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_cidade.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_estado.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_cep.grid(row=order_en, column=1,sticky=tk.W)
        # ---------------------------------------------------------------------------------------------------------------
        # BOTÕES DO FORMULÁRIO DE CADASTRO
        # ---------------------------------------------------------------------------------------------------------------
        self.grdButton = tk.Frame(self.interCadFrame, bg=self.corFundo)
        self.grdButton.grid(row=order_lb + 1, column=1, sticky=tk.E + tk.W + tk.S + tk.N)
        self.grdButton.columnconfigure(0, weight=1)
        self.grdButton.columnconfigure(1, weight=1)
        self.grdButton.columnconfigure(2, weight=1)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar = tk.Button(self.grdButton, text='Salvar', width=10, font=self.fonttypeComum)
        self.bt_cancelar = tk.Button(self.grdButton, text='Cancelar', width=10, font=self.fonttypeComum)
        self.bt_sair = tk.Button(self.grdButton, text='Sair', width=10, font=self.fonttypeComum)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar.grid(row=0, column=0)
        self.bt_cancelar.grid(row=0, column=1)
        self.bt_sair.grid(row=0, column=2)
        # ---------------------------------------------------------------------------------------------------------------
# ===================================================================================================================
# CLASSE CADASTRO: CREDOR
# ===================================================================================================================
class CadCredor(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS
        # --------------------------------------------------------------------------------------------------------------
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.corFundo = 'SystemWindow'
        self.fonttypeComum = ('Trebuchet',int(self.heightDefaultTopLevel * 0.0111) )
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        self.interCadFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.02604),
                                      pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo)
        self.interCadFrame.grid(row=0, column=0) # ,ipadx=int(self.widthDefaultTopLevel * 0.404),ipady=int(self.heightDefaultTopLevel * 0.3703)


        # METODOS PARA CONSTRUÇÃO DE WIDGETS
        self.widgets()
        # ------------------------------------------------------------------------------------------------------------
    def widgets(self):
        #---------------------------------------------------------------------------------------------------------------
        # LABELS
        #---------------------------------------------------------------------------------------------------------------
        self.lb_titulo=tk.Label(self.interCadFrame,text='CADASTRO DE CREDOR',pady=10,bg=self.corFundo,
                                font=('REFSAN',int(self.heightDefaultTopLevel*0.014814),'bold','underline'),fg=self.fontfgComum)
        self.lb_nome=tk.Label(self.interCadFrame,text='Nome:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cpfORcnpj = tk.Label(self.interCadFrame, text='CPF/CNPJ:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_telefone = tk.Label(self.interCadFrame, text='Telefone:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_logradouro = tk.Label(self.interCadFrame, text='Rua Nº:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cidade = tk.Label(self.interCadFrame, text='Cidade:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_estado = tk.Label(self.interCadFrame, text='Estado:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        self.lb_cep = tk.Label(self.interCadFrame, text='CEP:',pady=10,bg=self.corFundo,font=self.fonttypeComum)
        #---------------------------------------------------------------------------------------------------------------
        order_lb=0; self.lb_titulo.grid(row=order_lb,column=0,columnspan=2)
        order_lb += 1; self.lb_nome.grid(row=order_lb,column=0,sticky=tk.W)
        order_lb+=1; self.lb_cpfORcnpj.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_telefone.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_logradouro.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_cidade.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_estado.grid(row=order_lb, column=0,sticky=tk.W)
        order_lb += 1;self.lb_cep.grid(row=order_lb, column=0,sticky=tk.W)
        #---------------------------------------------------------------------------------------------------------------
        # ENTRYS
        #---------------------------------------------------------------------------------------------------------------
        self.en_nome=tk.Entry(self.interCadFrame,width=60,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_cpfORcnpj = tk.Entry(self.interCadFrame, width=14,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_telefone = tk.Entry(self.interCadFrame, width=14,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_logradouro = tk.Entry(self.interCadFrame, width=40,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_cidade = tk.Entry(self.interCadFrame, width=40,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_estado = tk.Entry(self.interCadFrame, width=9,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        self.en_cep = tk.Entry(self.interCadFrame, width=9,justify=tk.CENTER,bd=2,relief=tk.GROOVE,font=self.fonttypeComum)
        # ---------------------------------------------------------------------------------------------------------------
        order_en=1; self.en_nome.grid(row=order_en,column=1)
        order_en+=1; self.en_cpfORcnpj.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_telefone.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_logradouro.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_cidade.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_estado.grid(row=order_en, column=1,sticky=tk.W)
        order_en += 1; self.en_cep.grid(row=order_en, column=1,sticky=tk.W)
        # ---------------------------------------------------------------------------------------------------------------
        # BOTÕES DO FORMULÁRIO DE CADASTRO
        # ---------------------------------------------------------------------------------------------------------------
        self.grdButton = tk.Frame(self.interCadFrame, bg=self.corFundo)
        self.grdButton.grid(row=order_lb + 1, column=1, sticky=tk.E + tk.W + tk.S + tk.N)
        self.grdButton.columnconfigure(0, weight=1)
        self.grdButton.columnconfigure(1, weight=1)
        self.grdButton.columnconfigure(2, weight=1)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar = tk.Button(self.grdButton, text='Salvar', width=10, font=self.fonttypeComum)
        self.bt_cancelar = tk.Button(self.grdButton, text='Cancelar', width=10, font=self.fonttypeComum)
        self.bt_sair = tk.Button(self.grdButton, text='Sair', width=10, font=self.fonttypeComum)
        # ---------------------------------------------------------------------------------------------------------------
        self.bt_salvar.grid(row=0, column=0)
        self.bt_cancelar.grid(row=0, column=1)
        self.bt_sair.grid(row=0, column=2)
        # ---------------------------------------------------------------------------------------------------------------
# ===================================================================================================================
# CLASSE REALIZAR VENDA
# ===================================================================================================================
class CadVenda(tk.Frame):
    def __init__(self,TopLevel,cxAtributoComum,cxMetodoComum):
        tk.Frame.__init__(self,TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS ENTRE MODULOS
        # --------------------------------------------------------------------------------------------------------------
        self.cxAtributoComum=cxAtributoComum
        self.cxMetodoComum=cxMetodoComum
        self.cxMetodoComum[6]=self.buscarClientePorCodigo
        self.cxMetodoComum[9]=self.buscarProdutoPorCodigo
        self.widthDefaultTopLevel=cxAtributoComum[0] # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel=cxAtributoComum[1] # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callHomeFrame=cxMetodoComum[10] # PERMITE O ACESSO AO MÉTODO selectLoginHome QUE BLOQUEIA O PROGRAMA
        #self.callViewCliente=cxMetodoComum[3]
        self.corFundo = 'SystemWindow'
        self.fonttypeComum = ['Trebuchet',int(self.heightDefaultTopLevel * 0.0111) ]
        self.fontfgComum= 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0,weight=1)
        self['bg']=self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS ENTRE OS MÉTODOS DA CLASSE
        # --------------------------------------------------------------------------------------------------------------
        self.manip=cxAtributoComum['db']
        #self.codCliente=''
        # --------------------------------------------------------------------------------------------------------------
        # FRAME INTERNO
        # --------------------------------------------------------------------------------------------------------------
        self.interCadFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.02604),
                                      pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE, bg=self.corFundo,takefocus=0)
        self.interCadFrame.grid(row=0, column=0)
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------
        # METODOS PARA CONSTRUÇÃO DE WIDGETS
        self.widgetsInterFrame()
        #------------------------------------------------------------------------------------------------------------
        self.en_codCliente.focus_force()
        # HORA DA VENDA
        data=time.localtime()
        self.data_venda= '%02.d/%02.d/%d'%(data[2],data[1],data[0])
        self.en_data['state']=tk.NORMAL
        self.en_data.insert(0,self.data_venda)
        self.en_data['state']=tk.DISABLED
        # ------------------------------------------------------------------------------------------------------------

    def widgetsInterFrame(self):
        fontMin=['Trebuchet','8']
        # ------------------------------------------------------------------------------------------------------------
        # FRAMES
        # ------------------------------------------------------------------------------------------------------------
        interButtonFrame1 = tk.Frame(self.interCadFrame,bg=self.corFundo) # FRAME BASE BOTÕES INCLUIR E REMOVER
        interFormFrame = tk.Frame(self.interCadFrame,bg=self.corFundo) # FRAME BASE DA PARTE DE VALOR TOTAL E DATA COM SUAS ENTRYS
        interButtonFrame2 = tk.Frame(self.interCadFrame,bg=self.corFundo) # FRAME BASE PARA OS BOTÕES INFERIORES: CONFIRMAR, CANCELAR E SAIR
        self.interTableFrame = TableCarrinho(self.interCadFrame,[1050,200,self.manip]) # FRAME DA TABELA
        # ------------------------------------------------------------------------------------------------------------
        interButtonFrame1.rowconfigure(0, pad=30)
        self.interCadFrame.rowconfigure(7,pad=20)
        self.interCadFrame.rowconfigure(8, pad=30)
        interButtonFrame1.columnconfigure(0, pad=40)
        interFormFrame.columnconfigure([0, 1, 2, 3], weight=1)
        interButtonFrame2.columnconfigure([0, 1, 2, 3], weight=1)
        # ------------------------------------------------------------------------------------------------------------
        self.interTableFrame.grid(row=6, column=0, columnspan=4, sticky=tk.W + tk.E)
        interButtonFrame1.grid(row=6, column=4, sticky=tk.N + tk.S + tk.E + tk.W)
        interFormFrame.grid(row=7, column=2, sticky=tk.E + tk.W)
        interButtonFrame2.grid(row=8, column=2, sticky=tk.E + tk.W)
        # ------------------------------------------------------------------------------------------------------------
        # LABELS
        # ------------------------------------------------------------------------------------------------------------
        self.lb_titulo=tk.Label(self.interCadFrame, text='REALIZAR VENDA', pady=10, bg=self.corFundo,
                                font=('REFSAN',int(self.heightDefaultTopLevel*0.014814),'bold','underline'), fg=self.fontfgComum)
        lb_cliente = tk.Label(self.interCadFrame, text='Cliente:', font=self.fonttypeComum,bg=self.corFundo)
        lb_produto = tk.Label(self.interCadFrame, text='Produto:', font=self.fonttypeComum,bg=self.corFundo)
        lb_total = tk.Label(interFormFrame, text='Total:', font=self.fonttypeComum,bg=self.corFundo)
        lb_data = tk.Label(interFormFrame, text='Data:', font=self.fonttypeComum,bg=self.corFundo)
        lb_codCliente = tk.Label(self.interCadFrame, text='COD', font=fontMin, bg=self.corFundo)
        lb_nomeCliente = tk.Label(self.interCadFrame, text='NOME', font=fontMin, bg=self.corFundo)
        lb_codProduto = tk.Label(self.interCadFrame, text='COD', font=fontMin, bg=self.corFundo)
        lb_nomeProduto = tk.Label(self.interCadFrame, text='NOME', font=fontMin, bg=self.corFundo)
        lb_qtdProduto = tk.Label(self.interCadFrame, text='QTD', font=fontMin, bg=self.corFundo)
        lb_qtdEstoque = tk.Label(self.interCadFrame, text='ESTOQUE', font=fontMin, bg=self.corFundo)
        # ------------------------------------------------------------------------------------------------------------
        self.lb_titulo.grid(row=0, column=0, columnspan=5)
        lb_cliente.grid(row=2, column=0, sticky=tk.W)
        lb_produto.grid(row=5, column=0, sticky=tk.W)
        lb_total.grid(row=0, column=2, sticky=tk.E)
        lb_data.grid(row=0, column=0, sticky=tk.E)
        lb_codCliente.grid(row=1, column=1)
        lb_nomeCliente.grid(row=1, column=2)
        lb_qtdEstoque.grid(row=1,column=3)
        lb_codProduto.grid(row=4, column=1)
        lb_nomeProduto.grid(row=4, column=2)
        lb_qtdProduto.grid(row=4, column=3)
        # ------------------------------------------------------------------------------------------------------------
        # ENTRYS
        # ------------------------------------------------------------------------------------------------------------
        self.en_codCliente=tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, width=7, font=self.fonttypeComum,justify=tk.CENTER,
                                     validate='key', validatecommand=(self.register(self.verificarCOD), '%P', '%d'))
        self.en_codCliente.bind('<Return>',self.buscarClientePorCodigo)
        self.en_nomeCliente = tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=60,
                                       state=tk.DISABLED,disabledbackground=self.corFundo,disabledforeground='blue')
        self.en_codProduto = tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=7, justify=tk.CENTER,
                                     validate='key', validatecommand=(self.register(self.verificarCOD), '%P', '%d'))
        self.en_codProduto.bind('<Return>', self.buscarProdutoPorCodigo)
        self.en_nomeProduto = tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=60,
                                       state=tk.DISABLED,disabledbackground=self.corFundo,disabledforeground='blue')
        self.en_qtdProduto = tk.Entry(self.interCadFrame, bd=2,fg='blue', relief=tk.GROOVE, font=self.fonttypeComum, width=7, justify=tk.CENTER,
                                     validate='key', validatecommand=(self.register(self.verificarCOD), '%P', '%d'),
                                      state=tk.DISABLED,disabledbackground=self.corFundo,disabledforeground='blue')
        self.en_qtdProduto.bind('<Return>',self.incluirProduto)
        self.en_qtdEstoque = tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=7,
                                      justify=tk.CENTER,state=tk.DISABLED, disabledbackground=self.corFundo, disabledforeground='blue')
        self.en_total = tk.Entry(interFormFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=13,justify=tk.CENTER,
                                 state=tk.DISABLED,disabledbackground=self.corFundo,disabledforeground='blue')
        self.en_data = tk.Entry(interFormFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=10,justify=tk.CENTER,
                                state=tk.DISABLED,disabledbackground=self.corFundo,disabledforeground='dim gray')
        # ------------------------------------------------------------------------------------------------------------
        self.en_codCliente.grid(row=2, column=1)
        self.en_nomeCliente.grid(row=2, column=2)
        self.en_qtdEstoque.grid(row=2, column=3)
        self.en_codProduto.grid(row=5, column=1)
        self.en_nomeProduto.grid(row=5, column=2)
        self.en_qtdProduto.grid(row=5, column=3)
        self.en_total.grid(row=0, column=3, sticky=tk.W)
        self.en_data.grid(row=0, column=1, sticky=tk.W)
        # ------------------------------------------------------------------------------------------------------------
        # BUTTONS
        # ------------------------------------------------------------------------------------------------------------
        self.bt_buscarCliente=tk.Button(self.interCadFrame, text='Buscar Cliente', font=fontMin,
                                        width=14, relief=tk.GROOVE, bg=self.corFundo, command=self.buscarClienteWindow)
        self.bt_buscarCliente.bind('<Return>',self.buscarClienteWindow)
        self.bt_buscarProduto = tk.Button(self.interCadFrame, text='Buscar Produto', font=fontMin,
                                          width=14,relief=tk.GROOVE, bg=self.corFundo, command=self.buscarProdutoWindow)
        self.bt_buscarProduto.bind('<Return>', self.buscarProdutoWindow)
        self.bt_incluirProduto = tk.Button(interButtonFrame1, text='Incluir Produto', font=fontMin,width=14,relief=tk.GROOVE, bg=self.corFundo,
                                           command=self.incluirProduto)
        self.bt_incluirProduto.bind('<Return>',self.incluirProduto)
        self.bt_removerProduto = tk.Button(interButtonFrame1, text='Remover Produto', font=fontMin,width=14,relief=tk.GROOVE, bg=self.corFundo,
                                           command=self.removerProduto)
        self.bt_removerProduto.bind('<Return>', self.removerProduto)
        self.bt_salvar = tk.Button(interButtonFrame2, text='Confirmar', font=self.fonttypeComum,width=10,
                                   relief=tk.GROOVE, bg=self.corFundo,command=self.salvarVenda)
        self.bt_salvar.bind('<Return>', self.salvarVenda)
        self.bt_cancelar = tk.Button(interButtonFrame2, text='Cancelar', font=self.fonttypeComum,width=10,
                                     relief=tk.GROOVE, bg=self.corFundo,command=self.cancelar)
        self.bt_cancelar.bind('<Return>', self.cancelar)
        self.bt_sair = tk.Button(interButtonFrame2, text='Sair', font=self.fonttypeComum,width=10,
                                 relief=tk.GROOVE, bg=self.corFundo,command=self.sair)
        self.bt_sair.bind('<Return>', self.sair)
        # ------------------------------------------------------------------------------------------------------------
        self.bt_buscarCliente.grid(row=2, column=4)
        self.bt_buscarProduto.grid(row=5, column=4)
        self.bt_incluirProduto.grid(row=0, column=0)
        self.bt_removerProduto.grid(row=1, column=0)
        self.bt_salvar.grid(row=0, column=1)
        self.bt_cancelar.grid(row=0, column=2)
        self.bt_sair.grid(row=0, column=3)
        # ------------------------------------------------------------------------------------------------------------

    def buscarClienteWindow(self,event=None):
        win=tk.Tk()

        try: win.wm_iconbitmap("bussIcon.ico") # TROCA ICONE DA JANELA PADRÃO TK
        except: win.wm_iconbitmap(r".\images\bussIcon.ico")  # TROCA ICONE DA JANELA PADRÃO TK

        tb_clientebusca=ViewCliente(win,{0:int(self.widthDefaultTopLevel*0.915),1:int(self.heightDefaultTopLevel*0.2604),
                                         'db':self.manip},self.cxMetodoComum)
        win.focus_force()

        tb_clientebusca.grid()




    def buscarProdutoWindow(self,event=None):
        win=tk.Tk()
        try: win.wm_iconbitmap("bussIcon.ico") # TROCA ICONE DA JANELA PADRÃO TK
        except: win.wm_iconbitmap(r".\images\bussIcon.ico")  # TROCA ICONE DA JANELA PADRÃO TK
        tb_produtobusca=ViewProduto(win,{0:int(self.widthDefaultTopLevel*0.915),1:int(self.heightDefaultTopLevel*0.2604),
                                         'db':self.manip},self.cxMetodoComum)
        tb_produtobusca.grid()

    def buscarClientePorCodigo(self,event=None,cod=''):

        if cod=='': # CHAMNDO DA DIRETO DA CAIXA ENTRY
            if(self.en_codCliente.get()==''):
                self.buscarClienteWindow()
                return 0
            cod=self.en_codCliente.get()
            res=self.manip.buscaClientePorCod(cod)

            if (res == None):
                messagebox.showwarning('Aviso', 'Cliente Não Cadastrado!')
                self.en_nomeCliente['state'] = tk.NORMAL
                self.en_codCliente.delete(0, tk.END)
                self.en_nomeCliente.delete(0, tk.END)
                self.en_nomeCliente['state'] = tk.DISABLED
                return 0
            if (res == 'ERROSQL'):
                messagebox.showwarning('Aviso', 'Falha Ao Buscar No Banco De Dados!')
                self.en_nomeCliente['state'] = tk.NORMAL
                self.en_codCliente.delete(0, tk.END)
                self.en_nomeCliente.delete(0, tk.END)
                self.en_nomeCliente['state'] = tk.DISABLED
                return 0
            self.en_nomeCliente['state'] = tk.NORMAL
            self.en_nomeCliente.delete(0,tk.END)
            self.en_nomeCliente.insert(0,res[0])
            self.en_nomeCliente['state'] = tk.DISABLED
            self.en_codProduto.focus_force()
        else:
            res=self.manip.buscaClientePorCod(cod)
            self.en_nomeCliente['state']=tk.NORMAL
            self.en_nomeCliente.delete(0,tk.END)
            self.en_nomeCliente.insert(0,res[0])
            self.en_nomeCliente['state'] = tk.DISABLED
            self.en_codCliente.delete(0, tk.END)
            self.en_codCliente.insert(0, cod)
            self.en_codProduto.focus_force()

    def buscarProdutoPorCodigo(self,event=None,cod=''):

        if cod=='': # CHAMNDO DA DIRETO DA CAIXA ENTRY
            if(self.en_codProduto.get()==''):
                self.buscarProdutoWindow()
                return 0
            cod=self.en_codProduto.get()
            res=self.manip.buscaProdutoPorCod(cod)
            print(res)

            if (res == None):
                messagebox.showwarning('Aviso', 'Produto Não Cadastrado!')
                self.en_nomeProduto['state'] = tk.NORMAL
                self.en_qtdProduto['state'] = tk.NORMAL
                self.en_qtdEstoque['state'] = tk.NORMAL
                self.en_codProduto.delete(0, tk.END)
                self.en_nomeProduto.delete(0, tk.END)
                self.en_qtdProduto.delete(0, tk.END)
                self.en_qtdEstoque.delete(0,tk.END)
                self.en_qtdEstoque['state'] = tk.DISABLED
                self.en_nomeProduto['state'] = tk.DISABLED
                self.en_qtdProduto['state']=tk.DISABLED
                return 0
            if (res == 'ERROSQL'):
                messagebox.showwarning('Aviso', 'Falha Ao Buscar No Banco De Dados!')
                self.en_nomeProduto['state'] = tk.NORMAL
                self.en_qtdProduto['state'] = tk.NORMAL
                self.en_qtdEstoque['state'] = tk.NORMAL
                self.en_codProduto.delete(0, tk.END)
                self.en_nomeProduto.delete(0, tk.END)
                self.en_qtdProduto.delete(0, tk.END)
                self.en_qtdEstoque.delete(0, tk.END)
                self.en_qtdEstoque['state'] = tk.DISABLED
                self.en_nomeProduto['state'] = tk.DISABLED
                self.en_qtdProduto['state'] = tk.DISABLED
                return 0
            self.en_nomeProduto['state'] = tk.NORMAL
            self.en_qtdProduto['state'] = tk.NORMAL
            self.en_qtdEstoque['state'] = tk.NORMAL
            self.en_qtdProduto.delete(0,tk.END)
            self.en_qtdProduto.focus_force()
            self.en_nomeProduto.delete(0,tk.END)
            self.en_qtdEstoque.delete(0, tk.END)
            self.en_nomeProduto.insert(0,res[0])
            self.en_qtdEstoque.insert(0, res[3])
            self.en_qtdEstoque['state'] = tk.DISABLED
            self.en_nomeProduto['state'] = tk.DISABLED
        else:
            res = self.manip.buscaProdutoPorCod(cod)
            self.en_nomeProduto['state']=tk.NORMAL
            self.en_qtdProduto['state'] = tk.NORMAL
            self.en_qtdEstoque['state'] = tk.NORMAL
            self.en_nomeProduto.delete(0,tk.END)
            self.en_qtdEstoque.delete(0, tk.END)
            self.en_qtdProduto.delete(0, tk.END)
            self.en_qtdProduto.focus_force()
            self.en_nomeProduto.insert(0,res[0])
            self.en_qtdEstoque.insert(0, res[3])
            self.en_nomeProduto['state'] = tk.DISABLED
            self.en_qtdEstoque['state'] = tk.DISABLED
            self.en_codProduto.delete(0, tk.END)
            self.en_codProduto.insert(0, cod)

    def incluirProduto(self,event=None):
        tup=[]

        if self.en_qtdProduto.get()=='':
            self.en_qtdProduto.insert(0,1)

        if self.en_nomeProduto.get()=='': return
        if int(self.en_qtdEstoque.get())==0:
            messagebox.showwarning('Aviso','Produto indisponível no estoque!')
            return
        elif int(self.en_qtdEstoque.get())<int(self.en_qtdProduto.get()):
            messagebox.showwarning('Aviso', 'Quantidade em estoque insuficiente!')
            return


        carrinho=self.interTableFrame.capturaCodigosDaLista()
        for cod in range(len(carrinho)):
            #print(carrinho[cod][0])
            if carrinho[cod][0]==self.en_codProduto.get():
                messagebox.showwarning('AVISO','Você está tentado adicionar um ITEM JÁ INCLUSO NA LISTA.\n'
                                               'Caso queira você poderá MODIFICAR-lo REMOVENDO DO CARRINHO E ALTERANDO SUA QUANTIDADE.')
                return
            else:pass

        tup.append(self.en_codProduto.get())

        tup.append(self.en_nomeProduto.get())

        preco=float(self.manip.buscaProdutoPorCod(tup[0])[1])
        tup.append('%.2f'%preco)

        if int(self.en_qtdProduto.get())<=0:
            messagebox.showwarning('AVISO!','Produto Não pode ter quantidade Nula!')
            self.en_qtdProduto.delete(0,tk.END)
            return
        else: qtd=int(self.en_qtdProduto.get())
        tup.append(qtd)

        total=float(qtd*preco)
        tup.append('%.2f'%total)
        try:
            self.interTableFrame.InsertInTable(tup)
            # LIMPA OS CAMPOS DO PRODUTO ANTERIOR
            self.en_nomeProduto['state'] = tk.NORMAL
            self.en_qtdEstoque['state'] = tk.NORMAL
            self.en_codProduto.delete(0, tk.END)
            self.en_nomeProduto.delete(0, tk.END)
            self.en_qtdProduto.delete(0, tk.END)
            self.en_qtdEstoque.delete(0, tk.END)
            self.en_nomeProduto['state'] = tk.DISABLED
            self.en_qtdProduto['state'] = tk.DISABLED
            self.en_qtdEstoque['state'] = tk.DISABLED
            self.en_codProduto.focus_force() # FOCA EM CODIGO

            self.en_total['state']=tk.NORMAL
            if self.en_total.get()!='':
                totalVenda=float(self.en_total.get())
            else: totalVenda=0
            self.en_total.delete(0,tk.END)
            self.en_total.insert(0,'%.2f'%(totalVenda+total))
            self.en_total['state'] = tk.DISABLED

        except:
            messagebox.showerror('ERROR','Erro ao inserir produto no carrinho')
            #print('ERRO AO INSERIR NO CARRINHO')

    def removerProduto(self,event=None):

        produto=self.interTableFrame.eventSelect()

        if produto!=None:
            self.interTableFrame.deletePorIID(produto[0])
            total=float(produto[1])
            self.en_total['state'] = tk.NORMAL
            totalVenda = float(self.en_total.get())
            self.en_total.delete(0, tk.END)
            self.en_total.insert(0, '%.2f' % (totalVenda - total))
            self.en_total['state'] = tk.DISABLED

    def verificarCOD(self, stgEntry, action):
        #try:
        #    print('VALOR CHAR:',stgEntry)
       # except: pass

       # print('AÇÃO ENTRY:',action,type(action))
        if(action=='1'):
            if(stgEntry[-1] in ('0','1','2','3','4','5','6','7','8','9')):
                return True
            else:
                messagebox.showwarning('AVISO!','Contém Apenas Números!')
                return False

        elif action=='0':
            return True

    def cancelar(self,event=None):
        self.en_nomeCliente['state']=tk.NORMAL
        self.en_nomeProduto['state']=tk.NORMAL
        self.en_qtdProduto['state']=tk.NORMAL
        self.en_qtdEstoque['state'] = tk.NORMAL
        self.en_total['state']=tk.NORMAL
        self.en_codCliente.delete(0, tk.END)
        self.en_codProduto.delete(0, tk.END)
        self.en_nomeCliente.delete(0,tk.END)
        self.en_nomeProduto.delete(0, tk.END)
        self.en_qtdProduto.delete(0, tk.END)
        self.en_qtdEstoque.delete(0, tk.END)
        self.en_total.delete(0, tk.END)
        self.en_nomeCliente['state'] = tk.DISABLED
        self.en_nomeProduto['state'] = tk.DISABLED
        self.en_qtdProduto['state'] = tk.DISABLED
        self.en_qtdEstoque['state'] = tk.DISABLED
        self.en_total['state'] = tk.DISABLED
        self.interTableFrame.deleteAllInTable()
        self.en_codCliente.focus_force()

    def salvarVenda(self,event=None):
        if self.en_nomeCliente.get()=='':
            messagebox.showwarning('Aviso','Cliente Deve Ser Informado!')
            return 0
        elif self.interTableFrame.capturaCodigosDaLista()!=[]:
            cod_cliente=self.en_codCliente.get()
            produtos_venda=self.interTableFrame.capturaCodigosDaLista()
            if self.manip.gravarVenda(cod_cliente,self.data_venda,produtos_venda):
                messagebox.showinfo('OK', 'Salvo Com Sucesso!')
                self.cancelar()
            else:
                messagebox.showwarning('Erro','Erro Ao Gravar no Banco de Dados!')
                return
        else:
            messagebox.showwarning('Aviso', 'Lista de Produtos Vazia!')
            return 0

    def sair(self,event=None):
        self.callHomeFrame()
# ===================================================================================================================
# CLASSE REALIZAR COMPRA
# ===================================================================================================================
class CadCompra(tk.Frame):
    def __init__(self, TopLevel, cxAtributoComum, cxMetodoComum):
        tk.Frame.__init__(self, TopLevel)
        # --------------------------------------------------------------------------------------------------------------
        # PROPRIEDADES COMUNS ENTRE MODULOS
        # --------------------------------------------------------------------------------------------------------------
        self.cxAtributoComum = cxAtributoComum
        self.cxMetodoComum = cxMetodoComum
        self.cxMetodoComum[6] = self.buscarFornecedorPorCodigo
        self.cxMetodoComum[9] = self.buscarProdutoPorCodigo
        self.widthDefaultTopLevel = cxAtributoComum[0]  # DEFINE UM PADRÃO DE MEDIDA  HORIZONTAL PARA QQ TELA
        self.heightDefaultTopLevel = cxAtributoComum[1]  # DEFINE UM PADRÃO DE MEDIDA  VERTICAL PARA QQ TELA
        self.callHomeFrame = cxMetodoComum[10]  # PERMITE O ACESSO AO MÉTODO selectLoginHome QUE BLOQUEIA O PROGRAMA
        self.callViewFornecedor=cxMetodoComum[4]
        self.corFundo = 'SystemWindow'
        self.fonttypeComum = ['Trebuchet', int(self.heightDefaultTopLevel * 0.0111)]
        self.fontfgComum = 'DodgerBlue4'
        # --------------------------------------------------------------------------------------------------------------
        # METODOS/PROPRIEDADES DO FRAME PRINCIPAL
        self.grid_columnconfigure(0, weight=1)
        self['bg'] = self.corFundo
        # --------------------------------------------------------------------------------------------------------------
        # OBJETOS/VARIÁVEIS COMUNS ENTRE OS MÉTODOS DA CLASSE
        # --------------------------------------------------------------------------------------------------------------
        self.manip = cxAtributoComum['db']
        # self.codCliente=''
        # --------------------------------------------------------------------------------------------------------------
        # FRAME INTERNO
        # --------------------------------------------------------------------------------------------------------------
        self.interCadFrame = tk.Frame(self, padx=int(self.widthDefaultTopLevel * 0.02604),
                                      pady=int(self.heightDefaultTopLevel * 0.04629), bd=2, relief=tk.RIDGE,
                                      bg=self.corFundo, takefocus=0)
        self.interCadFrame.grid(row=0, column=0)
        # --------------------------------------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------------------------------------
        # METODOS PARA CONSTRUÇÃO DE WIDGETS
        self.widgetsInterFrame()
        # ------------------------------------------------------------------------------------------------------------
        self.en_codFornecedor.focus_force()
        # HORA DA VENDA
        data = time.localtime()
        self.data_compra = '%02.d/%02.d/%d' % (data[2], data[1], data[0])
        self.en_data.insert(0, self.data_compra)

        # ------------------------------------------------------------------------------------------------------------

    def widgetsInterFrame(self):
        fontMin = ['Trebuchet', '8']
        # ------------------------------------------------------------------------------------------------------------
        # FRAMES
        # ------------------------------------------------------------------------------------------------------------
        interButtonFrame1 = tk.Frame(self.interCadFrame, bg=self.corFundo)  # FRAME BASE BOTÕES INCLUIR E REMOVER
        interFormFrame = tk.Frame(self.interCadFrame,
                                  bg=self.corFundo)  # FRAME BASE DA PARTE DE VALOR TOTAL E DATA COM SUAS ENTRYS
        interButtonFrame2 = tk.Frame(self.interCadFrame,
                                     bg=self.corFundo)  # FRAME BASE PARA OS BOTÕES INFERIORES: CONFIRMAR, CANCELAR E SAIR
        self.interTableFrame = TableCarrinho(self.interCadFrame, [1050, 200,self.manip])  # FRAME DA TABELA
        # ------------------------------------------------------------------------------------------------------------
        interButtonFrame1.rowconfigure(0, pad=30)
        self.interCadFrame.rowconfigure(7, pad=20)
        self.interCadFrame.rowconfigure(8, pad=30)
        interButtonFrame1.columnconfigure(0, pad=40)
        interFormFrame.columnconfigure([0, 1, 2, 3], weight=1)
        interButtonFrame2.columnconfigure([0, 1, 2, 3], weight=1)
        # ------------------------------------------------------------------------------------------------------------
        self.interTableFrame.grid(row=6, column=0, columnspan=5, sticky=tk.W + tk.E)
        interButtonFrame1.grid(row=6, column=5, sticky=tk.N + tk.S + tk.E + tk.W)
        interFormFrame.grid(row=7, column=2, sticky=tk.E + tk.W)
        interButtonFrame2.grid(row=8, column=2, sticky=tk.E + tk.W)
        # ------------------------------------------------------------------------------------------------------------
        # LABELS
        # ------------------------------------------------------------------------------------------------------------
        self.lb_titulo = tk.Label(self.interCadFrame, text='REGISTRAR COMPRA', pady=10, bg=self.corFundo,
                                  font=('REFSAN', int(self.heightDefaultTopLevel * 0.014814), 'bold', 'underline'),
                                  fg=self.fontfgComum)
        lb_fornecedor = tk.Label(self.interCadFrame, text='Fornec.:', font=self.fonttypeComum, bg=self.corFundo)
        lb_produto = tk.Label(self.interCadFrame, text='Produto:', font=self.fonttypeComum, bg=self.corFundo)
        lb_total = tk.Label(interFormFrame, text='Total:', font=self.fonttypeComum, bg=self.corFundo)
        lb_data = tk.Label(interFormFrame, text='Data:', font=self.fonttypeComum, bg=self.corFundo)
        lb_codFornecedor = tk.Label(self.interCadFrame, text='COD', font=fontMin, bg=self.corFundo)
        lb_nomeFornecedor = tk.Label(self.interCadFrame, text='NOME', font=fontMin, bg=self.corFundo)
        lb_codProduto = tk.Label(self.interCadFrame, text='COD', font=fontMin, bg=self.corFundo)
        lb_nomeProduto = tk.Label(self.interCadFrame, text='NOME', font=fontMin, bg=self.corFundo)
        lb_precoProduto = tk.Label(self.interCadFrame, text='PREÇO UN', font=fontMin, bg=self.corFundo)
        lb_qtdProduto = tk.Label(self.interCadFrame, text='QTD', font=fontMin, bg=self.corFundo)
        # ------------------------------------------------------------------------------------------------------------
        self.lb_titulo.grid(row=0, column=0, columnspan=5)
        lb_fornecedor.grid(row=2, column=0, sticky=tk.W)
        lb_produto.grid(row=5, column=0, sticky=tk.W)
        lb_total.grid(row=0, column=2, sticky=tk.E)
        lb_data.grid(row=0, column=0, sticky=tk.E)
        lb_codFornecedor.grid(row=1, column=1)
        lb_nomeFornecedor.grid(row=1, column=2)
        lb_codProduto.grid(row=4, column=1)
        lb_nomeProduto.grid(row=4, column=2)
        lb_precoProduto.grid(row=4,column=3)
        lb_qtdProduto.grid(row=4, column=4)
        # ------------------------------------------------------------------------------------------------------------
        # ENTRYS
        # ------------------------------------------------------------------------------------------------------------
        self.en_codFornecedor = tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, width=7, font=self.fonttypeComum,
                                         justify=tk.CENTER,
                                         validate='key', validatecommand=(self.register(self.verificarCOD), '%P', '%d'))
        self.en_codFornecedor.bind('<Return>', self.buscarFornecedorPorCodigo)
        self.en_nomeFornecedor = tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=60,
                                          state=tk.DISABLED, disabledbackground=self.corFundo, disabledforeground='blue')
        self.en_codProduto = tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=7,
                                      justify=tk.CENTER,
                                      validate='key', validatecommand=(self.register(self.verificarCOD), '%P', '%d'))
        self.en_codProduto.bind('<Return>', self.buscarProdutoPorCodigo)
        self.en_nomeProduto = tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=60,
                                       state=tk.DISABLED, disabledbackground=self.corFundo, disabledforeground='blue')
        self.en_qtdProduto = tk.Entry(self.interCadFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=7,
                                      justify=tk.CENTER,fg='blue',
                                      validate='key', validatecommand=(self.register(self.verificarCOD), '%P', '%d'),
                                      state=tk.DISABLED, disabledbackground=self.corFundo, disabledforeground='dim gray')
        self.en_qtdProduto.bind('<Return>', self.incluirProduto)

        self.en_preco=  tk.Entry(self.interCadFrame, bd=2,fg='blue', relief=tk.GROOVE, font=self.fonttypeComum, width=9,
                                      justify=tk.CENTER,
                                      validate='key', validatecommand=(self.register(self.verificarPreco), '%P', '%d'))
        self.en_preco.bind('<Return>', self.passarFocusPreco)
        self.en_total = tk.Entry(interFormFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=13,
                                 justify=tk.CENTER,
                                 state=tk.DISABLED, disabledbackground=self.corFundo, disabledforeground='blue')
        self.en_data = tk.Entry(interFormFrame, bd=2, relief=tk.GROOVE, font=self.fonttypeComum, width=10,
                                justify=tk.CENTER,fg='blue')
        self.en_data.bind('<Return>', self.passarFocusData)
        # ------------------------------------------------------------------------------------------------------------
        self.en_codFornecedor.grid(row=2, column=1)
        self.en_nomeFornecedor.grid(row=2, column=2)
        self.en_codProduto.grid(row=5, column=1)
        self.en_nomeProduto.grid(row=5, column=2)
        self.en_preco.grid(row=5, column=3)
        self.en_qtdProduto.grid(row=5, column=4)
        self.en_total.grid(row=0, column=3, sticky=tk.W)
        self.en_data.grid(row=0, column=1, sticky=tk.W)
        # ------------------------------------------------------------------------------------------------------------
        # BUTTONS
        # ------------------------------------------------------------------------------------------------------------
        self.bt_buscarFornecedor = tk.Button(self.interCadFrame, text='Buscar Fornec.', font=fontMin,
                                             width=14, relief=tk.GROOVE, bg=self.corFundo,
                                             command=self.buscarFornecedorWindow)
        self.bt_buscarFornecedor.bind('<Return>', self.buscarFornecedorWindow)
        self.bt_buscarProduto = tk.Button(self.interCadFrame, text='Buscar Produto', font=fontMin,
                                          width=14, relief=tk.GROOVE, bg=self.corFundo,
                                          command=self.buscarProdutoWindow)
        self.bt_buscarProduto.bind('<Return>', self.buscarProdutoWindow)
        self.bt_incluirProduto = tk.Button(interButtonFrame1, text='Incluir Produto', font=fontMin, width=14,
                                           relief=tk.GROOVE, bg=self.corFundo,
                                           command=self.incluirProduto)
        self.bt_incluirProduto.bind('<Return>', self.incluirProduto)
        self.bt_removerProduto = tk.Button(interButtonFrame1, text='Remover Produto', font=fontMin, width=14,
                                           relief=tk.GROOVE, bg=self.corFundo,
                                           command=self.removerProduto)
        self.bt_removerProduto.bind('<Return>', self.removerProduto)
        self.bt_salvar = tk.Button(interButtonFrame2, text='Confirmar', font=self.fonttypeComum, width=10,
                                   relief=tk.GROOVE, bg=self.corFundo, command=self.salvar)
        self.bt_salvar.bind('<Return>', self.salvar)
        self.bt_cancelar = tk.Button(interButtonFrame2, text='Cancelar', font=self.fonttypeComum, width=10,
                                     relief=tk.GROOVE, bg=self.corFundo, command=self.cancelar)
        self.bt_cancelar.bind('<Return>', self.cancelar)
        self.bt_sair = tk.Button(interButtonFrame2, text='Sair', font=self.fonttypeComum, width=10,
                                 relief=tk.GROOVE, bg=self.corFundo, command=self.sair)
        self.bt_sair.bind('<Return>', self.sair)
        # ------------------------------------------------------------------------------------------------------------
        self.bt_buscarFornecedor.grid(row=2, column=5)
        self.bt_buscarProduto.grid(row=5, column=5)
        self.bt_incluirProduto.grid(row=0, column=0)
        self.bt_removerProduto.grid(row=1, column=0)
        self.bt_salvar.grid(row=0, column=1)
        self.bt_cancelar.grid(row=0, column=2)
        self.bt_sair.grid(row=0, column=3)
        # ------------------------------------------------------------------------------------------------------------

    def buscarFornecedorWindow(self, event=None):
        win = tk.Tk()

        try: win.wm_iconbitmap("bussIcon.ico") # TROCA ICONE DA JANELA PADRÃO TK
        except: win.wm_iconbitmap(r".\images\bussIcon.ico")  # TROCA ICONE DA JANELA PADRÃO TK

        tb_fornecedorbusca = ViewFornecedor(win, {0:int(self.widthDefaultTopLevel * 0.915),1:int(self.heightDefaultTopLevel * 0.2604),
                                                  'db':self.manip},self.cxMetodoComum)
        win.focus_force()

        tb_fornecedorbusca.grid()

    def buscarProdutoWindow(self, event=None):
        win = tk.Tk()

        try: win.wm_iconbitmap("bussIcon.ico") # TROCA ICONE DA JANELA PADRÃO TK
        except: win.wm_iconbitmap(r".\images\bussIcon.ico")  # TROCA ICONE DA JANELA PADRÃO TK

        tb_produtobusca = ViewProduto(win, {0:int(self.widthDefaultTopLevel * 0.915),1:int(self.heightDefaultTopLevel * 0.2604),
                                            'db':self.manip},self.cxMetodoComum)
        tb_produtobusca.grid()

    def buscarFornecedorPorCodigo(self, event=None, cod=''):

        if cod == '':  # CHAMNDO DA DIRETO DA CAIXA ENTRY
            if (self.en_codFornecedor.get() == ''):
                self.buscarFornecedorWindow()
                return 0
            cod = self.en_codFornecedor.get()
            res = self.manip.buscaFornecedorPorCod(cod)

            if (res == None):
                messagebox.showwarning('Aviso', 'Cliente Não Cadastrado!')
                self.en_nomeFornecedor['state'] = tk.NORMAL
                self.en_codFornecedor.delete(0, tk.END)
                self.en_nomeFornecedor.delete(0, tk.END)
                self.en_nomeFornecedor['state'] = tk.DISABLED
                return 0
            if (res == 'ERROSQL'):
                messagebox.showwarning('Aviso', 'Falha Ao Buscar No Banco De Dados!')
                self.en_nomeFornecedor['state'] = tk.NORMAL
                self.en_codFornecedor.delete(0, tk.END)
                self.en_nomeFornecedor.delete(0, tk.END)
                self.en_nomeFornecedor['state'] = tk.DISABLED
                return 0
            self.en_nomeFornecedor['state'] = tk.NORMAL
            self.en_nomeFornecedor.delete(0, tk.END)
            self.en_nomeFornecedor.insert(0, res[0])
            self.en_nomeFornecedor['state'] = tk.DISABLED
            self.en_codProduto.focus_force()
        else:
            res = self.manip.buscaFornecedorPorCod(cod)
            self.en_nomeFornecedor['state'] = tk.NORMAL
            self.en_nomeFornecedor.delete(0, tk.END)
            self.en_nomeFornecedor.insert(0, res[0])
            self.en_nomeFornecedor['state'] = tk.DISABLED
            self.en_codFornecedor.delete(0, tk.END)
            self.en_codFornecedor.insert(0, cod)
            self.en_codProduto.focus_force()

    def buscarProdutoPorCodigo(self, event=None, cod=''):

        if cod == '':  # CHAMNDO DA DIRETO DA CAIXA ENTRY
            if (self.en_codProduto.get() == ''):
                self.buscarProdutoWindow()
                return 0
            cod = self.en_codProduto.get()
            res = self.manip.buscaProdutoPorCod(cod)

            if (res == None):
                messagebox.showwarning('Aviso', 'Produto Não Cadastrado!')
                self.en_nomeProduto['state'] = tk.NORMAL
                self.en_qtdProduto['state'] = tk.NORMAL
                self.en_codProduto.delete(0, tk.END)
                self.en_nomeProduto.delete(0, tk.END)
                self.en_qtdProduto.delete(0, tk.END)
                self.en_nomeProduto['state'] = tk.DISABLED
                self.en_qtdProduto['state'] = tk.DISABLED
                return 0
            if (res == 'ERROSQL'):
                messagebox.showwarning('Aviso', 'Falha Ao Buscar No Banco De Dados!')
                self.en_nomeProduto['state'] = tk.NORMAL
                self.en_qtdProduto['state'] = tk.NORMAL
                self.en_codProduto.delete(0, tk.END)
                self.en_nomeProduto.delete(0, tk.END)
                self.en_qtdProduto.delete(0, tk.END)
                self.en_nomeProduto['state'] = tk.DISABLED
                self.en_qtdProduto['state'] = tk.DISABLED
                return 0
            self.en_nomeProduto['state'] = tk.NORMAL
            self.en_qtdProduto['state'] = tk.NORMAL
            self.en_qtdProduto.delete(0, tk.END)
            self.en_preco.focus_force()
            self.en_nomeProduto.delete(0, tk.END)
            self.en_nomeProduto.insert(0, res[0])
            self.en_nomeProduto['state'] = tk.DISABLED
        else:
            res = self.manip.buscaProdutoPorCod(cod)
            self.en_nomeProduto['state'] = tk.NORMAL
            self.en_qtdProduto['state'] = tk.NORMAL
            self.en_nomeProduto.delete(0, tk.END)
            self.en_qtdProduto.delete(0, tk.END)
            self.en_preco.focus_force()
            self.en_nomeProduto.insert(0, res[0])
            self.en_nomeProduto['state'] = tk.DISABLED
            self.en_codProduto.delete(0, tk.END)
            self.en_codProduto.insert(0, cod)

    def incluirProduto(self, event=None):
        tup = []
        if self.en_nomeProduto.get() == '': return
        if self.en_preco.get()=='':
            messagebox.showwarning('AVISO','O Preço Por Unidade Do Produto Deve Ser Informado!')
            self.en_preco.focus_force()
            return

        carrinho = self.interTableFrame.capturaCodigosDaLista()
        for cod in range(len(carrinho)):
            # print(carrinho[cod][0])
            if carrinho[cod][0] == self.en_codProduto.get():
                messagebox.showwarning('AVISO', 'Você está tentado adicionar um ITEM JÁ INCLUSO NA LISTA.\n'
                                                'Caso queira você poderá MODIFICAR-lo REMOVENDO DO CARRINHO E '
                                                'ALTERANDO SUA QUANTIDADE E/OU PREÇO.')
                return
            else:
                pass

        tup.append(self.en_codProduto.get())

        tup.append(self.en_nomeProduto.get())

        #preco = float(self.manip.buscaProdutoPorCod(tup[0])[1])
        preco=''
        for chr in self.en_preco.get():
            if (self.en_preco.get()[0]=='.'or self.en_preco.get()[0]==',' )and chr=='.' or chr==',': preco='0.'
            elif chr ==',': preco+='.'
            else: preco+=chr
        preco=float(preco)
        tup.append('%.2f' % preco)

        if self.en_qtdProduto.get() == '':
            qtd = 1
        elif int(self.en_qtdProduto.get())<=0:
            messagebox.showwarning('AVISO!','Produto Não pode ter quantidade Nula!')
            self.en_qtdProduto.delete(0,tk.END)
            return
        else:
            qtd = int(self.en_qtdProduto.get())
        tup.append(qtd)

        total = float(qtd * preco)
        tup.append('%.2f' % total)
        try:
            self.interTableFrame.InsertInTable(tup)
            # LIMPA OS CAMPOS DO PRODUTO ANTERIOR
            self.en_nomeProduto['state'] = tk.NORMAL
            self.en_codProduto.delete(0, tk.END)
            self.en_nomeProduto.delete(0, tk.END)
            self.en_qtdProduto.delete(0, tk.END)
            self.en_preco.delete(0,tk.END)
            self.en_nomeProduto['state'] = tk.DISABLED
            self.en_qtdProduto['state'] = tk.DISABLED
            self.en_codProduto.focus_force()  # FOCA EM CODIGO

            self.en_total['state'] = tk.NORMAL
            if self.en_total.get() != '':
                totalVenda = float(self.en_total.get())
            else:
                totalVenda = 0
            self.en_total.delete(0, tk.END)
            self.en_total.insert(0, '%.2f' % (totalVenda + total))
            self.en_total['state'] = tk.DISABLED

        except:
            #print('ERRO AO INSERIR NO CARRINHO')
            messagebox.showerror('Error', 'Erro ao inserir produto no carrinho!')

    def removerProduto(self, event=None):

        produto = self.interTableFrame.eventSelect()

        if produto != None:
            self.interTableFrame.deletePorIID(produto[0])
            total = float(produto[1])
            self.en_total['state'] = tk.NORMAL
            totalVenda = float(self.en_total.get())
            self.en_total.delete(0, tk.END)
            self.en_total.insert(0, '%.2f' % (totalVenda - total))
            self.en_total['state'] = tk.DISABLED

    def verificarCOD(self, stgEntry, action):
        # try:
        #    print('VALOR CHAR:',stgEntry)
        # except: pass

        # print('AÇÃO ENTRY:',action,type(action))
        if (action == '1'):
            if (stgEntry[-1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                return True
            else:
                messagebox.showwarning('AVISO!', 'Contém Apenas Números!')
                return False

        elif action == '0':
            return True

    def verificarPreco(self, stgEntry, action):
        # try:
        #    print('VALOR CHAR:',stgEntry)
        # except: pass

        # print('AÇÃO ENTRY:',action,type(action))
        if (action == '1'):
            if (stgEntry[-1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.',',')):
                return True
            else:
                messagebox.showwarning('AVISO!', 'Preço Inválido!')
                return False

        elif action == '0':
            return True

    def verificarData(self):
        data = []
        datapart=''
        for c in self.en_data.get():
            if c=='/':
                data.append(datapart)
                datapart=''
            else: datapart+=c
        data.append(datapart)
        try:
            datetime.datetime(int(data[2]),int(data[1]),int(data[0]))
            self.data_compra = '%02.d/%02.d/%d' % (int(data[0]), int(data[1]), int(data[2]))
            return True
        except:
            return False

    def passarFocusPreco(self,event=None):
        self.en_qtdProduto.focus_force()

    def passarFocusData(self,event=None):
        self.bt_salvar.focus_force()

    def cancelar(self, event=None):
        self.en_nomeFornecedor['state'] = tk.NORMAL
        self.en_nomeProduto['state'] = tk.NORMAL
        self.en_qtdProduto['state'] = tk.NORMAL
        self.en_total['state'] = tk.NORMAL
        self.en_codFornecedor.delete(0, tk.END)
        self.en_codProduto.delete(0,tk.END)
        self.en_nomeFornecedor.delete(0, tk.END)
        self.en_nomeProduto.delete(0, tk.END)
        self.en_qtdProduto.delete(0, tk.END)
        self.en_preco.delete(0,tk.END)
        self.en_total.delete(0, tk.END)
        self.en_nomeFornecedor['state'] = tk.DISABLED
        self.en_nomeProduto['state'] = tk.DISABLED
        self.en_qtdProduto['state'] = tk.DISABLED
        self.en_total['state'] = tk.DISABLED
        self.interTableFrame.deleteAllInTable()
        self.en_codFornecedor.focus_force()
        data = time.localtime()
        self.data_compra = '%02.d/%02.d/%d' % (data[2], data[1], data[0])
        self.en_data.delete(0,tk.END)
        self.en_data.insert(0, self.data_compra)

    def salvar(self, event=None):
        if self.en_nomeFornecedor.get() == '':
            messagebox.showwarning('Alerta', 'Cliente Deve Ser Informado!')
            return 0

        if self.verificarData():pass
        else:
            messagebox.showwarning('Alerta', 'Data Inválida!')
            return 0
        if self.interTableFrame.capturaCodigosDaLista() != []:
            cod_fornecedor = self.en_codFornecedor.get()
            produtos_compra = self.interTableFrame.capturaCodigosDaLista()
            if self.manip.gravarCompra(cod_fornecedor, self.data_compra,produtos_compra):
                messagebox.showinfo('OK', 'Salvo Com Sucesso!')
                self.cancelar()
            else:
                messagebox.showwarning('Erro', 'Erro Ao Gravar no Banco de Dados!')
                return
        else:
            messagebox.showwarning('Alerta', 'Lista de Produtos Vazia!')
            return 0

    def sair(self, event=None):
        self.callHomeFrame()
# ===================================================================================================================