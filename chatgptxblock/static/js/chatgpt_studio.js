function ChatGptXBlockStudio(runtime, element) {
    var displayNameInput = element.querySelector(".display-name");
    var apiKeyInput = element.querySelector(".api-key");
    var promptInput = element.querySelector(".prompt");
  
    function updateSettings() {
      var data = {
        display_name: displayNameInput.value,
        api_key: apiKeyInput.value,
        prompt: promptInput.value,
      };
      runtime.notify("save", { state: "start" });
      $.ajax({
        type: "POST",
        url: runtime.handlerUrl(element, "save_settings"),
        data: JSON.stringify(data),
        success: function(response) {
          runtime.notify("save", { state: "end" });
        },
        error: function(response) {
          runtime.notify("error", { msg: response });
        },
      });
    }
  
    displayNameInput.addEventListener("change", updateSettings);
    apiKeyInput.addEventListener("change", updateSettings);
    promptInput.addEventListener("change", updateSettings);
  }
  