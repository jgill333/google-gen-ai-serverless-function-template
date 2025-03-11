# 🎁 🐍 🍏 Use Google Generative AI + Gemini + Siri + Google Cloud Run Functions Together   

This a fully functioning example project for serverless `Generative AI`-as-a-Service and combining the apps and ecosystems of Google and Apple for practical automation and use cases.

<p align="center">
	<img src="https://github.com/user-attachments/assets/cdf25cca-cb9b-4876-b4b3-76d084c47c36">
</p>

## Purpose

Learn how to use Google Gemini, Apple Siri, and Google's serverless Google Cloud Run Functions together.

When deployed, this project is a **self-contained scalable serverless environment for Generative AI** in `google cloud` using `google cloud run functions`. While you are likely familiar with serverless web services, for the purposes of this project this means that you do not have to maintain servers and infrastructure. Google Cloud Platform (GCP) handles horizontal scaling, and you only pay for the time and resources used (which is perfect for a project like this or many types of large scale services). In many cases, running this project and services within GCP will be completely free if you are within the free tier limits.

This project and the associated videos also show a practical use case of calling `google cloud run functions` from apps and clients like [Apple Shortcuts](https://support.apple.com/guide/shortcuts/welcome/ios).

- Yes, anyone can run script on iOS with the built-in workflow app Apple Shortcuts (which is available on iOS, iPadOS, macOS, tabletOS, and watchOS).
- Yes, this is using Gemini and Siri together.
- Yes, this has function calling to enable Gemini to have access to Google search results.

![Diagram of Apple and Google Device and Ecosystem Interactions for This GeAI Example and Project](https://github.com/user-attachments/assets/f23ec04d-5bc1-4a28-a339-52181ed1f4b9)

### 📺 Video Intro (~3 min)

Watch the [intro and overview video](https://youtu.be/WUHeLYqgo3w), https://youtu.be/WUHeLYqgo3w. 

<p align="center">
  [![Video Intro of How To Use Apple Shortcuts with Google's Generative AI SDK, Google Gemini, and Google Cloud Run Functions](https://github.com/user-attachments/assets/b4796aeb-f592-4f83-8ae6-0aee47570c57)](https://youtu.be/WUHeLYqgo3w)
</p>

### 📺 Longer Video Explanation (~10 min)

Watch the [longer explainer video](https://youtu.be/zqkeiW9V5ew) for additional background and context, https://youtu.be/zqkeiW9V5ew.

It even mentions [HyperCard](https://en.wikipedia.org/wiki/HyperCard).

#### Connect

[![LinkedIn][LinkedIn]][Linkedin-url]

### Pre-requisites

[![Python][Python]][python-url]

- 🐍 Python 3.12 or greater
- Google Cloud CLI
- Google Gemini API Key

### Setup Steps 

1. Clone this repository locally
2. Set up a `virtual environment` from the local directory that the repository was cloned into from the command-line: 
    ```console
    $ python3 -m pip install virtualenv
    $ python3 -m virtualenv venv
    ```
> [!NOTE]
> `virtual environments` may be created in a different way, depending on your `python` installation and configuration. For example, for some setups the `virtual environment` setup will look similar to this without a `python` version and using the `venv` package: 
> 
> ```console
> $ python -m venv venv
> ```

3. Activate the `virtual environment` from within the directory of the local repository:
    ```console
    $ venv/bin/activate 
    # Note: The relative path to the activate script
    # may be at a location like the following: 
    # $ venv\scripts\activate 
    # Optionally, you may run one of the `activate` 
    # script helper files in the top-level directory
    # of the source for this repository. 
    # For example, on `windows` run `activate.bat` 
    # from the command-line (which this will do): 
    # > activate
    ```

4. If you do not already have the `google cloud cli` installed and configured on your system:
  - Install the `google cloud cli` ([aka](https://en.wikipedia.org/wiki/Aka#:~:text=%22Also%20Known%20As) `gcloud cli`, `google cloud sdk`)
    - https://cloud.google.com/sdk/docs/install-sdk
    - Setup or configure the `gcloud cli`
    ```console
    gcloud init
    ```
    - You may need to enable the Google Cloud APIs and capabilities for `artifact registry`, `cloud build`, `cloud run admin`, and `cloud logging` for your `google cloud project`.
      - https://console.cloud.google.com/flows/enableapi?apiid=artifactregistry.googleapis.com,cloudbuild.googleapis.com,run.googleapis.com,logging.googleapis.com
    
5. Get/set your `GEMINI_API_KEY`. Create a new API key at `google cloud` if you do not already have API a key(s).
  - See: https://ai.google.dev/gemini-api/docs/api-key and/or https://aistudio.google.com/app/apikey
  - Copy the key to a storage mechanism of your choice
  - Set the value for `gemini_api_key` or `gemini_api_key_fallback = "REPLACE_WITH_YOUR_GEMINI_API_KEY"` to your `GEMINI_API_KEY`.
    - Optionally, set the `GEMINI_API_KEY` environment variable in a manner that is accessible within a Google Cloud Run Function

5. Install the requirements needed to run the application locally with the following command from the same activated `virtual environment` command-line window:
```console
$ pip install -r requirements.txt
```

### Deploy Steps

The following will create a serverless Google Cloud Run Function in the Google Cloud Platform (GCP) and give you a URL that is externally accessible. 

1. Run the following command (it will error if you do not have the `Google Cloud/gcloud CLI` configured locally) from an activated `virtual environment` command-line window:

> [!NOTE]  
> The list of available Google Cloud regions and zones is available at: 
> https://cloud.google.com/compute/docs/regions-zones

```console
gcloud functions deploy cloud-jokes \
  --gen2 \
  --region=REPLACE_WITH_YOUR_REGION_OF_CHOICE \
  --runtime=python312 \
  --source=. \
  --entry-point=my_cloud_function \
  --trigger-http
```

or 

```console
gcloud functions deploy cloud-jokes --gen2 --region=REPLACE_WITH_YOUR_REGION_OF_CHOICE --runtime=python312 --source=. --entry-point=my_cloud_function --trigger-http
````

The command line output will look similar to the following as the service deploys: 
```console
Preparing function...
state: ACTIVE
url: https://{your-region}-{generated-function-instance-name}.cloudfunctions.net/cloud-jokes
```

> [!NOTE]  
> The externally accessible function invocation URL will have a format and pattern similar to: `https://{your-region}-{generated-function-instance-name}.cloudfunctions.net/{your-function-name}`

**The URL that is provided as part of the deploy or update process is a publicly accessible URL that you may access, share, run, etc. 🎉**

2. If you make any changes to the service and wish to redeploy it (and replace all running instances) then just re-run deploy command you used to originally deploy the service from an activated `virtual environment` command-line window

> [!NOTE]  
> To teardown the resources (deprovision) and make the URL inaccessible run the [`gcloud function delete command`](https://cloud.google.com/sdk/gcloud/reference/functions/delete):
> ```console
> $ gcloud functions delete cloud-jokes --region={REPLACE_WITH_YOUR_REGION_OF_CHOICE}
> ```

### Call The Serverless Generative AI Google Cloud Run Function

Generate AI or Large Language Model (LLM) output at the `/cloud-jokes` route, e.g. [`https://{your-region}-{generated-function-instance-name}.cloudfunctions.net/cloud-jokes`](https://{your-region}-{generated-function-instance-name}.cloudfunctions.net/cloud-jokes). You may also customize the prompt by appending the `?prompt=<value of prompt>` querystring like [`https://{your-region}-{generated-function-instance-name}.cloudfunctions.net/cloud-jokes?prompt=What is the meaning of life?`](https://{your-region}-{generated-function-instance-name}.cloudfunctions.net/cloud-jokes?prompt=What%20is%20the%20meaning%20of%20life%3F).

### Apple Shortcuts Integration

Click/tap the [video link](https://youtu.be/zqkeiW9V5ew) to learn more about how to call `google cloud run functions` from Apple Shortcuts.

<p align="center">
  [![Video Explainer On Using Apple Shortcuts with Google Gemini and Google Cloud Run Functions](https://github.com/user-attachments/assets/46a55d0e-45a0-4ca7-93c4-1436d9ffaf63)](https://youtu.be/zqkeiW9V5ew)
</p>

> [!TIP]
> If you want to use a different voice for `siri` on your `ios` and Apple-related operating system, navigate to `Settings -> Accessibility -> Spoken Content -> Voices -> {Language: English}` and select from the list of available voices.


<!-- Markdown Reference Links -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: https://img.shields.io/badge/Python-ffdf76?style=for-the-badge&logo=python&logoColor=#004d7a
[python-url]: https://www.python.org/
[LinkedIn]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=#ffffff
[linkedin-url]: https://www.linkedin.com/in/jonathangill1/
