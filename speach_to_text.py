import whisper
model = whisper.load_model("large-v2")
result = model.transcribe(audio="audios/8_Inline & Block Elements in HTML.mp3",
                          language="hi",
                          task="translate")
print(result["text"])