import whisper

def transcribe(file_name, model_name="base"):
    print(f"Loading Whisper model: {model_name}")
    model = whisper.load_model(model_name)

    print(f"Transcribing: {file_name}")
    result = model.transcribe(file_name)

    print("\n--- Transcription ---\n")
    print(result["text"])

    # optionally save to file
    with open("harvard.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])

    print("\n✅ Transcription saved to transcription.txt")
    return result["text"]

if __name__ == "__main__":
    # name of your .wav file here
    file_name = "harvard.wav"  # replace with your file name
    transcribe(file_name)
