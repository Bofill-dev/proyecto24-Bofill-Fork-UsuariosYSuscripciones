from sqlalchemy import *
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import class_mapper

# Crear una clase base para las tablas
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)  # Aquí podrías aplicar hashing al guardar la contraseña
    role = Column(String, nullable=False)  # Puede ser un rol como 'admin', 'user', etc.

    # Relación con perfiles 
    perfiles = relationship('Profile', back_populates='user', cascade="all, delete-orphan")
    # 'Subscription' es otro modelo relacionado
    subscriptions = relationship('Subscription', back_populates='user', cascade="all, delete-orphan")

    def to_dict(self, include_relations=True):
        """
        Convierte la instancia del modelo a un diccionario.

        :param include_relations: Si es True, incluye las relaciones (perfiles y subscriptions).
        :return: Diccionario con los datos del usuario.
        """
        # Mapea los atributos de la clase a un diccionario, excluyendo la contraseña
        user_dict = {
            column.key: getattr(self, column.key)
            for column in class_mapper(self.__class__).columns
            #if column.key != 'password'  # Excluir la contraseña
        }

        if include_relations:
            # Incluir perfiles
            user_dict['perfiles'] = [perfil.to_dict() for perfil in self.perfiles]
            # Incluir suscripciones
            user_dict['subscriptions'] = [subscription.to_dict() for subscription in self.subscriptions]

        return user_dict

class Profile(Base):
    __tablename__ = 'perfiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('users.id'), nullable=False)  # Clave foránea hacia la tabla User
    apodo = Column(String, nullable=False)
    imagen_avatar = Column(String, nullable=True)  # Puede ser nullable en caso de que el usuario no tenga imagen

    # Relación inversa con el modelo User
    user = relationship('User', back_populates='perfiles')

    def to_dict(self, include_user=False):
        """
        Convierte la instancia del modelo Perfil a un diccionario.

        :param include_user: Si es True, incluye información básica del usuario relacionado.
        :return: Diccionario con los datos del perfil.
        """
        perfil_dict = {
            column.key: getattr(self, column.key)
            for column in class_mapper(self.__class__).columns
        }

        if include_user and self.user:
            perfil_dict['user'] = {
                'id': self.user.id,
                'nombre': self.user.nombre,
                'apellido': self.user.apellido,
                'email': self.user.email,
                'role': self.user.role
                # Excluye campos sensibles como 'password'
            }

        return perfil_dict

class Plan(Base):
    __tablename__ = 'planes'

    id_plan = Column(Integer, primary_key=True, autoincrement=True)
    nombre_plan = Column(String, nullable=False)
    precio = Column(Float, nullable=False)  # El precio será de tipo float
    descripcion = Column(String, nullable=True)  # Descripción del plan, puede ser opcional

    def to_dict(self):
        """
        Convierte la instancia del modelo Plan a un diccionario.

        :return: Diccionario con los datos del plan.
        """
        plan_dict = {
            column.key: getattr(self, column.key)
            for column in class_mapper(self.__class__).columns
        }
        return plan_dict
    

class Subscription(Base):
    __tablename__ = 'subscriptions'

    id_subscription = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('users.id'), nullable=False)  # Clave foránea hacia User
    id_plan = Column(Integer, ForeignKey('planes.id_plan'), nullable=False)  # Clave foránea hacia Plan
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    estado = Column(String, nullable=False)  # Estado de la suscripción (e.g., activa, cancelada)

    # Relaciones con User y Plan
    user = relationship('User', back_populates='subscriptions')
    plan = relationship('Plan')
    

    def to_dict(self, include_user=False, include_plan=False):
        """
        Convierte la instancia del modelo Subscription a un diccionario.

        :param include_user: Si es True, incluye información básica del usuario relacionado.
        :param include_plan: Si es True, incluye información básica del plan relacionado.
        :return: Diccionario con los datos de la suscripción.
        """
        subscription_dict = {
            column.key: getattr(self, column.key)
            for column in class_mapper(self.__class__).columns
        }

        if include_user and self.user:
            subscription_dict['user'] = {
                'id': self.user.id,
                'nombre': self.user.nombre,
                'apellido': self.user.apellido,
                'email': self.user.email,
                'role': self.user.role
                # Excluye campos sensibles como 'password'
            }

        if include_plan and self.plan:
            subscription_dict['plan'] = {
                'id_plan': self.plan.id_plan,
                'nombre_plan': self.plan.nombre_plan,
                'precio': self.plan.precio,
                'descripcion': self.plan.descripcion
            }

        return subscription_dict

# Crear el motor de base de datos usando SQLite (el archivo se llamará 'mydatabase.db')
engine = create_engine('sqlite:///database.db')


# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
db = Session()
