"""Seed Files to make sample pets data"""

from models import Pet, db
from app import app

db.drop_all()
db.create_all()

dababy = Pet(name='Dababy', species='Curl Cat', photo_url='https://images.unsplash.com/photo-1557246565-8a3d3ab5d7f6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1170&q=80', age=2, notes='Name says it all', available=True)

kitkat = Pet(name='Kit Kat', species='Short Tail', photo_url='https://media.istockphoto.com/photos/kitten-at-home-garden-wall-picture-id1273661469?b=1&k=20&m=1273661469&s=170667a&w=0&h=K-b-88J89oSBIwbD0WhhDoOvybcbjfePJoOHS0grHHA=', age=3, notes='Cutest cat on earth', available=True)

zeus = Pet(name='Zeus', species='Great Dane', photo_url='https://images.unsplash.com/photo-1572017262635-8d454a28995e?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Z3JlYXQlMjBkYW5lfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60', age=1, notes='The Dogfather', available=True)

elon = Pet(name='Elon', species='Doge', photo_url='https://images.unsplash.com/photo-1622190994281-8b48849440e9?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1172&q=80', age=2, notes='Moon Boy', available=False)

db.session.add(dababy)
db.session.add(kitkat)
db.session.add(zeus)
db.session.add(elon)

db.session.commit()