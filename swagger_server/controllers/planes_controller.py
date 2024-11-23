import connexion
import six

from swagger_server.models.plan import Plan  # noqa: E501
from swagger_server import util


def planes_get():  # noqa: E501
    """Obtener lista de planes de suscripción que se enucuentren en la base de datos

     # noqa: E501


    :rtype: Plan
    """
    return 'do some magic!'


def planes_id_plan_delete(id_plan):  # noqa: E501
    """Eliminar una suscripción por ID

    Elimina una suscripción existente dada la ID de la suscripción. # noqa: E501

    :param id_plan: ID del plan que se quiere eliminar.
    :type id_plan: int

    :rtype: None
    """
    return 'do some magic!'


def planes_post(body):  # noqa: E501
    """Crear un nuevo plan de suscripción

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Plan.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def planes_put(body):  # noqa: E501
    """Actualizar una suscripción existente por ID

    Actualiza la suscripción n. Permite cambiar detalles como el plan, precio y estado. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Plan
    """
    if connexion.request.is_json:
        body = Plan.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
