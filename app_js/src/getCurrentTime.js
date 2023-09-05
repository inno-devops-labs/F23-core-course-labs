export function getCurrentTime() {
    const moscowTime = new Date().toLocaleTimeString('en-US', { timeZone: 'Europe/Moscow' });
    return moscowTime;
  }