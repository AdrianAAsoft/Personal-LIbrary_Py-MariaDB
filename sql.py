#Importar biblioteca de SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError

#Cadena de conexion de la bd
try:
    #cadena = motor+lenguaje://usuario:contraseña@red(comunmente localhost):puerto de bd(defecto 3306)/base de datos (ya creada)
    engine = create_engine("mysql+pymysql://root:admin1234@localhost:3306/libreria", echo=False, future=True)
except OperationalError as e:
    print("Error al conectar con la base de datos:", e)
    raise

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()       

#iniciador de tabla
class tabla1(Base):
    __tablename__ = "libro"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    autor = Column(String(100), nullable=False)
    genero = Column(String(80), nullable=False)
    ano = Column(Integer, nullable=False)
    estado_lectura = Column(Integer, nullable=False)   # 1 leído, 0 no leído

    def __repr__(self):
        return f"<Libro {self.id} - {self.titulo}>"

#Creacion de tabla
def tabla():
    try:
        Base.metadata.create_all(engine)
        print("Tablas listas.")
    except SQLAlchemyError as e:
        print(" Error al crear tablas:", e)

#Funciones para agregar, actualizar, eliminar, ver listado de libros y buscar libros 

def AddLibro(Titulo,Autor,Genero,Ano,Estado):
    db = SessionLocal()
    try:
        nuevo = tabla1(
            titulo=Titulo,
            autor=Autor,
            genero=Genero,
            ano=Ano,
            estado_lectura=Estado
        )

        db.add(nuevo)
        db.commit()
        db.close()
        print("Libro Agregado.")

    except IntegrityError:
        db.rollback()
        print("Error de integridad. Datos duplicados o invalidos.")
    except SQLAlchemyError as e:
        db.rollback()
        print("Error SQL:", e)
    finally:
        db.close()

def UpdateLibro(id1, Titulo, Autor, Genero, Ano, Estado):
    db = SessionLocal()
    libro = db.query(tabla1).filter_by(id=id1).first()

    try:

        if libro:
            libro.titulo = Titulo
            libro.autor = Autor
            libro.genero = Genero
            libro.ano = Ano
            libro.estado_lectura = Estado
            db.commit()
            print("Se actualizo el libro exitosamente.")
        else:
            print("No existe el libro.")

    except SQLAlchemyError as e:
        db.rollback()
        print("Error al actualizar libro:", e)
    finally:
        db.close()

def DeleteLibro(id1):
    db = SessionLocal()
    libro = db.query(tabla1).filter_by(id=id1).first()

    try:

        if libro:
            db.delete(libro)
            db.commit()
            print("Se ha eliminado un libro de la base de datos.")
        else:
            print("No existe el libro.")

    except SQLAlchemyError as e:
        db.rollback()
        print("Error al eliminar libro:", e)
    finally:
        db.close()

def ListLibros():
    db = SessionLocal()

    listado = db.query(tabla1).all()
    db.close()
    return listado

def GetLibro(campo,id):
    db = SessionLocal()

    if campo == "titulo":
        libro = db.query(tabla1).filter(tabla1.titulo.like(f"%{id}%")).all()

    elif campo == "autor":
        libro = db.query(tabla1).filter(tabla1.autor.like(f"%{id}%")).all()

    elif campo == "genero":
        libro = db.query(tabla1).filter(tabla1.genero.like(f"%{id}%")).all()

    else:
        libro = []
    
    db.close()
    return libro