# Philosopher Chatbot

Philosopher Chatbot es una aplicación interactiva de línea de comandos que permite a los usuarios conversar con simulaciones de famosos filósofos históricos en múltiples idiomas (español, inglés y catalán). La aplicación utiliza la API de Anthropic para generar respuestas basadas en el estilo y las ideas filosóficas de cada pensador en el idioma seleccionado por el usuario.

## Características

- Interfaz de línea de comandos interactiva
- Selección de filósofos históricos
- Conversación dinámica utilizando la API de Anthropic (Claude-3-Opus)
- Respuestas personalizadas basadas en el estilo y las ideas de cada fil�sofo
- Soporte multilingüe (español, inglés y catalán)
- Manejo de errores y codificación UTF-8 para compatibilidad con caracteres especiales

## Requisitos

- Python 3.6+
- Bibliotecas de Python (ver `requirements.txt`)
- Clave de API de Anthropic

## Instalación

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

1. Ejecute la aplicación:
   ```
   python app.py
   ```

2. Seleccione el idioma deseado (español, inglés o catalán) cuando se le solicite.

3. Elija un filósofo de la lista proporcionada ingresando el número correspondiente.

4. Inicie una conversación con el filósofo seleccionado. Puede hacer preguntas o discutir ideas relacionadas con su filosofía.

5. Para finalizar la conversación, escriba 'exit' (o 'salir' en español, 'sortir' en catalán).

## Estructura del Proyecto

- `app.py`: Contiene la lógica principal de la aplicación, incluyendo la interfaz de usuario y la integración con la API de Anthropic.
- `config.py`: Almacena la configuración de la aplicación, incluyendo la clave de API de Anthropic.
- `philosophers.py`: Define la lista de filósofos disponibles con sus nombres, períodos y principales ideas en múltiples idiomas.
- `translations.py`: Contiene las traducciones de los mensajes y prompts del sistema en múltiples idiomas.
- `requirements.txt`: Lista las dependencias del proyecto.

## Personalización

Para añadir nuevos filósofos o modificar los existentes, edite el archivo `philosophers.py`. Cada filósofo está representado por un diccionario con las siguientes claves para cada idioma soportado:

- `name`: Nombre del filósofo
- `period`: Período histórico al que pertenece
- `main_ideas`: Lista de las principales ideas o conceptos asociados al filósofo

Para añadir soporte para un nuevo idioma:
1. Actualice el archivo `philosophers.py` para incluir la información en el nuevo idioma.
2. Añada las traducciones correspondientes en el archivo `translations.py`.
3. Modifique la función `select_language()` en `app.py` para incluir el nuevo idioma como opción.

## Manejo de Errores

La aplicación incluye manejo de errores para:
- Entradas de usuario inválidas
- Errores de la API de Anthropic
- Problemas de codificación de caracteres

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de enviar un pull request.

## Licencia

[MIT License](https://opensource.org/licenses/MIT)

## Contacto

Para preguntas o soporte, por favor abra un issue en el repositorio de GitHub.
