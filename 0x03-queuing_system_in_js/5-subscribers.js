import { createClient } from 'redis';

const client = createClient();

// connects to the server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected too the server: ${error}`);
});

// subscribe to 'holberton school channel
client.subscribe('holberton school channel');

// listen on channel and print out messages received
client.on('message', (channel, message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.end(true);
  }
});
