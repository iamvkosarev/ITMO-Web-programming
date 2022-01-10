const gulp = require("gulp");
const browserSync = require("browser-sync").create();

gulp.task("hello", function(callback){
    console.log("Hello there!");
    callback();
});

gulp.task("bye", function(callback){
    console.log("Goodbye!");
    callback();
});


gulp.task("turn_on_lightsaber", function(callback){
    console.log("*Turning on the lightsaber*");
    callback();
});


gulp.task("series", gulp.series("hello", "bye"));


gulp.task("parallel", gulp.parallel("hello", "turn_on_lightsaber"));

gulp.task("server", function(){
    browserSync.init({
        server:{
            baseDir: "./src/",
            index: 'index.html'
        }
    })
});

gulp.task("watch", function(){
    gulp.watch("./src/*.html", gulp.parallel(browserSync.reload));
});

gulp.task("default", gulp.parallel("server","watch" ));