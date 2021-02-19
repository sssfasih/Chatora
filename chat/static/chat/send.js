function scroll() {
     let messages = document.getElementById("messages");
     messages.scrollTop = messages.scrollHeight;
 }

const csrftoken = getCookie('csrftoken');
document.addEventListener('DOMContentLoaded', () => {
    scroll();
    document.querySelector("#send").onsubmit = function () {
        console.log("Submitted");
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
                console.log(jsonresponse);
                let msgs = document.querySelector('#messages')
                msgs.innerHTML += `<div class="container my-3 text-white" style="text-align: right;">
            <span class="bg-primary container py-2" style="border-radius: 50px;">${jsonresponse['up_txt']}</span>
        </div>`;
                msg.value = '';
                scroll();


            })
        return false;
    }
})