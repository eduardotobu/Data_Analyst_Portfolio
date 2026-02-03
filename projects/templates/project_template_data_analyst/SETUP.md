# 🚀 Crear un Nuevo Proyecto

Nunca trabajar en la carpeta raíz. Crear siempre una carpeta aislada.

1. Copia la carpeta de template de proyecto de data analysis y pegala en proyectos, cambiale el nombre para que se llame como el nuevo proyecto

En Powershell

2. Cambiate al directorio de la carpeta del proyecto. Puedes copiar el path desde VS Code y ponerlo después de cd.
```powershell
cd path_de_carpeta_de_proyecto
```
3. Inicializa uv (Crea el entorno virtual)
```powershell
uv init
```

4. Instala el stack de Data Science (aquí podría ir cualquier librería)
```powershell
uv add pandas matplotlib seaborn scikit-learn jupyter notebook --native-tls
```

5. Crear un notebook dentro de la carpeta notebooks y seleccionar el .venv como nuevo kernel

6. Agregar las funciones necesarias (`utils`), constantes(`config.py`), queries o cualquier cosa que se necesite a src

7. Instalar las librerías que están dentro de `src` usando powershell
```powershell
uv pip install -e . --native-tls
```

Trabajo recurrente una vez comenzando el análisis.

8. Agregar las constantes y paths necesarios al config.py__

9. Actualizar el `README.md` explicando el proyecto



## Comandos para manejo de librerías en uv
| **Acción** | **Comando** |
| --- | --- |
| **Añadir librería** | `uv add plotly` |
| **Quitar librería** | `uv remove plotly` |
| **Ejecutar script** | `uv run script.py` |
| **Reparar entorno** | `uv sync` |
<br>

Cada que abras un nuevo proyecto, corre uv run y luego conectate al kernel.