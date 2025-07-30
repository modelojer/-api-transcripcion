from fastapi import FastAPI, UploadFile, File
import speech_recognition as sr
import uvicorn

app = FastAPI()

@app.post("/transcribir/")
async def transcribir_audio(file: UploadFile = File(...)):
    recognizer = sr.Recognizer()
    with open("temp_audio.wav", "wb") as f:
        f.write(await file.read())
    with sr.AudioFile("temp_audio.wav") as source:
        audio = recognizer.record(source)
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        return {"texto": texto}
    except Exception as e:
        return {"error": str(e)}
