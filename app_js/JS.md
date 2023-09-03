## Framework
I've chosen **React** JS framework (library actually) since it's the the most popular one, and I wanted to study it for my professional purposes (Continuous Learning and Improvement)  

## Best Practices

1. **Modularity and Componentization**: 
   - Components are modular with specific roles, promoting reuse, organization, and maintainability.

2. **State Management**: 
   - Utilizing `useState` and `useEffect` hooks for cleaner, more readable, and centralized state management.

3. **Error Handling**: 
   - Effective use of `try-catch` blocks during API calls to handle potential errors and prevent app crashes.

4. **Logging**:
   - Implementation of a dedicated logging utility with varying log levels ensures structured debugging and monitoring.

5. **Use of External APIs**:
   - Leveraging CoinGecko's public API for reliable cryptocurrency data.

6. **Client-Side Rendering**:
   - Ensuring faster interactivity by utilizing client-side rendering.

## Explain how you followed coding standards, implemented testing, and ensured code quality

### 1. **Coding Standards**:
   
- **Consistency**: Adopted a uniform naming convention, with capitalized component names (`CryptoPrice`, `RefreshButton`) and camelCase for variable/functions.
- **Comments and Documentation**: Added meaningful comments to complex code sections for clarity.
- **Separation of Concerns**: Organized the codebase by separating different functionalities, such as API calls, state management, and UI rendering.

### 2. **Testing**:

- **Manual Testing**: The application was run manually to ensure that it behaves as expected, especially after code changes or additions.
- **Error Handling**: The presence of a `try-catch` block in the `fetchData` function ensures that the application can handle unexpected errors gracefully and provides a basis for future testing.

### 3. **Code Quality**:

- **Logging**: Proper logging is incorporated to aid in monitoring and debugging. This contributes to code quality by making issues transparent and traceable.
- **Documentation**: Proper inline documentation and docstrings were emphasized to make the code more maintainable and understandable.