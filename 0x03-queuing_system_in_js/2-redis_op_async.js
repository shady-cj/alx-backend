import { createClient } from 'redis';
import redis from 'redis';
import { promisify } from 'util';



const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log("Redis client connected to the server"));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    const value = await promisify(client.get).bind(client, schoolName);
    const getValue = await value();
    console.log(getValue);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');