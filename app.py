from gtts import gTTS
import subprocess

# Texto que deseas convertir a voz
texto = """
Bienvenido a esta sesión de meditación guiada. Encuentra un lugar cómodo, cierra los ojos y comienza a centrarte en el presente. Esta es tu oportunidad para desconectar y regalarte un momento de paz interior.
"""

# Idioma de la síntesis de voz (puedes usar 'es' para español)
idioma = 'es'

# Crear el objeto gTTS
tts = gTTS(text=texto, lang=idioma, slow=False)

# Guardar el archivo de audio
nombre_archivo = "meditacion_guiada.mp3"
tts.save(nombre_archivo)

# Reproducir el archivo de audio en macOS
subprocess.run(['open', nombre_archivo])

print(f"El archivo de audio '{nombre_archivo}' ha sido generado y se está reproduciendo.")
