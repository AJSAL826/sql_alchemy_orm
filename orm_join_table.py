from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

base = declarative_base()

engine = create_engine('postgresql://postdb:postdb616@localhost:5432/btech')
Session = sessionmaker(bind=engine)
session = Session()

class Customer(base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)
    invoices = relationship("Invoice", back_populates="customer")

class Invoice(base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    order = Column(String)
    cust_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="invoices")

base.metadata.create_all(engine)

# session.add_all([Customer(name="ravi", address="kochi", email="...@gmail.com"),
#                  Customer(name='hari', address='trivandrum', email='......@gmail.com'),
#                 Customer( name="tanvi", address="kozhikkode", email="........@gmail.com")])
# session.add_all([Invoice(order="phone",cust_id=1),
#                  Invoice(order='lap',cust_id=2),
#                  Invoice(order='fan',cust_id=1),
#                  Invoice(order="switch",cust_id=3),
#                  Invoice(order="car",cust_id=2)])
# session.commit()


 # Specify the customer ID you want to query
session.query(Customer).update({Customer.name :"Mr "+Customer.name})
session.commit()

result = session.query(Customer, Invoice).join(Invoice).filter(Customer.id == 1).all()

if result:
    for customer, invoice in result:
        print(f"Customer ID: {customer.id}, Name: {customer.name}, Order: {invoice.order}")
else:
    print(f"Customer with ID {customer_id} not found.")

# Close the session when you're done
session.close()

#


