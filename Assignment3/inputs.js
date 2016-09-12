// create the first element and initialize the arrays
var inputs = [generateDiv()]; 
var removed = []; // Acts as first in last out stack
document.getElementById('container').appendChild(inputs[0]);

// Appends a generated div to both the container div
// and to the inputs array unless there is at least one
// div in the removed array. If there is at least one 
// in the remvoed array then the top element of the
// removed array is appended to the div and to the
// inputs array.
function addInput() {
  if (removed.length > 0) {
    var newDiv = removed.pop();
  }
  else {
    var newDiv = generateDiv();
  }
  inputs.push(newDiv);
  document.getElementById('container').appendChild(newDiv);
}

// Removes the given div from the parent div and 
// adds it to the removed array
function subtractInput(element) {
  if (inputs.length > 1) {
    var index = inputs.indexOf(element);
    removed.push(element);
    inputs.splice(index, 1);
    element.remove();
  }
}

// Sets the label to the number of characters in the
// text field.
function setNumber(element) {
  var len = element.childNodes[0].value.length;
  element.childNodes[2].innerHTML = len;
}

// Sorts the inputs array and then removes each input from the div
// followed by adding each element of the sorted array back to the
// div in order.
function sort() {
  // insertion sort
  for (var i = 1; i < inputs.length; i++) {
    var j = i;
    while (j > 0 && parseInt(inputs[j-1].childNodes[2].innerHTML) > parseInt(inputs[j].childNodes[2].innerHTML)) {
      var temp = inputs[j-1];
      inputs[j-1] = inputs[j];
      inputs[j] = temp;
      j--;
    }
  }
  // now remove elements from the container div and read them
  var div = document.getElementById('container');
  while (div.firstChild) {
    div.removeChild(div.firstChild);
  }
  for (var i = 0; i < inputs.length; i++) {
    div.appendChild(inputs[i]);
  }
}

function generateTF() {
  var input = document.createElement('input');
  input.setAttribute('type', 'text');
  input.setAttribute('onkeyup', 'setNumber(this.parentElement)');
  return input;
}

function generateButton() {
  var button = document.createElement('button');
  button.appendChild(document.createTextNode('-'));
  button.setAttribute('onClick', 'subtractInput(this.parentElement)');
  return button;
}

function generateLabel() {
  var label = document.createElement('label');
  label.innerHTML = '0';
  return label;
}

function generateDiv() {
  var div = document.createElement('div');
  div.appendChild(generateTF());
  div.appendChild(generateButton());
  div.appendChild(generateLabel());
  return div;
}
