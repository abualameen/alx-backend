
const chai = require('chai');
const expect = chai.expect;
const kue = require('kue');
// const createPushNotificationsJobs = require('./8-job.js'); 

import createPushNotificationsJobs from './8-job.js';

// const queue = kue.createQueue();
const queue = kue.createQueue({
    redis: {
        port: 6379,
        host: '127.0.0.1',
    },
});
// queue.testMode.enter();

describe('createPushNotificationsJobs', function(queue) {
    

    before(function() {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    after(function() {
        queue.testMode.clear();
        queue.testMode.exit();
    });
});

it('should create jobs in the queue for valid input', function() {
    const jobs = [/* array of valid jobs */];
    createPushNotificationsJobs(jobs, queue);

    // Assert that jobs are correctly created in the queue
    // Use queue.testMode.jobs to check which jobs are in the queue
    expect(queue.testMode.jobs.length).to.equal(jobs.length);
});

it('should throw an error for invalid input', function() {
    const invalidInput = 'not an array';
    expect(() => createPushNotificationsJobs(invalidInput, queue)).to.throw(Error);
});


it('should throw an error if the queue argument is missing', function() {
    const jobs = [{ id: 1, type: 'email', data: { to: 'user@example.com' } }];
    expect(() => createPushNotificationsJobs(jobs)).to.throw('Queue is required');
});




it('should handle an empty job array without creating jobs', function() {
    const emptyJobs = [];
    createPushNotificationsJobs(emptyJobs, queue);

    expect(queue.testMode.jobs.length).to.equal(0);
});



it('should handle exceptions when queue creation fails', function() {
    const jobs = [{ id: 1, type: 'email', data: { to: 'user@example.com' } }];
    const faultyQueue = {
        create: () => { throw new Error('Failed to create queue'); }
    };

    expect(() => createPushNotificationsJobs(jobs, faultyQueue)).to.throw('Failed to create queue');
});