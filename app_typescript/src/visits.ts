export async function preload() {
    const response = await fetch('/visits');
    const { visits } = await response.json();
    return { visits };
  }
