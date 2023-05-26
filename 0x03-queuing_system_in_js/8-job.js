export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error("Jobs is not an array");
    }
    for (const job of jobs) {
        const current_job = queue.create("push_notification_code_3", job).save((err) => {
            if (!err) {
                console.log("Notification job created:", current_job.id)
            }
        });
        current_job.on('complete', (res) => {
            console.log(`Notification job ${current_job.id} completed`)
        });
        current_job.on('failed', (err) => {
            console.log(`Notification job ${current_job.id} failed: ${err}`)
        })
        current_job.on('progress', (progress, data) => {
            console.log(`Notification job ${current_job.id} ${progress}% complete`);
        })
    }
}
