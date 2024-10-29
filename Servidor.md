# Cómo configurar Django con Postgres, Nginx y Gunicorn en Ubuntu.

## 1 Acerca de root
```
root@django:~# 
```
El usuario root es el usuario administrativo en un entorno Linux con privilegios elevados. Debido a ello, se desaconseja su uso habitual. La cuenta root puede realizar cambios muy destructivos, incluso por accidente. Debes configurar una nueva cuenta de usuario con privilegios reducidos para el uso diario. 

## 2 Crear un nuevo usuario

Una vez que inicie sesión como root , podrá agregar la nueva cuenta de usuario. En el futuro, iniciaremos sesión con esta nueva cuenta en lugar de root .

Este ejemplo crea un nuevo usuario llamado christian:
```
adduser christian
contraseña: 123456
```

# 3 Concesión de privilegios administrativos

Ahora tienes una nueva cuenta de usuario con privilegios de cuenta normales. Sin embargo, a veces tendrás que realizar tareas administrativas como usuario root .

Para evitar cerrar la sesión de su usuario habitual y volver a iniciarla como cuenta raíz , puede configurar lo que se conoce como privilegios de superusuario o raíz para la cuenta habitual de su usuario. Estos privilegios le permitirán a su usuario normal ejecutar comandos con privilegios administrativos colocando la palabra **sudo** antes del comando.

Para agregar estos privilegios a su nuevo usuario, deberá agregarlo al grupo del sistema sudo. De manera predeterminada, en Ubuntu, los usuarios que son miembros del grupo sudo pueden usar el comando **sudo**.

Como root, ejecute este comando para agregar su nuevo usuario al grupo sudo:
```
usermod -aG sudo christian
```
Ahora puedes escribir sudoantes los comandos para ejecutarlos con privilegios de superusuario cuando inicias sesión como tu usuario habitual.




https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu


1 Creamos un entorno virtual:
![image](https://github.com/user-attachments/assets/b954f28f-e764-4a6d-803d-16aa65f27df6)

2 Me aparece un error:
![image](https://github.com/user-attachments/assets/f308020c-d45f-4ae1-b6aa-00e37fedb72e)



