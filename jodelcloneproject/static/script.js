

let local = localStorage.getItem("current1");
console.log(local)


function increaseHandler(count){
    var id = `.up${count} > .count`
    var child = document.querySelectorAll(id)[0].innerHTML;
    localStorage.setItem(`current${id}`,child);
    let local =localStorage.getItem(`current${id}`)
    

    currentCount = parseInt(child);
    state = currentCount+1;

    
    //console.log(local)
    document.querySelectorAll(id)[0].innerHTML = state;
        //document.querySelectorAll(id)[0].innerHTML = local;
    currentCount = parseInt(child);
    state = currentCount+1;
    localStorage.setItem(`current${id}`,state);
    local= localStorage.getItem(`current${id}`)
    document.querySelectorAll(id)[0].innerHTML = local;
    

}

//document.querySelectorAll(".arrow-up").addEventListener("click",increaseHandler);



function decreaseHandler(count){
    var id = `.up${count} > .count`
    var child = document.querySelectorAll(id)[0].innerHTML;
    currentCount = parseInt(child);
    state = currentCount - 1;
    document.querySelectorAll(id)[0].innerHTML = state;
    

}




