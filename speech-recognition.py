#Mengambahkan Framework yang digunakan untuk speech recognition
import speech_recognition as sr
import pyttsx3

#Program di bawah untuk membuat setelah tiga detik kita tidak bicara maka kalimat akan di rekam. default 0.8 sekon
#engine.puse_treshold = 3

with mic as source:
    print("silahkan mulai bicara")
    rekaman = engine.listen(source)
    print("waktu habis")
    
    try:
        hasil = engine.recognize_google(rekaman, language = "id-ID")
        print(hasil)
    #except engine.UnknownValueError:
        #print("Maaf tidak dapat dideteksi, Silahkan Coba Lagi")
    except Exception as e:
        print(e)
