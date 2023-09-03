import React from 'react';

function RefreshButton() {
  return <button onClick={() => window.location.reload()}>Refresh</button>;
}

export default RefreshButton;
