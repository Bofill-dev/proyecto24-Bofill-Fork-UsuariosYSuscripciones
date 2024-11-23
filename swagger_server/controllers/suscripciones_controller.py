import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.suscripcion import Suscripcion  # noqa: E501
from swagger_server import util
from swagger_server.data_access.Subscription_DA import Subscription_DA
from swagger_server.data_access.User_DA import User_DA
from swagger_server.data_access.Plans_DA import Plan_DA



def suscripciones_id_subscription_delete(id_subscription):  # noqa: E501
    """Eliminar una suscripción de usuario

    Elimina una relación de suscripción existente entre un usuario y un plan de suscripción. # noqa: E501

    :param id_subscription: ID de la suscripción de usuario a eliminar.
    :type id_subscription: int

    :rtype: None
    """
    sub=Subscription_DA.get_subscription_by_id(id_subscription)
    if sub is None:
        return "La suscripcion no existe", 404
    else:
        Subscription_DA.change_subscription_state(id_subscription, "Cancelada")
        return 'Cancelada subscripcion con el id: ' + str(id_subscription)


def suscripciones_id_subscription_get(id_subscription):  # noqa: E501
    """Obtener las suscripciones de un usuario

    Devuelve todas las suscripciones (activas, canceladas, o finalizadas) asociadas a un usuario específico según el ID del usuario. # noqa: E501

    :param id_subscription: ID del usuario para obtener todas sus suscripciones.
    :type id_subscription: int

    :rtype: List[Suscripcion]
    """
    user = User_DA.get_user_by_id(id_subscription)
    if user is None:
        return "El usuario no existe", 404
    else:
        subs = User_DA.get_user_subscriptions(id_subscription)
        subs_dict = [sub.to_dict() for sub in subs]
        return subs_dict  # Ahora `subs_dict` es JSON serializable



def suscripciones_put(body):  # noqa: E501
    """Actualizar los detalles de la suscripción de usuario

    Permite actualizar los detalles de la suscripción de un usuario, como las fechas o el estado de la suscripción. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id_subscription: ID de la suscripción de usuario a actualizar.
    :type id_subscription: int

    :rtype: Suscripcion
    """
    if connexion.request.is_json:
        body = Suscripcion.from_dict(connexion.request.get_json())  # noqa: E501
    Subscription_DA.update_subscription(body)
    return None


def suscripciones_post(body):  # noqa: E501
    """Crear una nueva suscripción de usuario

    Crea una nueva relación entre un usuario y un plan de suscripción. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Suscripcion
    """
    
    if connexion.request.is_json:
        body = Suscripcion.from_dict(connexion.request.get_json())  # noqa: E501
    Subscription_DA.create_subscription(body)
    return None

  
  
def usuarios_id_usuario_suscripcion_get(id_usuario):  # noqa: E501
    """Obtener el nombre del plan de suscripción de un usuario

    Devuelve el nombre del plan de suscripción al que está suscrito un usuario específico según el ID del usuario. # noqa: E501

    :param id_usuario: ID del usuario
    :type id_usuario: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'

def usuarios_id_usuario_suscripcion_post(body, id_usuario):  # noqa: E501
    """Crear una nueva suscripción para un usuario

    Permite crear una suscripción. La suscripción se añadirá con el plan y detalles proporcionados. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id_usuario: ID del usuario para el que se va a crear la suscripción.
    :type id_usuario: int

    :rtype: Suscripcion
    """
    if connexion.request.is_json:
        body = Suscripcion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'