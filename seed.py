from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

lynt = Pet(name='Lynt', species='dog', photo_url='https://animalcorner.org/wp-content/uploads/2020/06/black-pomeranian.png', age=1, available=True)
huskers = Pet(name='Huskers', species='dog', photo_url='https://thumbs.dreamstime.com/z/old-husky-lying-boards-nibbles-bone-138541128.jpg', age=32, available=True)
cheeto = Pet(name='Cheeto', species='dog', photo_url='https://post.bark.co/wp-content/uploads/2019/06/chihuahua-1024x634.png', age=2, available=True)

pets = [lynt, huskers, cheeto]

db.session.add_all(pets)
db.session.commit()