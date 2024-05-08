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


const setNewSchool = function(schoolName, value){
    client.set(schoolName, value, (err, reply)=>{
        if  (!err) {
            redis.print('Reply:' +  reply);
            // console.log('Set key:', reply)
        }
    });
};

const displaySchoolValue = function(schoolName){
    client.get(schoolName, (err, reply) => {
        if (!err) {
            console.log(reply);
        }
    });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');    