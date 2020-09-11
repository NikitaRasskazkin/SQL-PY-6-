from models import Publisher, Book, Shop, Stock, Sale, session

if __name__ == '__main__':
    session.add_all([
        Publisher(id=1, name='Поставщик №1'),
        Publisher(id=2, name='Поставщик №2'),
        Publisher(id=3, name='Поставщик №3')
    ])
    session.commit()
    session.add_all([
        Book(id=1, title='Книга 1 поставщика №1', id_publisher=1),
        Book(id=2, title='Книга 2 поставщика №1', id_publisher=1),
        Book(id=3, title='Книга 3 поставщика №1', id_publisher=1),
        Book(id=4, title='Книга 1 поставщика №2', id_publisher=2),
        Book(id=5, title='Книга 2 поставщика №2', id_publisher=2),
        Book(id=6, title='Книга 1 поставщика №3', id_publisher=3)
    ])
    session.commit()
    session.add_all([
        Shop(id=1, name='Магазин №1'),
        Shop(id=2, name='Магазин №2')
    ])
    session.commit()
    session.add_all([
        Stock(id=1, count=3, id_book=1, id_shop=1),
        Stock(id=2, count=2, id_book=1, id_shop=2),
        Stock(id=3, count=5, id_book=2, id_shop=2),
        Stock(id=4, count=0, id_book=3, id_shop=1),
        Stock(id=5, count=2, id_book=4, id_shop=1),
        Stock(id=6, count=3, id_book=4, id_shop=2),
        Stock(id=7, count=4, id_book=6, id_shop=1)
    ])
    session.commit()
    session.add_all([
        Sale(id=1, price=15, date_sale='11.02.2020', id_stock=1, count=3),
        Sale(id=2, price=10, date_sale='11.03.2020', id_stock=1, count=2),
        Sale(id=3, price=13, date_sale='10.02.2020', id_stock=2, count=1),
        Sale(id=4, price=30, date_sale='11.04.2020', id_stock=3, count=3),
        Sale(id=5, price=14, date_sale='11.04.2020', id_stock=4, count=2)
    ])
    session.commit()
