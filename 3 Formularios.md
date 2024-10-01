# Formularios

[Working with forms](https://docs.djangoproject.com/en/5.1/topics/forms/)

## Índice

* [1 El archivo forms.py](#1-El-archivo-forms.py)
  * [a) Listar todos los empleados](#a-Listar-todos-los-empleados)

## 1 El archivo forms.py

1 Trabajemos en forma experimental dentro de nuestra aplicación **exp**. En ella, construyamos el siguiente modelo:
![image](https://github.com/user-attachments/assets/2e9fc619-686b-4022-bb51-879a9b9c0184)

2 Le asociamos una vista **CreateView** y **SuccessView**:
![image](https://github.com/user-attachments/assets/e0d6a6fd-cae8-4674-a1dd-34f331aca7d5)

3 Construimos las urls que activen las vistas:
![image](https://github.com/user-attachments/assets/d1810929-1867-442f-8798-730cdc95cb93)

4 Construímos los htmls asociados:




Dentro del archivo **forms.py** escribiremos la personalización para los campos de nuestos modelos que se visualizarán en los **htmls**. El código dentro de éste archivo es lo que en Django llamaremos formularios. Para ello:

1 Definamos la estructura básica completa para un modelo.

2 Comencemos a trabajar dentro de un archivo **forms.py**.

Conectamos el modelo con el formulario y la vista.

3 validaciones.

4 Personalizaciones de los campos.

Para hacer ésto utilizamos widgets.

Los formularios simples(FormView) no dependen de un modelo y nos permiten hacer registros vinculados a dos tablas.

### a) Listar todos los emp
