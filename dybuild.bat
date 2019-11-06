emcc -o build\index.js main.cpp --source-map-base http://localhost:8080/ -Oz -std=c++14 -s MAIN_MODULE=2 --pre-js preload.js -s ALLOW_MEMORY_GROWTH=1 -s INCLUDE_FULL_LIBRARY=1 -s EXPORT_ALL=1 && emcc side.cpp -Oz -o build\side.js -s SIDE_MODULE=2 -s FORCE_FILESYSTEM=1 -s WASM=1  -s DISABLE_EXCEPTION_CATCHING=0 -s ALLOW_MEMORY_GROWTH=1 -std=c++14 --source-map-base http://localhost:8080/


