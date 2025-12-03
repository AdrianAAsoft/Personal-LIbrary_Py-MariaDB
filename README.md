# Personal-LIbrary_Py-MariaDB
Modificar la aplicación original de biblioteca personal para sustituir SQLite por MariaDB como motor de base de datos e integrar el uso de Object-Relational Mapping (ORM) mediante la biblioteca SQLAlchemy

## 📌 Instalacion de MySql:
1. Ingresar al sitio: [https://dev.mysql.com/downloads/installer/]
2. Instalar
3. Ejecutar instalador
   
## 🧪 Creacion de la base de datos
- Abrir MySql Command Line Client
- Colocar contraseña creada en la instalacion
- Escribir el siguiente comando: "Create Database libreria"
```bash
Create Database libreria
exit
```

## 📌 Instalacion de libreria para el ambiente:

```bash
pip install sqlalchemy pymysql
```

## 📁 Archivos

```bash
├── main.py            # Modulo principal
├── sql.py             # Modulo de funciones MySql con SQLAlchemy 
```

## ▶️ Ejecución
Ejecuta el programa con:
```bash
python main.py
```

## 🧪 Ejemplo de Uso

```python
#Ejecucion interna para creacion de las tablas de la base de datos
======= BIBLIOTECA =======
1. Agregar nuevo libro
2. Actualizar información de un libro
3. Eliminar libro existente
4. Ver listado de libros
5. Buscar libros
6. Salir
```
