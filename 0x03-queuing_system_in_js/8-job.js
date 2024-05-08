const createPushNotificationsJobs = function(jobs, push_notification_code_3) {
    if (!Array.isArray(jobs)) {
        throw new Error("Jobs is not an array");
    }
    if (!push_notification_code_3) {
        throw new Error('Queue is required');
    }
    for (let index = 0; index < jobs.length; index++) {
        const job = push_notification_code_3.create('data',jobs[index]);
        job.on('enqueue', function() {
            console.log(`Notification job created: ${job.id}`);
        });
        job.on('complete', function() {
            console.log(`Notification job ${job.id} completed`);
        });
        job.on('failed', function() {
            console.log(`Notification job ${job.id} failed`);
        });
        
        job.on('progress', function(progress) {
            console.log( `Notification job ${job.id} ${progress}% complete` )
        })
        job.save();
    }
}

export default createPushNotificationsJobs;