from swagger_server.data_access.Plans_DA import Plan_DA
from swagger_server.database_setup import db, Subscription
from swagger_server.models.suscripcion import Suscripcion
from swagger_server.database_setup import Plan
from sqlalchemy.orm import joinedload


class Subscription_DA:
    def __init__(self) -> None:
        pass
    
    def create_subscription(subscription:Suscripcion):
        # Crear una suscripcion
        subscriptionDB = Subscription(
            id_usuario=subscription.id_usuario,
            id_subscription=subscription.id_subscription,
            fecha_inicio=subscription.fecha_inicio,
            fecha_fin=subscription.fecha_fin,
            estado=subscription.estado,
            id_plan=subscription.id_plan
        )
        try:
            new = db.add(subscriptionDB)
            db.commit()
            return subscriptionDB
        except Exception as e:
            db.rollback()
            print(e)
            return None
    def get_subscription_by_id(id_:int):
        # Obtener una suscripcion por ID
        try:
            subscription = db.query(Subscription).get(id_)
            return subscription
        except Exception as e:
            return None
    def get_all_subscriptions():
        # Obtener todas las suscripciones
        try:
            subscriptions = db.query(Subscription).all()
            return subscriptions
        except Exception as e:
            return None
    from datetime import datetime

    def update_subscription(subscription: Suscripcion):
        # Actualizar una suscripcion
        try:
            subscriptionDB = db.query(Subscription).get(subscription.id_subscription)
            if not subscriptionDB:
                return None  # La suscripción no existe

            subscriptionDB.id_usuario = subscription.id_usuario
            subscriptionDB.id_subscription = subscription.id_subscription
            subscriptionDB.fecha_inicio = subscription.fecha_inicio
            subscriptionDB.fecha_fin = subscription.fecha_fin
            subscriptionDB.estado = subscription.estado
            subscriptionDB.id_plan = subscription.id_plan

            db.commit()
            return subscriptionDB
        except Exception as e:
            db.rollback()
            print(f"Error updating subscription: {e}")
            return None

    def delete_subscription(id_:int):
        # Eliminar una suscripcion
        try:
            subscription = db.query(Subscription).get(id_)
            db.delete(subscription)
            db.commit()
            return subscription
        except Exception as e:
            return None
    def change_subscription_state(id_:int, estado:str):
        # Cambiar estado de una suscripcion
        try:
            subscription = db.query(Subscription).get(id_)
            subscription.estado = estado
            db.commit()
            return subscription
        except Exception as e:
            return None
    def get_plan_names_by_user_id(id_usuario):
        try:
            # Obtener las suscripciones del usuario
            suscripciones = db.query(Subscription).filter_by(id_usuario=id_usuario).all()
            
            
            if not suscripciones:
                
                return None, "No subscriptions found for this user"
            
            # Recuperar los nombres de los planes a partir de las suscripciones
            nombres_planes = []
            for suscripcion in suscripciones:
                
                plan = Plan_DA.get_plan_by_id(int(suscripcion.id_plan))
                print(f"Plan recuperado: {plan}")
                
                if plan:
                    
                    nombres_planes.append(plan.nombre_plan)
                else:
                    print(f"No se encontró ningún plan con id_plan: {suscripcion.id_plan}")
            
            print(f"Nombres de planes recopilados: {nombres_planes}")
            return nombres_planes, None
        except Exception as e:
            print(f"Error retrieving plan names: {e}")
            return None, "Internal server error"
        

