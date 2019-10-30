from db.Models import Usuario, Profile, Rol
from flask import request, Response
from flask import jsonify
from app import db, app
import re
import rut_chile

@app.route('/registro', methods=['POST'])
def registry():
    bodydata = request.get_json()
    new_user = Usuario()
    new_person = Profile()
    new_rol = Rol()
    persona = {
        "name": bodydata['name'],
        "lastname": bodydata['lastname'],
        "rut": bodydata['rut'],
        "verifcador": bodydata['verificador'],
        "email": bodydata['email'],
        "username": bodydata['username'],
        "password": bodydata['password'],
        "thumbnail": bodydata['thumbnail']
    }
    respuesta= persona + Response.status_code
    if bodydata is True:
        new_user.name = persona["name"]
        if (20 >= len(new_person.name) >= 5) and new_person.name:
            new_person.name.capitalize()
            new_person.last_name = persona["lastname"]
            if (20 <= len(new_person.last_name) >= 5) and new_person.last_name:
                new_person.last_name.capitalize()
                new_person.rut = persona["rut"]
                if rut_chile.is_valid_rut(new_person.rut):
                    new_person.persona["verificador"]
                    if rut_chile.get_verifiction_digit(new_person.rut) == new_person.dv:
                        new_user.mail = persona["email"]
                        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)][(a-z)]{2,15}$', new_user.mail.lower()):
                            new_user.username = persona["username"]
                            if 10 >= len(new_user.username) <=12:
                                new_user.password = persona["password"]
                                if re.match('^[(a-z0-9A-Z\_\.)]', new_user.password):
                                    new_user.image = persona["thumbnail"]
                                    if new_user.lower().endswitch('.jpeg','.png','.gif'):
                                         try:
                                            insertion = db.session.add(
                                                new_person.name,
                                                new_person.last_name,
                                                new_person.rut,
                                                new_person.dv,
                                                new_user.username,
                                                new_user.password,
                                                new_user.image)
                                            db.session.commit()
                                            raise ValueError("error al realizar la insercion de datos a la DB favor revisar")
                                         except ValueError as ve:
                                                print(ve)                                       
                                    else:
                                        jsonify("Formatos permitodos JPEG, PNG, GIF,Escritos en minisculas")
                            else:
                                jsonify("el correo exede o le faltan la cantidad de carateres permitidos")
                        else:
                            jsonify("favor validar el formato del correo electronico").Response.status_code=406
                    else:
                        jsonify(" favor validar que el digito verificador sea correcto ")
                else:
                    jsonify("rut invalido")
            else:
                return jsonify("validar cantdad de caracteres del apellido").Response
        else:
            return jsonify("validar largo de caracteres para usuario")
