  Module["mmh"] = function() {
    if (ENVIRONMENT_IS_NODE) {
      FS.mkdir('/output'); 
      FS.mount(NODEFS, {
        root: 'D:/git/largeimports/build/'
      }, '/output');
    } else {
      FS.createPreloadedFile('/output', 'side.wasm', "http://localhost:8080/side.wasm", true, true);
    }
      
    var sideExists = FS.analyzePath("/output/side.wasm").exists;
    console.log("mmh sideExists:%d" + sideExists);
    loadDynamicLibrary("/output/side.wasm", {global: true, nodelete: true, fs:FS});
  }

var postTestMessage = function(message)  {
      console.log('msg:' + message);
  }