import connexion
import six

from swagger_server.models.perfil import Perfil  # noqa: E501
from swagger_server import util


def usuarios_id_usuario_perfiles_get(id_usuario):  # noqa: E501
    """Obtener todos los perfiles asociados a un usuario

    Devuelve una lista de todos los perfiles asociados a un usuario específico según el ID del usuario. # noqa: E501

    :param id_usuario: ID del usuario
    :type id_usuario: int

    :rtype: List[Perfil]
    """
    return 'do some magic!'


def usuarios_perfiles_id_delete(id):  # noqa: E501
    """Eliminar un perfil dada un ID

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def usuarios_perfiles_id_get(id):  # noqa: E501
    """Obtener un perfil por la ID del perfil

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Perfil
    """
    return 'do some magic!'


def usuarios_perfiles_post(body):  # noqa: E501
    """Crear un perfil de usuario asociado a un usuario

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Perfil.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usuarios_perfiles_put(body):  # noqa: E501
    """Actualizar un perfil dada la ID del objeto pasado

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Perfil.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
