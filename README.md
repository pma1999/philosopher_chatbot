# Philosopher Chatbot

Philosopher Chatbot es una aplicaci�n interactiva de l�nea de comandos que permite a los usuarios conversar con simulaciones de famosos fil�sofos hist�ricos en m�ltiples idiomas (espa�ol, ingl�s y catal�n). La aplicaci�n utiliza la API de Anthropic para generar respuestas basadas en el estilo y las ideas filos�ficas de cada pensador en el idioma seleccionado por el usuario.

## Caracter�sticas

- Interfaz de l�nea de comandos interactiva
- Selecci�n de fil�sofos hist�ricos
- Conversaci�n din�mica utilizando la API de Anthropic (Claude-3-Opus)
- Respuestas personalizadas basadas en el estilo y las ideas de cada fil�sofo
- Soporte multiling�e (espa�ol, ingl�s y catal�n)
- Manejo de errores y codificaci�n UTF-8 para compatibilidad con caracteres especiales

## Requisitos

- Python 3.6+
- Bibliotecas de Python (ver `requirements.txt`)
- Clave de API de Anthropic

## Instalaci�n

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

1. Ejecute la aplicaci�n:
   ```
   python app.py
   ```

2. Seleccione el idioma deseado (espa�ol, ingl�s o catal�n) cuando se le solicite.

3. Elija un fil�sofo de la lista proporcionada ingresando el n�mero correspondiente.

4. Inicie una conversaci�n con el fil�sofo seleccionado. Puede hacer preguntas o discutir ideas relacionadas con su filosof�a.

5. Para finalizar la conversaci�n, escriba 'exit' (o 'salir' en espa�ol, 'sortir' en catal�n).

## Estructura del Proyecto

- `app.py`: Contiene la l�gica principal de la aplicaci�n, incluyendo la interfaz de usuario y la integraci�n con la API de Anthropic.
- `config.py`: Almacena la configuraci�n de la aplicaci�n, incluyendo la clave de API de Anthropic.
- `philosophers.py`: Define la lista de fil�sofos disponibles con sus nombres, per�odos y principales ideas en m�ltiples idiomas.
- `translations.py`: Contiene las traducciones de los mensajes y prompts del sistema en m�ltiples idiomas.
- `requirements.txt`: Lista las dependencias del proyecto.

## Personalizaci�n

Para a�adir nuevos fil�sofos o modificar los existentes, edite el archivo `philosophers.py`. Cada fil�sofo est� representado por un diccionario con las siguientes claves para cada idioma soportado:

- `name`: Nombre del fil�sofo
- `period`: Per�odo hist�rico al que pertenece
- `main_ideas`: Lista de las principales ideas o conceptos asociados al fil�sofo

Para a�adir soporte para un nuevo idioma:
1. Actualice el archivo `philosophers.py` para incluir la informaci�n en el nuevo idioma.
2. A�ada las traducciones correspondientes en el archivo `translations.py`.
3. Modifique la funci�n `select_language()` en `app.py` para incluir el nuevo idioma como opci�n.

## Manejo de Errores

La aplicaci�n incluye manejo de errores para:
- Entradas de usuario inv�lidas
- Errores de la API de Anthropic
- Problemas de codificaci�n de caracteres

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de enviar un pull request.

## Licencia

[MIT License](https://opensource.org/licenses/MIT)

## Contacto

Para preguntas o soporte, por favor abra un issue en el repositorio de GitHub.