function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


let intsruments = document.querySelectorAll('.instruments');
for (let i = 0; i < intsruments.length; i++) {
    intsruments[i].addEventListener('click', function() {
        let typeInstrument = this.dataset.action;
        let taskID = this.dataset.task;

        update(typeInstrument, taskID)
        
        console.log("Instrument: " + typeInstrument + ", id: " + taskID);
    });
};

function update(typeInstrument, taskID) {
    let new_description = '';

    if (typeInstrument === 'edit') {
        new_description = prompt('You are in edit mode. Update your task.')
    };

    fetch('/update/', {
        method: 'POST',
        credentials: "same-origin",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'instrument': typeInstrument,
            'task_id': taskID,
            'new_description': new_description
        })
    }).then((response) => {
        return response.json()
    }).then((data) => {
        location.reload()
        alert(data['message'])
    })
};