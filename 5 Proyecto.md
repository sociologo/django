Construyendo el proyecto

<br>
<br>
<br>
<br>

28 febrero.
comenzando la 72

<br>
<br>
<br>
<br>
---
---



Apariencia de nuestro prototipo.

1 Creamos un header.html dentro de la carpeta includes. En el, pegamos el codigo de Top Bar copiado desde Foundation.

![image](https://github.com/user-attachments/assets/224a338a-6e5e-43fc-aaab-9254ce8a7bae)
![image](https://github.com/user-attachments/assets/a594f417-46eb-46fc-9f17-fb17d4369640)

2 Incluimos el header dentro de nuestro inicio.html.

![image](https://github.com/user-attachments/assets/089bca2f-9429-499c-825c-f92429c016d6)

3 Enrutamos correctamente los archivos dinamicos en base.html.

![image](https://github.com/user-attachments/assets/64583535-d13e-4a19-84e5-37a3cfbaa9b4)

4 Adaptamos las etiquetas del Top Bar de Fundation en header.html a nuestros requerimientos.

![image](https://github.com/user-attachments/assets/ced51fab-a32f-4aa6-b884-8491d76a0687)

5 Agregamos imagenes de portada con Orbit de Foundation pegandolo dentro de nuestro inicio.html y adaptandolo a nuestros requerimientos. 

![image](https://github.com/user-attachments/assets/4a69616b-df36-4e7f-a40e-570e76a410a8)
![image](https://github.com/user-attachments/assets/334bc422-7c4c-415a-a3fe-550fb1086ac5)
![image](https://github.com/user-attachments/assets/8b1b3f8c-713e-40e0-bd9b-d9ae768c6c55)

6 Agregamos otro **bloque** de Fundation centrado con una caja Callout de Fundation.
![image](https://github.com/user-attachments/assets/869b897b-efe2-4511-be66-da8a0f64b540)
![image](https://github.com/user-attachments/assets/bb738792-6471-4551-82c9-00d621a5fb23)
![image](https://github.com/user-attachments/assets/012babb1-1232-474f-9db0-298ea9ca115d)

7 Le damos funcionalidad al listar del inicio utilizando nuestra vista ListAllEmpleados accediendo a la url por su nombre.

Consideremos la vista **ListAllEmpleados**. Accedamos a su url por su nombre **empleados-all** y diseñemos **list_all.html** copiando un button y una tabla de foundation.

![image](https://github.com/user-attachments/assets/09ca4d27-8823-4216-aafc-264b97bf521b)
![image](https://github.com/user-attachments/assets/b14f1c08-acd9-484b-b719-c2901a99063c)
![image](https://github.com/user-attachments/assets/b93f1154-12dc-482f-a21c-fefbd82273de)
![image](https://github.com/user-attachments/assets/eca40001-77cd-4bf7-8663-c2297565e635)

8 Accedamos a listar:

![image](https://github.com/user-attachments/assets/0c9c0e61-b046-4882-b64f-c8b492666544)

***
***
## 1 Dándole funcionalidad al botón **Buscar**.

En el archivo **views.py** de la aplicacion **persona** identifiquemos la vista basada en clases **ListEmpeladosByKword**. De ella, copiamos la funcion **get_queryset** y la pegamos en la clase **ListAllEmpleados**, en la que estamos trabajando actualmente. Como estamos sobreescribiendo el metodo **get_queryset**, ya no es necesario el parametro model = Empleado. Filtramos el full_name utilizando en atributo de Django **icontains** en base a palabra_clave.
![image](https://github.com/user-attachments/assets/f64a9c2d-79b7-4e71-a315-fa81174c0bcd)

En el list_all.html asociado debemos agregar los parametros **id** y **name** al **input**, debemos encerrar el codigo en un formulario, especificar el metodo GET, agregar el token y establecer el button type como tipo **submit**.
![image](https://github.com/user-attachments/assets/d055d064-502a-454c-8449-79cbfe0507f4)

## 2 Dándole funcionalidad al botón **Ver** el detale del empleado.

Identifiquemos la vista basada en clases **EmpleadoDetailView** y le asignamos a su url el nombre **empleado_detail**
![image](https://github.com/user-attachments/assets/78da1654-07c3-4f35-be62-1a08d9bd48c9)

En el boton de **list_all.html** asociado al **Ver** vinculamos la url **empleado_detail** asociandole el identificador de un empleado en especifico (e.id).
![image](https://github.com/user-attachments/assets/8f4df555-a90b-4f08-8774-2d1405851b84)
***

## 3 Dandole paginacion a la vista

buscamos en la pagina de foundation un codigo para la paginacion
https://get.foundation/sites/docs/pagination.html
![image](https://github.com/user-attachments/assets/43306d89-0641-410c-955b-9c1717c42e22)

pegamos en el siguiente sitio el codigo
![image](https://github.com/user-attachments/assets/00113110-6495-4db5-aa60-40e1553d2269)

Debemos darle paginacion a nuestra vista
![image](https://github.com/user-attachments/assets/c3c51605-86dd-4042-9cbc-10513f70ad47)

Agregamos un condicional para la existencia de la paginacion, agregamos condicionales para determinar la existencia de los objetos de paginacion previos y posteriores, 
construimos un for para desplegar toda la cantidad de paginaciones y le asignamos un color para la paginacion actual.

![image](https://github.com/user-attachments/assets/7349f529-f130-492e-a70d-2ff147f8c6b8)

![image](https://github.com/user-attachments/assets/665129b9-3a02-443f-a55a-e44bbefc9fff)

***
## Construyendo la pagina de listado de departamentos con la funcionalidad de ver todos los empleados por departamento.

1 Construimos dentro del archivo **views.py** de nuestra aplicacion **departamentos** la vista basada en clases **DepartamentoView**, importando **ListView**. Cramos la vista con sus hmtl y rutas de activacion asociados.
![image](https://github.com/user-attachments/assets/26fae047-ff22-4d9f-97d5-14b59cbeb6ac)
![image](https://github.com/user-attachments/assets/77812958-e710-403c-8926-2a09e3a8889a)
![image](https://github.com/user-attachments/assets/39432ac5-f2b6-4690-a3c5-83f44535b4a3)

2 hacemos el vinculo de la cabecera dirigirse a la url de departamentos, donde seran listados. Por lo que modificamos header.html de la siguiente manera:
![image](https://github.com/user-attachments/assets/ca633886-2587-4685-8745-233a6a2809aa)

Recordemos asignarle un nombre al conjunto de urls de departamentos y hagamos editable el campo name del modelo Departamento:
![image](https://github.com/user-attachments/assets/b090f652-85cb-4954-9e15-9505f2b2b39c)
![image](https://github.com/user-attachments/assets/e8bae8e4-6cbb-4eeb-bb3f-c5d42d8ec8e3)

3 Hacemos la funcionalidad del boton Ver utilizando la vista basada en clase **ListByDept** del archivo views.py de la aplicacion empleados. A la url que activa esta vista le ponemos el nombre **empleados_by_dept** y la direccionamos apropiadamente en nuestra listbydept.html
![image](https://github.com/user-attachments/assets/a40b7c2c-c654-4cab-ae64-5cc12cb15769)
![image](https://github.com/user-attachments/assets/1dbd2420-8d60-4fb2-9c70-e134b980f390)
![image](https://github.com/user-attachments/assets/4754ee9d-3dd1-4a53-a810-0ad9f7bc8cff)

4 Veamos los resultados

![image](https://github.com/user-attachments/assets/a8264b03-a15c-4af2-89a3-c27aa0dbf9b0)
![image](https://github.com/user-attachments/assets/b71f0529-d9bf-4dff-bd33-1bae0771002f)





































