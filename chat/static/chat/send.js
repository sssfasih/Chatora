function scroll() {
     let messages = document.getElementById("messages");
     messages.scrollTop = messages.scrollHeight;
 }

const csrftoken = getCookie('csrftoken');
document.addEventListener('DOMContentLoaded', () => {
    scroll();
    document.querySelector("#send").onsubmit = function () {
        //console.log("Submitted");
        let msg = document.querySelector('.msg')
        let txt = msg.value;
        let convoID = msg.id
        //console.log(txt);
        //console.log(convoID);

        //console.log(csrftoken);

        fetch('/send/' + convoID, {
            method: "PUT",
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({txt: txt, convoID: convoID})
        })
            .then(response => {
                return response.json();

            })
            .then(jsonresponse => {

                if (jsonresponse['Done'] === false){
                    console.log(jsonresponse);
                }
                else{
                let msgs = document.querySelector('#messages')
                msgs.innerHTML += `<div class="container" style="display: flex; flex-direction: row;">
                        <div class="col"></div>
                    <div class=" my-2 text-white bg-primary py-2" style="text-align: right; border-radius: 20px;">
                        <span class="container">${jsonresponse['up_txt']}</span>
                    </div>
                    </div>`

                msg.value = '';
                scroll();
                update();
                }

            })
        return false;
    }
})