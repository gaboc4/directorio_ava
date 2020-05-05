import os
import stripe
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

import smtplib
from .models import Users, Business
from . import db

main = Blueprint('main', __name__)

services = ['Alquiler de vivienda', 'Compra de vivienda', 'Plomeria', 'Manicura', 'Seguro', 'Servicios Venezolanos', 'Comida',
            'Electricidad', 'Pintura', 'Reparaciones Generales', 'Pediatra', 'Medico General - Familiar',
            'Medico Natural', 'Dentista', 'Optometro', 'Clases de Ingles', 'Escuelas y Colegios', 'Escuelas Superiores',
            'Gimnasios', 'Baile', 'Restaurantes', 'Food Truck', 'Compra o Venta de Vehiculos', 'Reparacion Mecanica',
            'Pintura', 'Peluqueria', 'Traducciones', 'Abogado', 'Immigracion', 'Impueastos', 'Otro']


@main.route('/')
@main.route('/index')
def index():
	businesses = Business.query.all()
	businesses_list = []
	for b in businesses:
		business_dict = {}
		owner = Users.query.filter_by(id=b.owner_id).first()
		business_dict['name'] = b.name
		business_dict['owner'] = owner.first_name + ' ' + owner.last_name
		business_dict['business_email'] = b.business_email
		business_dict['phone_number'] = b.phone_number
		business_dict['sector'] = b.sector
		business_dict['address'] = b.address
		business_dict['description'] = b.description
		businesses_list.append(business_dict)

	return render_template('index.html', businesses=businesses_list)


@main.errorhandler(500)
def internal_server_error(e):
	return render_template('error.html')


@main.route('/contact_form', methods=['POST'])
def contact_form():
	try:
		smtp_obj = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
		smtp_obj.ehlo()
		smtp_obj.login(os.environ['EMAIL_ACCT'], os.environ['EMAIL_PASS'])
		message = 'Subject: {}\n\n{}'.format('Servicios Contact Form',
		                                     str(request.form.get('contact_msg')))
		smtp_obj.sendmail(request.form.get('contact_email'), "info@venezuelaenaustin.org",
		                  message)
		flash("Gracias, te responderemos pronto!")
		return redirect(url_for('main.index'))
	except Exception as e:
		print(e)
		flash('Uvo un problema mandando tu pregunta, por favor intente de nuevo o contacte a info@venezuelaenaustin.org')
		return redirect(url_for('main.index'))


@main.route('/profile')
@login_required
def profile():
	user = Users.query.filter_by(email=current_user.email).first()
	business = Business.query.filter_by(owner_id=user.id).first()

	if business is None:
		return render_template('profile.html', name=user.first_name, business_name='',
	                       business_address='', phone_number='',
	                       services=services, business_email='')
	else:
		return render_template('profile.html', name=user.first_name, business_name=business.name,
	                       business_address=business.address, phone_number=business.phone_number,
	                       services=services, business_email=business.business_email)


@main.route('/update_company', methods=['POST'])
@login_required
def update_company():
	user = Users.query.filter_by(email=current_user.email).first()
	business = Business.query.filter_by(owner_id=user.id).first()

	name = request.form.get('business_name')
	address = request.form.get('business_address')
	phone_number = request.form.get('phone_number')
	email = request.form.get('business_email')
	sector = request.form.get('business_sector')
	description = request.form.get('business_description')

	if business is not None:
		business.name = name
		business.address = address
		business.phone_number = phone_number
		business.business_email = email
		business.sector = sector
		business.description = description

		db.session.commit()
	else:
		new_business = Business(owner_id=user.id, name=name,
		                        address=address, phone_number=phone_number,
		                        sector=sector, business_email=email, description=description)
		db.session.add(new_business)
		db.session.commit()

	return redirect(url_for('main.profile'))
