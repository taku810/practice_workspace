# #cspell:ignore pyaudio audiodata langage sprec speechrecognizer textise
# import speech_recognition as sr
# import wave
# import time
# from datetime import datetime

# import pyaudio

# FORMAT = pyaudio.paInt16
# SAMPLE_RATE = 44100
# CHANNELS = 1
# INPUT_DEVICE_INDEX = 1
# CALL_BACK_FREQUENCY = 3

# OUTPUT_TXT_FILES = "./" + datetime.now().strftime("%Y%m_%H_%M") + ".txt" #テキストファイルの名前 = 日付

# def look_for_audio_input():
#     pa = pyaudio.PyAudio()

#     for i in range(pa.get_device_count()):
#         print(pa.get_device_info_by_index(i))
#         print()

#     pa.terminate()

# def callback(in_data,frame_count,time_info,status):

#     global sprec

#     try:
#         audiodata = sr.AudioData(in_data,SAMPLE_RATE,2)
#         sprec_text = sprec.recognize_google(audiodata,langage="ja-JP")

#         with open(OUTPUT_TXT_FILES,"a") as f:
#             f.write("\n" + sprec_text)

#     except sr.UnknownValueError:
#         pass
#     except sr.RequestError:
#         pass
#     finally:
#         return (None,pyaudio.paContinue)

# def realtime_textise():
#     with open(OUTPUT_TXT_FILES,"w") as f:
#         DATE = datetime.now().strftime("%Y%m%d_%H:%M:%S")
#         f.write(f"日時:{DATE}" + "\n")

#     global sprec

#     #speechrecognizerインスタンスを取得
#     sprec = sr.Recognizer()

#     #audioインスタンス取得
#     audio = pyaudio.PyAudio()

#     #ストリームオブジェクトを作成
#     stream = audio.open(format = FORMAT,
#                         rate = SAMPLE_RATE,
#                         channels = CHANNELS,
#                         input_device_index = INPUT_DEVICE_INDEX,
#                         input = True,
#                         frames_per_buffer = SAMPLE_RATE*CALL_BACK_FREQUENCY,
#                         stream_callback = callback)
    
#     stream.start_stream()

#     while stream.is_active():
#         time.sleep(0.1)

#     stream.stop_stream()
#     stream.close()
#     audio.terminate()


# def main():
#     look_for_audio_input()
#     realtime_textise()


# if __name__ == "__main__":
#     main()


#cspell:ignore pyaudio audiodata langage sprec speechrecognizer textise
import speech_recognition as sr
import wave
import time
from datetime import datetime

import pyaudio

FORMAT = pyaudio.paInt16
SAMPLE_RATE = 44100
CHANNELS = 1
INPUT_DEVICE_INDEX =  1 # 適切なインデックスに変更してください
CALL_BACK_FREQUENCY = 3

OUTPUT_TXT_FILES = "./" + datetime.now().strftime("%Y%m_%H_%M") + ".txt" #テキストファイルの名前 = 日付

def look_for_audio_input():
    pa = pyaudio.PyAudio()

    for i in range(pa.get_device_count()):
        print(pa.get_device_info_by_index(i))
        print()

    pa.terminate()

def callback(in_data, frame_count, time_info, status):
    global sprec

    try:
        audiodata = sr.AudioData(in_data, SAMPLE_RATE, 2)
        sprec_text = sprec.recognize_google(audiodata, language="ja-JP")

        with open(OUTPUT_TXT_FILES, "a") as f:
            f.write("\n" + sprec_text)

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    finally:
        return (None, pyaudio.paContinue)

def realtime_textise():
    with open(OUTPUT_TXT_FILES, "w") as f:
        DATE = datetime.now().strftime("%Y%m%d_%H:%M:%S")
        f.write(f"日時:{DATE}" + "\n")

    global sprec

    # speechrecognizerインスタンスを取得
    sprec = sr.Recognizer()

    # audioインスタンス取得
    audio = pyaudio.PyAudio()

    # ストリームオブジェクトを作成
    stream = audio.open(format=FORMAT,
                        rate=SAMPLE_RATE,
                        channels=CHANNELS,
                        input_device_index=INPUT_DEVICE_INDEX,
                        input=True,
                        frames_per_buffer=SAMPLE_RATE * CALL_BACK_FREQUENCY,
                        stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    audio.terminate()

def main():
    look_for_audio_input()
    realtime_textise()

if __name__ == "__main__":
    main()