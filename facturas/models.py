
from sqlalchemy import Column, Integer, String, Float
from facturas.database import Base

class Entrada(Base):
    __tablename__ = 'Entradas'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    dia = Column(Integer)
    mes = Column(Integer)
    empresa = Column(String(120), unique=True)
    base_imponible = Column(Float)
    iva = Column(Integer)

    def as_dict(self):
	return {"numero" : self.numero,
	        "dia" : self.dia,
	        "mes" : self.mes,
	        "empresa" : self.empresa,
	        "base_imponible" : self.base_imponible,
	        "iva" : self.iva }

    def __init__(self, numero, dia, empresa, base_imponible, iva, mes):
        self.numero = numero
        self.dia = dia
        self.empresa = empresa
	self.base_imponible = base_imponible
	self.iva = iva
	self.mes = mes

    def __repr__(self):
        return '<Entrada {0} - {1}>'.format(self.numero, self.empresa)
