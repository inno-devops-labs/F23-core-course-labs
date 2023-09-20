// logger.js
const log = (message, level = 'info') => {
    switch (level) {
      case 'error':
        console.error(message);
        break;
      case 'warn':
        console.warn(message);
        break;
      case 'info':
      default:
        console.log(message);
        break;
    }
  };
  
  export default log;
  