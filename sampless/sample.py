# import subprocess

# subprocess.run([
#     "ffmpeg", "-i", "audios/8_Inline & Block Elements in HTML.mp3",
#     "-t", "10",
#     "audios/sample10s.mp3"
# ])

import whisper
import json

model = whisper.load_model("large-v2")
result = model.transcribe(
    audio="audios/sample10s.mp3",
    language="hi",
    task="translate",
    word_timestamps=False
)

# # Save as JSON
# with open("transcription.json", "w", encoding="utf-8") as f:
#     json.dump(result, f, ensure_ascii=False, indent=4)

# print("Saved to transcription.json")
chunks=[]
for segment in result["segments"]:
    chunks.append({"start":segment["start"],
                   "end": segment["end"],
                   "text":segment["text"]})
    
print(chunks)
with open("output.json","w") as f:
    json.dump(chunks,f)