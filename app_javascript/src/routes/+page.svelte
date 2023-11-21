<script>
	let date = new Date();
	$: time = date.toLocaleTimeString();

	import { onMount } from 'svelte';
	import { counter } from './stores.js';

	onMount(() => {
		counter.update(n => n + 1);
	});
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<main>
	<h1>Moscow Time</h1>
	<h3>
		Current time in Moscow is {time}
	</h3>
</main>



