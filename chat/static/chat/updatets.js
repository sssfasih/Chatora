//console.log("GET UPDATES");
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
            //console.log(jsoned);
            for (i in jsoned) {
                //console.log(i);
                //console.log(jsoned[i]);
                let txt = document.querySelector("#lst-" + i);
                    if (txt === null){
                        //console.log("Text is undefined");
                        document.querySelector('#all_messages').innerHTML += `<form class="card" style="" method="GET" onclick="this.submit()" action="/chat/">

                            <input name="conv_id" value="${i}" hidden="">
                            <div class="card-body">
                                <h5 class="card-title">Someone</h5>
                                <p class="card-text" id="lst-${i}"></p>
                            </div>
                        </form>`;
                        txt = document.querySelector("#lst-" + i);

                    }
                    txt.innerText = jsoned[i].slice(0, 17) + "...";


            }
            return jsoned
        })
        .then(jsoned => {
            var current_disp = document.querySelector(".msg").id
            if (current_disp in jsoned) {
                //console.log("display needs update");
                updateDisplay(current_disp);

            }
            setTimeout(update, 6000); // try again in 6 secs
        })
}

function updateDisplay(current_disp){
    //console.log("UPDATING DISPLAY")
    fetch('/updates/', {
        method: "PUT",
        headers: {'X-CSRFToken': getcsrftoken},
        body: JSON.stringify({disp:current_disp})

    })
        .then(response => {
            return response.json();

        })
        .then(jsoned => {
            //console.log(jsoned);
            var selff = document.querySelector('.selff').id;
            selff = selff.slice(5,);
            var display = document.querySelector("#messages")
            for (each_new_msg in jsoned){
                if (jsoned[each_new_msg][1] === parseInt(selff)){continue;}

            display.innerHTML += `<div class="container" style="display: flex; flex-direction: row;">

                    <div class=" my-2 text-white bg-secondary py-2" style="text-align: left; border-radius: 20px;">
                        <span class="container " style="">${jsoned[each_new_msg][0]}</span>
                    </div>
                    <div class="col"></div>
                    </div>`;

            }
            scroll();
            return jsoned;
        })

}


update();