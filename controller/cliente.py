#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, validade, preco):
    db.cur.execute("""
                   INSERT into public.produto (nome, validade, preco)
                   VALUES ('%s','%s','%s')
                   """ % (nome, validade, preco))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM produto
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def excluir (id):
    db.cur.execute("""
        DELETE FROM produto WHERE id_produto = '%s' """ % (id))
    db.con.commit()