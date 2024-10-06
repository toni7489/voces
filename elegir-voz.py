import pyttsx3

# Inicializar el motor
engine = pyttsx3.init()

# Obtener y listar todas las voces disponibles
voces = engine.getProperty('voices')

# Mostrar las voces disponibles
for idx, voz in enumerate(voces):
    print(f"Voz {idx}: {voz.name}, idioma: {voz.languages}")

# Seleccionar una voz específica (puedes cambiar el índice para elegir otra voz)
engine.setProperty('voice', voces[31].id)  # Cambia el índice para probar otras voces

# Configurar la velocidad de la voz (opcional)
engine.setProperty('rate', 150)

# Texto que deseas convertir a voz
texto = """
Bienvenido a esta sesión de meditación guiada. Encuentra un lugar cómodo, cierra los ojos y comienza a centrarte en el presente.
"""

# Convertir texto a voz
engine.say(texto)

# Ejecutar el motor de síntesis
engine.runAndWait()
