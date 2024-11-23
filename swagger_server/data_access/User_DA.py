from swagger_server.database_setup import db, User
from swagger_server.models.usuario import Usuario

class User_DA:
    def __init__(self) -> None:
        pass


    def create_user(user:Usuario):
        # Crear un usuario
        userDB = User(
            nombre=user.nombre,
            apellido=user.apellido,
            email=user.email,
            password=user.password,
            role='user',
        )
        try:
            new = db.add(userDB)
            db.commit()
            return userDB
        except Exception as e:
            db.rollback()
            print(e)
            return None
    
    def get_user_by_id(id:int):
        # Obtener un usuario por ID
        try:
            user = db.query(User).get(id)
            return user
        except Exception as e:
            return None
        
    def get_user_by_email(email:str):
        # Obtener un usuario por email
        try:
            user = db.query(User).filter(User.email == email).first()
            return user
        except Exception as e:
            return None
    
    def get_all_users():
        # Obtener todos los usuarios
        try:
            users = db.query(User).all()
            return users
        except Exception as e:
            return None
    
    def update_user(user:Usuario):
        # Actualizar un usuario
        try:
            userDB = db.query(User).get(user.id)
            userDB.nombre = user.nombre
            userDB.apellido = user.apellido
            userDB.email = user.email
            userDB.password = user.password
            userDB.role = user.role
            db.commit()
            return userDB
        except Exception as e:
            db.rollback()
            return None

    
    def delete_user(id:int):
        # Eliminar un usuario
        user = db.query(User).get(id)
        db.delete(user)
        db.commit()
        return None
    
    def get_user_profiles(id_usuario:int):
        # Obtener todos los perfiles asociados a un usuario
        user = db.query(User).get(id_usuario)
        return user.perfiles
    
    def get_user_subscriptions(id_usuario:int):
        # Obtener todas las suscripciones asociadas a un usuario
        user = db.query(User).get(id_usuario)
        return user.subscriptions
    
