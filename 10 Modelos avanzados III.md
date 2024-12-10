# Modelos avanzados II

Debo corregir esto. En realidad este archivo es modelos avanzados II, modelos avanzados I debe ser la construccion de la aplicacion biblioteca.

En definitiva debe quedar asi:

-1 Modelos avanzados - construcción de la aplicación.\
-2 Modelos avanzados I.\
-3 Modelos avanzados II.

IMPORTANTE: DEBES utilizar la ORM de Django cada vez que puedas en vez de usar solamente codigo python al hacer consultas a la base de datos, para optimizar al maximo. La ORM de Django estan absolutamente documentadas todas las posibilidades de interacciones con las bases de datos.

```bash
cd /
C:\> cd /mis_entornos/entorno_2/Scripts
C:\mis_entornos\entorno_2\Scripts> activate
(entorno_2) C:\mis_entornos\entorno_1\Scripts> cd \mis_proyectos\biblio\biblioteca
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py runserver 
```

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

IMPORTANTE: Son COMUNES las salidas erroneas cuando verificamos los managers por la shell, por lo que es conveniente reiniciar la shell de Django `>>> exit()` cada vez que se va a revisar el comportamiento de un manager.

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py shell
>>> exit()
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

## Índice

* [1 Values I](#1-Values-I)
  * [11 Características](#11-Caracteristicas)
* [2 Values II](#2-Values-II)
* [3 Herramientas de Postgres para busquedas (trigram similarity)](#3-Herramientas-de-Postgres-para-busquedas-(trigram-similarity))
  * [3.1 Concepto e instalacion](#31-Concepto-e-instalacion)
  * [3.2 Implementacion de triagram](#32-Implementacion-de-triagram)

# 1 Values I

Consideremos la tabla **Prestamo**. Queremos saber **cuántas veces se ha prestado cada libro**. Esto podríamos resolverlo con un **annotate()** construyendo un manager en el modelo Prestamo.

```python
 def num_libros_prestados(self): 
    resultado = self.annotate( 
       num_prestados = Count('libro')      
    )
    for r in resultado:
       print('---')
       print(r, r.num_prestados)
    return resultado
```

Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.num_libros_prestados()
```

![image](https://github.com/user-attachments/assets/282937d9-cb13-4f19-856f-dd5b7bd058db)
![image](https://github.com/user-attachments/assets/d5ea8d69-95a2-48e4-8941-6358240820ab)

Vemos que lista todo.

Lo que sucede es que **annotate()** requiere de un criterio de agrupación que, por defecto, **toma del id de prestamo**, lo que genera un error en el despliegue de resultados: los lista todos. La consulta deberia hacerse dentro del modelo Libro. No olvidemos utilizar la clave inversa: libro_prestamo.

```python
class LibroManager(models.Manager):

// some code
   
   def num_libros_prestados(self): 
      resultado = self.annotate( 
         num_prestados = Count('libro_prestamo')      
      )
      for r in resultado:
         print('---')
         print(r, r.num_prestados)
      return resultado
```

Verificamos en la shell:

```bash
from applications.libro.models import *
Libro.objects.num_libros_prestados()
```

**Me dice la shell que no reconoce la funcion**

Modificamos el manager:

La función values() en Django se utiliza para crear una QuerySet que devuelve diccionarios en lugar de instancias de modelos. Cada diccionario representa un objeto y **las claves** del diccionario son los nombres de los campos del modelo. Con **values** indicamos el criterio sobre el cual agrupar.

```python
class PrestamoManager(models.Manager): 

// some code
   
   def num_libros_prestados(self): 
      resultado = self.values('libro'
      ).annotate( 
         num_prestados = Count('libro')      
      )
      for r in resultado:
         print('---')
         print(r, r['num_prestados'])
      return resultado
```

Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.num_libros_prestados()
```

**Me continua desplegado el resultado sin considerar la modificacion a la funcion**

# 2 Values II

Ahora, queremos que la consulta devuelva el titulo del libro, para ello utilizamos la función **Lower**.

```python
from django.db.models.functions import Lower # type: ignore
 
class PrestamoManager(models.Manager): 

//some code
   
   def num_libros_prestados(self): 
      resultado = self.values('libro'
      ).annotate( 
         num_prestados = Count('libro'),
         titulo = Lower('libro__titulo')     
      )
      for r in resultado:
         print('---')
         print(r, r['num_prestados'])
      return resultado
```

Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.num_libros_prestados()
```

![image](https://github.com/user-attachments/assets/fd86b2c7-628f-4685-aea9-2d23730f759b)

podemos agregar la funcionalidad de incluir un lector:

```python
from django.db.models.functions import Lower # type: ignore
 
class PrestamoManager(models.Manager): 

//some code
   
   def num_libros_prestados(self): 
      resultado = self.values('libro','lector'
      ).annotate( 
         num_prestados = Count('libro'),
         titulo = Lower('libro__titulo')     
      )
      for r in resultado:
         print('---')
         print(r, r['num_prestados'])
      return resultado
```

![image](https://github.com/user-attachments/assets/7d040b34-c4ae-47ba-bbdc-0eb29350011d)

# 3 Herramientas de Postgres para busquedas (trigram similarity)

## 3.1 Concepto e instalacion

Queremos un buscador que nos retorne un libro a partir de una palabra clave. La trigram similarity de postgres en Django es una técnica que permite realizar búsquedas de texto más flexibles y precisas utilizando el concepto de trigramas. Un trigrama es una **secuencia de tres caracteres consecutivos** de una cadena que se combinan obteniendo diferentes secuencias para hacer un calculo de probabilidades que coincida con algun dato. Esta técnica se utiliza para medir la similitud entre cadenas de texto, lo que es útil para encontrar coincidencias aproximadas.

Debemos activar triagram e indicar sobre que tabla y atributo actúe postgres. Vamos a la shell de Postgres sobre Windows:

Para ir a PowerShell como administrador:

- 1 presiona Windows + X y selecciona "Terminal (Administrador)" o "Windows PowerShell (Admin)".\
- 2 dirígete al binario de postgres
- 3 conéctate a la base de datos como superusuario
- 4 ingresa la contraseña
- 5 crear la extensión pg_trgm.

```bash
Windows PowerShell
Copyright (C) Microsoft Corporation. Todos los derechos reservados.

Instale la versión más reciente de PowerShell para obtener nuevas características y mejoras. https://aka.ms/PSWindows

PS C:\Users\chris> cd 'C:\Program Files\PostgreSQL\16\bin'
PS C:\Program Files\PostgreSQL\16\bin> psql -U postgres -d dbbiblioteca
psql : El término 'psql' no se reconoce como nombre de un cmdlet, función, archivo de script o
programa ejecutable. Compruebe si escribió correctamente el nombre o, si incluyó una ruta de
acceso, compruebe que dicha ruta es correcta e inténtelo de nuevo.
En línea: 1 Carácter: 1
+ psql -U postgres -d dbbiblioteca
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (psql:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: No se encontró el comando psql, pero existe en la ubicación actual. Windows PowerShell no carga comandos de la ubicación actual de forma predeterminada. Si confía en este comando, escriba ".\psql". Vea "get-help about_Command_Precedence" para obtener información más detallada.
PS C:\Program Files\PostgreSQL\16\bin> .\psql -U postgres -d dbbiblioteca
Contraseña para usuario postgres:

psql (16.4)
ADVERTENCIA: El código de página de la consola (850) difiere del código
            de página de Windows (1252).
            Los caracteres de 8 bits pueden funcionar incorrectamente.
            Vea la página de referencia de psql «Notes for Windows users»
            para obtener más detalles.
Digite «help» para obtener ayuda.

dbbiblioteca=# CREATE EXTENSION pg_trgm;
CREATE EXTENSION
dbbiblioteca=#
```

- 6 crea el index:

```bash
dbbiblioteca=# CREATE INDEX libro_titulo_idx ON libro_libro USING GIN(titulo gin_trgm_ops);
CREATE INDEX
dbbiblioteca=#

GIN(titulo gin_trgm_ops);: titulo es el atributo sobre el cual queremos que actue la triagramación.
```

## 3.2 Implementacion de triagram

- 1 Debemos indicarle a Django que trabajaremos con la triagramacion de Postgres.

Para ello nos dirigimos a **base.py** de la aplicacion biblioteca y le indicamos que traiga complementos de postgres para django:

![image](https://github.com/user-attachments/assets/e8172c2a-95ab-458b-bc6b-0a036abd2a75)

- 2 Creamos el manager:

Importamos TrigramSimilarity y creamos el manager listar_libros_trg en la clase **LibroManager()**:

```python
from django.contrib.postgres.search import TrigramSimilarity # type: ignore
   
class LibroManager(models.Manager):

   def listar_libros_trg(self,kword):
      if kword:
         resultado = self.filter(
            titulo__trigram_similar =kword,
      )
         return resultado
      else:
         self.all()[:10]
      return resultado
```     
      
- 3 Creamos una vista en views.py de la aplicacion libro:

```python
class ListLibrosTrg(ListView):
   context_object_name ='lista_libros'
   template_name = 'libro/lista.html'

   def get_queryset(self):
      palabra_clave = self.request.GET.get('kword','')

      return Libro.objects.listar_libros_trg(palabra_clave)
```
      
- 4 construimos una url en urls.py de la app libro:

```python
   path(
      'libros-trg/', 
      views.ListLibrosTrg.as_view(),
      name ='libros-trg'
  ),
```







***
***
<br>
<br>
<br>



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

145

class RegistrarPrestamo(FormView):











































