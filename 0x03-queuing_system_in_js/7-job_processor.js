const blacklistedNumbers = [4153518780, 4153518781];

const kue = require('kue');
const push_notification_code_2 = kue.createQueue({
    concurrency: 2,
    redis: {
        port: 6379,
        host: '127.0.0.1',
    },
});

push_notification_code_2.on('connect', ()=> {
    console.log('Redis client connected to the server');
});

push_notification_code_2.on('error', (err)=> {
    console.log('Redis client not connected to the server:', err);
});


const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100);
    for (let index = 0; index < blacklistedNumbers.length; index++) {
        if (phoneNumber === blacklistedNumbers[index]) {
            done(new Error(`Phone number ${phoneNumber} is blacklisted`));
        }

    }
    job.progress(50, 100);
    console.log( `Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
};

push_notification_code_2.process('data', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done)
});


