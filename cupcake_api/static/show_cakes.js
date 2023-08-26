
// const axios_ = axios.create({baseUrl:"http://127.0.0.1:5000"})
async function showAll(){
   let res =  await axios.get("http://127.0.0.1:5000/api/cupcakes")
   let cupcakes = res.data.cupcakes
    console.log(res)
    for (let i=0; i<=cupcakes.length-1; i++){
        $("div").append(`<h4 style= "text-decoration:underline";>${cupcakes[i].flavor}</h4>`)
        console.log("loop")
        let parent =  $("div").append(`<ul id=${[i]}></ul>`)
        parent.append (`<img src="${cupcakes[i].image}" style="width: 100px; height: 100px">`)
        parent.append(`<li>Size: ${cupcakes[i].size}</li>`)
        parent.append(`<li> Rating: ${cupcakes[i].rating}</li>`)
    }
} 

$("#showAll").click(showAll)


async function createCake(e){
    e.preventDefault()
    flavor=$("#flavor").val()
    size=$("#size").val()
    rating=$("#rating").val()
    image=$("#image").val()
    console.log(image)
    let res =  await axios.post("http://127.0.0.1:5000/api/cupcakes", {flavor:flavor, size:size, rating:rating, image:image})
    


}
$("#add").click(createCake)