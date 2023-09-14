# Best Practices implemented

- **Caching**: `actions/setup-python` caching is used to speed up builds
- **Deploy on success**: Docker push is triggered only on successful tests
- **Artifacts**: They are used to store test results
- **Trigger on changes**: Pipeline is triggered only on changes in `app_python` folder