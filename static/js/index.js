const showLoader = () => {
    $('#ajax-loader').show();
  }
  const hideLoader = () => {
    $('#ajax-loader').hide();
  }

const postData = async(url="", data={}) => {
    const response = await fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "cors",
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin",
        headers: {"Content-Type": "application/json",},
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });
    return response.json();
}

const getData = async(url) => {
    const response = await fetch(url);
    const jsonData = await response.json();
    return jsonData;
}