# This is a Python text-to-speech project using Microsoft Azure.
# To run locally, you must pip install azure-cognitiveservices-speech
# Local: Create an .venv file on your system
# Local: Create an .env file for your SPEEDH_KEY and SPEECH_REGION
# Connect or upload this file to Azure. There may be an extension in your code editor that connects to Azure.

import os
import azure.cognitiveservices.speech as speechsdk # type: ignore

# Set up the subscription info for the Speech Service:
speech_key = os.environ.get('SPEECH_KEY')
service_region = os.environ.get('SPEECH_REGION')

# Create an instance of a speech config with specified subscription key and service region.
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Create a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Get text from the user
text = "Hello, this is a text-to-speech conversion example."

# Synthesize the text to speech
result = speech_synthesizer.speak_text_async(text).get()

# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
