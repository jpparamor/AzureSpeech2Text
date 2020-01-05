import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = "9f1ddc34f50c4ab2b3383b66bfd06254", "uksouth"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language="en-GB")

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

counter = 0
output = ""

def recognized(args):
    global output
    global counter
    resultString = args.result.text
    print(resultString.lower())
    if resultString.lower() == "danger will robinson.":
        speech_recognizer.stop_continuous_recognition()
        counter = 1000000000
        print("Okay I'll stop listening then.\n")
    else:
        output = output + ' ' + resultString

print("Say as much as you like...")
speech_recognizer.recognized.connect(recognized)
speech_recognizer.start_continuous_recognition()

while counter < 1000000000:
    counter = counter + 1

print('\nThe complete output is as follows')
print(output)

print('\n\nEnd of message')
