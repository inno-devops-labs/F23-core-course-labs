import { get } from 'svelte/store';

let visits = 0;

export function get(request) {
  try {
    const file = Deno.readTextFileSync('./volume/visits');
    visits = parseInt(file);
  } catch (error) {
    visits = 0;
  }

  return {
    body: JSON.stringify({ visits }),
    headers: { 'Content-Type': 'application/json' },
  };
}
