// create the first element and initialize the arrays
var inputs = [generateDiv()]; 
var removed = []; // Acts as first in last out stack
document.getElementById('container').appendChild(inputs[0]);

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

function subtract(element) {
  if (inputs.length > 1) {
    var index = inputs.indexOf(element);
    removed.push(element);
    inputs.splice(index, 1);
    element.remove();
  }
}

function setNumber(element) {
  var len = element.childNodes[0].value.length;
  element.childNodes[2].innerHTML = len;
}

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
  button.setAttribute('onClick', 'subtract(this.parentElement)');
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
