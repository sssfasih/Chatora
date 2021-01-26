document.addEventListener('DOMContentLoaded', function () {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);

    // By default, load the inbox
    load_mailbox('inbox');

    document.querySelector('#compose-form').addEventListener('submit', event => {
        alert("Form Submmitted ");
        event.preventDefault();
        const recipients = document.querySelector('#compose-recipients').value;
        const subject = document.querySelector('#compose-subject').value;
        const body = document.querySelector('#compose-body').value;
        //console.log(recipients);
        //console.log(subject);
        //console.log(body);
        fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                recipients: recipients,
                subject: subject,
                body: body
            })
        })
            .then(response => response.json())
            .then(result => {
                //console.log(result);
                const message = document.createElement('div');
                if (result['message']) {
                    message.innerText = result['message'];
                    message.setAttribute('class', 'alert alert-success');
                    load_mailbox('sent');
                } else {
                    message.innerText = result['error'];
                    message.setAttribute('class', 'alert alert-danger');
                }
                message.setAttribute('role', 'alert');


                document.getElementById('alert_message').append(message);
            });
        return false;
    });


});

function compose_email() {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#email-content').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email-content').style.display = 'none';

    // Show the mailbox name
    //console.log("mailboxName is");
    //console.log(mailbox);
    //console.log("**************");
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
    append_emails(mailbox);

}

function append_emails(mailbox) {
    const emails_view = document.querySelector('#emails-view');

    var eachEmail;
    fetch('/emails/' + mailbox, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(jsoned => jsoned.forEach(email => {
                //console.log(email);

                eachEmail = document.createElement('div');
                eachEmail.setAttribute('class', 'card card-body');

                if (mailbox === 'sent') {
                    eachEmail.innerHTML = `<span class="container-fluid d-flex"><span class="col-9"><b>${email['subject']}</b>.  To: ${email['recipients']}</span> <span class="col-3 text-right">At ${email['timestamp']}</span></span>`;

                } else {
                    eachEmail.innerHTML = `<span class="container-fluid d-flex"><span class="col-9"><b>${email['subject']}</b>.  From: ${email['sender']}</span> <span class="col-3 text-right">At ${email['timestamp']}</span></span>`;
                }


                if (!email['read']) {

                } else {
                    eachEmail.style.backgroundColor = 'rgba(242,245,245,0.8)';
                }

                eachEmail.addEventListener('click', () => displayEmail(email['id'], mailbox));
                emails_view.append(eachEmail);


            })
        )
}

function archive_unarchive(mailbox, id) {
    var condition;
    var state = false;
    if (mailbox === 'inbox') {
        condition = true;
        state = true;
    } else if (mailbox === 'archive') {
        condition = false;
        state = true
    }
    if (state) {

        fetch('emails/' + id, {
            method: 'PUT',
            body: JSON.stringify({archived: condition})
        })
            .then(() => load_mailbox(mailbox))
    }
}

function reply_mail(mailbox,emailJSON){
//    console.log("**************************");
//    console.log(mailbox);
//    console.log(emailJSON);
//    console.log("**************************");

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#email-content').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = emailJSON['sender'];
    if (emailJSON['subject'].slice(0,4) ==="Re: "){

    }
    else{
        //console.log(emailJSON['subject'].slice(0,5));
        emailJSON['subject'] = "Re: "+emailJSON['subject'];
    }
    document.querySelector('#compose-subject').value = emailJSON['subject'];
    document.querySelector('#compose-body').value = `\nOn ${emailJSON['timestamp']} ${emailJSON['sender']} wrote: \n${emailJSON['body']}`;
}



function displayEmail(id, mailbox) {
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email-content').style.display = 'block';


    const emailDiv = document.querySelector('#email-content');
    // fetch email
    fetch('emails/' + id, {
        method: 'GET'
    })
        // JSON it
        .then((StringJSOM) => {
                return StringJSOM.json();
            }
        )
        // print it
        .then(JSOM => {
            const emailJSON = JSOM;
            var button = '';
            //console.log(emailJSON);
            if (mailbox === 'inbox') {
                //console.log('defining button on inbox');
                var button = `<button onclick=archive_unarchive('${String(mailbox)}',${emailJSON['id']}) class="btn btn-sm btn-outline-primary mt-5">Add to Archive</button>`
            } else if (mailbox === 'archive') {

                //console.log('defining button on archive');
                var button = `<button onclick=archive_unarchive('${String(mailbox)}',${emailJSON['id']}) class="btn btn-sm btn-outline-primary mt-5">Remove from Archives</button>`
            }
            //console.log(emailJSON['body']);
            emailDiv.innerHTML = `<div class="card">
                <h4 class="card-header">${emailJSON['subject']}</h4>
                <div class="card-body">
                <p class="card-title">From: ${emailJSON['sender']}</p>
                <p class="card-title">Recipients: ${emailJSON['recipients']}</p>
                <p class="card-title">at: ${emailJSON['timestamp']}</p></br>
                    <textarea class="container-fluid" disabled>${emailJSON['body']}</textarea>
                    <button onclick="load_mailbox('${String(mailbox)}')" class="btn btn-sm btn-outline-primary mt-5">Back</button>
                    <button id="rep-${emailJSON['id']}" class="btn btn-sm btn-outline-primary mt-5">Reply</button>
                    ` + button +


                `</div>
            </div>`;
            document.querySelector('#rep-'+emailJSON['id']).addEventListener('click',(eve)=>{
                reply_mail(mailbox,emailJSON);
            })
            return emailJSON['id'];
        })
        //mark it read
        .then(id => {
            fetch('emails/' + id, {
                method: 'PUT',
                body: JSON.stringify({
                    read: true
                })
            })
        })


}

