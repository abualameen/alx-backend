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
const util = require('util')
const getAsync = util.promisify(client.get).bind(client);
const setAsync = util.promisify(client.set).bind(client);

const setNewSchool = async function(schoolName, value){
    try {
        const val = await setAsync(schoolName, value)
        redis.print('Reply:' +  val);
    }catch (err) {
        console.error('Error:', err);
    }
};

const displaySchoolValue = async function(schoolName){
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    }catch (err) {
        console.error('Error:', err);
    }

};


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');