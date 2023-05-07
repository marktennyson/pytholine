const showLoader = () => {
    $('#ajax-loader').show();
  }
  const hideLoader = () => {
    $('#ajax-loader').hide();
  }

const postData = async(url="", data={}) => {
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {"Content-Type": "application/json",},
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });
    return response.json();
}

const getData = async (url = "", data = {}) => {
    const queryParameters = Object.entries(data)
        .map(([key, value]) => `${encodeURIComponent(key)}=${encodeURIComponent(value)}`)
        .join("&");

    const response = await fetch(`${url}?${queryParameters}`, {
        method: "GET",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
        "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
    });
    return response.json();
    };

const makeBatchNameByDate = (startDate, endDate) => {
    let startdate = new Date(startDate);
    let enddate = new Date(endDate);
    let options = {
        timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: true,
    };
    let startDateStr = startdate.toLocaleString("en-US", options);
    let endDateStr = enddate.toLocaleString("en-US", options);

    return `${startDateStr} - ${endDateStr}`;
}

const logout = () => {
    getData(`/accounts/logout-api/`)
    .then(data => {
        if (data.status){
            window.location.replace(data.login_url);
        }
    })
}

const showAlert = (message, type) => {
    var alertBox = $("#id__alert_box");

	alertBox.find("p").html(message);

	// Set the background color based on the message type
	switch(type) {
		case "success":
			alertBox.css("background-color", "#4CAF50");
			break;
		case "info":
			alertBox.css("background-color", "#2196F3");
			break;
		case "error":
			alertBox.css("background-color", "#f44336");
			break;
	}

	// Show the alert box
	alertBox.addClass("show").removeClass('hide');

	// Hide the alert box after 3 seconds
	setTimeout(function() {
		closeAlertBox();
	}, 2000);
} 

const closeAlertBox = obj => {
    $("#id__alert_box").addClass('hide').removeClass("show");
}