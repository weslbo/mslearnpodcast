import requests
import os
import sys
import azure.cognitiveservices.speech as speechsdk
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from openai import AzureOpenAI

def importLearnModuleText(url):
    filename = "modules/" + url.rsplit('/', 2)[-2] + ".txt"

    if os.path.exists(filename):
        os.remove(filename)

    responseModule = requests.get(url)

    if responseModule.status_code == 200:
        with open(filename, "a", encoding="utf-8") as file:
            contentModule = responseModule.text
            soupMain = BeautifulSoup(contentModule, "html.parser")
            links = soupMain.find_all(class_="unit-title")
            absolute_urls = [urljoin(url, link["href"]) for link in links]

            for absolute_url in absolute_urls:
                responseArticle = requests.get(absolute_url)
                if responseArticle.status_code == 200:
                    contentArticle = responseArticle.text
                    soupArticle = BeautifulSoup(contentArticle, "html.parser")
                    
                    div = soupArticle.find(id="unit-inner-section")
                    if div:
                        # Remove <ul> elements from div if it has a metadata class
                        for ul in div.find_all("ul", class_="metadata"):
                            ul.decompose()
                        for d in div.find_all("div", class_="xp-tag"):
                            d.decompose()
                        for next in div.find_all("div", class_="next-section"):
                            next.decompose()
                        for header in div.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
                            header.string = "\n# " + header.get_text() + "\n"
                        for u in div.find_all(["li"]):
                            u.string = "- " + u.get_text()
                        
                        txtContent = div.get_text()

                        file.write(str(txtContent))
                    else:
                        print(f"Failed to find div with id='unit-inner-section' from page {absolute_url}")
                else:
                    print(f"Failed to retrieve the page: {absolute_url}")

def createPodcastFromText(url):
    client = AzureOpenAI(azure_endpoint="https://wedebolsaiopenai2.openai.azure.com/", api_version="2023-07-01-preview", api_key=os.getenv("OPENAI_API_KEY"))

    filename = "modules/" + url.rsplit('/', 2)[-2] + ".txt"
    podcast = "podcasttxt/" + url.rsplit('/', 2)[-2] + ".txt"

    with open(filename, "r", encoding="utf-8") as learmodule_file:
        learnmodule_contents = learmodule_file.read()

    with open("prompts/prompt.txt", "r") as prompt_file:
        prompt = prompt_file.read()

    message_text = [
        {"role":"system","content":prompt.replace("{{content}}", learnmodule_contents)},
        {"role":"user","content":"Create the podcast"}
    ]

    completion = client.chat.completions.create(
        model="gpt-35-turbo-16k",
        messages = message_text,
        temperature=0.1,
        max_tokens=9500,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    output = completion.choices[0].message.content

    with open("prompts/speechml.txt", "r") as speech_prompt_file:
        speech_prompt = speech_prompt_file.read().replace("{{text}}", output)

    message_text = [
        {"role":"system","content":""},
        {"role":"user","content":speech_prompt}
    ]

    completion = client.chat.completions.create(
        model="gpt-35-turbo-16k",
        messages = message_text,
        temperature=0.3,
        max_tokens=10000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    output = completion.choices[0].message.content

    with open(podcast, "w") as file:
        file.write(output)

def createAudio(url):
    service_region = "eastus"
    speech_key = api_key=os.getenv("SPEECH_API_KEY")
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio24Khz96KBitRateMonoMp3)  

    podcast = "podcasttxt/" + url.rsplit('/', 2)[-2] + ".txt"
    mp3_filename = "podcastmp3/" + url.rsplit('/', 2)[-2] + ".mp3"

    file_config = speechsdk.audio.AudioOutputConfig(filename=mp3_filename)  

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)  

    with open(podcast, "r") as podcastfile:
        podcastspeechml = podcastfile.read()

    # Synthesizes the received text to speech.
    # The synthesized speech is expected to be heard on the speaker with this line executed.
    result = speech_synthesizer.speak_ssml_async(podcastspeechml).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Audio completed")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")

def main():
    if len(sys.argv) < 2:
        print("Please provide the URL as a command line argument.")
        sys.exit(1)

    url = sys.argv[1]

    if len(sys.argv) >= 3 and sys.argv[2] == "speechonly":
        speechonly = True
    else:
        speechonly = False
    
    print(f"Start to create a podcast for url: {url}")

    if not speechonly:
        print(f"Importing text (1/3)")
        importLearnModuleText(url)

        print("Creating podcast speech ml (2/3)")
        createPodcastFromText(url)

    print("Creating audio (3/3)")
    createAudio(url)

    print("Finished")


if __name__ == "__main__":
    main()