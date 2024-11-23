from swagger_server.database_setup import db, Plan as PlanDB
from swagger_server.models.plan import Plan

class Plan_DA:
    def __init__(self) -> None:
        pass

    def create_plan(plan:Plan):
        # Crear un plan
        planDB = PlanDB(
            nombre_plan=plan.nombre_plan,
            precio=plan.precio,
            descripcion=plan.descripcion,
        )
        try:
            new = db.add(planDB)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
            return None
    def get_plan_by_id(id_p: int):
        try:
            
            # Usar el nombre correcto del campo
            plan = db.query(PlanDB).filter(PlanDB.id_plan == id_p).first()
            
            return plan
        except Exception as e:
            print(f"Error retrieving plan with id_plan {id_p}: {e}")
            return None
    def get_all_plans():
        # Obtener todos los planes
        try:
            plans = db.query(PlanDB).all()
            return plans
        except Exception as e:
            return None
    def update_plan(plan:Plan):
        # Actualizar un plan
        try:
            plannDB = db.query(PlanDB).get(plan.id_plan)
            plannDB.nombre_plan = plan.nombre_plan
            plannDB.precio = plan.precio
            plannDB.descripcion = plan.descripcion
            db.commit()
            return plannDB
        except Exception as e:
            db.rollback()
            return None
    def delete_plan(id_plan:int):
        # Eliminar un plan
        try:
            plan = db.query(PlanDB).get(id_plan)
            db.delete(plan)
            db.commit()
            return True
        except Exception as e:
            return False