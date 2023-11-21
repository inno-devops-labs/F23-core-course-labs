<script>
	import { counter } from '../stores.js';
</script>

<svelte:head>
	<title>Visits</title>
	<meta name="description" content="number of visits of demo app" />
</svelte:head>

<main>
	<h1>Visits of Time Check</h1>
	<h3>Number of visits: { $counter } </h3>
</main>

