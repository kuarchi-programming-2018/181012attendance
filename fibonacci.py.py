﻿<!DOCTYPE html>
<!-- saved from url=(0044)http://localhost:8889/notebooks/fibonacci.py -->
<html lang="ja"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>fibonacci</title>
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./fibonacci_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./fibonacci_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    


<script type="text/javascript" src="./fibonacci_files/MathJax.js.ダウンロード" charset="utf-8"></script>

<script type="text/javascript">
// MathJax disabled, set as null to distingish from *missing* MathJax,
// where it will be undefined, and should prompt a dialog later.
window.mathjax_url = "/static/components/MathJax/MathJax.js";
</script>

<link rel="stylesheet" href="./fibonacci_files/bootstrap-tour.min.css" type="text/css">
<link rel="stylesheet" href="./fibonacci_files/codemirror.css">


    <link rel="stylesheet" href="./fibonacci_files/style.min.css" type="text/css">
    

<link rel="stylesheet" href="./fibonacci_files/override.css" type="text/css">
<link rel="stylesheet" href="http://localhost:8889/notebooks/fibonacci.py" id="kernel-css" type="text/css">


    <link rel="stylesheet" href="./fibonacci_files/custom.css" type="text/css">
    <script src="./fibonacci_files/promise.min.js.ダウンロード" type="text/javascript" charset="utf-8"></script>
    <script src="./fibonacci_files/index.js.ダウンロード" type="text/javascript"></script>
    <script src="./fibonacci_files/index.js(1).ダウンロード" type="text/javascript"></script>
    <script src="./fibonacci_files/index.js(2).ダウンロード" type="text/javascript"></script>
    <script src="./fibonacci_files/require.js.ダウンロード" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20181012152952",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/ui/minified/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./fibonacci_files/contents.js.ダウンロード"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./fibonacci_files/custom.js.ダウンロード"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="nbextensions/jupyter-js-widgets/extension" src="./fibonacci_files/extension.js.ダウンロード"></script><style type="text/css">div.MathJax_MathML {text-align: center; margin: .75em 0px; display: block!important}
