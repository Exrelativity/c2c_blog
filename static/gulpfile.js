/*

=========================================================
* Simple SCSS compiler via Gulp
=========================================================

*/

var autoprefixer = require("gulp-autoprefixer");
var browserSync = require("browser-sync").create();
var cleanCss = require("gulp-clean-css");
var gulp = require("gulp");
var sass = require("gulp-sass")(require("sass"));
var wait = require("gulp-wait");
var sourcemaps = require("gulp-sourcemaps");
var rename = require("gulp-rename");
var uglify = require('gulp-uglify');
var babel = require('gulp-babel');

// Define COMMON paths

const paths = {
  src: {
    base: "./",
    css: "./css",
    scss: "./scss",
    js: "./js",
    node_modules: "./node_modules/",
    vendor: "./vendor",
  },
};

function minifyCss(){
    return gulp
    .src([paths.src.css + "/custom-boostrap.css"])
    .pipe(cleanCss())
    .pipe(rename(function (path) {
        // Updates the object in-place
        path.dirname += "";
        path.basename += "-min";
        path.extname = ".css";
      }))
    .pipe(gulp.dest(paths.src.css));
}

function scss(){
    return gulp
    .src([paths.src.scss + "/custom-boostrap.scss"])
    .pipe(wait(500))
    .pipe(sourcemaps.init())
    .pipe(sass().on("error", sass.logError))
    .pipe(
      autoprefixer({
        overrideBrowserslist: ["> 1%"],
      })
    )
    .pipe(sourcemaps.write("."))
    .pipe(gulp.dest(paths.src.css))
    .pipe(browserSync.stream());
}

function js(){
  return gulp
  .src(paths.src.js + "/custom-boostrap.js")
  .pipe(wait(500))
  .pipe(sourcemaps.init())
  .pipe(babel())
  .pipe(uglify())
  .pipe(sourcemaps.write("."))
  .pipe(rename(function (path) {
    // Updates the object in-place
    path.dirname += "";
    path.basename += "-min";
    path.extname = ".js";
  }))
  .pipe(gulp.dest(paths.src.js))
}

gulp.task('scss', () => scss());
gulp.task('minifyCss', () => minifyCss());
gulp.task('js', () => js());
//   gulp.task('minifyCss', minifyCss());
gulp.task('watch', function  () {
  // Or a composed task  
  gulp.watch(paths.src.scss, gulp.series('scss', 'minifyCss'));
  gulp.watch(paths.src.js+"/custom-boostrap.js", gulp.series('js'));
});