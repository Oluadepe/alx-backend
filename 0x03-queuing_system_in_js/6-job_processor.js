import { createQueue } from 'kue';

const queue = createQueue();

function sendNotificationMessage(phoneNumber, message) {
  console.log(`sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('push_notification_code', (job, done) => {
  sendNotificationMessage(job.data.phoneNumber, job.data.message);
  done();
});
