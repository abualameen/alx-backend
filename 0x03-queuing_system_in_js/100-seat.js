const express = require('express');
const { promisify } = require('util');
const redis = require('redis');
const kue = require('kue');

const app = express();
const port = 1245;

// Redis client
const client = redis.createClient();

// Promisify Redis functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Reserve a seat in Redis
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

// Get the current available seats count from Redis
const getCurrentAvailableSeats = async () => {
  const seats = await getAsync('available_seats');
  return parseInt(seats) || 0;
};

// Initialize available seats to 50 and reservationEnabled to true
reserveSeat(50);
let reservationEnabled = true;

// Create Kue queue
const queue = kue.createQueue();

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

// Route to process the queue and reserve seats
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Process the queue asynchronously
  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats <= 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      await reserveSeat(availableSeats - 1);
      if (availableSeats - 1 === 0) {
        reservationEnabled = false;
      }
      done();
    }
  });
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app; // Export the app for testing purposes
