
const editor = ace.edit("id__code_editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");

$("#id__refresh_editor").on("click", () => {
    showLoader();
    editor.setValue("");
    hideLoader();
})

// Function to run the code
function runCode() {
    // Get the code from the editor
    var code = editor.getValue();
  
    // Send a request to Repl.it's API to compile and run the code
    fetch("https://repl.it/api/v0/repls/python3", {
      method: "POST",
      body: JSON.stringify({ code: code }),
      headers: { 
        "Content-Type": "application/json" ,
        "Authorization": "ApiKey YOUR_API_KEY_HERE",
    },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        // Display the output
        var output = data.output;
        console.log(output)
      });
  }
  

$("#id__compile_code").on("click", function(e) {
    compileTheCode();
})


const compileTheCode = () => {
    let code = editor.getValue();
    let data = {
        code: code
    }
    postData("/editor/code-compiler/", data)
    .then(result => {
        if (result.status){

        }
    })
}