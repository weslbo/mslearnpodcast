# mslearnpodcast

This project aims to generate podcasts from Microsoft Learn modules. A conversation happens between Brian (the interviewer) and Andrew (guest), and they discuss the topics of certain module in detail.

All of the content is generated using Azure OpenAI and translated to speech using the SDK. This is how the process works:

- The code will take a learn module (main page) and extract all the units. It uses beatifullsoup to parse the contents.
- The output of all the units is saved as a text file.
- A prompt is send to Azure OpenAI to create the podcast. The prompt will contain the learn module output and produces a transcript.
- The transcript is send again to Azure OpenAI, but this time transforming the content to Speech Syntheses Markup Language
- The resulting output is transformed using the Speech SDK into an mp3 file.

## Prerequisites

- Deploy an Azure OpenAI resource
- Deploy the gpt-35-turbo-16k model (with same name)
- Set the OPENAI_API_KEY as an environment variable
- Create an Azure Speech Service
- Set the SPEECH_API_KEY as an environment variable

## Usage

```bash
$ python podcast.py "https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-app-service/"
```

An optional parameter [speechonly] can be appended, to only generate the mp3. (not re-generating the transcript speech ml)