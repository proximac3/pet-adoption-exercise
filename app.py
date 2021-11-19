from flask import Flask, request, render_template, flash, redirect, session
from models import db, connect_db, Pet
from forms import AddPetForm
 
from flask_debugtoolbar import DebugToolbarExtension
 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
 
app.config['SECRET_KEY'] = 'trisolarian879'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
 
connect_db(app)

@app.route('/')
def homepage():
    """Display Pets On HomePage"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/newPet', methods=['GET','POST'])
def add_new_pet():
    """Serve form for new pet['GET'] and submit form['POST'] """
    form = AddPetForm()

    if form.validate_on_submit():
        newPet = Pet(name=form.name.data, species=form.species.data, 
        photo_url=form.photo_url.data , age=form.age.data , 
        notes=form.notes.data , available=form.available.data)

        db.session.add(newPet)
        db.session.commit()
        return redirect('/')
    else:
        return  render_template('add_pet.html', form=form)


@app.route('/pet/details/<int:id>')
def petDetails(id):
    """Display Pet Details """
    pet = Pet.query.get_or_404(id)
    return render_template('pet_details.html', pet=pet)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_pet(id):

    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.species = form.species.data
        pet.name = form.name.data
        pet.age = form.age.data
        pet.available = form.available.data

        db.session.commit()

        return redirect('/')
    else:
        return render_template('edit_pet.html', form=form, pet=pet)













