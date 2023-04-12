import json
import logging
import os

from xblock.core import XBlock
from xblock.fields import Integer, String, Scope
from xblock.fragment import Fragment

from xblockutils.resources import ResourceLoaderMixin
from xblockutils.studio_editable import StudioEditableXBlockMixin


# Set up logging
log = logging.getLogger(__name__)


# Define the ChatGptXBlock class
class ChatGptXBlock(XBlock, ResourceLoaderMixin, StudioEditableXBlockMixin):
    # Define the fields for the XBlock
    display_name = String(
        display_name="Display Name",
        help="This is the name that will be displayed to learners.",
        default="Chat with GPT-3",
        scope=Scope.settings,
    )

    api_key = String(
        display_name="API Key",
        help="This is the API key for your OpenAI account.",
        scope=Scope.settings,
    )

    prompt = String(
        display_name="Prompt",
        help="This is the prompt that will be used for the GPT-3 chat.",
        scope=Scope.settings,
    )

    chat_history = String(
        display_name="Chat History",
        help="This is the chat history for the GPT-3 chat.",
        scope=Scope.user_state,
        default=json.dumps([]),
    )

    chat_count = Integer(
        display_name="Chat Count",
        help="This is the number of chats that have been conducted.",
        scope=Scope.user_state,
        default=0,
    )

    # Define the view for the XBlock
    def student_view(self, context=None):
        # Load the HTML template for the XBlock
        html_str = self.resource_string("static/html/chatgpt.html")

        # Create the context for the template
        context = {
            "display_name": self.display_name,
            "api_key": self.api_key,
            "prompt": self.prompt,
            "chat_history": json.loads(self.chat_history),
            "chat_count": self.chat_count,
        }

        # Render the HTML template with the context
        frag = Fragment(html_str.format(context))
        frag.add_css(self.resource_string("static/css/chatgpt.css"))
        frag.add_javascript(self.resource_string("static/js/chatgpt.js"))
        frag.initialize_js("ChatGptXBlock")

        return frag

    # Define the Studio view for the XBlock
    def studio_view(self, context=None):
        # Load the HTML template for the Studio view
        html_str = self.resource_string("static/html/chatgpt_studio.html")

        # Create the context for the template
        context = {
            "display_name": self.display_name,
            "api_key": self.api_key,
            "prompt": self.prompt,
        }

        # Render the HTML template with the context
        frag = Fragment(html_str.format(context))
        frag.add_javascript(self.resource_string("static/js/chatgpt_studio.js"))
        frag.initialize_js("ChatGptXBlockStudio")

        return frag

    # Define the JSON handler for the XBlock
    @XBlock.json_handler
    def chat_message(self, data, suffix=''):
        # Get the user's message from the data
        message = data.get("message", "")

        # Call the GPT-3 API to get the chat response
        response = self.get_chat_response(message)

        # Update the chat history with the new message and response
        chat_history = json.loads(self.chat_history)
        chat_history.append({"message": message, "response": response})
        self.chat_history = json.dumps(chat_history
