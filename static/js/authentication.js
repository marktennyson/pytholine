
$("#id__login_btn").on("click", () => {
    let payload = {
        username: $("#id__login_username").val(),
        password: $("#id__login_password").val()
    }
    showLoader();
    postData("/authentication/login-api/", payload)
    .then(data => {
        hideLoader();
        if (data.status){
            window.location.href = "/website/dashboard/"
        }else{
            alert(data.message)
        }
    })
})