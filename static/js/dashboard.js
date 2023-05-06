const fetchCategories = () => {
    let tableBodyHtml = "";
    showLoader();
    getData('/curriculum/get-all-question-categories/')
    .then(data => {
        hideLoader();
        if (data.status){
            for (let category of data.categories){
                if (category.first_question_uuid){
                    var firstTd = `<td><a target="_blank" href="/curriculum/question/${category.first_question_uuid}/">${category.name}</a></td>`;
                }else{
                    var firstTd = `<td>${category.name}</td>`
                }
                tableBodyHtml += `
                <tr>
                    ${firstTd}
                    <td>${category.description}</td>
                    <td>${category.no_of_question}</td>
                    <td>${category.total_score}</td>
                    <td>${category.student_score}</td>
                    <td>${category.last_submission_date}</td>
                </tr>
                `;
            }
        }
        $("#id__question_category_listing_table tbody").html(tableBodyHtml);
    })
}