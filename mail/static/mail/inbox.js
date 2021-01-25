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
        console.log(recipients);
        console.log(subject);
        console.log(body);
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
                console.log(result);
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

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>
`;
    append_emails(mailbox);

}

function append_emails(mailbox) {
    const emails_view = document.querySelector('#emails-view')

    var eachEmail;
    fetch('/emails/'+mailbox, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(jsoned => jsoned.forEach(email => {
                console.log(email);
                eachEmail = document.createElement('div');
                eachEmail.setAttribute('class', 'card card-body');

                if (mailbox === 'sent'){
                eachEmail.innerHTML = `<span class="container-fluid d-flex"><span class="col-9"><b>${email['subject']}</b>.  To: ${email['recipients']}</span> <span class="col-3 text-right">At ${email['timestamp']}</span></span>`;

                }
                else{
                eachEmail.innerHTML = `<span class="container-fluid d-flex"><span class="col-9"><b>${email['subject']}</b>.  From: ${email['sender']}</span> <span class="col-3 text-right">At ${email['timestamp']}</span></span>`;
                }



                if (!email['read']) {

                } else {
                    eachEmail.style.backgroundColor = 'rgba(242,245,245,0.8)';
                }
                emails_view.append(eachEmail);


            })
        )
}



