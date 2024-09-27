# Vistas basadas en clases

[ccbv.co.uk](https://ccbv.co.uk)

## Índice

* [El método ListView](#1-El-método-ListView)
  * [a) Listar todos los empleados](#a-Listar-todos-los-empleados)
  * [b) Listar todos los empleados que pertenezcan a un departamento](#b-Listar-todos-los-empleados-que-pertenezcan-a-un-departamento)
  * [c) Listar todos los empleados que pertenezcan a un departamento mediante urls con un filtro en una caja de texto](#c-Listar-todos-los-empleados-que-pertenezcan-a-un-departamento-mediante-urls-con-un-filtro-en-una-caja-de-texto)
  * [Algunas propiedades de la vista ListView](#Algunas-propiedades-de-la-vista-ListView)
    * [Paginación en la vista ListView](#Paginación-en-la-vista-ListView)
    * [Orden al listado](#Orden-al-listado)   
  * [d) Listar las habilidades de un empleado](#d-Listar-las-habilidades-de-un-empleado)
    
## El método ListView

[Documentacion ListView](https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/#listview)

El método **ListView** en Django es una vista genérica basada en clases utilizada para listar objetos de un modelo en una página web. 

Entrega tres grandes funcionalidades:

1 se encarga de obtener una lista de objetos de un modelo y renderizarlos en una plantilla.\
2 puede habilitar la paginación para dividir la lista de objetos en varias páginas.\
3 proporciona un **contexto** a la plantilla que incluye la lista de objetos y otros datos adicionales.

Implementaremos cinco requerimientos de listado sobre nuestra aplicación **empleados**.

a) Listar todos los empleados.\
b) Listar todos los empleados que pertenezcan a un departamento.\
c) Listar todos los empleados que pertenezcan a un departamento mediante urls con un filtro en una caja de texto.\
d) Listar las habilidades de un empleado.

### a) Listar todos los empleados.
