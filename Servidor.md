Cómo configurar Django con Postgres, Nginx y Gunicorn en Ubuntu.

Acerca de root
```
root@django:~# 
```
El usuario root es el usuario administrativo en un entorno Linux con privilegios elevados. Debido a ello, se desaconseja su uso habitual. La cuenta root puede realizar cambios muy destructivos, incluso por accidente. Debes configurar una nueva cuenta de usuario con privilegios reducidos para el uso diario. 

Crear un nuevo usuario

Una vez que inicie sesión como root , podrá agregar la nueva cuenta de usuario. En el futuro, iniciaremos sesión con esta nueva cuenta en lugar de root .

Este ejemplo crea un nuevo usuario llamado christian:
```
adduser christian
contraseña: 123456
```

https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu


1 Creamos un entorno virtual:
![image](https://github.com/user-attachments/assets/b954f28f-e764-4a6d-803d-16aa65f27df6)

2 Me aparece un error:
![image](https://github.com/user-attachments/assets/f308020c-d45f-4ae1-b6aa-00e37fedb72e)



