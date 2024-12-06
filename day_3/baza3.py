# sqlalchemy - system ORM do pracy z bazą danych w sposób obiektowy
# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///moja_baza.db', echo=True)
Base = declarative_base()


# encja - kalsa odwzorowująca tabele w bazie danych
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship('Address',
                             back_populates="person",
                             order_by="Address.email",
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person",
                          back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

anakin = Person(name="Anakin", age=38)
obi = Person(name="Obi Wan Kenobi", age=45)
obi.addresses = [
    Address(email='obi@example.pl'),
    Address(email='obi@example.com'),
]

session.add(anakin)
session.add(obi)

session.commit()

all_ = session.query(Person).all()
print(all_)
# [Anakin(id=1),
# Anakin(id=2),
# Obi Wan Kenobi(id=3),
# Anakin(id=4),
# Obi Wan Kenobi(id=5),
# Anakin(id=6), Obi Wan
#  Kenobi(id=7)]
