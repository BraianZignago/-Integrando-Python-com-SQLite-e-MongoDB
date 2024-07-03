from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Numeric)

    cliente = relationship('Cliente', back_populates='contas')

# Configuração do SQLite
engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)

# Criação da sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de dados
cliente1 = Cliente(nome="João Silva", cpf="123456789", endereco="Rua A")
cliente2 = Cliente(nome="Maria Oliveira", cpf="987654321", endereco="Rua B")

conta1 = Conta(tipo="corrente", agencia="0001", num=1234, saldo=1000.50, cliente=cliente1)
conta2 = Conta(tipo="poupança", agencia="0002", num=5678, saldo=2000.75, cliente=cliente2)

session.add_all([cliente1, cliente2, conta1, conta2])
session.commit()


# Recuperação de todos os clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f'Cliente: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}')
    for conta in cliente.contas:
        print(f'    Conta: {conta.tipo}, Agência: {conta.agencia}, Número: {conta.num}, Saldo: {conta.saldo}')

# Recuperação de todas as contas
contas = session.query(Conta).all()
for conta in contas:
    print(f'Conta: {conta.tipo}, Agência: {conta.agencia}, Número: {conta.num}, Saldo: {conta.saldo}, Cliente: {conta.cliente.nome}') 