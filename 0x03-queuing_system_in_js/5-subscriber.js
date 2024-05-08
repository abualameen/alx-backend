import redis from 'redis';

const client = redis.createClient({
    host: 'localhost',
    port: 6379,
});
client.on('connect', ()=> {
    console.log('Redis client connected to the server');
});

client.on('error', (err)=> {
    console.error('Redis client not connected to the server:', err);
});
const chanName = "holberton school channel";
client.subscribe(chanName);

client.on('message', (channel, message) => {
    if (message === "KILL_SERVER") {
        console.log(message);
        client.unsubscribe(chanName);
        process.exit();
    }
    console.log(message);
});



client.on('error', (err) => {
    console.error('Error occured:', err);
})