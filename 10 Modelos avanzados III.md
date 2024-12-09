# Modelos avanzados II

Debo corregir esto. En realidad este archivo es modelos avanzados II, modelos avanzados I debe ser la construccion de la aplicacion biblioteca.

En definitiva debe quedar asi:

-1 Modelos avanzados - construcción de la aplicación.\
-2 Modelos avanzados I.\
-3 Modelos avanzados II.

IMPORTANTE: DEBES utilizar la ORM de Django cada vez que puedas en vez de usar solamente codigo python al hacer consultas a la base de datos, para optimizar al maximo. La ORM de Django estan absolutamente documentadas todas las posibilidades de interacciones con las bases de datos.

## Índice

* [1 Values, Group_by en la ORM Django](#1-Values,-Group_by-en-la-ORM-Django)
  * [11 Características](#11-Caracteristicas)

# 1 Values I

Queremos saber **cuantas veces se ha prestado un libro**. Esto podriamos resolverlo con un annotate() construyendo un manager en el modelo prestamo.

annotate() requiere de un criterio de agrupacion y por defecto, para esto toma el id de prestamo, lo que genera un error en el despliegue de resultados. En nuestro ejercicio los lista todos.

Debemos hacer la consulta en el modelo libro, pero tambien generara un error, porque cosiderara todos. Debemos utilizar la funcion **values**.

La función values() en Django se utiliza para crear una QuerySet que devuelve diccionarios en lugar de instancias de modelos. Cada diccionario representa un objeto y **las claves** del diccionario son los nombres de los campos del modelo.

# 2 Values II

Ahora, queremos que la consulta devuelva el titulo del libro, para ello utilizamos la función **Lower**.

podemos agregar la funcionalidad de incluir un lector.

# 3 Herramientas de Postgres para busquedas (trigram similarity)

## 3.1 Concepto e instalacion

Queremos un buscador que nos retorne un libro a partir de una palabra clave. La trigram similarity de postgres en Django es una técnica que permite realizar búsquedas de texto más flexibles y precisas utilizando el concepto de trigramas. Un trigrama es una secuencia de tres caracteres consecutivos de una cadena que se combinan obteniendo diferentes secuencias para hacer un calculo de probabilides que coincida con algun dato. Esta técnica se utiliza para medir la similitud entre cadenas de texto, lo que es útil para encontrar coincidencias aproximadas.

Debemos activar triagram e indicar sobre que tabla y atributo actue a postgres:

sudo apt-get 

su postgres
psql dbbiblioteca
CREATE EXTENSION pg_trgm;
CREATE INDEX libro_titulo_idx ON libro_libro USING GIN(titulo gin_trgm_ops);

## 3.2 Implementacion de triagram

- Declaramos complementos de postgres para Django en nuesta seccion INSTALLED_APPS

- Escribimos nuestro manager:

from django.contrib.postgres.search import TrigramSimilarity

// some code

def listar_libros_trg(self, kword):
   if kword:
      resultado
      
- Hacemos una vista ListLibrosTrg

- Creamos la vista 

# Registrando datos dentro de nuestra base de datos La class Meta

## la class Meta introduccion

En Django, la clase Meta es una clase interna que se utiliza para proporcionar opciones de configuración adicionales a un modelo. Estas opciones permiten personalizar el comportamiento del modelo, como el nombre de la tabla en la base de datos, el orden de los registros, las restricciones únicas, entre otros.

## Cambiando nombres a las tablas en Postgres

Crearemos una nueva aplicacion en nuestra appbiblioteca:

django-admin startapp home

Vamos a postgres desde pgadmin y vemos como se han creado las tablas de nuestras aplicaciones

Posgres crea los nombres de tablas con el nombre de la app y luego el nombre de la tabla.

Para ello creamos un modelo Persona en nuestra nueva aplicacion home:

class Persona(models.Model):

## unique_together

## No  ingresar a menores de 18 (constrains) (gte)

- hacemos las migraciones:

- Registramos en los admin

- Verifiquemos agregando una persona menor de 18 en el administrador de django.

## Creamos dos modelos que hereden de persona

Necesitamos ingresar a empleados que hereden de persona y cliente.

Podemos no necesitar que se construya el modelo Persona en la base de datos, para ello agregamos el atributo abstract = True.

## Aplicando herencia en nuestra app biblioteca

los modelos autor y lector pueden heredar de un modelo teorico Persona.

- Debemos homologar los campos.

- Quitamos la aplicacion home de als app_instaladas
  
- Hacemos las migraciones

- Vamos a reestructurar nuestra base de datos, para lo que que instalaremos una nueva, pero para no perder toda la data almacenada debemos hacer un back up de datos.

## Crear un BackApp de datos y resstructuracion de los modelos.

- Creamos una carpeta llamada **resguardo**
- accedemos a postgres
- eliminamos la base de datos
- creamos la base de datos
  >
- ingresamos a ella y le damos permisos
- reestablecemos la base de datos

  <

- En django borramos todas la migraciones hechas.

- Resstructuramos nuestro proyecto

Creamos el modelo Persona y los que heredan: Autor y Lector

Haremos una falsa migracion

# Managers de tipo registro

## FormView para registrar un prestamo

144

- Hacemos la vista FormView ReguistraPrestamo(FormView):

class RegistrarPrestamo(FormView):
   template_name = ''

- construimos un formulario (forms.py)
  
- creamos el template add_prestamo.html
  
* agregamos la url y tmabien la principal de la aplicaicon

## Metodos Create y Save

class RegistrarPrestamo(FormView):











































