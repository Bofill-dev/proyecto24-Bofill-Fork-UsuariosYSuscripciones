import connexion
import six

from swagger_server.models.perfil import Perfil  # noqa: E501
from swagger_server import util
from swagger_server.data_access.Profile_DA import Profile_DA
from swagger_server.models.perfil import Perfil
from swagger_server.data_access.User_DA import User_DA




def usuarios_perfiles_id_delete(id_):  # noqa: E501
    """Eliminar un perfil dada un ID

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    # Comprobar si el perfil existe
    perfil = Profile_DA.get_profile_by_id(id_)
    if perfil is None:
        return "El perfil no existe", 404
    
    # Eliminar el perfil
    Profile_DA.delete_profile(id_)
    return None, 204


def usuarios_perfiles_id_get(id_):  # noqa: E501
    """Obtener un perfil por la ID del perfil

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Perfil
    """
    perfil = Profile_DA.get_profile_by_id(id_)
    if perfil is None:
        return "El perfil no existe", 404
    return perfil.to_dict(), 200



def usuarios_perfiles_post(body):  # noqa: E501
    """Crear un perfil de usuario asociado a un usuario

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Perfil.from_dict(connexion.request.get_json())  # noqa: E501
        nuevoPerfil = Profile_DA.create_profile(body)
        if nuevoPerfil is None:
            return "Error al crear el perfil", 400
    return nuevoPerfil.to_dict(), 201

def usuarios_perfiles_put(body):  # noqa: E501
    """Actualizar un perfil dada una ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Perfil.from_dict(connexion.request.get_json())  # noqa: E501
        perfil = Profile_DA.update_profile(body)
        if perfil is None:
            return "Error al actualizar el perfil", 400
    return None, 204




def usuarios_id_usuario_perfiles_get(id_usuario):  # noqa: E501
    """Obtener todos los perfiles asociados a un usuario

    Devuelve una lista de todos los perfiles asociados a un usuario específico según el ID del usuario. # noqa: E501

    :param id_usuario: ID del usuario
    :type id_usuario: int

    :rtype: List[Perfil]
    """
    user_profiles = User_DA.get_user_profiles(id_usuario)
    return [profile.to_dict() for profile in user_profiles]