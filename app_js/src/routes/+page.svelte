<script>
	import { onDestroy, onMount } from 'svelte';
	import moment from 'moment-timezone';

	/**
	 * @type {string }
	 */
	let currentTime = moment().format('HH:mm:ss');
	/**
	 * @type {NodeJS.Timeout }
	 */
	let interval;

	onMount(() => {
		interval = setInterval(() => {
			currentTime = moment().tz('Europe/Moscow').format('HH:mm:ss');
		}, 1000);
	});

	onDestroy(() => {
		clearInterval(interval);
	});
</script>

<h1>Current Time in Moscow (Updated every second)</h1>
<p>{currentTime}</p>
