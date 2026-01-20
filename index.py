from flask import Blueprint, render_template, abort, request, redirect, url_for, flash, session
from models import Users, db, BikeComputers, Orders

bp_index = Blueprint('index', __name__)

items = {
    'FC-001': {
        'id': 'FC-001',
        'title': 'Fahrradcomputer blau',
        'summary': 'Fahrradcomputer in der Farbe blau',
        'image_url': '/static/images/fc-1.jpg',
        'description': 'Ein robuster Fahrradcomputer mit Farbdisplay. Ideal für den täglichen Gebrauch.',
        'price': '€ 199,00'
    },
    'FC-002': {
        'id': 'FC-002',
        'title': 'Fahrradcomputer grau',
        'summary': 'Fahrradcomputer in der Farbe grau',
        'image_url': '/static/images/fc-2.jpg',
        'description': 'Eleganter Fahrradcomputer mit langen Batterielaufzeiten.',
        'price': '€ 199,00'
    },
    'FC-003': {
        'id': 'FC-003',
        'title': 'Fahrradcomputer grün',
        'summary': 'Fahrradcomputer in der Farbe grün',
        'image_url': '/static/images/fc-3.jpg',
        'description': 'Leichter Fahrradcomputer mit einfacher Bedienung.',
        'price': '€ 199,00'
    }
}


@bp_index.route('/')
def index():
    return render_template('index.html')


@bp_index.route('/catalog')
def catalog():
    items = BikeComputers.query.all()
    return render_template('catalog.html', items=items)


@bp_index.route('/detail/<int:item_id>')
def detail(item_id):
    item = BikeComputers.query.filter_by(bc_id=item_id).first()
    if not item:
        abort(404)
    return render_template('detail.html', item=item)

@bp_index.route('/login', methods=['POST'])
def login():
    print("Pressed Login Button")
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"Email: {email}, Password: {password}")

    user = Users.query.filter_by(email=email).first()

    if user and user.password == password:
        session['user_email'] = email
        session['user_id'] = user.user_id
        session['user_first_name'] = user.first_name
        session['user_last_name'] = user.last_name
        flash('Login erfolgreich!', 'success')
        return redirect(url_for('index.index'))
    else:
        flash('Ungültige E-Mail oder Passwort.', 'danger')
        return "Error: Falsche Daten"


@bp_index.route('/logout')
def logout():
    session.clear()
    flash('Sie wurden erfolgreich abgemeldet.', 'success')
    return redirect(url_for('index.index'))


@bp_index.route('/profile')
def profile():
    if 'user_email' not in session:
        flash('Bitte melden Sie sich zunächst an.', 'warning')
        return redirect(url_for('index.index'))
    
    user_email = session.get('user_email')
    user = Users.query.filter_by(email=user_email).first()
    
    if not user:
        session.clear()
        flash('Benutzerkonto nicht gefunden.', 'danger')
        return redirect(url_for('index.index'))
    
    return render_template('profile.html', user=user)


@bp_index.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')
    address = request.form.get('address')
    house_number = request.form.get('house_number')
    postal_code = request.form.get('postal_code')
    city = request.form.get('city')
    country = request.form.get('country')
    iban = request.form.get('iban')
    phone_number = request.form.get('phone_number')

    if Users.query.filter_by(email=email).first():
        flash('Ein Benutzer mit dieser E-Mail existiert bereits.', 'danger')
        return redirect(url_for('index.index'))

    new_user = Users(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password,
        address=address,
        house_number=house_number,
        postal_code=postal_code,
        city=city,
        country=country,
        iban=iban,
        phone_number=phone_number
    )


    db.session.add(new_user)
    db.session.commit()

    user = Users.query.filter_by(email=email).first()

    session['user_email'] = email
    session['user_id'] = user.user_id
    flash('Registrierung erfolgreich! Sie können sich jetzt anmelden.', 'success')
    return redirect(url_for('index.index'))


@bp_index.route('/orders')
def orders():
    if 'user_id' not in session:
        flash('Bitte melden Sie sich zunächst an.', 'warning')
        return redirect(url_for('index.index'))
    
    user_id = session.get('user_id')
    orders = Orders.query.filter_by(user_id=user_id).all()
    
    return render_template('orders.html', orders=orders)