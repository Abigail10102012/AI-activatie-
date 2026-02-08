import threading
import sys
import math
import random

try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
    from speech_recognition import AudioData
except ImportError as e:
    print(f"Missing library: {e.name}")
    print("\nInstall using:")
    print("pip install SpeechRecognition pyaudio numpy matplotlib")
    sys.exit(1)

stop_event = threading.Event()


def wait_for_enter():
    input()
    stop_event.set()


def record_audio(label):
    stop_event.clear()
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1024
    )

    frames = []

    print(f"\n🎙️ {label}")
    print("Press Enter to stop...")
    threading.Thread(target=wait_for_enter, daemon=True).start()
    print("Recording", end="", flush=True)

    while not stop_event.is_set():
        frames.append(stream.read(1024, exception_on_overflow=False))
        print(".", end="", flush=True)

    print("\nDone")

    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()

    return b''.join(frames), 16000, width


def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    return {
        "duration": len(samples) / rate,
        "avg_volume": np.mean(np.abs(samples)),
        "max_volume": np.max(np.abs(samples)),
        "samples": samples
    }


def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    try:
        return recognizer.recognize_google(AudioData(data, rate, width))
    except:
        return "[Could not transcribe]"


def display_stats(stats, text, label):
    print("\n" + "-" * 40)
    print(label)
    print("-" * 40)
    print(f"Duration: {stats['duration']:.2f} seconds")
    print(f"Average Volume: {stats['avg_volume']:.0f}")
    print(f"Max Volume: {stats['max_volume']:.0f}")
    print(f"Transcription: {text}")


def compare(stats1, stats2):
    print("\n" + "=" * 40)
    print("COMPARISON RESULTS")
    print("=" * 40)

    if stats1["duration"] > stats2["duration"]:
        print("Recording 1 is longer")
    else:
        print("Recording 2 is longer")

    if stats1["avg_volume"] > stats2["avg_volume"]:
        print("Recording 1 is louder")
    else:
        print("Recording 2 is louder")


def plot_both(stats1, stats2, rate):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

    t1 = np.linspace(0, stats1["duration"], len(stats1["samples"]))
    ax1.plot(t1, stats1["samples"])
    ax1.set_title("Recording 1")
    ax1.set_ylabel("Amplitude")

    t2 = np.linspace(0, stats2["duration"], len(stats2["samples"]))
    ax2.plot(t2, stats2["samples"])
    ax2.set_title("Recording 2")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Amplitude")

    plt.tight_layout()
    plt.show()


def main():
    print("=" * 40)
    print("VOICE ANALYSIS LAB")
    print("=" * 40)

    audio1, rate, width = record_audio("Recording 1: Speak normally")
    stats1 = analyze_audio(audio1, rate)
    text1 = transcribe(audio1, rate, width)
    display_stats(stats1, text1, "Recording 1 Results")

    input("\nPress Enter to record again...")

    audio2, rate, width = record_audio("Recording 2: Speak louder or faster")
    stats2 = analyze_audio(audio2, rate)
    text2 = transcribe(audio2, rate, width)
    display_stats(stats2, text2, "Recording 2 Results")

    compare(stats1, stats2)
    plot_both(stats1, stats2, rate)


if __name__ == "__main__":
    main()



