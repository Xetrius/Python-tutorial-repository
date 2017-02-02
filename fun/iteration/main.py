from time import  sleep
import espeak
es = espeak.ESpeak()
var1 = 0
mess1 = "this is a test."
while True:
    var1 = (var1 + 1)
    var2 = "iteration " + str(var1)
    es.say(var2)
    sleep(0.5)
    es.say(mess1)
    sleep(0.5)
