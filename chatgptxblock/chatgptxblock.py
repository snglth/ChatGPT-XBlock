import openai

import xblock.core as xc

from xblock.fields import Scope, String 
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin
from xblockutils.settings import XBlockWithSettingsMixin


class ChatGptXBlock (xc.XBlock, StudioEditableXBlockMixin, XBlockWithSettingsMixin):
    """
    A simple XBlock that allows users to chat with a ChatGPT model.
    """
    message = String(
        help="The current message from the ChatGPT model.",
        default=None,
        scope=Scope.user_state
    )

    def student_view(self, context=None):
        """
        The student view of the XBlock.
        """
        # Generate a message from the ChatGPT model.
        openai.api_key = "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"
        prompt = "Hello, how are you?"
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5
        )
        self.message = response.choices[0].text
        
        # Render the message in the XBlock.
        html = '<div class="chat-message">{}</div>'.format(self.message)
        frag = Fragment(html)
        # frag.add_css(self.load_resource_string("static/css/chat.css"))
        # frag.add_javascript(self.load_resource_string("static/js/chat.js"))
        return frag

    # def load_resource_string(self, resource_path):
    #     """
    #     Load a resource from the XBlock's static directory.
    #     """
    #     resource_loader = ResourceLoader(self.runtime, self.scope_ids, self.block_id, self.runtime.local_resource_url)
    #     return resource_loader.load_unicode(resource_path).decode('utf-8')


# """TO-DO: Write a description of what this XBlock is."""

# import pkg_resources
# import openai
# from web_fragments.fragment import Fragment
# from xblock.core import XBlock
# from xblock.fields import Integer, Scope, string


# class ChatGptXBlock(XBlock):
#     """
#     TO-DO: document what your XBlock does.
#     """

#     # Fields are defined on the class.  You can access them in your code as
#     # self.<fieldname>.

#     # TO-DO: delete count, and define your own fields.
#    message = string(
#        help = "The current message from ChatGPT model."
#        default=None;
#        scope=scope.user_states

#    )

    # def resource_string(self, path):
    #     """Handy helper for getting resources from our kit."""
    #     data = pkg_resources.resource_string(__name__, path)
    #     return data.decode("utf8")

#     # TO-DO: change this view to display your data your own way.
#     def student_view(self, context=None):
#         """
#         The primary view of the ChatGptXBlock, shown to students
#         when viewing courses.
#         """
#         html = self.resource_string("static/html/chatgptxblock.html")
#         frag = Fragment(html.format(self=self))
#         frag.add_css(self.resource_string("static/css/chatgptxblock.css"))
#         frag.add_javascript(self.resource_string("static/js/src/chatgptxblock.js"))
#         frag.initialize_js('ChatGptXBlock')
#         return frag

#     # TO-DO: change this handler to perform your own actions.  You may need more
#     # than one handler, or you may not need any handlers at all.
#     @XBlock.json_handler
#     def increment_count(self, data, suffix=''):
#         """
#         An example handler, which increments the data.
#         """
#         # Just to show data coming in...
#         assert data['hello'] == 'world'

#         self.count += 1
#         return {"count": self.count}

#     # TO-DO: change this to create the scenarios you'd like to see in the
#     # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ChatGptXBlock","""<chatgptxblock/>"""),
            # ("Multiple ChatGptXBlock",
            #  """<vertical_demo>
            #     <chatgptxblock/>
            #     <chatgptxblock/>
            #     <chatgptxblock/>
            #     </vertical_demo>
            #  """),
        ]
