from models import session, Publisher, Book, Shop, Stock, Sale
from sqlalchemy import and_
if __name__ == '__main__':
    publisher_id = input('id издателя: ')
    p = session.query(Shop).\
        join(Stock, Stock.id_shop == Shop.id).\
        join(Book, Book.id == Stock.id_book).\
        join(Publisher, Publisher.id == Book.id_publisher).\
        filter(Publisher.id == int(publisher_id)).all()
    if len(p) > 0:
        for row in p:
            print(f'{row.name}')
    else:
        print(f'Издатель с индексом {publisher_id} не продаётся ни в одном магазине')
