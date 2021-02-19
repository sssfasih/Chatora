console.log("GET UPDATES");
const getcsrftoken = getCookie('csrftoken')

function update (){
    fetch('/updates/', {
        method: "POST",
        headers: {'X-CSRFToken': getcsrftoken},

    })
        .then(response => {
            return response.json();

        })
        .then(jsoned => {
            console.log(jsoned);
            for (i in jsoned) {
                console.log(i);
                console.log(jsoned[i]);
                document.querySelector("#lst-" + i).innerText = jsoned[i].slice(0, 17) + "...";


            }
            return jsoned
        })
        .then(jsoned => {
            var current_disp = document.querySelector(".msg").id
            if (current_disp in jsoned) {
                console.log("display needs update");
                updateDisplay(current_disp);

            }
            setTimeout(update, 6000); // try again in 6 secs
        })
}

function updateDisplay(current_disp){
    console.log("UPDATING DISPLAY")
    fetch('/updates/', {
        method: "PUT",
        headers: {'X-CSRFToken': getcsrftoken},
        body: JSON.stringify({disp:current_disp})

    })
        .then(response => {
            return response.json();

        })
        .then(jsoned => {
            console.log(jsoned);
            var display = document.querySelector("#messages");
            for (each_new_msg in jsoned){
                console.log(display)
            display.innerHTML += `<div class="container my-3 text-white">
                <span class="bg-secondary container py-2" style="border-radius: 50px;">${jsoned[each_new_msg]}</span>
            </div>`;
            }
            scroll();
            return jsoned
        })

}


update();