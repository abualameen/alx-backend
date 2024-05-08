const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

const kue = require('kue');
const push_notification_code_2 = kue.createQueue({
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

for (let index = 0; index < jobs.length; index++) {
    const job = push_notification_code_2.create('data',jobs[index]);
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
  
