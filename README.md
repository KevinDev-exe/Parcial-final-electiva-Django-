# Sistema de Seguimiento de Proyectos Académicos

## Descripción

Proyecto desarrollado en Django para la gestión y seguimiento de proyectos académicos.
Permite a estudiantes registrar proyectos y a docentes revisarlos, comentarlos y aprobarlos.

---

## Funcionalidades

* Autenticación de usuarios
* Roles de estudiante y docente
* CRUD de proyectos
* Gestión de comentarios
* Notificaciones por correo electrónico
* Filtros por estado y estudiante
* Exportación de reportes CSV
* Carga de documentos PDF
* Panel de administración Django

---

## Tecnologías usadas

* Python
* Django
* SQLite3
* django-crispy-forms
* Bootstrap 5

---

## Instalación

1. Crear entorno virtual:

```bash
python -m venv ambiente
```

2. Activar entorno virtual:

Windows:

```bash
ambiente\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install django
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install pillow
pip install reportlab
```

4. Ejecutar migraciones:

```bash
python manage.py migrate
```

5. Ejecutar servidor:

```bash
python manage.py runserver
```

---

## Roles del sistema

### Docente

Usuario:

```text
alejandro
```

Contraseña:

```text
Ac12345*
```

---

### Estudiante

Usuario:

```text
kevin
```

Contraseña:

```text
ky12345*
```

---

## Autor

Kevin Yamid Agreda Pianda
