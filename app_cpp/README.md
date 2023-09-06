# Description
Display moscow time

# Build and run
    1. conan install . --output-folder=${BUILD_DIR} --build=missing
    2. cmake -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -B ${BUILD_DIR}
    3. cmake --build ${BUILD_DIR}
    4. Run 'TestCmakeDemo' from ${BUILD_DIR}