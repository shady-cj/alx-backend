import kue from 'kue';


const blacklisted_nums = ["4153518780", "4153518781"];


const sendNotification = (phoneNumber, message, job, done) => {
    let meter = 0;
    let interval = setInterval(()=> {
        job.progress(meter, 100);
        if (blacklisted_nums.includes(phoneNumber)) {
            done(new Error(`Phone number ${phoneNumber} is blacklisted`));
            return;
        }
        if (meter === 50) {
            console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
            clearInterval(interval);
            done();
            return;
        }
        meter += 50;
    }, 1000);
}

const queue = kue.createQueue();

queue.process("push_notification_code_2", 2, function(job, done) {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
})