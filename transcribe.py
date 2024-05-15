import whisper

model = whisper.load_model("base")


def transcribe(data):
    id = data[1]
    text_file_path = "/media/naveen/253eda55-9f25-43e1-a970-07c1269e1cbe/Projects/temp/Ozonetel/Task1/uploads/"+ id + ".txt"
    audio_path = data[0]
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    #result= ""+data[0]+" "+data[1]
    with open(text_file_path, "w") as text_file:
        text_file.write(result.text)
    return {
        "success": True,
        "job_id": id,
        "transcription": result.text
    }