/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./website/static/css/main.scss":
/*!**************************************!*\
  !*** ./website/static/css/main.scss ***!
  \**************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("// removed by extract-text-webpack-plugin\n\n//# sourceURL=webpack:///./website/static/css/main.scss?");

/***/ }),

/***/ "./website/static/js/index.js":
/*!************************************!*\
  !*** ./website/static/js/index.js ***!
  \************************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _utils_Router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./utils/Router */ \"./website/static/js/utils/Router.js\");\n/* harmony import */ var _routes_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./routes/common */ \"./website/static/js/routes/common.js\");\n// import external dependencies\n// import 'popper.js'\n// import 'imports-loader?jQuery=jquery!bootstrap'\n\n// import local dependencies\n\n\n\n\n/** Populate Router instance with DOM routes */\nconst routes = new _utils_Router__WEBPACK_IMPORTED_MODULE_0__[\"default\"]({\n  // All pages\n  common: _routes_common__WEBPACK_IMPORTED_MODULE_1__[\"default\"],\n\n});\n\n// Load Events\n// jQuery(document).ready(() => routes.loadEvents());\n/** Load Events */\ndocument.addEventListener(\"DOMContentLoaded\", function(){\n  // Handler when the DOM is fully loaded\n  routes.loadEvents()\n});\n\n\n\n//# sourceURL=webpack:///./website/static/js/index.js?");

/***/ }),

/***/ "./website/static/js/routes/common.js":
/*!********************************************!*\
  !*** ./website/static/js/routes/common.js ***!
  \********************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n\nclass Common {\n  constructor() {\n\n  }\n\n  init() {\n    console.log('common init');\n  }\n}\n\n/* harmony default export */ __webpack_exports__[\"default\"] = (new Common());\n\n\n//# sourceURL=webpack:///./website/static/js/routes/common.js?");

/***/ }),

/***/ "./website/static/js/utils/Router.js":
/*!*******************************************!*\
  !*** ./website/static/js/utils/Router.js ***!
  \*******************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _camelCase__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./camelCase */ \"./website/static/js/utils/camelCase.js\");\n\n\n/**\n * DOM-based Routing\n *\n * Based on {@link http://goo.gl/EUTi53|Markup-based Unobtrusive Comprehensive DOM-ready Execution} by Paul Irish\n *\n * The routing fires all common scripts, followed by the page specific scripts.\n * Add additional events for more control over timing e.g. a finalize event\n */\nclass Router {\n\n  /**\n   * Create a new Router\n   * @param {Object} routes\n   */\n  constructor(routes) {\n    this.routes = routes;\n  }\n\n  /**\n   * Fire Router events\n   * @param {string} route DOM-based route derived from body classes (`<body class=\"...\">`)\n   * @param {string} [event] Events on the route. By default, `init` and `finalize` events are called.\n   * @param {string} [arg] Any custom argument to be passed to the event.\n   */\n  fire(route, event = 'init', arg) {\n    const fire = route !== '' && this.routes[route] && typeof this.routes[route][event] === 'function';\n    if (fire) {\n      this.routes[route][event](arg);\n    }\n  }\n\n  /**\n   * Automatically load and fire Router events\n   *\n   * Events are fired in the following order:\n   *  * common init\n   *  * page-specific init\n   *  * page-specific finalize\n   *  * common finalize\n   */\n  loadEvents() {\n    // Fire common init JS\n    this.fire('common');\n\n    // Fire page-specific init JS, and then finalize JS\n    document.body.className\n      .toLowerCase()\n      .replace(/-/g, '_')\n      .split(/\\s+/)\n      .map(_camelCase__WEBPACK_IMPORTED_MODULE_0__[\"default\"])\n      .forEach((className) => {\n        this.fire(className);\n        this.fire(className, 'finalize');\n      });\n\n    // Fire common finalize JS\n    this.fire('common', 'finalize');\n  }\n}\n\n/* harmony default export */ __webpack_exports__[\"default\"] = (Router);\n\n\n//# sourceURL=webpack:///./website/static/js/utils/Router.js?");

/***/ }),

/***/ "./website/static/js/utils/camelCase.js":
/*!**********************************************!*\
  !*** ./website/static/js/utils/camelCase.js ***!
  \**********************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/**\n * the most terrible camelizer on the internet, guaranteed!\n * @param {string} str String that isn't camel-case, e.g., CAMeL_CaSEiS-harD\n * @return {string} String converted to camel-case, e.g., camelCaseIsHard\n */\n/* harmony default export */ __webpack_exports__[\"default\"] = (str => `${str.charAt(0).toLowerCase()}${str.replace(/[\\W_]/g, '|').split('|')\n  .map(part => `${part.charAt(0).toUpperCase()}${part.slice(1)}`)\n  .join('')\n  .slice(1)}`);\n\n\n//# sourceURL=webpack:///./website/static/js/utils/camelCase.js?");

/***/ }),

/***/ 0:
/*!*************************************************************************!*\
  !*** multi ./website/static/js/index.js ./website/static/css/main.scss ***!
  \*************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("__webpack_require__(/*! ./website/static/js/index.js */\"./website/static/js/index.js\");\nmodule.exports = __webpack_require__(/*! ./website/static/css/main.scss */\"./website/static/css/main.scss\");\n\n\n//# sourceURL=webpack:///multi_./website/static/js/index.js_./website/static/css/main.scss?");

/***/ })

/******/ });