.MathJax_MathML {font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
span.MathJax_MathML {display: inline!important}
.MathJax_mmlExBox {display: block!important; overflow: hidden; height: 1px; width: 60ex; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0}
[class="MJX-tex-oldstyle"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-oldstyle-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
[class="MJX-tex-caligraphic"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-caligraphic-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
@font-face /*1*/ {font-family: MathJax_Caligraphic-WEB; src: url('http://localhost:8889/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf')}
@font-face /*2*/ {font-family: MathJax_Caligraphic-WEB; font-weight: bold; src: url('http://localhost:8889/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Bold.otf')}
[mathvariant="double-struck"] {font-family: MathJax_AMS, MathJax_AMS-WEB}
[mathvariant="script"] {font-family: MathJax_Script, MathJax_Script-WEB}
[mathvariant="fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB}
[mathvariant="bold-script"] {font-family: MathJax_Script, MathJax_Caligraphic-WEB; font-weight: bold}
[mathvariant="bold-fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB; font-weight: bold}
[mathvariant="monospace"] {font-family: monospace}
[mathvariant="sans-serif"] {font-family: sans-serif}
[mathvariant="bold-sans-serif"] {font-family: sans-serif; font-weight: bold}
[mathvariant="sans-serif-italic"] {font-family: sans-serif; font-style: italic}
[mathvariant="sans-serif-bold-italic"] {font-family: sans-serif; font-style: italic; font-weight: bold}
@font-face /*3*/ {font-family: MathJax_AMS-WEB; src: url('http://localhost:8889/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_AMS-Regular.otf')}
@font-face /*4*/ {font-family: MathJax_Script-WEB; src: url('http://localhost:8889/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Script-Regular.otf')}
@font-face /*5*/ {font-family: MathJax_Fraktur-WEB; src: url('http://localhost:8889/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Regular.otf')}
@font-face /*6*/ {font-family: MathJax_Fraktur-WEB; font-weight: bold; src: url('http://localhost:8889/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Bold.otf')}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_ExBox {display: block!important; overflow: hidden; width: 1px; height: 60ex; min-height: 0; max-height: none}
.MathJax .MathJax_EmBox {display: block!important; overflow: hidden; width: 1px; height: 60em; min-height: 0; max-height: none}
.MathJax_LineBox {display: table!important}
.MathJax_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Blank; src: url('about:blank')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/* Override the correction for the prompt area in https://github.com/jupyter/notebook/blob/dd41d9fd5c4f698bd7468612d877828a7eeb0e7a/IPython/html/static/notebook/less/outputarea.less#L110 */

.jupyter-widgets-output-area div.output_subarea {
    max-width: 100%;
}

/* Work-around for the bug fixed in https://github.com/jupyter/notebook/pull/2961 */

.jupyter-widgets-output-area > .out_prompt_overlay {
    display: none;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-Widget {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}
.p-Widget.p-mod-hidden {
  display: none !important;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-CommandPalette {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-CommandPalette-search {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-CommandPalette-content {
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}
.p-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.p-CommandPalette-item {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}
.p-CommandPalette-itemIcon {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-CommandPalette-itemContent {
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
}
.p-CommandPalette-itemShortcut {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-DockPanel {
  z-index: 0;
}
.p-DockPanel-widget {
  z-index: 0;
}
.p-DockPanel-tabBar {
  z-index: 1;
}
.p-DockPanel-handle {
  z-index: 2;
}
.p-DockPanel-handle.p-mod-hidden {
  display: none !important;
}
.p-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}
.p-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}
.p-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}
.p-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  -webkit-transform: translateX(-50%);
          transform: translateX(-50%);
}
.p-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  -webkit-transform: translateY(-50%);
          transform: translateY(-50%);
}
.p-DockPanel-overlay {
  z-index: 3;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  pointer-events: none;
}
.p-DockPanel-overlay.p-mod-hidden {
  display: none !important;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}
.p-Menu-item {
  display: table-row;
}
.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed {
  display: none !important;
}
.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}
.p-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}
.p-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-MenuBar-content {
  margin: 0;
  padding: 0;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  list-style-type: none;
}
.p-MenuBar-item {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
}
.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel {
  display: inline-block;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-ScrollBar {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-ScrollBar[data-orientation='horizontal'] {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}
.p-ScrollBar[data-orientation='vertical'] {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}
.p-ScrollBar-button {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-ScrollBar-track {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  position: relative;
  overflow: hidden;
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
}
.p-ScrollBar-thumb {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  position: absolute;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-SplitPanel-child {
  z-index: 0;
}
.p-SplitPanel-handle {
  z-index: 1;
}
.p-SplitPanel-handle.p-mod-hidden {
  display: none !important;
}
.p-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle {
  cursor: ew-resize;
}
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle {
  cursor: ns-resize;
}
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  -webkit-transform: translateX(-50%);
          transform: translateX(-50%);
}
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  -webkit-transform: translateY(-50%);
          transform: translateY(-50%);
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-TabBar {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.p-TabBar[data-orientation='horizontal'] {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}
.p-TabBar[data-orientation='vertical'] {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}
.p-TabBar-content {
  margin: 0;
  padding: 0;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  list-style-type: none;
}
.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}
.p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}
.p-TabBar-tab {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  overflow: hidden;
}
.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}
.p-TabBar-tabLabel {
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}
.p-TabBar-tab.p-mod-hidden {
  display: none !important;
}
.p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}
.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  -webkit-transition: left 150ms ease;
  transition: left 150ms ease;
}
.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  -webkit-transition: top 150ms ease;
  transition: top 150ms ease;
}
.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  -webkit-transition: none;
  transition: none;
}
/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
.p-TabPanel-tabBar {
  z-index: 1;
}
.p-TabPanel-stackedPanel {
  z-index: 0;
}
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 .jupyter-widgets-disconnected::before {
    content: "\F127"; /* chain-broken */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #d9534f;
    padding: 3px;
    -ms-flex-item-align: start;
        align-self: flex-start;
}
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 /* We import all of these together in a single css file because the Webpack
loader sees only one file at a time. This allows postcss to see the variable
definitions when they are used. */

 /*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

 /*
This file is copied from the JupyterLab project to define default styling for
when the widget styling is compiled down to eliminate CSS variables. We make one
change - we comment out the font import below.
*/

 /**
 * The material design colors are adapted from google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/dist/palette.var.css
 *
 * The license for the material design color CSS variables is as follows (see
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/LICENSE)
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 Dan Le Van
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

 /*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

 /*
 * Optional monospace font for input/output prompt.
 */

 /* Commented out in ipywidgets since we don't need it. */

 /* @import url('https://fonts.googleapis.com/css?family=Roboto+Mono'); */

 /*
 * Added for compabitility with output area
 */

 :root {

  /* Borders

  The following variables, specify the visual styling of borders in JupyterLab.
   */

  /* UI Fonts

  The UI font CSS variables are used for the typography all of the JupyterLab
  user interface elements that are not directly user generated content.
  */ /* Base font size */ /* Ensures px perfect FontAwesome icons */

  /* Use these font colors against the corresponding main layout colors.
     In a light theme, these go from dark to light.
  */

  /* Use these against the brand/accent/warn/error colors.
     These will typically go from light to darker, in both a dark and light theme
   */

  /* Content Fonts

  Content font variables are used for typography of user generated content.
  */ /* Base font size */


  /* Layout

  The following are the main layout colors use in JupyterLab. In a light
  theme these would go from light to dark.
  */

  /* Brand/accent */

  /* State colors (warn, error, success, info) */

  /* Cell specific styles */
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */

  /* Notebook specific styles */

  /* Console specific styles */

  /* Toolbar specific styles */
}

 /* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 /*
 * We assume that the CSS variables in
 * https://github.com/jupyterlab/jupyterlab/blob/master/src/default-theme/variables.css
 * have been defined.
 */

 /* This file has code derived from PhosphorJS CSS files, as noted below. The license for this PhosphorJS code is:

Copyright (c) 2014-2017, PhosphorJS Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

 /*
 * The following section is derived from https://github.com/phosphorjs/phosphor/blob/23b9d075ebc5b73ab148b6ebfc20af97f85714c4/packages/widgets/style/tabbar.css 
 * We've scoped the rules so that they are consistent with exactly our code.
 */

 .jupyter-widgets.widget-tab > .p-TabBar {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

 .jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}

 .jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}

 .jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
  margin: 0;
  padding: 0;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  list-style-type: none;
}

 .jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
}

 .jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  overflow: hidden;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
  -webkit-box-flex: 0;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel {
  -webkit-box-flex: 1;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-hidden {
  display: none !important;
}

 .jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}

 .jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  -webkit-transition: left 150ms ease;
  transition: left 150ms ease;
}

 .jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  -webkit-transition: top 150ms ease;
  transition: top 150ms ease;
}

 .jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  -webkit-transition: none;
  transition: none;
}

 /* End tabbar.css */

 :root { /* margin between inline elements */

    /* From Material Design Lite */
}

 .jupyter-widgets {
    margin: 2px;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    color: black;
    overflow: visible;
}

 .jupyter-widgets.jupyter-widgets-disconnected::before {
    line-height: 28px;
    height: 28px;
}

 .jp-Output-result > .jupyter-widgets {
    margin-left: 0;
    margin-right: 0;
}

 /* vbox and hbox */

 .widget-inline-hbox {
    /* Horizontal widgets */
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
        -ms-flex-direction: row;
            flex-direction: row;
    -webkit-box-align: baseline;
        -ms-flex-align: baseline;
            align-items: baseline;
}

 .widget-inline-vbox {
    /* Vertical Widgets */
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
}

 .widget-box {
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    margin: 0;
    overflow: auto;
}

 .widget-gridbox {
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    display: grid;
    margin: 0;
    overflow: auto;
}

 .widget-hbox {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
        -ms-flex-direction: row;
            flex-direction: row;
}

 .widget-vbox {
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
}

 /* General Button Styling */

 .jupyter-button {
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 0px;
    padding-bottom: 0px;
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
    font-size: 13px;
    cursor: pointer;

    height: 28px;
    border: 0px solid;
    line-height: 28px;
    -webkit-box-shadow: none;
            box-shadow: none;

    color: rgba(0, 0, 0, .8);
    background-color: #EEEEEE;
    border-color: #E0E0E0;
    border: none;
}

 .jupyter-button i.fa {
    margin-right: 4px;
    pointer-events: none;
}

 .jupyter-button:empty:before {
    content: "\200B"; /* zero-width space */
}

 .jupyter-widgets.jupyter-button:disabled {
    opacity: 0.6;
}

 .jupyter-button i.fa.center {
    margin-right: 0;
}

 .jupyter-button:hover:enabled, .jupyter-button:focus:enabled {
    /* MD Lite 2dp shadow */
    -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14),
                0 3px 1px -2px rgba(0, 0, 0, .2),
                0 1px 5px 0 rgba(0, 0, 0, .12);
            box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14),
                0 3px 1px -2px rgba(0, 0, 0, .2),
                0 1px 5px 0 rgba(0, 0, 0, .12);
}

 .jupyter-button:active, .jupyter-button.mod-active {
    /* MD Lite 4dp shadow */
    -webkit-box-shadow: 0 4px 5px 0 rgba(0, 0, 0, .14),
                0 1px 10px 0 rgba(0, 0, 0, .12),
                0 2px 4px -1px rgba(0, 0, 0, .2);
            box-shadow: 0 4px 5px 0 rgba(0, 0, 0, .14),
                0 1px 10px 0 rgba(0, 0, 0, .12),
                0 2px 4px -1px rgba(0, 0, 0, .2);
    color: rgba(0, 0, 0, .8);
    background-color: #BDBDBD;
}

 .jupyter-button:focus:enabled {
    outline: 1px solid #64B5F6;
}

 /* Button "Primary" Styling */

 .jupyter-button.mod-primary {
    color: rgba(255, 255, 255, 1.0);
    background-color: #2196F3;
}

 .jupyter-button.mod-primary.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #1976D2;
}

 .jupyter-button.mod-primary:active {
    color: rgba(255, 255, 255, 1);
    background-color: #1976D2;
}

 /* Button "Success" Styling */

 .jupyter-button.mod-success {
    color: rgba(255, 255, 255, 1.0);
    background-color: #4CAF50;
}

 .jupyter-button.mod-success.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #388E3C;
 }

 .jupyter-button.mod-success:active {
    color: rgba(255, 255, 255, 1);
    background-color: #388E3C;
 }

 /* Button "Info" Styling */

 .jupyter-button.mod-info {
    color: rgba(255, 255, 255, 1.0);
    background-color: #00BCD4;
}

 .jupyter-button.mod-info.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #0097A7;
}

 .jupyter-button.mod-info:active {
    color: rgba(255, 255, 255, 1);
    background-color: #0097A7;
}

 /* Button "Warning" Styling */

 .jupyter-button.mod-warning {
    color: rgba(255, 255, 255, 1.0);
    background-color: #FF9800;
}

 .jupyter-button.mod-warning.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #F57C00;
}

 .jupyter-button.mod-warning:active {
    color: rgba(255, 255, 255, 1);
    background-color: #F57C00;
}

 /* Button "Danger" Styling */

 .jupyter-button.mod-danger {
    color: rgba(255, 255, 255, 1.0);
    background-color: #F44336;
}

 .jupyter-button.mod-danger.mod-active {
    color: rgba(255, 255, 255, 1);
    background-color: #D32F2F;
}

 .jupyter-button.mod-danger:active {
    color: rgba(255, 255, 255, 1);
    background-color: #D32F2F;
}

 /* Widget Button*/

 .widget-button, .widget-toggle-button {
    width: 148px;
}

 /* Widget Label Styling */

 /* Override Bootstrap label css */

 .jupyter-widgets label {
    margin-bottom: 0;
    margin-bottom: initial;
}

 .widget-label-basic {
    /* Basic Label */
    color: black;
    font-size: 13px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: 28px;
}

 .widget-label {
    /* Label */
    color: black;
    font-size: 13px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: 28px;
}

 .widget-inline-hbox .widget-label {
    /* Horizontal Widget Label */
    color: black;
    text-align: right;
    margin-right: 8px;
    width: 80px;
    -ms-flex-negative: 0;
        flex-shrink: 0;
}

 .widget-inline-vbox .widget-label {
    /* Vertical Widget Label */
    color: black;
    text-align: center;
    line-height: 28px;
}

 /* Widget Readout Styling */

 .widget-readout {
    color: black;
    font-size: 13px;
    height: 28px;
    line-height: 28px;
    overflow: hidden;
    white-space: nowrap;
    text-align: center;
}

 .widget-readout.overflow {
    /* Overflowing Readout */

    /* From Material Design Lite
        shadow-key-umbra-opacity: 0.2;
        shadow-key-penumbra-opacity: 0.14;
        shadow-ambient-shadow-opacity: 0.12;
     */
    -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .2),
                        0 3px 1px -2px rgba(0, 0, 0, .14),
                        0 1px 5px 0 rgba(0, 0, 0, .12);

    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .2),
                0 3px 1px -2px rgba(0, 0, 0, .14),
                0 1px 5px 0 rgba(0, 0, 0, .12);
}

 .widget-inline-hbox .widget-readout {
    /* Horizontal Readout */
    text-align: center;
    max-width: 148px;
    min-width: 72px;
    margin-left: 4px;
}

 .widget-inline-vbox .widget-readout {
    /* Vertical Readout */
    margin-top: 4px;
    /* as wide as the widget */
    width: inherit;
}

 /* Widget Checkbox Styling */

 .widget-checkbox {
    width: 300px;
    height: 28px;
    line-height: 28px;
}

 .widget-checkbox input[type="checkbox"] {
    margin: 0px 8px 0px 0px;
    line-height: 28px;
    font-size: large;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    -ms-flex-negative: 0;
        flex-shrink: 0;
    -ms-flex-item-align: center;
        align-self: center;
}

 /* Widget Valid Styling */

 .widget-valid {
    height: 28px;
    line-height: 28px;
    width: 148px;
    font-size: 13px;
}

 .widget-valid i:before {
    line-height: 28px;
    margin-right: 4px;
    margin-left: 4px;

    /* from the fa class in FontAwesome: https://github.com/FortAwesome/Font-Awesome/blob/49100c7c3a7b58d50baa71efef11af41a66b03d3/css/font-awesome.css#L14 */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

 .widget-valid.mod-valid i:before {
    content: "\F00C";
    color: green;
}

 .widget-valid.mod-invalid i:before {
    content: "\F00D";
    color: red;
}

 .widget-valid.mod-valid .widget-valid-readout {
    display: none;
}

 /* Widget Text and TextArea Stying */

 .widget-textarea, .widget-text {
    width: 300px;
}

 .widget-text input[type="text"], .widget-text input[type="number"]{
    height: 28px;
    line-height: 28px;
}

 .widget-text input[type="text"]:disabled, .widget-text input[type="number"]:disabled, .widget-textarea textarea:disabled {
    opacity: 0.6;
}

 .widget-text input[type="text"], .widget-text input[type="number"], .widget-textarea textarea {
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    border: 1px solid #9E9E9E;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    font-size: 13px;
    padding: 4px 8px;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    -ms-flex-negative: 1;
        flex-shrink: 1;
    outline: none !important;
}

 .widget-textarea textarea {
    height: inherit;
    width: inherit;
}

 .widget-text input:focus, .widget-textarea textarea:focus {
    border-color: #64B5F6;
}

 /* Widget Slider */

 .widget-slider .ui-slider {
    /* Slider Track */
    border: 1px solid #BDBDBD;
    background: #BDBDBD;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    position: relative;
    border-radius: 0px;
}

 .widget-slider .ui-slider .ui-slider-handle {
    /* Slider Handle */
    outline: none !important; /* focused slider handles are colored - see below */
    position: absolute;
    background-color: white;
    border: 1px solid #9E9E9E;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    z-index: 1;
    background-image: none; /* Override jquery-ui */
}

 /* Override jquery-ui */

 .widget-slider .ui-slider .ui-slider-handle:hover, .widget-slider .ui-slider .ui-slider-handle:focus {
    background-color: #2196F3;
    border: 1px solid #2196F3;
}

 .widget-slider .ui-slider .ui-slider-handle:active {
    background-color: #2196F3;
    border-color: #2196F3;
    z-index: 2;
    -webkit-transform: scale(1.2);
            transform: scale(1.2);
}

 .widget-slider  .ui-slider .ui-slider-range {
    /* Interval between the two specified value of a double slider */
    position: absolute;
    background: #2196F3;
    z-index: 0;
}

 /* Shapes of Slider Handles */

 .widget-hslider .ui-slider .ui-slider-handle {
    width: 16px;
    height: 16px;
    margin-top: -7px;
    margin-left: -7px;
    border-radius: 50%;
    top: 0;
}

 .widget-vslider .ui-slider .ui-slider-handle {
    width: 16px;
    height: 16px;
    margin-bottom: -7px;
    margin-left: -7px;
    border-radius: 50%;
    left: 0;
}

 .widget-hslider .ui-slider .ui-slider-range {
    height: 8px;
    margin-top: -3px;
}

 .widget-vslider .ui-slider .ui-slider-range {
    width: 8px;
    margin-left: -3px;
}

 /* Horizontal Slider */

 .widget-hslider {
    width: 300px;
    height: 28px;
    line-height: 28px;

    /* Override the align-items baseline. This way, the description and readout
    still seem to align their baseline properly, and we don't have to have
    align-self: stretch in the .slider-container. */
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
}

 .widgets-slider .slider-container {
    overflow: visible;
}

 .widget-hslider .slider-container {
    height: 28px;
    margin-left: 6px;
    margin-right: 6px;
    -webkit-box-flex: 1;
        -ms-flex: 1 1 148px;
            flex: 1 1 148px;
}

 .widget-hslider .ui-slider {
    /* Inner, invisible slide div */
    height: 4px;
    margin-top: 12px;
    width: 100%;
}

 /* Vertical Slider */

 .widget-vbox .widget-label {
    height: 28px;
    line-height: 28px;
}

 .widget-vslider {
    /* Vertical Slider */
    height: 200px;
    width: 72px;
}

 .widget-vslider .slider-container {
    -webkit-box-flex: 1;
        -ms-flex: 1 1 148px;
            flex: 1 1 148px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 6px;
    margin-top: 6px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
}

 .widget-vslider .ui-slider-vertical {
    /* Inner, invisible slide div */
    width: 4px;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    margin-left: auto;
    margin-right: auto;
}

 /* Widget Progress Styling */

 .progress-bar {
    -webkit-transition: none;
    transition: none;
}

 .progress-bar {
    height: 28px;
}

 .progress-bar {
    background-color: #2196F3;
}

 .progress-bar-success {
    background-color: #4CAF50;
}

 .progress-bar-info {
    background-color: #00BCD4;
}

 .progress-bar-warning {
    background-color: #FF9800;
}

 .progress-bar-danger {
    background-color: #F44336;
}

 .progress {
    background-color: #EEEEEE;
    border: none;
    -webkit-box-shadow: none;
            box-shadow: none;
}

 /* Horisontal Progress */

 .widget-hprogress {
    /* Progress Bar */
    height: 28px;
    line-height: 28px;
    width: 300px;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;

}

 .widget-hprogress .progress {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    margin-top: 4px;
    margin-bottom: 4px;
    -ms-flex-item-align: stretch;
        align-self: stretch;
    /* Override bootstrap style */
    height: auto;
    height: initial;
}

 /* Vertical Progress */

 .widget-vprogress {
    height: 200px;
    width: 72px;
}

 .widget-vprogress .progress {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    width: 20px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0;
}

 /* Select Widget Styling */

 .widget-dropdown {
    height: 28px;
    width: 300px;
    line-height: 28px;
}

 .widget-dropdown > select {
    padding-right: 20px;
    border: 1px solid #9E9E9E;
    border-radius: 0;
    height: inherit;
    -webkit-box-flex: 1;
        -ms-flex: 1 1 148px;
            flex: 1 1 148px;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    outline: none !important;
    -webkit-box-shadow: none;
            box-shadow: none;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    font-size: 13px;
    vertical-align: top;
    padding-left: 8px;
	appearance: none;
	-webkit-appearance: none;
	-moz-appearance: none;
    background-repeat: no-repeat;
	background-size: 20px;
	background-position: right center;
    background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCAxOCAxOCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTggMTg7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDpub25lO30KPC9zdHlsZT4KPHBhdGggZD0iTTUuMiw1LjlMOSw5LjdsMy44LTMuOGwxLjIsMS4ybC00LjksNWwtNC45LTVMNS4yLDUuOXoiLz4KPHBhdGggY2xhc3M9InN0MCIgZD0iTTAtMC42aDE4djE4SDBWLTAuNnoiLz4KPC9zdmc+Cg");
}

 .widget-dropdown > select:focus {
    border-color: #64B5F6;
}

 .widget-dropdown > select:disabled {
    opacity: 0.6;
}

 /* To disable the dotted border in Firefox around select controls.
   See http://stackoverflow.com/a/18853002 */

 .widget-dropdown > select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 #000;
}

 /* Select and SelectMultiple */

 .widget-select {
    width: 300px;
    line-height: 28px;

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    -webkit-box-align: start;
        -ms-flex-align: start;
            align-items: flex-start;
}

 .widget-select > select {
    border: 1px solid #9E9E9E;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    font-size: 13px;
    -webkit-box-flex: 1;
        -ms-flex: 1 1 148px;
            flex: 1 1 148px;
    outline: none !important;
    overflow: auto;
    height: inherit;

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    padding-top: 5px;
}

 .widget-select > select:focus {
    border-color: #64B5F6;
}

 .wiget-select > select > option {
    padding-left: 4px;
    line-height: 28px;
    /* line-height doesn't work on some browsers for select options */
    padding-top: calc(28px - var(--jp-widgets-font-size) / 2);
    padding-bottom: calc(28px - var(--jp-widgets-font-size) / 2);
}

 /* Toggle Buttons Styling */

 .widget-toggle-buttons {
    line-height: 28px;
}

 .widget-toggle-buttons .widget-toggle-button {
    margin-left: 2px;
    margin-right: 2px;
}

 .widget-toggle-buttons .jupyter-button:disabled {
    opacity: 0.6;
}

 /* Radio Buttons Styling */

 .widget-radio {
    width: 300px;
    line-height: 28px;
}

 .widget-radio-box {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: stretch;
        -ms-flex-align: stretch;
            align-items: stretch;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    margin-bottom: 8px;
}

 .widget-radio-box label {
    height: 20px;
    line-height: 20px;
    font-size: 13px;
}

 .widget-radio-box input {
    height: 20px;
    line-height: 20px;
    margin: 0 8px 0 1px;
    float: left;
}

 /* Color Picker Styling */

 .widget-colorpicker {
    width: 300px;
    height: 28px;
    line-height: 28px;
}

 .widget-colorpicker > .widget-colorpicker-input {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    -ms-flex-negative: 1;
        flex-shrink: 1;
    min-width: 72px;
}

 .widget-colorpicker input[type="color"] {
    width: 28px;
    height: 28px;
    padding: 0 2px; /* make the color square actually square on Chrome on OS X */
    background: white;
    color: rgba(0, 0, 0, .8);
    border: 1px solid #9E9E9E;
    border-left: none;
    -webkit-box-flex: 0;
        -ms-flex-positive: 0;
            flex-grow: 0;
    -ms-flex-negative: 0;
        flex-shrink: 0;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    -ms-flex-item-align: stretch;
        align-self: stretch;
    outline: none !important;
}

 .widget-colorpicker.concise input[type="color"] {
    border-left: 1px solid #9E9E9E;
}

 .widget-colorpicker input[type="color"]:focus, .widget-colorpicker input[type="text"]:focus {
    border-color: #64B5F6;
}

 .widget-colorpicker input[type="text"] {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    outline: none !important;
    height: 28px;
    line-height: 28px;
    background: white;
    color: rgba(0, 0, 0, .8);
    border: 1px solid #9E9E9E;
    font-size: 13px;
    padding: 4px 8px;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    -ms-flex-negative: 1;
        flex-shrink: 1;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
}

 .widget-colorpicker input[type="text"]:disabled {
    opacity: 0.6;
}

 /* Date Picker Styling */

 .widget-datepicker {
    width: 300px;
    height: 28px;
    line-height: 28px;
}

 .widget-datepicker input[type="date"] {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    -ms-flex-negative: 1;
        flex-shrink: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    outline: none !important;
    height: 28px;
    border: 1px solid #9E9E9E;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    font-size: 13px;
    padding: 4px 8px;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
}

 .widget-datepicker input[type="date"]:focus {
    border-color: #64B5F6;
}

 .widget-datepicker input[type="date"]:invalid {
    border-color: #FF9800;
}

 .widget-datepicker input[type="date"]:disabled {
    opacity: 0.6;
}

 /* Play Widget */

 .widget-play {
    width: 148px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: stretch;
        -ms-flex-align: stretch;
            align-items: stretch;
}

 .widget-play .jupyter-button {
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    height: auto;
}

 .widget-play .jupyter-button:disabled {
    opacity: 0.6;
}

 /* Tab Widget */

 .jupyter-widgets.widget-tab {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
}

 .jupyter-widgets.widget-tab > .p-TabBar {
    /* Necessary so that a tab can be shifted down to overlay the border of the box below. */
    overflow-x: visible;
    overflow-y: visible;
}

 .jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
    /* Make sure that the tab grows from bottom up */
    -webkit-box-align: end;
        -ms-flex-align: end;
            align-items: flex-end;
    min-width: 0;
    min-height: 0;
}

 .jupyter-widgets.widget-tab > .widget-tab-contents {
    width: 100%;
    -webkit-box-sizing: border-box;
            box-sizing: border-box;
    margin: 0;
    background: white;
    color: rgba(0, 0, 0, .8);
    border: 1px solid #9E9E9E;
    padding: 15px;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    overflow: auto;
}

 .jupyter-widgets.widget-tab > .p-TabBar {
    font: 13px Helvetica, Arial, sans-serif;
    min-height: 25px;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
    -webkit-box-flex: 0;
        -ms-flex: 0 1 144px;
            flex: 0 1 144px;
    min-width: 35px;
    min-height: 25px;
    line-height: 24px;
    margin-left: -1px;
    padding: 0px 10px;
    background: #EEEEEE;
    color: rgba(0, 0, 0, .5);
    border: 1px solid #9E9E9E;
    border-bottom: none;
    position: relative;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current {
    color: rgba(0, 0, 0, 1.0);
    /* We want the background to match the tab content background */
    background: white;
    min-height: 26px;
    -webkit-transform: translateY(1px);
            transform: translateY(1px);
    overflow: visible;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current:before {
    position: absolute;
    top: -1px;
    left: -1px;
    content: '';
    height: 2px;
    width: calc(100% + 2px);
    background: #2196F3;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:first-child {
    margin-left: 0;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:hover:not(.p-mod-current) {
    background: white;
    color: rgba(0, 0, 0, .8);
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon {
    margin-left: 4px;
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon:before {
    font-family: FontAwesome;
    content: '\F00D'; /* close */
}

 .jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
    line-height: 24px;
}

 /* Accordion Widget */

 .p-Collapse {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: stretch;
        -ms-flex-align: stretch;
            align-items: stretch;
}

 .p-Collapse-header {
    padding: 4px;
    cursor: pointer;
    color: rgba(0, 0, 0, .5);
    background-color: #EEEEEE;
    border: 1px solid #9E9E9E;
    padding: 10px 15px;
    font-weight: bold;
}

 .p-Collapse-header:hover {
    background-color: white;
    color: rgba(0, 0, 0, .8);
}

 .p-Collapse-open > .p-Collapse-header {
    background-color: white;
    color: rgba(0, 0, 0, 1.0);
    cursor: default;
    border-bottom: none;
}

 .p-Collapse .p-Collapse-header::before {
    content: '\F0DA\A0';  /* caret-right, non-breaking space */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

 .p-Collapse-open > .p-Collapse-header::before {
    content: '\F0D7\A0'; /* caret-down, non-breaking space */
}

 .p-Collapse-contents {
    padding: 15px;
    background-color: white;
    color: rgba(0, 0, 0, .8);
    border-left: 1px solid #9E9E9E;
    border-right: 1px solid #9E9E9E;
    border-bottom: 1px solid #9E9E9E;
    overflow: auto;
}

 .p-Accordion {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-align: stretch;
        -ms-flex-align: stretch;
            align-items: stretch;
}

 .p-Accordion .p-Collapse {
    margin-bottom: 0;
}

 .p-Accordion .p-Collapse + .p-Collapse {
    margin-top: 4px;
}

 /* HTML widget */

 .widget-html, .widget-htmlmath {
    font-size: 13px;
}

 .widget-html > .widget-html-content, .widget-htmlmath > .widget-html-content {
    /* Fill out the area in the HTML widget */
    -ms-flex-item-align: stretch;
        align-self: stretch;
    -webkit-box-flex: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    -ms-flex-negative: 1;
        flex-shrink: 1;
    /* Makes sure the baseline is still aligned with other elements */
    line-height: 28px;
    /* Make it possible to have absolutely-positioned elements in the html */
    position: relative;
}
</style><link id="favicon" type="image/x-icon" rel="shortcut icon" href="http://localhost:8889/static/base/images/favicon-notebook.ico"></head>

<body class="notebook_app edit_mode" data-jupyter-api-token="d47556ca6a96f9bfdcec7dc5d547dadd9c413fc30f5e536c" data-base-url="/" data-ws-url="" data-notebook-name="Untitled1.ipynb" data-notebook-path="Untitled1.ipynb" dir="ltr"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div>

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8889/tree?token=d47556ca6a96f9bfdcec7dc5d547dadd9c413fc30f5e536c" title="dashboard">
      <img src="./fibonacci_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  


<span id="save_widget" class="save_widget">
    <span id="notebook_name" class="filename">fibonacci</span>
    <span class="checkpoint_status" title="2018年10月12日 15:30 金曜日">Last Checkpoint: 1時間前</span>
    <span class="autosave_status">(autosaved)</span>
</span>

<span id="kernel_logo_widget">
  
  <img class="current_kernel_logo" alt="Current Kernel Logo" src="./fibonacci_files/logo-64x64.png" title="Python 3" style="display: inline;">
  
</span>


  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
<div id="menubar-container" class="container">
<div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
            <button type="button" class="btn btn-default navbar-btn navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <i class="fa fa-bars"></i>
              <span class="navbar-text">Menu</span>
            </button>
            <p id="kernel_indicator" class="navbar-text indicator_area">
              <span class="kernel_indicator_name">Python 3</span>
              <i id="kernel_indicator_icon" class="kernel_idle_icon" title="Kernel Idle"></i>
            </p>
            <i id="readonly-indicator" class="navbar-text" title="This notebook is read-only" style="display: none;">
                <span class="fa-stack">
                    <i class="fa fa-save fa-stack-1x"></i>
                    <i class="fa fa-ban fa-stack-2x text-danger"></i>
                </span>
            </i>
            <i id="modal_indicator" class="navbar-text modal_indicator" title="Edit Mode"></i>
            <span id="notification_area"><div id="notification_kernel" class="notification_widget btn btn-xs navbar-btn undefined info" style="display: none;"><span></span></div><div id="notification_notebook" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div><div id="notification_trusted" class="notification_widget btn btn-xs navbar-btn" style="cursor: help;" disabled="disabled"><span title="Javascript enabled for notebook display">Trusted</span></div><div id="notification_widgets" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></span>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown"><a href="http://localhost:8889/notebooks/fibonacci.py#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">File</a>
                    <ul id="file_menu" class="dropdown-menu">
                        <li id="new_notebook" class="dropdown-submenu">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">New Notebook</a>
                            <ul class="dropdown-menu" id="menu-new-notebook-submenu"><li id="new-notebook-submenu-python3"><a href="http://localhost:8889/notebooks/fibonacci.py#">Python 3</a></li></ul>
                        </li>
                        <li id="open_notebook" title="Opens a new window with the Dashboard view">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Open...</a></li>
                        <!-- <hr/> -->
                        <li class="divider"></li>
                        <li id="copy_notebook" title="Open a copy of this notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Make a Copy...</a></li>
                        <li id="save_notebook_as" title="Save a copy of the notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Save as...</a></li>
                        <li id="rename_notebook"><a href="http://localhost:8889/notebooks/fibonacci.py#">Rename...</a></li>
                        <li id="save_checkpoint"><a href="http://localhost:8889/notebooks/fibonacci.py#">Save and Checkpoint</a></li>
                        <!-- <hr/> -->
                        <li class="divider"></li>
                        <li id="restore_checkpoint" class="dropdown-submenu"><a href="http://localhost:8889/notebooks/fibonacci.py#">Revert to Checkpoint</a>
                          <ul class="dropdown-menu"><li><a href="http://localhost:8889/notebooks/fibonacci.py#">2018年10月12日 15:30 金曜日</a></li></ul>
                        </li>
                        <li class="divider"></li>
                        <li id="print_preview"><a href="http://localhost:8889/notebooks/fibonacci.py#">Print Preview</a></li>
                        <li class="dropdown-submenu"><a href="http://localhost:8889/notebooks/fibonacci.py#">Download as</a>
                            <ul id="download_menu" class="dropdown-menu">
                                <li id="download_ipynb"><a href="http://localhost:8889/notebooks/fibonacci.py#">Notebook (.ipynb)</a></li>
                                <li id="download_script"><a href="http://localhost:8889/notebooks/fibonacci.py#">Python (.py)</a></li>
                                <li id="download_html"><a href="http://localhost:8889/notebooks/fibonacci.py#">HTML (.html)</a></li>
                                <li id="download_slides"><a href="http://localhost:8889/notebooks/fibonacci.py#">Reveal.js slides (.html)</a></li>
                                <li id="download_markdown"><a href="http://localhost:8889/notebooks/fibonacci.py#">Markdown (.md)</a></li>
                                <li id="download_rst"><a href="http://localhost:8889/notebooks/fibonacci.py#">reST (.rst)</a></li>
                                <li id="download_latex"><a href="http://localhost:8889/notebooks/fibonacci.py#">LaTeX (.tex)</a></li>
                                <li id="download_pdf"><a href="http://localhost:8889/notebooks/fibonacci.py#">PDF via LaTeX (.pdf)</a></li>
                                
                                <li id="download_asciidoc">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">asciidoc (.asciidoc)</a>
                                </li>
                                
                                <li id="download_custom">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">custom (.txt)</a>
                                </li>
                                
                                <li id="download_html">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">custom (.html)</a>
                                </li>
                                
                                <li id="download_latex">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">latex (.tex)</a>
                                </li>
                                
                                <li id="download_markdown">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">markdown (.md)</a>
                                </li>
                                
                                <li id="download_notebook">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">notebook (.ipynb)</a>
                                </li>
                                
                                <li id="download_pdf">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">pdf (.tex)</a>
                                </li>
                                
                                <li id="download_python">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">python (.py)</a>
                                </li>
                                
                                <li id="download_rst">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">rst (.rst)</a>
                                </li>
                                
                                <li id="download_script">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">custom (.txt)</a>
                                </li>
                                
                                <li id="download_slides">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">slides (.slides.html)</a>
                                </li>
                                
                            </ul>
                        </li>
                        <li class="dropdown-submenu hidden"><a href="http://localhost:8889/notebooks/fibonacci.py#">Deploy as</a>
                            <ul id="deploy_menu" class="dropdown-menu"></ul>
                        </li>
                        <li class="divider"></li>
                        <li id="trust_notebook" title="Trust the output of this notebook" class="disabled">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Trusted Notebook</a></li>
                        <li class="divider"></li>
                        <li id="close_and_halt" title="Shutdown this notebook&#39;s kernel, and close this window">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Close and Halt</a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8889/notebooks/fibonacci.py#" class="dropdown-toggle" data-toggle="dropdown">Edit</a>
                    <ul id="edit_menu" class="dropdown-menu">
                        <li id="cut_cell"><a href="http://localhost:8889/notebooks/fibonacci.py#">Cut Cells</a></li>
                        <li id="copy_cell"><a href="http://localhost:8889/notebooks/fibonacci.py#">Copy Cells</a></li>
                        <li id="paste_cell_above" class="disabled"><a href="http://localhost:8889/notebooks/fibonacci.py#">Paste Cells Above</a></li>
                        <li id="paste_cell_below" class="disabled"><a href="http://localhost:8889/notebooks/fibonacci.py#">Paste Cells Below</a></li>
                        <li id="paste_cell_replace" class="disabled"><a href="http://localhost:8889/notebooks/fibonacci.py#">Paste Cells &amp; Replace</a></li>
                        <li id="delete_cell"><a href="http://localhost:8889/notebooks/fibonacci.py#">Delete Cells</a></li>
                        <li id="undelete_cell" class="disabled"><a href="http://localhost:8889/notebooks/fibonacci.py#">Undo Delete Cells</a></li>
                        <li class="divider"></li>
                        <li id="split_cell"><a href="http://localhost:8889/notebooks/fibonacci.py#">Split Cell</a></li>
                        <li id="merge_cell_above"><a href="http://localhost:8889/notebooks/fibonacci.py#">Merge Cell Above</a></li>
                        <li id="merge_cell_below"><a href="http://localhost:8889/notebooks/fibonacci.py#">Merge Cell Below</a></li>
                        <li class="divider"></li>
                        <li id="move_cell_up"><a href="http://localhost:8889/notebooks/fibonacci.py#">Move Cell Up</a></li>
                        <li id="move_cell_down"><a href="http://localhost:8889/notebooks/fibonacci.py#">Move Cell Down</a></li>
                        <li class="divider"></li>
                        <li id="edit_nb_metadata"><a href="http://localhost:8889/notebooks/fibonacci.py#">Edit Notebook Metadata</a></li>
                        <li class="divider"></li>
                        <li id="find_and_replace"><a href="http://localhost:8889/notebooks/fibonacci.py#"> Find and Replace </a></li>
                        <li class="divider"></li>
                        <li id="cut_cell_attachments"><a href="http://localhost:8889/notebooks/fibonacci.py#">Cut Cell Attachments</a></li>
                        <li id="copy_cell_attachments"><a href="http://localhost:8889/notebooks/fibonacci.py#">Copy Cell Attachments</a></li>
                        <li id="paste_cell_attachments" class="disabled"><a href="http://localhost:8889/notebooks/fibonacci.py#">Paste Cell Attachments</a></li>
                        <li class="divider"></li>
                        <li id="insert_image" class="disabled"><a href="http://localhost:8889/notebooks/fibonacci.py#"> Insert Image </a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8889/notebooks/fibonacci.py#" class="dropdown-toggle" data-toggle="dropdown">View</a>
                    <ul id="view_menu" class="dropdown-menu">
                        <li id="toggle_header" title="Show/Hide the logo and notebook title (above menu bar)">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Toggle Header</a>
                        </li>
                        <li id="toggle_toolbar" title="Show/Hide the action icons (below menu bar)">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Toggle Toolbar</a>
                        </li>
                        <li id="toggle_line_numbers" title="Show/Hide line numbers in cells">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Toggle Line Numbers</a>
                        </li>
                        <li id="menu-cell-toolbar" class="dropdown-submenu">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Cell Toolbar</a>
                            <ul class="dropdown-menu" id="menu-cell-toolbar-submenu"><li data-name="None"><a href="http://localhost:8889/notebooks/fibonacci.py#">None</a></li><li data-name="Edit%20Metadata"><a href="http://localhost:8889/notebooks/fibonacci.py#">Edit Metadata</a></li><li data-name="Raw%20Cell%20Format"><a href="http://localhost:8889/notebooks/fibonacci.py#">Raw Cell Format</a></li><li data-name="Slideshow"><a href="http://localhost:8889/notebooks/fibonacci.py#">Slideshow</a></li><li data-name="Attachments"><a href="http://localhost:8889/notebooks/fibonacci.py#">Attachments</a></li><li data-name="Tags"><a href="http://localhost:8889/notebooks/fibonacci.py#">Tags</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8889/notebooks/fibonacci.py#" class="dropdown-toggle" data-toggle="dropdown">Insert</a>
                    <ul id="insert_menu" class="dropdown-menu">
                        <li id="insert_cell_above" title="Insert an empty Code cell above the currently active cell">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Insert Cell Above</a></li>
                        <li id="insert_cell_below" title="Insert an empty Code cell below the currently active cell">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Insert Cell Below</a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8889/notebooks/fibonacci.py#" class="dropdown-toggle" data-toggle="dropdown">Cell</a>
                    <ul id="cell_menu" class="dropdown-menu">
                        <li id="run_cell" title="Run this cell, and move cursor to the next one">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Run Cells</a></li>
                        <li id="run_cell_select_below" title="Run this cell, select below">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Run Cells and Select Below</a></li>
                        <li id="run_cell_insert_below" title="Run this cell, insert below">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Run Cells and Insert Below</a></li>
                        <li id="run_all_cells" title="Run all cells in the notebook">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Run All</a></li>
                        <li id="run_all_cells_above" title="Run all cells above (but not including) this cell">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Run All Above</a></li>
                        <li id="run_all_cells_below" title="Run this cell and all cells below it">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Run All Below</a></li>
                        <li class="divider"></li>
                        <li id="change_cell_type" class="dropdown-submenu" title="All cells in the notebook have a cell type. By default, new cells are created as &#39;Code&#39; cells">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Cell Type</a>
                            <ul class="dropdown-menu">
                              <li id="to_code" title="Contents will be sent to the kernel for execution, and output will display in the footer of cell">
                                  <a href="http://localhost:8889/notebooks/fibonacci.py#">Code</a></li>
                              <li id="to_markdown" title="Contents will be rendered as HTML and serve as explanatory text">
                                  <a href="http://localhost:8889/notebooks/fibonacci.py#">Markdown</a></li>
                              <li id="to_raw" title="Contents will pass through nbconvert unmodified">
                                  <a href="http://localhost:8889/notebooks/fibonacci.py#">Raw NBConvert</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li id="current_outputs" class="dropdown-submenu"><a href="http://localhost:8889/notebooks/fibonacci.py#">Current Outputs</a>
                            <ul class="dropdown-menu">
                                <li id="toggle_current_output" title="Hide/Show the output of the current cell">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">Toggle</a>
                                </li>
                                <li id="toggle_current_output_scroll" title="Scroll the output of the current cell">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_current_output" title="Clear the output of the current cell">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">Clear</a>
                                </li>
                            </ul>
                        </li>
                        <li id="all_outputs" class="dropdown-submenu"><a href="http://localhost:8889/notebooks/fibonacci.py#">All Output</a>
                            <ul class="dropdown-menu">
                                <li id="toggle_all_output" title="Hide/Show the output of all cells">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">Toggle</a>
                                </li>
                                <li id="toggle_all_output_scroll" title="Scroll the output of all cells">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_all_output" title="Clear the output of all cells">
                                    <a href="http://localhost:8889/notebooks/fibonacci.py#">Clear</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8889/notebooks/fibonacci.py#" class="dropdown-toggle" data-toggle="dropdown">Kernel</a>
                    <ul id="kernel_menu" class="dropdown-menu">
                        <li id="int_kernel" title="Send Keyboard Interrupt (CTRL-C) to the Kernel">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Interrupt</a>
                        </li>
                        <li id="restart_kernel" title="Restart the Kernel">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Restart</a>
                        </li>
                        <li id="restart_clear_output" title="Restart the Kernel and clear all output">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Restart &amp; Clear Output</a>
                        </li>
                        <li id="restart_run_all" title="Restart the Kernel and re-run the notebook">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Restart &amp; Run All</a>
                        </li>
                        <li id="reconnect_kernel" title="Reconnect to the Kernel">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Reconnect</a>
                        </li>
                        <li id="shutdown_kernel" title="Shutdown the Kernel">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Shutdown</a>
                        </li>
                        <li class="divider"></li>
                        <li id="menu-change-kernel" class="dropdown-submenu">
                            <a href="http://localhost:8889/notebooks/fibonacci.py#">Change kernel</a>
                            <ul class="dropdown-menu" id="menu-change-kernel-submenu"><li id="kernel-submenu-python3"><a href="http://localhost:8889/notebooks/fibonacci.py#">Python 3</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8889/notebooks/fibonacci.py#" data-toggle="dropdown" class="dropdown-toggle">Widgets</a><ul id="widget-submenu" class="dropdown-menu"><li title="Save the notebook with the widget state information for static rendering"><a href="http://localhost:8889/notebooks/fibonacci.py#">Save Notebook Widget State</a></li><li title="Clear the widget state information from the notebook"><a href="http://localhost:8889/notebooks/fibonacci.py#">Clear Notebook Widget State</a></li><ul class="divider"></ul><li title="Download the widget state as a JSON file"><a href="http://localhost:8889/notebooks/fibonacci.py#">Download Widget State</a></li><li title="Embed interactive widgets"><a href="http://localhost:8889/notebooks/fibonacci.py#">Embed Widgets</a></li></ul></li><li class="dropdown"><a href="http://localhost:8889/notebooks/fibonacci.py#" class="dropdown-toggle" data-toggle="dropdown">Help</a>
                    <ul id="help_menu" class="dropdown-menu">
                        
                        <li id="notebook_tour" title="A quick tour of the notebook user interface"><a href="http://localhost:8889/notebooks/fibonacci.py#">User Interface Tour</a></li>
                        <li id="keyboard_shortcuts" title="Opens a tooltip with all keyboard shortcuts"><a href="http://localhost:8889/notebooks/fibonacci.py#">Keyboard Shortcuts</a></li>
                        <li id="edit_keyboard_shortcuts" title="Opens a dialog allowing you to edit Keyboard shortcuts"><a href="http://localhost:8889/notebooks/fibonacci.py#">Edit Keyboard Shortcuts</a></li>
                        <li class="divider"></li>
                        

						
                        
                            
                                <li><a rel="noreferrer" href="http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Notebook Help
                                </a></li>
                            
                                <li><a rel="noreferrer" href="https://help.github.com/articles/markdown-basics/" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Markdown
                                </a></li>
                            
                            
                        
                        <li id="kernel-help-links" class="divider"></li><li><a target="_blank" title="Opens in a new window" href="https://docs.python.org/3.7?v=20181012152952"><i class="fa fa-external-link menu-icon pull-right"></i><span>Python Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://ipython.org/documentation.html?v=20181012152952"><i class="fa fa-external-link menu-icon pull-right"></i><span>IPython Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/numpy/reference/?v=20181012152952"><i class="fa fa-external-link menu-icon pull-right"></i><span>NumPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://docs.scipy.org/doc/scipy/reference/?v=20181012152952"><i class="fa fa-external-link menu-icon pull-right"></i><span>SciPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://matplotlib.org/contents.html?v=20181012152952"><i class="fa fa-external-link menu-icon pull-right"></i><span>Matplotlib Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="http://docs.sympy.org/latest/index.html?v=20181012152952"><i class="fa fa-external-link menu-icon pull-right"></i><span>SymPy Reference</span></a></li><li><a target="_blank" title="Opens in a new window" href="https://pandas.pydata.org/pandas-docs/stable/?v=20181012152952"><i class="fa fa-external-link menu-icon pull-right"></i><span>pandas Reference</span></a></li><li class="divider"></li>
                        <li title="About Jupyter Notebook"><a id="notebook_about" href="http://localhost:8889/notebooks/fibonacci.py#">About</a></li>
                        
                    </ul>
                </li>
              </ul>
            </div>
        </div>
    </div>
</div>

<div id="maintoolbar" class="navbar">
  <div class="toolbar-inner navbar-inner navbar-nobg">
    <div id="maintoolbar-container" class="container toolbar"><div class="btn-group" id="save-notbook"><button class="btn btn-default" title="Save and Checkpoint" data-jupyter-action="jupyter-notebook:save-notebook"><i class="fa-save fa"></i></button></div><div class="btn-group" id="insert_above_below"><button class="btn btn-default" title="insert cell below" data-jupyter-action="jupyter-notebook:insert-cell-below"><i class="fa-plus fa"></i></button></div><div class="btn-group" id="cut_copy_paste"><button class="btn btn-default" title="cut selected cells" data-jupyter-action="jupyter-notebook:cut-cell"><i class="fa-cut fa"></i></button><button class="btn btn-default" title="copy selected cells" data-jupyter-action="jupyter-notebook:copy-cell"><i class="fa-copy fa"></i></button><button class="btn btn-default" title="paste cells below" data-jupyter-action="jupyter-notebook:paste-cell-below"><i class="fa-paste fa"></i></button></div><div class="btn-group" id="move_up_down"><button class="btn btn-default" title="move selected cells up" data-jupyter-action="jupyter-notebook:move-cell-up"><i class="fa-arrow-up fa"></i></button><button class="btn btn-default" title="move selected cells down" data-jupyter-action="jupyter-notebook:move-cell-down"><i class="fa-arrow-down fa"></i></button></div><div class="btn-group" id="run_int"><button class="btn btn-default" title="Run" data-jupyter-action="jupyter-notebook:run-cell-and-select-next"><i class="fa-step-forward fa"></i><span class="toolbar-btn-label">Run</span></button><button class="btn btn-default" title="interrupt the kernel" data-jupyter-action="jupyter-notebook:interrupt-kernel"><i class="fa-stop fa"></i></button><button class="btn btn-default" title="restart the kernel (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel"><i class="fa-repeat fa"></i></button><button class="btn btn-default" title="restart the kernel, then re-run the whole notebook (with dialog)" data-jupyter-action="jupyter-notebook:confirm-restart-kernel-and-run-all-cells"><i class="fa-forward fa"></i></button></div><select id="cell_type" class="form-control select-xs"><option value="code">Code</option><option value="markdown">Markdown</option><option value="raw">Raw NBConvert</option><option value="heading">Heading</option><option value="multiselect" disabled="disabled" style="display: none;">-</option></select><div class="btn-group"><button class="btn btn-default" title="open the command palette" data-jupyter-action="jupyter-notebook:show-command-palette"><i class="fa-keyboard-o fa"></i></button></div></div>
  </div>
</div>
</div>

<div class="lower-header-bar"></div>

</div>

<div id="site" style="display: block; height: 591.427px;">


<div id="ipython-main-app">
    <div id="notebook_panel">
        <div id="notebook" tabindex="-1"><div class="container" id="notebook-container"><div class="cell code_cell rendered selected" tabindex="2"><div class="input"><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[36]:</div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython CodeMirror-focused"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 238.932px; left: 5.59894px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="false"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 246.333px; margin-bottom: -21px; border-right-width: 9px; min-height: 344px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre>x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 5.83331px; top: 0px; width: 1002.17px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 5px; top: 233px; width: 0.598938px; height: 17px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 5px; top: 17px; width: 1003px; height: 216px;"></div></div><div class="CodeMirror-cursors" style="visibility: hidden;"></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">fib</span>(<span class="cm-variable">k</span>):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">a</span>,<span class="cm-variable">b</span><span class="cm-operator">=</span><span class="cm-number">0</span>,<span class="cm-number">1</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">for</span> <span class="cm-variable">n</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">k</span>):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">a</span>,<span class="cm-variable">b</span><span class="cm-operator">=</span><span class="cm-variable">b</span>,<span class="cm-variable">a</span><span class="cm-operator">+</span><span class="cm-variable">b</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">return</span> <span class="cm-variable">b</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">i</span><span class="cm-operator">=</span><span class="cm-builtin">int</span>(<span class="cm-builtin">input</span>())</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment">#print([fib(n) for n in range(i)])</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-string">"n="</span><span class="cm-operator">+</span><span class="cm-builtin">str</span>(<span class="cm-variable">i</span>)<span class="cm-operator">+</span><span class="cm-string">"の時,"</span>,<span class="cm-variable">end</span><span class="cm-operator">=</span><span class="cm-string">""</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-string">"F(n)="</span><span class="cm-operator">+</span> <span class="cm-builtin">str</span>(<span class="cm-variable">fib</span>(<span class="cm-variable">i</span>)))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        </span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    </span></pre></div></div></div></div></div><div style="position: absolute; height: 9px; width: 1px; border-bottom: 0px solid transparent; top: 344px;"></div><div class="CodeMirror-gutters" style="display: none; height: 353px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout"><pre>2018
n=2018の時,F(n)=39496686472772163397874981928532586937785000709985018165227544505583956123892491583992043369010510473852474871823919949628656144692626488180105707977212947225784927555125847822065435826037363716924714565553298478909956798245598759168652339244838488670328632476925440191393691741920312935346241800034867950746972804090992175422630866247531341721589487617557085576900215798341862472548933587106152708259589526498478046850306
</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell rendered unselected" tabindex="2"><div class="input"><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[37]:</div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 155.599px; left: 62.1406px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 485.656px; margin-bottom: -21px; border-right-width: 9px; min-height: 194px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 62.1406px; top: 150px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">fib</span>(<span class="cm-variable">k</span>):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">a</span>,<span class="cm-variable">b</span><span class="cm-operator">=</span><span class="cm-number">0</span>,<span class="cm-number">1</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">for</span> <span class="cm-variable">n</span>  <span class="cm-keyword">in</span> <span class="cm-builtin">range</span> (<span class="cm-variable">k</span>):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">a</span>,<span class="cm-variable">b</span><span class="cm-operator">=</span><span class="cm-variable">b</span>,<span class="cm-variable">a</span><span class="cm-operator">+</span><span class="cm-variable">b</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">return</span> <span class="cm-variable">b</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">m</span><span class="cm-operator">=</span><span class="cm-builtin">int</span>(<span class="cm-builtin">input</span>())</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">l</span><span class="cm-operator">=</span><span class="cm-number">0</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">while</span> <span class="cm-variable">fib</span> (<span class="cm-variable">l</span>)<span class="cm-operator">&lt;=</span><span class="cm-variable">m</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">l</span><span class="cm-operator">+=</span><span class="cm-number">1</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-builtin">str</span>(<span class="cm-variable">m</span>)<span class="cm-operator">+</span><span class="cm-string">"以下で最大のフィボナッチ数は,"</span><span class="cm-operator">+</span><span class="cm-builtin">str</span>(<span class="cm-variable">fib</span>(<span class="cm-variable">l</span><span class="cm-operator">-</span><span class="cm-number">1</span>))<span class="cm-operator">+</span><span class="cm-string">"です。"</span>)</span></pre></div></div></div></div></div><div style="position: absolute; height: 9px; width: 1px; border-bottom: 0px solid transparent; top: 194px;"></div><div class="CodeMirror-gutters" style="display: none; height: 203px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to scroll output; double click to hide"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_text output_stream output_stdout"><pre>2018
2018以下で最大のフィボナッチ数は,1597です。
</pre></div></div></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div><div class="cell code_cell unrendered unselected" tabindex="2"><div class="input"><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[&nbsp;]:</div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59894px; left: 5.59375px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 8.59375px; margin-bottom: -21px; border-right-width: 9px; min-height: 27px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 5.59375px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 9px; width: 1px; border-bottom: 0px solid transparent; top: 27px;"></div><div class="CodeMirror-gutters" style="display: none; height: 36px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="click to expand output; double click to hide output"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="click to expand output" style="display: none;">. . .</div></div></div></div><div class="end_space"></div></div>
        <div id="tooltip" class="ipython_tooltip" style="display:none"><div class="tooltipbuttons"><a href="http://localhost:8889/notebooks/fibonacci.py#" role="button" class="ui-button"><span class="ui-icon ui-icon-close">Close</span></a><a href="http://localhost:8889/notebooks/fibonacci.py#" class="ui-corner-all" role="button" id="expanbutton" title="Grow the tooltip vertically (press shift-tab twice)"><span class="ui-icon ui-icon-plus">Expand</span></a><a href="http://localhost:8889/notebooks/fibonacci.py#" role="button" class="ui-button" title="show the current docstring in pager (press shift-tab 4 times)"><span class="ui-icon ui-icon-arrowstop-l-n">Open in Pager</span></a><a href="http://localhost:8889/notebooks/fibonacci.py#" role="button" class="ui-button" title="Tooltip will linger for 10 seconds while you type" style="display: none;"><span class="ui-icon ui-icon-clock">Close</span></a></div><div class="pretooltiparrow"></div><div class="tooltiptext smalltooltip"></div></div>
    </div>
</div>



</div>



<div id="pager" class="ui-resizable">
    <div id="pager-contents">
        <div id="pager-container" class="container"></div>
    </div>
    <div id="pager-button-area"><a role="button" title="Open the pager in an external window" class="ui-button"><span class="ui-icon ui-icon-extlink"></span></a><a role="button" title="Close the pager" class="ui-button"><span class="ui-icon ui-icon-close"></span></a></div>
<div class="ui-resizable-handle ui-resizable-n" style="z-index: 90;"></div></div>






<script type="text/javascript">
    sys_info = {"notebook_version": "5.6.0", "notebook_path": "C:\\Users\\ryoic\\Anaconda3\\lib\\site-packages\\notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)]", "sys_executable": "C:\\Users\\ryoic\\Anaconda3\\python.exe", "sys_platform": "win32", "platform": "Windows-10-10.0.17134-SP0", "os_name": "nt", "default_encoding": "utf-8"};
</script>

<script src="./fibonacci_files/encoding.js.ダウンロード" charset="utf-8"></script>

<script src="./fibonacci_files/main.min.js.ダウンロード" type="text/javascript" charset="utf-8"></script>



<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


<div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal;"></div></div><div class="modal fade" role="dialog" style="display: none;"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button><h4 class="modal-title">Notebook changed</h4></div><div class="modal-body"><p>The notebook file has changed on disk since the last time we opened or saved it. Do you want to overwrite the file on disk with the version open here, or load the version on disk (reload the page)?</p></div><div class="modal-footer"><button class="btn btn-default btn-sm btn-warning" data-dismiss="modal">Reload</button><button class="btn btn-default btn-sm" data-dismiss="modal">Cancel</button><button class="btn btn-default btn-sm btn-danger save-confirm-btn" data-dismiss="modal">Overwrite</button></div></div></div></div></body></html>