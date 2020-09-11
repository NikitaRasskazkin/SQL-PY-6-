from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy import sql
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql+psycopg2://postgres:password@localhost/SQLPY(6)')
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    id_publisher = Column(Integer, ForeignKey('publisher.id'))
    children = relationship('Publisher', backref='book')


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    id_book = Column(Integer, ForeignKey('book.id'))
    id_shop = Column(Integer, ForeignKey('shop.id'))
    book = relationship('Book', backref='stock')
    shop = relationship('Shop', backref='stock')


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    date_sale = Column(Date)
    id_stock = Column(Integer, ForeignKey('stock.id'))
    count = Column(Integer)
    children = relationship('Stock', backref='sale')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
