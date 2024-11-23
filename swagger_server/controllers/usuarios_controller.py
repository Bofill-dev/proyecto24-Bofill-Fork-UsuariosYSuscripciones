import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.perfil import Perfil  # noqa: E501
from swagger_server.models.suscripcion import Suscripcion  # noqa: E501
from swagger_server.models.usuario import Usuario  # noqa: E501
from swagger_server import util
from swagger_server.data_access.User_DA import User_DA

def login_get(username, password):  # noqa: E501
    """Iniciar sesión

    Permite verificar las credenciales de un usuario para iniciar sesión. # noqa: E501

    :param username: Nombre de usuario para autenticación.
    :type username: str
    :param password: Contraseña del usuario.
    :type password: str

    :rtype: InlineResponse200
    """
    user = User_DA.get_user_by_email(username)
    if user and user.password == password:
        return {
            "success":True,
            "id":user.id,
            "nombre":user.nombre,
            "apellido":user.apellido,
            "email":user.email,
            "role":user.role,
            }, 200
    else:
        return InlineResponse200(success=False), 403
    


def usuarios_get():  # noqa: E501
    """Obtener lista de usuarios que se encuentra en la base de datos

     # noqa: E501


    :rtype: List[Usuario]
    """
    users = User_DA.get_all_users()
    return [user.to_dict() for user in users]


def usuarios_id_delete(id_):  # noqa: E501
    """Eliminar un usuario según la ID pasada

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    # Comprobar si el usuario existe
    user = User_DA.get_user_by_id(id_)
    if user is None:
        return "El usuario no existe", 404
    
    User_DA.delete_user(id_)
    return None


def usuarios_id_get(id_):  # noqa: E501
    """Obtener un usuario por la ID pasada

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Usuario
    """
    user = User_DA.get_user_by_id(id_)
    if user is None:
        return "El usuario no existe", 404
    return user.to_dict()


def usuarios_post(body):  # noqa: E501
    """Crear un nuevo usuario en la pagina web

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
        # Verificar si el usuario ya existe
        usuario_existente = User_DA.get_user_by_email(body.email)
        if usuario_existente is not None:
            return "El usuario ya existe", 400
        
        nuevo_usuario_creado = User_DA.create_user(body)
        if nuevo_usuario_creado is None:
            return "Error creando el usuario, el usuario nuevo es igual a None", 500
        
    return nuevo_usuario_creado.to_dict(), 201



def usuarios_put(body):  # noqa: E501
    """Actualizar un usuario segun la ID pasada en el objeto usuario

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
        user = User_DA.update_user(body)
    return None

