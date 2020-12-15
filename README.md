
# BiblioNLU

Procesador de Lenguaje Natural para el proyecto [BiblioBot](https://github.com/luis-tapiaa/biblio-bot).

## Getting Started

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local.

### Pre-requisitos

Para poder utilizar BiblioNLU se necesita contar con lo siguiente:

- Python v3.7
- Pip en su ultma version

### Instalación

Para instalar BiblioNLU debe clonar el repositorio de GitHub.

```git clone https://github.com/luis-tapiaa/biblio-bot-nlu.git```

O puede simplemente descargar el codigo fuente.

Despues debe crear un entorno virtual de Python donde descargo el proyecto.

```python3 -m venv ./venv```

Luego debemos activar el entorno virtual cada que queramos utilizar el servicio.

``.\venv\Scripts\activate``

Despues se instala Rasa el cual contiene las dependencias para el proyecto.

``pip install rasa``

## Running

Antes de iniciar el servicio debemos entrenar el modelo de lenguaje natural:

``rasa train nlu``

Esto nos va a entregar un modelo en la carpeta `models/`.

### Probando el modelo

Para probar que el modelo fucniona correctamente usaremos el siguiente comando:

``rasa shell nlu``

Esto iniciara el nlu para que puedas enviar oraciones.

Si quieres probar un modelo en especifico debes utilizar:

``rasa shell -m models/<nombre_modelo>``

### Iniciar el servidor NLU
Para iniciar el servicio con el modelo NLU que obtivimos debemos ejecutar:

``rasa run --enable-api -m models/<nombre_modelo>``

El servidor estara disponible en [localhost:5005/model/parse](localhost:5005/model/parse), puedes hacer solo `POST`

## Herramentas de desarrollo

Este proyecto fue desarrollado utilizando:
* [Rasa](https://rasa.com/) - Marco de aprendizaje automático para automatizar asistentes.
