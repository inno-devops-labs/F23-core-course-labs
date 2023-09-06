# JavaScript.md

## Justification for Using Svelte

If you see commits, firstly i developed it on Vue.js, but decided to redo it fully on svelte. The reasons are:

- It setups automatically testing packages, linting and other stuff
- It still allows to use DRY principle in html - you can have templates and reuse them like in Vue
- We actually studied it in Innopolis in Frontend elective course
- THE TESTS WORK. FINALLY. Installing test and setuping other frameworks are so painful. I spend 3 hours integrating tests, as it just didn't work with Vue. Node Js and React were much harder to setup. Svelte took only half an hour.

## Implementation of Best Practices and Coding Standards

- **Gitignore**: The same: I've added a gitignore file to ignore the virtual environment and the cache. Used default Vue gitignore for it.
- **Tests**: Created some unit tests so you could check if application works.
- **Linter**: Checked the quality of code by `eslint` linter and markdown linter for vscode.
- **Code**: added types for some variables, as js can be unpredictable without them

## Testing

To run tests, run the following command:

> `npm run test`

They have simple tests: is the site even loaded, and if the displayed time is correct.
