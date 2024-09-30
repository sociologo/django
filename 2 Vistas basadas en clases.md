# Vistas basadas en clases

[ccbv.co.uk](https://ccbv.co.uk)

## Índice

* [1 El método ListView](#1-El-método-ListView)
  * [a) Listar todos los empleados](#a-Listar-todos-los-empleados)
  * [b) Listar todos los empleados que pertenezcan a un departamento](#b-Listar-todos-los-empleados-que-pertenezcan-a-un-departamento)
  * [c) Listar todos los empleados que pertenezcan a un departamento mediante urls con un filtro en una caja de texto](#c-Listar-todos-los-empleados-que-pertenezcan-a-un-departamento-mediante-urls-con-un-filtro-en-una-caja-de-texto)
  * [Algunas propiedades de la vista ListView](#Algunas-propiedades-de-la-vista-ListView)
   * [Paginación en la vista ListView](#Paginación-en-la-vista-ListView)
   * [Orden al listado](#Orden-al-listado)   
  * [d) Listar las habilidades de un empleado](#d-Listar-las-habilidades-de-un-empleado)
* [2 El método DetailView](#2-El-método-DetailView)
* [3 El método CreateView](#3-El-método-CreateView)
  * [Nuevos campos compuestos en el modelo de empleados.](#Nuevos-campos-compuestos-en-el-modelo-de-empleados.)
* [4 El método UpdateView](#4-El-método-UpdateView)
* [5 El método DeleteView](#5-El-método-DeleteView)

## 1 El método ListView

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

1 En el archivo **views.py** de la aplicación **empleados** debemos importar el método **ListView**, el modelo **Empleado** y construir la clase **ListAllEmpleados**:

![image](https://github.com/user-attachments/assets/491a04e7-d89c-4090-bc02-e62e51e4b613)

2 Debemos activar nuestra vista genérica, para lo cual vamos al archivo urls.py de la aplicacion empleados, importamos las **views**, declaramos la url: **listar-todo-empleado/** y hacemos el llamado a la clase sobre la cual hemos basado nuestra vista:

![image](https://github.com/user-attachments/assets/65b5777f-d842-4d0b-8396-43ffe3e926bc)

3 La url recién declarada no la hemos activado en las urls principales de Django, para lo cual vamos al archivo urls.py de la aplicación **empleado** (acá se puede producir una confusión. La aplicación en singular **empleado** es la que alberga por completo nuestro proyecto; la aplicación el plural **empleados**, alberga la aplicación del contexto específico del modelo empleados).

![image](https://github.com/user-attachments/assets/f3d27b19-6972-4d3c-b98e-766378bfcd00)

4 Por último debemos construir el archivo list_all.html dentro de una carpeta **persona** en la ruta de los **templates**:

![image](https://github.com/user-attachments/assets/a00d7484-f0e6-436a-a604-58b4f01aecd5)

en la que iteramos sobre registros de modelos para listarlos:

```
<h1>
    Lista de todos los empleados
</h1>

<ul>
    {% for e in lista %}
        <li>{{ e }}</li>
    {% endfor %}
</ul>
```

5 Y ejecutamos nuestro proyecto:

![image](https://github.com/user-attachments/assets/3d22080e-b269-43aa-b2de-2cc4f7c29a74)

### b) Listar todos los empleados que pertenezcan a un departamento.

Hagamos una modificación en en el archivo admin.py de **empleados** para que en el despliegue de registros de empleados vía nuestro administrador Django, también aparezca el filtro de departamentos:

![image](https://github.com/user-attachments/assets/a56029c8-95b0-41a0-bc18-9e16251719f2)

![image](https://github.com/user-attachments/assets/58b8a710-240f-43c1-a043-339758e38407)

Es éste el proceso que replicaremos con código utilizando el atributo **queryset**:

Primero haremos ésto en duro listando todos los empleados del departamento 'ciencias matemáticas'.

1 En **views.py** de la aplicación **empleados** construímos la clase **ListAllByDept**:

![image](https://github.com/user-attachments/assets/61ff3f4a-820c-4b58-87fa-cb570d968ba9)

2 En **urls.py** de la aplicación **empleado** le asignamos su ruta:

![image](https://github.com/user-attachments/assets/6874053f-f969-44c8-93a7-b5bd66a77bc1)

3 En la carpeta **persona** que está en la carpeta **templates** añadimos **AllByDept.html**:

![image](https://github.com/user-attachments/assets/2d933f85-416e-4ea8-8f3e-a54680b41a13)

4 y obtenemos:

![image](https://github.com/user-attachments/assets/4501354e-605f-4d0c-b97d-9d2b6e3f1a25)

que comprobamos es correcto:

![image](https://github.com/user-attachments/assets/f8380b72-1ec0-478b-a8fc-71bff0fee0f2)

Debemos utilizar ahora una forma eficiente para hacer lo anterior utilizando **get_queryset()**, filtrando a través de una caja de texto:

### c) Listar todos los empleados que pertenezcan a un departamento mediante urls con un filtro en una caja de texto.

1 Debemos utilizar el método **get_queryset** para recoger un parámetro desde la url. **kwards** es un método de Django que nos permite recoger elementos desde las urls.

![image](https://github.com/user-attachments/assets/a1a5d8bc-d7a8-49f2-b8d8-9f40adaa414f)

2 Necesitamos una caja de texto html para que el usuario pueda hacer una búsqueda filtrada. En la carpeta **persona** de templates construímos **by_kword.html**. Añadimos una clave de acceso {% csrf_token %}

![image](https://github.com/user-attachments/assets/978b96de-2042-459b-b419-71b71524291e)

Nuestro resultado de búsqueda para 'ciencias matemáticas' es:

![image](https://github.com/user-attachments/assets/086db168-ed34-425a-9edb-4f888c91402d)

Nuestro resultado de búsqueda para 'ciencias físicas' es:

![image](https://github.com/user-attachments/assets/793e997f-1ecb-4aa5-95a2-fcb05ff67450)

### Algunas propiedades de la vista ListView.

#### Paginación en la vista ListView.

La paginación es crucial al listar registros en Django por varias razones:

**Rendimiento**: Cargar todos los registros de una base de datos grande en una sola página puede ser muy lento y consumir muchos recursos del servidor. La paginación permite dividir los datos en partes más manejables, mejorando el rendimiento de la aplicación.

**Usabilidad**: Presentar demasiados datos en una sola página puede ser abrumador para los usuarios. La paginación facilita la navegación y hace que la interfaz sea más amigable y fácil de usar.

**Carga de Red**: Al limitar la cantidad de datos enviados al cliente en cada solicitud, se reduce la carga de red, lo que puede ser especialmente importante en aplicaciones con muchos usuarios concurrentes.

**Experiencia del Usuario**: La paginación permite a los usuarios encontrar y acceder a la información de manera más eficiente, mejorando su experiencia general en la aplicación.

Con **paginate_by** le indicamos a la clase **ListAllEmpleados** la cantidad de registros que despligue por página:

![image](https://github.com/user-attachments/assets/9dde698d-5393-4cd1-9855-daddaaec6c72)
![image](https://github.com/user-attachments/assets/29e4c2c9-6d3d-4a31-b419-926e4b27684e)
![image](https://github.com/user-attachments/assets/d1ef1023-dc74-4328-b906-bc657583d4a0)

#### Orden al listado.

El atributo **ordering** en la vista ListView de Django se utiliza para especificar el orden en que se deben mostrar los objetos en la lista. Este atributo espera una lista o tupla de nombres de campos por los cuales se debe ordenar el queryset. 

![image](https://github.com/user-attachments/assets/d87577d1-ca09-4e3a-a562-defd67768cd4)
![image](https://github.com/user-attachments/assets/b46c3c31-7cb5-4ad1-9f49-6b0d8d90c4e3)

### d) Listar las habilidades de un empleado.

Recordemos que **habilidades** con **empleado** es una relación de muchos a muchos:

![image](https://github.com/user-attachments/assets/474c08a0-0f4b-4b25-923f-d0a0abce7570)

1 Hacemos que en el listado de empleados del administrador de django se visualice el id de cada registro:
![image](https://github.com/user-attachments/assets/f6fb0e9f-c29d-4e34-b46a-7f8c241a83d4)
![image](https://github.com/user-attachments/assets/d5d6e353-d41b-48f5-90c4-17018d9bf6f0)

2 Construímos la vista **ListEmpByHabili** en la que recuperamos de un cuadro de texto el id de un empleado
y desplegamos la lista de sus habilidades. Le asignamos por defecto el valor id = 4 y añadimos un control de excepciones:

![image](https://github.com/user-attachments/assets/ce01ea5b-3613-41e7-9155-a09dbe3a18ad)

3 Activamos la vista:
![image](https://github.com/user-attachments/assets/336ad63c-7d11-4886-91b2-92c71a7e6fc3)

4 Construímos el html **by_habili.html**:

![image](https://github.com/user-attachments/assets/9b245bf7-5bbf-4560-99b0-3324214867f5)

5 Buscamos por id = 5

![image](https://github.com/user-attachments/assets/28e7092a-b400-4ed5-8168-2b0307276a63)
![image](https://github.com/user-attachments/assets/f6d0ef91-8102-417d-b116-b774b0c64306)

## 2 El método DetailView

La vista DetailView en Django es una vista genérica basada en clases que se utiliza para mostrar los detalles de un solo objeto. 

Atributos Principales:

**model**: Especifica el modelo del objeto que se va a mostrar.\
**template_name**: Define el nombre de la plantilla que se utilizará para renderizar la vista. Si no se especifica, Django buscará una plantilla con el nombre <nombre_del_modelo>_detail.html.\
**context_object_name**: Define el nombre del objeto en el contexto de la plantilla. Por defecto, Django usa object, pero puedes cambiarlo a algo más descriptivo.

URL y Parámetros:

La URL que apunta a una DetailView generalmente incluye un parámetro que identifica al objeto, como un ID o un slug (en el contexto de desarrollo web, un slug es la parte final de una URL que identifica de manera única una página específica dentro de un sitio web. Por ejemplo, en la URL https://www.ejemplo.com/articulos/que-es-un-slug, el slug es **que-es-un-slug**. Los slugs son importantes para el SEO (optimización en motores de búsqueda) porque pueden contener palabras clave que ayudan a los motores de búsqueda a entender el contenido de la página. Un buen slug debe ser claro, conciso y relevante para el contenido de la página). Este parámetro se pasa a la vista para que pueda recuperar el objeto correcto de la base de datos.

Métodos Personalizables:

**get_queryset()**: Puedes sobrescribir este método para personalizar la consulta que obtiene el objeto.\
**get_context_data()**: Permite agregar datos adicionales al contexto que se pasa a la plantilla.

1 Importamos DetailView:
![image](https://github.com/user-attachments/assets/a2b7d679-6503-471e-98b1-dce877a58779)

2 Creamos una clase DetailView:
![image](https://github.com/user-attachments/assets/2f52d8e2-0ee5-4de2-ade0-ceb5ccaea4ad)

3 Activamos la vista declarando una URL con un pk:
![image](https://github.com/user-attachments/assets/60899bde-374d-4746-aaf1-9a8665da7956)

4 Construimos el html asociado:
![image](https://github.com/user-attachments/assets/b1082852-2cab-4f9b-8c12-bbc66fa94b94)

5 Accedemos a la URL con un pk específico:

![image](https://github.com/user-attachments/assets/a279bf78-aa95-4efb-95f5-36493a89c24a)

### 1 El método **get_context_data**.

El método **get_context_data** en Django se utiliza para agregar datos adicionales al contexto que se pasa a la plantilla. Este método devuelve un diccionario de contexto que luego se utiliza para renderizar (en el contexto de Django, renderizar se refiere al proceso de tomar una plantilla (template) y combinarla con datos del contexto para generar una página web completa que se envía al navegador del usuario) la plantilla.

![image](https://github.com/user-attachments/assets/7b3584dd-7b96-493c-b13c-e01fd6903fb6)

![image](https://github.com/user-attachments/assets/1046ab85-e330-49df-bfc3-1d7a5dd02de8)

![image](https://github.com/user-attachments/assets/cdb3d9ab-6f6d-4b1d-809f-a27ad02d9f42)



## 3 El método CreateView

1 Importamos las vistas genericas que necesitaremos, el paquete reverse_lazy y construimos la clase con su template y los **fields**:

En Django, los fields en la vista CreateView son cruciales porque determinan qué campos del modelo se incluirán en el formulario que se presenta al usuario para crear una nueva instancia del modelo. Aquí hay algunas razones por las que son importantes:

**Control de Datos**: Permiten especificar exactamente qué campos del modelo deben ser rellenados por el usuario, asegurando que solo se recopile la información necesaria.

**Validación**: Los campos definidos en el formulario se validan automáticamente según las reglas establecidas en el modelo, lo que ayuda a mantener la integridad de los datos.

**Seguridad**: Al definir explícitamente los campos, se evita que usuarios malintencionados envíen datos no deseados o intenten modificar campos que no deberían ser accesibles.

**Facilidad de Uso**: Proporcionan una manera sencilla de generar formularios sin necesidad de escribir mucho código adicional, aprovechando las capacidades de las vistas basadas en clases (CBV) de Django

Diferencias entre los métodos GET y POST en el protocolo HTTP, especialmente en relación con las URLs:

Método GET

**Transmisión de Datos**: Los datos se envían a través de la URL como parámetros de consulta (query string). Por ejemplo, http://example.com/page?name=John&age=30.

**Visibilidad**: Los datos son visibles en la barra de direcciones del navegador, lo que puede ser menos seguro para información sensible.

**Uso Común**: Ideal para solicitudes de lectura, como obtener datos de un servidor sin realizar cambios en él.

**Limitaciones de Tamaño**: Tiene restricciones en la cantidad de datos que se pueden enviar debido a la longitud máxima de la URL.

Método POST

**Transmisión de Datos**: Los datos se envían en el cuerpo de la solicitud HTTP, no en la URL.

**Visibilidad**: Los datos no son visibles en la barra de direcciones del navegador, lo que proporciona mayor seguridad para información sensible.

**Uso Común**: Adecuado para solicitudes de escritura, como enviar datos a un servidor para ser procesados (por ejemplo, formularios de registro).

**Sin Limitaciones de Tamaño**: No tiene restricciones significativas en la cantidad de datos que se pueden enviar.

Debemos indicar una vez que se haya hecho el post a que pagina deseamos redireccionar.

![image](https://github.com/user-attachments/assets/fb96eace-ebb5-415d-b687-684f22258744)

2 Construimos los htmls

![image](https://github.com/user-attachments/assets/5f656981-16f5-4d68-8820-38609a101819)

![image](https://github.com/user-attachments/assets/78d48cc8-60d7-4883-871e-72406dcbc083)

3 Activamos las vistas con urls:

El paquete **reverse_lazy**

El paquete reverse_lazy en Django es una versión evaluada de forma diferida de la función reverse. Se utiliza para generar una URL para una vista en un momento posterior, generalmente cuando se necesita la URL. Esto es especialmente útil en situaciones donde la configuración de URL de tu proyecto aún no se ha cargado, como en vistas basadas en clases genéricas, ya que los atributos de clase en Python se evalúan al importar.

![image](https://github.com/user-attachments/assets/617e0be1-f8f3-46eb-8293-c8f78e2269fe)

4 Agreguemos un empleado:

![image](https://github.com/user-attachments/assets/4465a0a6-dd6c-423b-9551-cf31024e56b7)

![image](https://github.com/user-attachments/assets/421f4595-9bdb-4b19-90d3-eaa4c2e086df)

![image](https://github.com/user-attachments/assets/1b7b780e-6a06-41b1-ba91-4518f7716850)

![image](https://github.com/user-attachments/assets/7a5c9965-781b-49de-a900-b63d267b37a0)

### Nuevos campos compuestos en el modelo de empleados.

Supongamos 





## 4 El método UpdateView



## 5 El método DeleteView



