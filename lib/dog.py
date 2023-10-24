from models import Dog  # Import your Dog model here

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    pass
    session.add(dog)
    session.commit()

def get_all(session):
    pass
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    pass
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    pass
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    pass
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    pass
    session.query(Dog).update({
        Dog.breed: breed
    })