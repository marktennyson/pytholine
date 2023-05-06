
$("#id__login_btn").on("click", () => {
    let payload = {
        username: $("#id__login_username").val(),
        password: $("#id__login_password").val()
    }
    showLoader();
    postData("/accounts/login-api/", payload)
    .then(data => {
        hideLoader();
        if (data.status){
            window.location.href = `/curriculum/dashboard/?${data.next}`
        }else{
            showAlert(data.message, "error");
        }
    })
})