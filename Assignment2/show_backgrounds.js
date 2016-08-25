function change(tag) {
  // The class that determines the background or foreground color
  // must be first in the list of classes.
  var tag_class = tag.classList.item(0);
  if(tag_class.includes("color")) {
    document.getElementById("foreground").className = tag_class;
  }
  else {
    document.getElementById("background").className = tag_class;
  }
}
