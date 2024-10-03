# Formularios

[Working with forms](https://docs.djangoproject.com/en/5.1/topics/forms/)

## Índice

* [El archivo forms.py](#1-El-archivo-forms.py)
  * [1 Formularios forms.ModelForm](#1-Formularios-formsModelForm)
  * [2 Formularios forms.Form](#2-Formularios-formsForm)
    
## El archivo forms.py

### 1 Formularios formsModelForm

Los formularios ModelForm están vinculados directamente a un modelo.

1 Trabajemos en forma experimental dentro de nuestra aplicación **exp**. En ella, construyamos el siguiente modelo:
![image](https://github.com/user-attachments/assets/2e9fc619-686b-4022-bb51-879a9b9c0184)

2 Le asociamos una vista **CreateView** y **SuccessView**:
![image](https://github.com/user-attachments/assets/e0d6a6fd-cae8-4674-a1dd-34f331aca7d5)

3 Construimos las urls que activen las vistas:
![image](https://github.com/user-attachments/assets/d1810929-1867-442f-8798-730cdc95cb93)
![image](https://github.com/user-attachments/assets/b36a2e8b-36d7-4628-8369-7c914491cbb7)

4 Construímos los htmls asociados:
![image](https://github.com/user-attachments/assets/491f46cb-a2db-4bc5-9977-eeb8aa5b8dcc)
![image](https://github.com/user-attachments/assets/05cd132a-e58e-4a81-8252-fa7234aae89a)

5 Levantemos el servidor y vayamos a la vista:
![image](https://github.com/user-attachments/assets/bb2df9bd-4dd2-4599-aa06-907021f33076)

6 Agregamos un archivo forms.py
![image](https://github.com/user-attachments/assets/631a515d-e257-485c-82cc-297bb1f5cf53)

Dentro del archivo **forms.py** escribiremos la personalización para los campos de nuestos modelos que se visualizarán en los **htmls**. El código dentro de éste archivo es lo que en Django llamaremos formularios. Para ello:
En él conectamos el modelo con el formulario y la vista.

7 Modificamos nuestra vista importando el formulario:
![image](https://github.com/user-attachments/assets/ef700024-45c2-423b-836d-0f6419d584b5)

8 Validaciones

Supongamos que deseamos que nuestra cantidad sea igual o superior a 10:

Modificamos la clase PruebaForm y ejecutamos la aplicación:
![image](https://github.com/user-attachments/assets/eaf054ff-d8ae-48a7-a55a-cb05c5cb0320)
![image](https://github.com/user-attachments/assets/03bb6857-4e0a-4463-ae97-6a16b155a602)

9 Personalizaciones de los campos.
![image](https://github.com/user-attachments/assets/3ebc5d75-bd44-4782-82ae-eae09c5a0450)

### 2 Formularios Form

Los formularios Form no están vinculados directamente a un solo modelo, por lo que nos sirven cuando deseamos ingresar registros asociados a modelos distintos. Lo vamos a hacer sobre el proyecto que hemos venido desarrollando y que contiene los modelos **empleado** y **departamento**.

1 En la aplicación **departamento** construiremos un nuevo forms.py en el que registraremos campos de un departamento y un empleado asociado a él:
![image](https://github.com/user-attachments/assets/6a881efe-9557-45e6-b2cd-5eee8b64bd78)

2 En la aplicación **departamento** construiremos la vista NewDepartmentView en el que registraremos campos de un departamento y un empleado asociado a él:

Primero, el código importa varias herramientas y componentes necesarios para trabajar con Django, incluyendo funciones para renderizar plantillas, manejar URLs, y vistas genéricas que facilitan la creación de formularios y plantillas.

Luego, se define una vista llamada SuccessView que simplemente muestra una página de éxito cuando se accede a ella. Esta página se utiliza para informar al usuario que una operación se ha completado correctamente.

La parte principal del código es una vista llamada NewDepartmentView. Esta vista se encarga de mostrar un formulario al usuario para que pueda crear un nuevo departamento. Cuando el usuario envía el formulario, la vista verifica que los datos sean válidos.

Si los datos son válidos, la vista crea un nuevo departamento utilizando la información proporcionada por el usuario. Además, también crea un nuevo empleado asociado a este departamento, utilizando otros datos del formulario. Una vez que ambos registros se han guardado correctamente en la base de datos, el usuario es redirigido a una página de éxito.

En resumen, este código maneja la creación de un nuevo departamento y un empleado asociado, asegurándose de que ambos se guarden correctamente en la base de datos y proporcionando retroalimentación al usuario sobre el éxito de la operación.

![image](https://github.com/user-attachments/assets/ccc97b4f-ae20-4e5a-a1a8-e44b39c4dfdb)

3 Construímos las URLS para activar las vistas.
![image](https://github.com/user-attachments/assets/d9628226-345e-40d6-894b-43305563e431)
![image](https://github.com/user-attachments/assets/d8cbc229-9544-45a8-943a-53162980ec38)

4 Creamos los htmls asociados a las vistas:
![image](https://github.com/user-attachments/assets/b505c12d-6305-47b1-8965-da79b552bd15)
![image](https://github.com/user-attachments/assets/4cbcdcd3-e31b-42e6-bf52-2def56165ad5)

5 Ingresamos un nuevo registro y verificamos:
![image](https://github.com/user-attachments/assets/51177aae-b6f2-42f8-8f37-5e921b7333c4)
![image](https://github.com/user-attachments/assets/9b3de7a6-dc54-4b63-a78f-d5ffeda6a009)
![image](https://github.com/user-attachments/assets/3b296643-d1d4-40fb-9b08-52ec787d6b50)
