function ChatGptXBlock(runtime, element) {
    var input = element.querySelector(".chatgpt-input input");
    var sendButton = element.querySelector(".chatgpt-send");
    var history = element.querySelector(".chatgpt-history");
  
    function scrollToBottom() {
      history.scrollTop = history.scrollHeight;
    }
  
    scrollToBottom();
  
    sendButton.addEventListener("click", function() {
      var message = input.value;
  
      if (message) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", runtime.handlerUrl(element, "chat_message"));
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.onload = function() {
          var response = JSON.parse(xhr.responseText);
          var messageDiv = document.createElement("div");
          var userDiv = document.createElement("div");
          var responseDiv = document.createElement("div");
  
          messageDiv.classList.add("chatgpt-message");
          userDiv.classList.add("chatgpt-user");
          responseDiv.classList.add("chatgpt-response");
  
          userDiv.textContent = message;
          responseDiv.textContent = response.message;
  
          messageDiv.appendChild(userDiv);
          messageDiv.appendChild(responseDiv);
          history.appendChild(messageDiv);
  
          input.value = "";
          input.focus();
  
          scrollToBottom();
        };
        xhr.send(JSON.stringify({ message: message }));
      }
    });
  }
  