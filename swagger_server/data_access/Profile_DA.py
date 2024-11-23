from swagger_server.database_setup import db, Profile
from swagger_server.models.perfil import Perfil

class Profile_DA:
    def __init__(self) -> None:
        pass
    
    def create_profile(profile:Perfil):
        # Crear un perfil
        profileDB = Profile(
            id_usuario=profile.id_usuario,
            apodo=profile.apodo,
            imagen_avatar=profile.imagen_avatar,
        )
        try:
            new = db.add(profileDB)
            db.commit()
            return profileDB
        except Exception as e:
            db.rollback()
            print(e)
            return None
    
    def get_profile_by_id(id:int):
        # Obtener un perfil por ID
        try:
            profile = db.query(Profile).get(id)
            return profile
        except Exception as e:
            return None
        
    def get_all_profiles():
        # Obtener todos los perfiles
        try:
            profiles = db.query(Profile).all()
            return profiles
        except Exception as e:
            return None
    
    def update_profile(profile:Perfil):
        # Actualizar un perfil
        try:
            profileDB = db.query(Profile).get(profile.id)
            profileDB.id_usuario = profile.id_usuario
            profileDB.apodo = profile.apodo
            profileDB.imagen_avatar = profile.imagen_avatar
            db.commit()
            return profileDB
        except Exception as e:
            return None
        
    def delete_profile(id:int):
        # Eliminar un perfil
        try:
            profile = db.query(Profile).get(id)
            db.delete(profile)
            db.commit()
        except Exception as e:
            db.rollback()
            return None