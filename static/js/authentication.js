
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
            showAlert("Login successfull", 'success');
            window.location.href = `/curriculum/dashboard/?${data.next}`
        }else{
            showAlert(data.message, "error");
        }
    })
})

$(".register-form").on("input", "#id__password, #id__confirm_password", () => {
    if ($("#id__password").val() == $("#id__confirm_password").val()) {
        $("#id__err_txt_1_pcnf").hide();
    }else{
        $("#id__err_txt_1_pcnf").show();
    }
})

$("#id__signup_btn").on("click", function() {
    if ($("#id__password").val() == $("#id__confirm_password").val()){
        let payload = {
            first_name: $("#id__first_name").val(),
            last_name: $("#id__last_name").val(),
            username: $("#id__username").val(),
            password: $("#id__password").val(),
            email: $("#id__email").val(),
        }
        postData("/accounts/signup-api/", payload)
        .then(data => {
            if (data.success) {
                showAlert("Registration successfull", "success");
                window.location.replace("/curriculum/dashboard/");
            }else{
                showAlert(data.message, "error");
            }
        })
    }
})