from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,MetaData,Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()
base = declarative_base()
r=(os.getenv("s"))
engine = create_engine(r)
Session = sessionmaker(bind=engine)
session = Session()
# metadata=MetaData()
class Customerse(base):
    __tablename__ = 'customerses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)
    age=Column(Integer)
    invoices = relationship("Invoice",secondary="cus_inv", back_populates="customer", passive_deletes=True)
class Invoice(base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    order = Column(String)
    customer = relationship("Customerse", secondary="cus_inv",back_populates="invoices",passive_deletes=True)
    del_ids= relationship("delivery",secondary="del_inv",back_populates="inv_ids",passive_deletes=True)

class delivery(base):
    __tablename__="deliveries"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    inv_ids=relationship("Invoice",secondary="del_inv",back_populates="del_ids",passive_deletes=True)

class Cus_inv(base):
    __tablename__='cus_inv'
    user_id= Column(Integer,ForeignKey("customerses.id",ondelete="CASCADE"),primary_key=True)
    cust_id=Column(Integer,ForeignKey("invoices.id",ondelete="CASCADE"),primary_key=True)

class Del_inv(base):
    __tablename__="del_inv"
    del_id=Column(Integer,ForeignKey("deliveries.id",ondelete="CASCADE"),primary_key=True)
    inv_id=Column(Integer,ForeignKey("invoices.id",ondelete="CASCADE"),primary_key=True)


base.metadata.create_all(engine)

# session.add_all([Customerse(name="ravi", address="kochi", email="...@gmail.com"),
#                  Customerse(name='hari', address='trivandrum', email='......@gmail.com'),
#                 Customerse( name="tanvi", address="kozhikkode", email="........@gmail.com")])
# session.commit()

# session.add_all([Invoice(order="phone"),
#                  Invoice(order='lap'),
#                  Invoice(order='fan'),
#                  Invoice(order="switch"),
#                  Invoice(order="car")])
# session.add_all([delivery(name="man1"),delivery(name="man2"),delivery(name="man3")])
# session.commit()
# session.add_all([Del_inv(del_id=1,inv_id=1),Del_inv(del_id=3,inv_id=2),Del_inv(del_id=2,inv_id=1)])
# cus_inv_data = session.add_all([
#     Cus_inv(user_id=2, cust_id=1),  # Associate customer with ID 1 with invoice with ID 1
#     Cus_inv(user_id=3, cust_id=1),  # Associate customer with ID 1 with invoice with ID 2
#     Cus_inv(user_id=1, cust_id=3),  # Associate customer with ID 2 with invoice with ID 3
#     # Add more entries as needed
# ])
# session.add(Invoice(order='fan',cust_id=5))


# Create a Table object and associate it with the metadata



session.commit()
# session.query(Customerse).update({Customerse.name :"Mr "+Customerse.name})

# result = session.query(Customerse,Invoice).join(Cus_inv,Customerse.id==Cus_inv.user_id).join(Invoice,Invoice.id==Cus_inv.cust_id).filter(Customerse.id == 2).all()

# if result:
# #     for customer, invoice in result:
#         print(f"Customer ID: {customer.id}, Name: {customer.name}, Order: {invoice.order}")
# else:
#     print(f"Customer with ID  not found.")

# Close the session when you're done
session.close()
