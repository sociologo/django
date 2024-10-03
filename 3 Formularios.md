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

Los formularios Form no están vinculados directamente a un solo modelo, lo que nos sirve cuando deseamos hacer el ingreso de un registro asociado a dos modelos distintos. Es algo que vamos a hacer sobre el proyecto que hemos venido desarrollando y que contiene los modelos **empleado** y **departamento**.

1 En la aplicacion **departamento** construiremos un nuevo forms.py en el que registraremos un departamento y un empleado asociado a el:

1.1 Construiremos el formulario forms.Form

2 En la aplicacion departamento construiremos un nuevo forms.py en el que:
2.1 hacemos la clase en la vista importando FormView, render, el formulario, la aplicacion empleado y los modelos
2.2 en la vista basada en clases sobreescribimos el metodo form_valid

3 En la aplicacion departamento construiremos la url importando views:

4 En la aplicacion departamento creamos el template:









