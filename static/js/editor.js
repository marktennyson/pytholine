
showLoader();
const editor = ace.edit("id__code_editor");
editor.session.on('changeMode', () => {
    hideLoader();
  });
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");

$("#id__refresh_editor").on("click", () => {
    showLoader();
    editor.setValue("");
    $(".card .card-footer #id__output").html("<b>Output:&nbsp;</b>&nbsp;!");
    $(".card .card-footer #id__status").html("<b>Status:&nbsp;</b>&nbsp;!");
    hideLoader();
})

$("#id__compile_code").on("click", function(e) {
    compileTheCode();
})

const compileTheCode = () => {
    let code = editor.getValue();
    let data = {
        code: code
    }
    showLoader();
    postData("/editor/code-compiler/", data)
    .then(result => {
        hideLoader();
        if (result.status){
            let outputHtml = `
            <b>Output:&nbsp;</b>
            <span class="badge bg-${result.is_execution_succeed ? 'success' : 'danger'}">
                ${result.is_execution_succeed ? 'Success' : 'Error'}
            </span>&nbsp;&nbsp;
            ${result.output}
            `;
            let statusHtml = `
            <b>Status:&nbsp;</b>
            <span class="badge bg-${result.is_correct_answer ? 'success' : 'danger'}">
            ${result.is_correct_answer ? 'Right' : 'Wrong'}
            </span>
            `;
            $(".card .card-footer #id__output").html(outputHtml);
            $(".card .card-footer #id__status").html(statusHtml);
        }
    })
}