const fetchBatches = (studentId) => {
    let payload = {student_id: studentId}
    let cardHtml = "";
    showLoader();
    getData('/curriculum/get-all-batches-of-student/', payload)
    .then(data => {
        hideLoader();
        if (data.status){
            for (let batch of data.batches){
                cardHtml += `
                <div class="col-md-4">
                    <div class="card text-white bg-dark mb-3" style="max-width: 18rem;">
                        <img src="${batch.language_logo}" class="card-img-top" alt="...">
                        <div class="card-body">
                        <h5 class="card-title">${batch.name}</h5>
                        <p class="card-text"><b>${makeBatchNameByDate(batch.start_date, batch.end_date)}</b></p>
                        <a href="#" class="btn btn-primary">Open</a>
                        </div>
                    </div><br/>
                </div>
                `
            }
        }
        $("#id__batch_list").html(cardHtml);
    })
}