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

const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

push_notification_code.process('data', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message)
    done();
});