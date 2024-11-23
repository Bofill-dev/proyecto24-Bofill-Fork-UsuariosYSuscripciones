import connexion
import six

from swagger_server.models.plan import Plan  # noqa: E501
from swagger_server import util
from swagger_server.data_access.Plans_DA import Plan_DA
from flask import jsonify


def planes_get():  # noqa: E501
    """Obtener lista de planes de suscripción que se enucuentren en la base de datos

     # noqa: E501


    :rtype: Plan
    """
    plans = Plan_DA.get_all_plans()
    if plans is None:
        plans=[]
        return plans, 500
    
    # Convertir los objetos Plan a diccionarios
    plans_list = [plan.to_dict() for plan in plans]
    return jsonify(plans_list), 200
    


def planes_id_plan_delete(id_plan):  # noqa: E501
    """Eliminar una suscripción por ID

    Elimina una suscripción existente dada la ID de la suscripción. # noqa: E501

    :param id_plan: ID del plan que se quiere eliminar.
    :type id_plan: int

    :rtype: None
    """
    plan=Plan_DA.get_plan_by_id(id_plan)
    if plan is not None:
        Plan_DA.delete_plan(id_plan)
        return "Plan eliminado exitosamente"
    else:
        return "Plan no encontrado"
    


def planes_put(body):  # noqa: E501
    """Actualizar una suscripción existente por ID

    Actualiza la suscripción n. Permite cambiar detalles como el plan, precio y estado. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id_plan: ID del plan que se desea actualizar.
    :type id_plan: int

    :rtype: Plan
    """

    if connexion.request.is_json:
        body = Plan.from_dict(connexion.request.get_json())  # noqa: E501
        plan=Plan_DA.get_plan_by_id(body.id_plan)
        if not plan:
            return "Plan no encontrado", 404
    plan=Plan_DA.update_plan(body)
    print(f"Plan: {plan}")
    return None


def planes_post(body):  # noqa: E501
    """Crear un nuevo plan de suscripción

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Plan.from_dict(connexion.request.get_json())  # noqa: E501
    Plan_DA.create_plan(body)
    return None