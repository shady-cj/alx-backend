import kue from 'kue';

let queue = kue.createQueue();

const jobData = {
    phoneNumber: "+2348184926924",
    message: "Excommunicado"
};
const job = queue.create("push_notification_code", jobData).save((err) => {
    if (!err) {
        console.log("Notification job created:", job.id)
    }
});

job.on('complete', (res)=> {
    console.log("Notification job completed")
});

job.on('failed attempt', (errorMsg, doneAttempts) => {
    console.log("Notification job failed")
})