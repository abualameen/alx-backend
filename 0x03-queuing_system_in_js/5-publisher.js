import redis from 'redis';

const client = redis.createClient({
    host: 'localhost',
    port: 6379,
});
client.on('connect', ()=> {
    console.log('Redis client connected to the server');
});

const chanName = "holberton school channel";
const publishMessage = function(message, time) {
    setTimeout(function() {
        console.log( "About to send MESSAGE", message);
        
    }, time);
    client.publish(chanName, message);
    
};
client.on('error', (err)=> {
    console.error('Redis client not connected to the server:', err);
});


publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
