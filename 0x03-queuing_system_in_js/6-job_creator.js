const kue = require('kue');
const push_notification_code = kue.createQueue({
    redis: {
        port: 6379,
        host: '127.0.0.1',
    },
});

push_notification_code.on('connect', ()=> {
    console.log('Redis client connected to the server');
});

push_notification_code.on('error', (err)=> {
    console.log('Redis client not connected to the server:', err);
});

const jobData = {
    phoneNumber: "1234567890",
    message: "This is a test notification message."
  };
  

const job = push_notification_code.create('data',jobData);
job.on('enqueue', function() {
    console.log(`Notification job created: ${job.id}`);
});
job.on('complete', function() {
    console.log("Notification job completed");
});
job.on('failed', function() {
    console.log("Notification job failed");
});

job.save();