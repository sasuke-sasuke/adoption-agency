from flask import Flask, redirect, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'mychickensteve'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()


@app.route('/')
def home():
    """Home Page"""
    pets = Pet.query.order_by(Pet.id.desc()).limit(3).all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Handles serving the pet form and adding pet to database"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f'{pet.name} added successfully!')
        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route('/<pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Handles serving the edit pet form and updating the database"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f'{ pet.name } updated successfully')
        return redirect('/')
    else:
        return render_template('edit.html', pet=pet, form=form)