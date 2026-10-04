// file saving ---------------------------------------- -->

// hand-code to avoid scalajs binding
function my_save(s) {
  var blob = new Blob([s], {type: "text/plain;charset=utf-8"});
  saveAs(blob,"index.html");
}


// get parameters ---------------------------------------- -->
// hand-code to use URI lib without scalajs binding
var my_params = URI.parseQuery(new URI().query());
// var my_fragment = new URI().fragment()
console.log(my_params);


// key shortcut ---------------------------------------- -->

Mousetrap.bind(['command+e', 'ctrl+e'], function(e) {
  console.log("C-e");
  twiki.Ip().toggle_edit();
  return false;
});

Mousetrap.bind(['n'], function(e) {
  console.log("n");
  twiki.Ip().next_slide(1);
  return false;
});

Mousetrap.bind(['p'], function(e) {
  console.log("p");
  twiki.Ip().next_slide(-1);
  return false;
});

Mousetrap.bind(['1'], function(e) {
  console.log("1");
  twiki.Ip().first_slide();
  return false;
});


// reordering ---------------------------------------- -->

function new_sortable(elt) {
  console.log("new_sortable:");
  console.log(elt);
  Sortable.create(elt);
}


// after doc load ----------------------------------------


// chrome extension
// get_user_html().document.addEventListener('DOMContentLoaded', function() {
//   twiki.Ip().main(); // FIXME what if already called by extension?
// });
