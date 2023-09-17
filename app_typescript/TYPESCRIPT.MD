# Typescript Web Application Development - Daniil Okrug

## Framework choosing:

- The Web application uses the NextJS framework.
- TypeScript Support: Next.js has built-in TypeScript support, making it easier to catch type-related errors during development and providing better code completion and documentation.
- Automatic Code Splitting: Next.js automatically splits your JavaScript code into smaller bundles, which are loaded on-demand as users navigate your site. This reduces the initial page load size and improves performance.
- Next.js allows you to render pages on the server, which improves initial page load times and SEO performance. This means that the server sends fully rendered HTML to the client, reducing the time it takes for the page to become interactive.
- Next.js can automatically optimize your application by pre-fetching data, optimizing images, and other performance enhancements.

## Best practices:

- TypeScript: If you're using TypeScript, take advantage of TypeScript's static type checking to catch errors early in the development process. Use TypeScript interfaces or types to define prop types.
- Code Splitting: Break your code into smaller modules and use dynamic imports for components or libraries that are not needed on the initial page load. This reduces the initial bundle size.
- File-Based Routing: Leverage Next.js's file-based routing system. Create pages in the "pages" directory to define your routes, and let Next.js handle the routing automatically.
