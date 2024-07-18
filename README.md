# Philosopher Chatbot

<<<<<<< HEAD
Philosopher Chatbot es una aplicaci髇 interactiva de l韓ea de comandos que permite a los usuarios conversar con simulaciones de famosos fil髎ofos hist髍icos en m鷏tiples idiomas (espa駉l, ingl閟 y catal醤). La aplicaci髇 utiliza la API de Anthropic para generar respuestas basadas en el estilo y las ideas filos骹icas de cada pensador en el idioma seleccionado por el usuario.
=======
Philosopher Chatbot es una aplicaci贸n interactiva de l铆nea de comandos que permite a los usuarios conversar con simulaciones de famosos fil贸sofos hist贸ricos. La aplicaci贸n utiliza la API de Anthropic para generar respuestas basadas en el estilo y las ideas filos贸ficas de cada pensador.
>>>>>>> ba863acaabbe6b1f98ce3c8cb30df8821cb692e0

## Caracter铆sticas

<<<<<<< HEAD
- Interfaz de l韓ea de comandos interactiva
- Selecci髇 de fil髎ofos hist髍icos
- Conversaci髇 din醡ica utilizando la API de Anthropic (Claude-3-Opus)
- Respuestas personalizadas basadas en el estilo y las ideas de cada fil髎ofo
- Soporte multiling黣 (espa駉l, ingl閟 y catal醤)
- Manejo de errores y codificaci髇 UTF-8 para compatibilidad con caracteres especiales
=======
- Interfaz de l铆nea de comandos interactiva
- Selecci贸n de fil贸sofos hist贸ricos
- Conversaci贸n din谩mica utilizando la API de Anthropic (Claude-3.5-Sonnet)
- Respuestas personalizadas basadas en el estilo y las ideas de cada fil贸sofo
- Manejo de errores y codificaci贸n UTF-8 para compatibilidad con caracteres especiales
>>>>>>> ba863acaabbe6b1f98ce3c8cb30df8821cb692e0

## Requisitos

- Python 3.6+
- Bibliotecas de Python (ver `requirements.txt`)
- Clave de API de Anthropic

## Instalaci贸n

1. Clone el repositorio:
   ```
   git clone https://github.com/pma1999/philosopher_chatbot.git
   cd philosopher-chatbot
   ```

2. Instale las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Configure su clave de API de Anthropic:
   - Abra el archivo `config.py`
   - Reemplace `'your_api_key_here'` con su clave de API real de Anthropic

## Uso

1. Ejecute la aplicaci贸n:
   ```
   python app.py
   ```

<<<<<<< HEAD
2. Seleccione el idioma deseado (espa駉l, ingl閟 o catal醤) cuando se le solicite.

3. Elija un fil髎ofo de la lista proporcionada ingresando el n鷐ero correspondiente.

4. Inicie una conversaci髇 con el fil髎ofo seleccionado. Puede hacer preguntas o discutir ideas relacionadas con su filosof韆.

5. Para finalizar la conversaci髇, escriba 'exit' (o 'salir' en espa駉l, 'sortir' en catal醤).

## Estructura del Proyecto

- `app.py`: Contiene la l骻ica principal de la aplicaci髇, incluyendo la interfaz de usuario y la integraci髇 con la API de Anthropic.
- `config.py`: Almacena la configuraci髇 de la aplicaci髇, incluyendo la clave de API de Anthropic.
- `philosophers.py`: Define la lista de fil髎ofos disponibles con sus nombres, per韔dos y principales ideas en m鷏tiples idiomas.
- `translations.py`: Contiene las traducciones de los mensajes y prompts del sistema en m鷏tiples idiomas.
=======
2. Seleccione un fil贸sofo de la lista proporcionada ingresando el n煤mero correspondiente.

3. Inicie una conversaci贸n con el fil贸sofo seleccionado. Puede hacer preguntas o discutir ideas relacionadas con su filosof铆a.

4. Para finalizar la conversaci贸n, escriba 'exit'.

## Estructura del Proyecto

- `app.py`: Contiene la l贸gica principal de la aplicaci贸n, incluyendo la interfaz de usuario y la integraci贸n con la API de Anthropic.
- `config.py`: Almacena la configuraci贸n de la aplicaci贸n, incluyendo la clave de API de Anthropic.
- `philosophers.py`: Define la lista de fil贸sofos disponibles con sus nombres, per铆odos y principales ideas.
>>>>>>> ba863acaabbe6b1f98ce3c8cb30df8821cb692e0
- `requirements.txt`: Lista las dependencias del proyecto.

## Personalizaci贸n

<<<<<<< HEAD
Para a馻dir nuevos fil髎ofos o modificar los existentes, edite el archivo `philosophers.py`. Cada fil髎ofo est� representado por un diccionario con las siguientes claves para cada idioma soportado:
=======
Para a帽adir nuevos fil贸sofos o modificar los existentes, edite el archivo `philosophers.py`. Cada fil贸sofo est谩 representado por un diccionario con las siguientes claves:
>>>>>>> ba863acaabbe6b1f98ce3c8cb30df8821cb692e0

- `name`: Nombre del fil贸sofo
- `period`: Per铆odo hist贸rico al que pertenece
- `main_ideas`: Lista de las principales ideas o conceptos asociados al fil贸sofo

Para a馻dir soporte para un nuevo idioma:
1. Actualice el archivo `philosophers.py` para incluir la informaci髇 en el nuevo idioma.
2. A馻da las traducciones correspondientes en el archivo `translations.py`.
3. Modifique la funci髇 `select_language()` en `app.py` para incluir el nuevo idioma como opci髇.

## Manejo de Errores

La aplicaci贸n incluye manejo de errores para:
- Entradas de usuario inv谩lidas
- Errores de la API de Anthropic
- Problemas de codificaci贸n de caracteres

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de enviar un pull request.

## Licencia

[MIT License](https://opensource.org/licenses/MIT)

## Contacto

Para preguntas o soporte, por favor abra un issue en el repositorio de GitHub.
