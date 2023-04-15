// JavaScript source code
document.body.style.background = 'url(https://images.unsplash.com/photo-1486427944299-d1955d23e34d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80)'

//$('OURCLASS').click(function () {

//    alert('you clicked')

//})

$('.fa-circle-xmark').click(deleteCupcake)

async function deleteCupcake() {
    const id = $(this).attr('id')
    console.log($(this).parent().parent().parent().parent().parent().parent().parent())
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().parent().parent().parent().parent().parent().parent().remove()
}

$("#new_cupcake_form").submit(addNewCupcake)

async function addNewCupcake() {
    let flavor = $("#flavor").val();
    let rating = $("#rating").val();
    let size = $("#size").val();
    console.log(`${flavor}, ${rating}, ${size}`);
    
    await axios.post("/api/cupcakes", {
        "flavor": `${flavor}`,
        "size": `${size}`,
        "rating": `${rating}`,
        "image": ""
    })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
}