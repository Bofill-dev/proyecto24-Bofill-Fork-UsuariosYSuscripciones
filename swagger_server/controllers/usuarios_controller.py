import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.usuario import Usuario  # noqa: E501
from swagger_server import util


def login_get(username, password):  # noqa: E501
    """Iniciar sesión

    Permite verificar las credenciales de un usuario para iniciar sesión. # noqa: E501

    :param username: Nombre de usuario para autenticación.
    :type username: str
    :param password: Contraseña del usuario.
    :type password: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def usuarios_get():  # noqa: E501
    """Obtener lista de usuarios que se encuentra en la base de datos

     # noqa: E501


    :rtype: List[Usuario]
    """
    return 'do some magic!'


def usuarios_id_delete(id):  # noqa: E501
    """Eliminar un usuario según la ID pasada

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def usuarios_id_get(id):  # noqa: E501
    """Obtener un usuario por la ID pasada

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Usuario
    """
    return 'do some magic!'


def usuarios_post(body):  # noqa: E501
    """Crear un nuevo usuario en la pagina web

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usuarios_put(body):  # noqa: E501
    """Actualizar un usuario segun la ID pasada en el objeto usuario

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
