# coding: utf-8

# PROJECT: WALLBASE
# MODULE: walldb
# DESCRIPTION: MÓDULO DE CONEXÃO COM POSTGRESQL PORTABLE
# AUTHOR: WALYSSON P. DOS REIS
# EMAIL: walyssondosreis@email.com

import psycopg2
import os
from tkinter import messagebox


class db:

    def __init__(self):
        #try:
            #self.startDBService()
            #pass
        #except:
            #print('Não foi possivel iniciar o serviço do banco de dados')
        try:
            self.connect()
        except:
            print('Não foi possivel conectar ao banco de dados')
        #print('Construiu')

    def __del__(self): # FUNÇÃO DESTRUTORA
        self.disconnect()
        #self.stopDBService()
        #print('destruiu!')

    # ===================================================================================================================
    # MÉTODOS DE CONEXÃO COM O BANCO DE DADOS
    # ===================================================================================================================
    def startDBService(self):  # METODO QUE INICIA O SERVIÇO DO POSTGRESQL PORTABLE
        try:
            os.system(r'.\pgsql\App\PgSQL\bin\pg_ctl -D ".\pgsql\Data\data" start')
        except:
            error='ERRO AO INICAR O SERVIÇO DO BANCO DE DADOS POSTGRESQL'
            messagebox.showerror('ERROR!',error)
            print(error)

    def stopDBService(self):  # METODO QUE ENCERRA O SERVIÇO DO POSTGRESQL PORTABLE
        try:
            os.system(r'.\pgsql\App\PgSQL\bin\pg_ctl -D ".\pgsql\Data\data" stop')
        except:
            error='ERRO AO ENCERRAR O SERVIÇO DO BANCO DE DADOS POSTGRESQL'
            messagebox.showerror('ERROR!', error)
            print(error)

    def connect(self): # METODO QUE INICIA A CONEXÃO COM BANCO DE DADOS
        try:
            for x in range(2):
                #print('TENTATIVA',x,'DE CONEXÃO COM POSTGRESQL')
                try:
                    self.con = psycopg2.connect(host='localhost',port='5432', user='postgres', password='123', dbname='meidb')
                    self.c = self.con.cursor()
                    break
                except: pass
        except:
            error='ERRO CONECTAR NO BANCO!'
            messagebox.showerror('ERROR!', error)
            print(error)

    def disconnect(self): # METODO QUE ENCERRA A CONEXÃO COM BANCO DE DADOS
        self.c.close()
        self.con.close()

    # ===================================================================================================================
    # MÉTODOS DE MANIPULAÇÃO PARA TABELA: CLIENTE
    # ===================================================================================================================
    def gravarCliente(self, nome, cpfcnpj, telefone='null', logradouro='null',
                      cidade='null', estado='null', cep='null'): # METODO QUE GRAVA NO BANCO DE DADOS/TABLE FILME
        #self.connect()
        #self.c = self.con.cursor()

        #TRATA OS ARGUMENTOS NULOS NO BANCO QUE QUANDO NÃO NULOS EXIGEM '' MARCAÇÃO DE STRING SQL
        if nome != 'null': nome = "'%s'" % nome
        if cpfcnpj != 'null': cpfcnpj = "'%s'" % cpfcnpj
        if telefone!='null': telefone="'%s'" % telefone
        if logradouro != 'null': logradouro = "'%s'" % logradouro
        if cidade != 'null': cidade = "'%s'" % cidade
        if estado != 'null': estado = "'%s'" % estado
        if cep!= 'null': cep = "'%s'" % cep

        try:
            self.c.execute("INSERT INTO cliente (nome,cpfcnpj,telefone,logradouro,cidade,estado,cep) VALUES (%s,%s,%s,%s,%s,%s,%s);"
                           % (nome, cpfcnpj, telefone, logradouro, cidade, estado, cep))

        except psycopg2.Error as erro:
            #print(erro.pgcode)
            #print(erro.pgerror)
            #if(erro.pgcode=='23502'): return 'NOME NÃO PODE SER NULO!'
            #if(erro.pgcode=='23505'): return 'CLIENTE JÁ CADASTRADO!'
            #self.disconnect()
            self.con.rollback()
            return 'ERRO AO SALVAR!'

        #self.disconnect()
        self.con.commit()
        return 'SALVO!'

    def excluirCliente(self,cod):
        #self.connect()
        self.c=self.con.cursor()
        try:
            self.c.execute("DELETE FROM cliente WHERE cod = %s;"%cod)

        except:
            #self.disconnect()
            self.con.rollback()
            return 'NO'
        #self.disconnect()
        self.con.commit()
        return 'OK'

    def updateCliente(self, cod, nome, cpfcnpj, telefone='null', logradouro='null',
                      cidade='null', estado='null', cep='null'): # METODO QUE GRAVA NO BANCO DE DADOS/TABLE FILME
        #self.connect()
        #self.c = self.con.cursor()

        #TRATA OS ARGUMENTOS NULOS NO BANCO QUE QUANDO NÃO NULOS EXIGEM '' MARCAÇÃO DE STRING SQL
        if cod != 'null': cod = "'%s'" % cod
        if nome != 'null': nome = "'%s'" % nome
        if cpfcnpj != 'null': cpfcnpj = "'%s'" % cpfcnpj
        if telefone!='null': telefone="'%s'" % telefone
        if logradouro != 'null': logradouro = "'%s'" % logradouro
        if cidade != 'null': cidade = "'%s'" % cidade
        if estado != 'null': estado = "'%s'" % estado
        if cep!= 'null': cep = "'%s'" % cep

        try:
            self.c.execute("UPDATE cliente SET nome=%s,cpfcnpj=%s,telefone=%s,logradouro=%s,cidade=%s,estado=%s,cep=%s WHERE cod=%s;"
                           % (nome, cpfcnpj, telefone, logradouro, cidade, estado, cep, cod))

        except psycopg2.Error as erro:
            #print(erro.pgcode)
            #print(erro.pgerror)
            #if(erro.pgcode=='23502'): return 'NOME NÃO PODE SER NULO!'
            #if(erro.pgcode=='23505'): return 'CLIENTE JÁ CADASTRADO!'
            #self.disconnect()
            self.con.rollback()
            return 'ERRO AO ATUALIZAR!'

        #self.disconnect()
        self.con.commit()
        return 'SALVO!'

    def listarCliente(self): # METODO QUE BUSCA TODOS OS REGISTROS NO BANCO DE DADOS RETORNANDO NUMA TUPLA
        #self.connect()
        #self.c = self.con.cursor()
        self.c.execute("SELECT cod,nome,cpfcnpj,telefone,logradouro,cidade,estado,cep FROM cliente ORDER BY nome;")
        res = self.c.fetchall()
        #self.disconnect()
        return res

    def buscaClientePorCod(self, cod):
        #self.connect()
        #self.c = self.con.cursor()
        try:
            self.c.execute("SELECT nome,cpfcnpj,telefone,logradouro,cidade,estado,cep FROM cliente WHERE cod='%s';"%cod)
            res = self.c.fetchone()
        except:
            #self.disconnect()
            return 'ERROSQL'

        #self.disconnect()
        return res

    # ===================================================================================================================
    # MÉTODOS DE MANIPULAÇÃO PARA TABELA: FORNECEDOR
    # ===================================================================================================================
    def gravarFornecedor(self, nome, cnpj, telefone='null', logradouro='null',
                         cidade='null', estado='null', cep='null'): # METODO QUE GRAVA NO BANCO DE DADOS/TABLE FILME
        #self.connect()
        #self.c = self.con.cursor()

        #TRATA OS ARGUMENTOS NULOS NO BANCO QUE QUANDO NÃO NULOS EXIGEM '' MARCAÇÃO DE STRING SQL
        if nome != 'null': nome = "'%s'" % nome
        if cnpj != 'null': cnpj = "'%s'" % cnpj
        if telefone!='null': telefone="'%s'" % telefone
        if logradouro != 'null': logradouro = "'%s'" % logradouro
        if cidade != 'null': cidade = "'%s'" % cidade
        if estado != 'null': estado = "'%s'" % estado
        if cep!= 'null': cep = "'%s'" % cep

        try:
            self.c.execute("INSERT INTO fornecedor (nome,cnpj,telefone,logradouro,cidade,estado,cep) VALUES (%s,%s,%s,%s,%s,%s,%s);"
                           % (nome, cnpj, telefone, logradouro, cidade, estado, cep))

        except psycopg2.Error as erro:
            #print(erro.pgcode)
            #print(erro.pgerror)
            #if(erro.pgcode=='23502'): return 'NOME NÃO PODE SER NULO!'
            #if(erro.pgcode=='23505'): return 'CLIENTE JÁ CADASTRADO!'
            #self.disconnect()
            self.con.rollback()
            return 'ERRO AO SALVAR!'

        #self.disconnect()
        self.con.commit()
        return 'SALVO!'

    def excluirFornecedor(self,cod):
        #self.connect()
        self.c=self.con.cursor()
        try:
            self.c.execute("DELETE FROM fornecedor WHERE cod = %s;"%cod)

        except:
            #self.disconnect()
            self.con.rollback()
            return 'NO'
        #self.disconnect()
        self.con.commit()
        return 'OK'

    def updateFornecedor(self, cod, nome, cnpj, telefone='null', logradouro='null',
                         cidade='null', estado='null', cep='null'): # METODO QUE GRAVA NO BANCO DE DADOS/TABLE FILME
        #self.connect()
        #self.c = self.con.cursor()

        #TRATA OS ARGUMENTOS NULOS NO BANCO QUE QUANDO NÃO NULOS EXIGEM '' MARCAÇÃO DE STRING SQL
        if cod != 'null': cod = "'%s'" % cod
        if nome != 'null': nome = "'%s'" % nome
        if cnpj != 'null': cnpj = "'%s'" % cnpj
        if telefone!='null': telefone="'%s'" % telefone
        if logradouro != 'null': logradouro = "'%s'" % logradouro
        if cidade != 'null': cidade = "'%s'" % cidade
        if estado != 'null': estado = "'%s'" % estado
        if cep!= 'null': cep = "'%s'" % cep

        try:
            self.c.execute("UPDATE fornecedor SET nome=%s,cnpj=%s,telefone=%s,logradouro=%s,cidade=%s,estado=%s,cep=%s WHERE cod=%s;"
                           % (nome, cnpj, telefone, logradouro, cidade, estado, cep, cod))

        except psycopg2.Error as erro:
            #print(erro.pgcode)
            #print(erro.pgerror)
            #if(erro.pgcode=='23502'): return 'NOME NÃO PODE SER NULO!'
            #if(erro.pgcode=='23505'): return 'CLIENTE JÁ CADASTRADO!'
            #self.disconnect()
            self.con.rollback()
            return 'ERRO AO ATUALIZAR!'

        #self.disconnect()
        self.con.commit()
        return 'SALVO!'

    def listarFornecedor(self): # METODO QUE BUSCA TODOS OS REGISTROS NO BANCO DE DADOS RETORNANDO NUMA TUPLA
        #self.connect()
        #self.c = self.con.cursor()
        self.c.execute("SELECT cod,nome,cnpj,telefone,logradouro,cidade,estado,cep FROM fornecedor ORDER BY nome;")
        res = self.c.fetchall()
        #self.disconnect()
        return res

    def buscaFornecedorPorCod(self, cod):
        #self.connect()
        #self.c = self.con.cursor()
        try:
            self.c.execute("SELECT nome,cnpj,telefone,logradouro,cidade,estado,cep FROM fornecedor WHERE cod='%s';"%cod)
            res = self.c.fetchone()
        except:
            #self.disconnect()
            return 'ERROSQL'

        #self.disconnect()
        return res

    # ===================================================================================================================
    # MÉTODOS DE MANIPULAÇÃO PARA TABELA: PRODUTO
    # ===================================================================================================================
    def gravarProduto(self, nome, preco=0, descricao='null'): # METODO QUE GRAVA NO BANCO DE DADOS/TABLE FILME
        #self.connect()
        #self.c = self.con.cursor()

        #TRATA OS ARGUMENTOS NULOS NO BANCO QUE QUANDO NÃO NULOS EXIGEM '' MARCAÇÃO DE STRING SQL
        if nome != 'null': nome = "'%s'" % nome
        if preco != 'null': preco = "'%s'" % preco
        if descricao!= 'null': descricao= "'%s'" % descricao

        try:
            self.c.execute("INSERT INTO produto (nome,preco_venda,descricao) VALUES (%s,%s,%s) ;"
                           % (nome, preco, descricao))


        except psycopg2.Error as erro:
            #print(erro.pgcode)
            #print(erro.pgerror)
            #if(erro.pgcode=='23502'): return 'NOME NÃO PODE SER NULO!'
            #if(erro.pgcode=='23505'): return 'CLIENTE JÁ CADASTRADO!'
            #self.disconnect()
            self.con.rollback()
            return 'ERRO AO SALVAR!'

        #self.disconnect()
        self.con.commit()
        return 'SALVO!'

    def excluirProduto(self,cod):
        #self.connect()
        self.c=self.con.cursor()
        try:
            self.c.execute("DELETE FROM produto WHERE cod = %s;"%cod)

        except:
            #self.disconnect()
            self.con.rollback()
            return 'NO'
        #self.disconnect()
        self.con.commit()
        return 'OK'

    def updateProduto(self, cod, nome, preco, descricao='null'):
        #self.connect()
        #self.c = self.con.cursor()

        #TRATA OS ARGUMENTOS NULOS NO BANCO QUE QUANDO NÃO NULOS EXIGEM '' MARCAÇÃO DE STRING SQL
        if cod != 'null': cod = "'%s'" % cod
        if nome != 'null': nome = "'%s'" % nome
        if preco != 'null': preco = "'%s'" % preco
        if descricao!= 'null': descricao= "'%s'" % descricao

        try:
            self.c.execute("UPDATE produto SET nome=%s,preco_venda=%s,descricao=%s WHERE cod=%s;"
                           % (nome, preco, descricao, cod))

        except psycopg2.Error as erro:
            #print(erro.pgcode)
            #print(erro.pgerror)
            #if(erro.pgcode=='23502'): return 'NOME NÃO PODE SER NULO!'
            #if(erro.pgcode=='23505'): return 'CLIENTE JÁ CADASTRADO!'
            self.con.rollback()
            return 'ERRO AO ATUALIZAR!'

        #self.disconnect()
        self.con.commit()
        return 'SALVO!'

    def listarProduto(self): # METODO QUE BUSCA TODOS OS REGISTROS NO BANCO DE DADOS RETORNANDO NUMA TUPLA
        #self.connect()
        #self.c = self.con.cursor()
        self.c.execute("SELECT cod,nome,preco_venda,descricao FROM produto ORDER BY nome;")
        res = self.c.fetchall()
        #self.disconnect()
        return res

    def buscaProdutoPorCod(self, cod):
        #self.connect()
        #self.c = self.con.cursor()
        try:
            self.c.execute("SELECT nome,preco_venda,descricao,qtd_estoque FROM produto WHERE cod='%s';"%cod)
            res = self.c.fetchone()
        except:
            #self.disconnect()
            return 'ERROSQL'

        #self.disconnect()
        return res

    # ===================================================================================================================
    # MÉTODOS DE MANIPULAÇÃO DE VENDA DAS TABELAS: VENDA e PRODUTOS_VENDA
    # ===================================================================================================================

    def gravarVenda(self, cod_cliente, data, produtos): # METODO QUE GRAVA NO BANCO DE DADOS/TABLE FILME
        #self.connect()
        #self.c = self.con.cursor()

        datatemp = []
        datapart = ''
        for c in data:
            if c == '/':
                datatemp.append(datapart)
                datapart = ''
            else:
                datapart += c
        datatemp.append(datapart)
        datatemp = datatemp[::-1]
        data = '' + datatemp[0] + '/' + datatemp[1] + '/' + datatemp[2]

        try:
            self.c.execute("INSERT INTO venda (cod_cliente,data) VALUES ('%s','%s') RETURNING cod;"
                           % (cod_cliente, data))
            cod_venda = self.c.fetchone()[0]
            #self.con.commit()

            #print(cod_venda)
        except psycopg2.Error as erro:
            #print(erro.pgcode)
            #print(erro.pgerror)
            #if(erro.pgcode=='23502'): return 'NOME NÃO PODE SER NULO!'
            #if(erro.pgcode=='23505'): return 'CLIENTE JÁ CADASTRADO!'
            self.con.rollback()
            #self.disconnect()
            return False

        for produto in produtos:
            try:
                self.c.execute("INSERT INTO produtos_venda (cod_venda, cod_produto, preco_venda, quantidade) VALUES ('%s','%s','%s','%s');"
                           % (cod_venda,produto[0],produto[1],produto[2]))

            except psycopg2.Error as erro:
                self.con.rollback()
                #self.disconnect()
                return False

        for produto in produtos:
            try:
                self.c.execute("UPDATE produto SET qtd_estoque=qtd_estoque-'%s' WHERE cod='%s';"% (produto[2],produto[0]))

            except psycopg2.Error as erro:
                self.con.rollback()
                #self.disconnect()
                return False

        self.con.commit()
        #self.disconnect()
        return True

    def listarVenda(self): # METODO QUE BUSCA TODOS OS REGISTROS NO BANCO DE DADOS RETORNANDO NUMA TUPLA
        #self.connect()
        #self.c = self.con.cursor()
        self.c.execute("SELECT venda.cod,data,cliente.nome "
                       "FROM venda JOIN cliente ON venda.cod_cliente=cliente.cod ORDER BY (data,venda.cod) DESC ;")
        resVenda = self.c.fetchall()

        def interFunctionProdutosVenda(cod_venda):
            self.c.execute("SELECT cod_produto,quantidade,preco_venda "
                           "FROM produtos_venda "
                           "WHERE cod_venda='%s';"%cod_venda)
            resProdutos_Venda = self.c.fetchall()
            return resProdutos_Venda
        todasAsVendas=[]
        for tup in range(len(resVenda)): # BUSCA TODAS AS VENDAS
            tuptemp=[]
            vd=resVenda[tup]
            tuptemp.extend([vd[0],'%02d/%02d/%d'%(vd[1].day,vd[1].month,vd[1].year),vd[2]])

            pdt = interFunctionProdutosVenda(resVenda[tup][0])
            tuptemppdt=[]
            tuptemppdtfinal=[]
            for tup in range(len(pdt)):
                pt=pdt[tup]
                tuptemppdt=[pt[0],pt[1],'%.2f'%pt[2]]
                #print(tuptemppdt)
                tuptemppdtfinal.append(tuptemppdt)
            tuptemp.extend(tuptemppdtfinal)
            todasAsVendas.append(tuptemp)

        #print(todasAsVendas)
        #self.disconnect()
        #print({'VENDA':resVenda,'PRODUTOS':resProdutos_Venda})
        return todasAsVendas

    def excluirVenda(self,cod):
        #self.connect()
        self.c=self.con.cursor()
        try:
            self.c.execute("DELETE FROM produtos_venda WHERE cod_venda = %s RETURNING cod_produto,quantidade;"%cod)
            produtos=self.c.fetchall()

        except:
            #self.disconnect()
            self.con.rollback()
            return 'NO'

        for produto in produtos:
            try:
                self.c.execute("UPDATE produto SET qtd_estoque=qtd_estoque+'%s' WHERE cod='%s';"% (produto[1],produto[0]))

            except psycopg2.Error as erro:
                self.con.rollback()
                #self.disconnect()
                return False
        try:
            self.c.execute("DELETE FROM venda WHERE cod = %s;"%cod)
        except:
            #self.disconnect()
            self.con.rollback()
            return 'NO'

        #self.disconnect()
        self.con.commit()
        return 'OK'

    def buscarProdutosDaVendaPorCOD(self,cod_venda):
        self.c.execute("SELECT cod_produto,nome,produtos_venda.preco_venda,quantidade,(quantidade*produtos_venda.preco_venda) AS TOTAL "
                       "FROM produtos_venda JOIN produto ON produto.cod=cod_produto "
                       "WHERE cod_venda=%s "
                       "GROUP BY (cod_venda,cod_produto,nome)"%cod_venda)
        res=self.c.fetchall()
        return res
    # ===================================================================================================================
    # MÉTODOS DE MANIPULAÇÃO DE COMPRA DAS TABELAS: COMPRA e PRODUTOS_COMPRA
    # ===================================================================================================================

    def gravarCompra(self, cod_fornecedor, data, produtos): # METODO QUE GRAVA NO BANCO DE DADOS/TABLE FILME
        #self.connect()
        #self.c = self.con.cursor()

        datatemp = []
        datapart = ''
        for c in data:
            if c == '/':
                datatemp.append(datapart)
                datapart = ''
            else:
                datapart += c
        datatemp.append(datapart)
        datatemp=datatemp[::-1]
        data=''+datatemp[0]+'/'+datatemp[1]+'/'+datatemp[2]

        try:
            self.c.execute("INSERT INTO compra (cod_fornecedor,data) VALUES ('%s','%s') RETURNING cod;"
                           % (cod_fornecedor, data))
            cod_compra = self.c.fetchone()[0]

        except psycopg2.Error as erro:
            #print(erro.pgcode)
            #print(erro.pgerror)
            #if(erro.pgcode=='23502'): return 'NOME NÃO PODE SER NULO!'
            #if(erro.pgcode=='23505'): return 'CLIENTE JÁ CADASTRADO!'
            self.con.rollback()
            #self.disconnect()
            return False

        for produto in produtos:
            try:
                self.c.execute("INSERT INTO produtos_compra (cod_compra, cod_produto, preco_compra, quantidade) VALUES ('%s','%s','%s','%s');"
                           % (cod_compra,produto[0],produto[1],produto[2]))

            except psycopg2.Error as erro:
                self.con.rollback()
                #self.disconnect()
                return False

        for produto in produtos:
            try:
                self.c.execute("UPDATE produto SET qtd_estoque=qtd_estoque+'%s' WHERE cod='%s';"% (produto[2],produto[0]))

            except psycopg2.Error as erro:
                self.con.rollback()
                #self.disconnect()
                return False

        self.con.commit()
        #self.disconnect()
        return True

    def listarCompra(self): # METODO QUE BUSCA TODOS OS REGISTROS NO BANCO DE DADOS RETORNANDO NUMA TUPLA
        #self.connect()
        #self.c = self.con.cursor()
        self.c.execute("SELECT compra.cod,data,fornecedor.nome "
                       "FROM compra JOIN fornecedor ON compra.cod_fornecedor=fornecedor.cod ORDER BY (data,compra.cod) DESC ;")
        resCompra = self.c.fetchall()

        def interFunctionProdutosCompra(cod_compra):
            self.c.execute("SELECT cod_produto,quantidade,preco_compra "
                           "FROM produtos_compra "
                           "WHERE cod_compra='%s';" % cod_compra)
            resProdutos_compra = self.c.fetchall()
            return resProdutos_compra
        todasAsCompras=[]
        for tup in range(len(resCompra)): # BUSCA TODAS AS VENDAS
            tuptemp=[]
            vd=resCompra[tup]
            tuptemp.extend([vd[0],'%02d/%02d/%d'%(vd[1].day,vd[1].month,vd[1].year),vd[2]])

            pdt = interFunctionProdutosCompra(resCompra[tup][0])
            tuptemppdt=[]
            tuptemppdtfinal=[]
            for tup in range(len(pdt)):
                pt=pdt[tup]
                tuptemppdt=[pt[0],pt[1],'%.2f'%pt[2]]
                #print(tuptemppdt)
                tuptemppdtfinal.append(tuptemppdt)
            tuptemp.extend(tuptemppdtfinal)
            todasAsCompras.append(tuptemp)

        #print(todasAsCompras)
        #self.disconnect()
        #print({'VENDA':resCompra,'PRODUTOS':resProdutos_compra})
        return todasAsCompras

    def buscarProdutosDaCompraPorCOD(self, cod_compra):
        self.c.execute("SELECT cod_produto,nome,produtos_compra.preco_compra,quantidade,(quantidade*produtos_compra.preco_compra) AS TOTAL "
                       "FROM produtos_compra JOIN produto ON produto.cod=cod_produto "
                       "WHERE cod_compra=%s "
                       "GROUP BY (cod_compra,cod_produto,nome)" % cod_compra)
        res=self.c.fetchall()
        return res

    def excluirCompra(self,cod):
        #self.connect()
        self.c=self.con.cursor()
        try:
            self.c.execute("DELETE FROM produtos_compra WHERE cod_compra = %s RETURNING cod_produto,quantidade;"%cod)
            produtos=self.c.fetchall()

        except:
            #self.disconnect()
            self.con.rollback()
            return 'NO'

        for produto in produtos:
            try:
                self.c.execute("UPDATE produto SET qtd_estoque=qtd_estoque-'%s' WHERE cod='%s';"% (produto[1],produto[0]))

            except psycopg2.Error as erro:
                self.con.rollback()
                #self.disconnect()
                return False
        try:
            self.c.execute("DELETE FROM compra WHERE cod = %s;"%cod)
        except:
            #self.disconnect()
            self.con.rollback()
            return 'NO'

        #self.disconnect()
        self.con.commit()
        return 'OK'
    # ===================================================================================================================
    # MÉTODOS DE MANIPULAÇÃO GERAL: CONSULTAS ESPECÍFICAS
    # ===================================================================================================================

    def listarEstoque(self): # METODO QUE BUSCA TODOS OS REGISTROS NO BANCO DE DADOS RETORNANDO NUMA TUPLA
        self.c.execute("SELECT * FROM view_estoque")
        res = self.c.fetchall()
        #self.disconnect()
        return res

    def totalVendasMensal(self):  # METODO QUE BUSCA TODOS OS REGISTROS NO BANCO DE DADOS RETORNANDO NUMA TUPLA
            self.c.execute("SELECT EXTRACT(MONTH FROM data) AS mes, SUM(sltsum.total_venda) AS total_mensal "
                           "FROM venda JOIN (SELECT cod_venda,SUM(preco_venda*quantidade) AS total_venda FROM produtos_venda GROUP BY(cod_venda)) AS sltsum ON venda.cod=sltsum.cod_venda "
                           "GROUP BY (mes) "
                           "ORDER BY(mes);")
            res = self.c.fetchall()
            # self.disconnect()
            return res

    def totalComprasMensal(self):  # METODO QUE BUSCA TODOS OS REGISTROS NO BANCO DE DADOS RETORNANDO NUMA TUPLA
            self.c.execute("SELECT EXTRACT(MONTH FROM data) AS mes, SUM(sltsum.total_compra) AS total_mensal "
                           "FROM compra JOIN (SELECT cod_compra,SUM(preco_compra*quantidade) AS total_compra FROM produtos_compra GROUP BY(cod_compra)) AS sltsum ON compra.cod=sltsum.cod_compra "
                           "GROUP BY (mes) "
                           "ORDER BY(mes);")
            res = self.c.fetchall()
            # self.disconnect()
            return res


