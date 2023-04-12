
# ChatGPT XBlock

The ChatGPT-XBlock is a custom XBlock for Open edX that uses the GPT-3.5 architecture to generate text-based responses to user inputs.


## Installation

To install the ChatGPT-XBlock, you can use the following command:

```bash
  pip install git+https://github.com/SRDeveloperVishal/ChatGPT-XBlock
```
Alternatively, you can clone the repository and install the XBlock using the following commands:

```bash
git clone https://github.com/SRDeveloperVishal/ChatGPT-XBlock.git
cd ChatGPT-XBlock
pip install -e .

```
    
## Usage

To use the ChatGPT-XBlock in your Open edX course, follow these steps:

- Log in to the Open edX Studio and create a new course, or open an existing course.

- Navigate to the desired unit where you want to add the ChatGPT-XBlock.

- Click on the "Advanced" tab and select "Add new component".

- Select the "ChatGPT-XBlock" from the list of available components and add it to the unit.

- Configure the XBlock settings, including the prompt text and the API key for the GPT-3.5 API.

- Save the changes and view the course to see the ChatGPT-XBlock in action.
## Configuration

The ChatGPT-XBlock can be configured using the following settings:

- prompt_text: The text prompt that the user will respond to.
- api_key: The API key for the GPT-3.5 API.
- max_tokens: The maximum number of tokens that the GPT-3.5 API will generate in response to a prompt.
- temperature: The "temperature" parameter for the GPT-3.5 API, which controls the "creativity" of the generated responses.
- top_p: The "top-p" parameter for the GPT-3.5 API, which controls the diversity of the generated responses.
## Credits

The ChatGPT-XBlock was created by Vishal Bhardwaj and Mohit Aggarwal is released under the MIT License. The XBlock is based on the OpenAI GPT-3.5 API, which is developed by OpenAI and is subject to its own terms and conditions.

- [@srdevelopervishal](https://www.github.com/srdevelopervishal)
- [@Mister-maker](https://www.github.com/Mister-maker)

