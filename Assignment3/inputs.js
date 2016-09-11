var inputContainers = [];
var removed = [];

function add() {
  if (removed.length > 0) {
    console.log(';test');
    var newDiv = removed.pop();
  }
  else {
    var newDiv = generateDiv();
  }
  inputContainers.push(newDiv);
  document.getElementById('container').appendChild(newDiv);
}

function subtract(element) {
  var index = inputContainers.indexOf(element);
  console.log(index);
  removed.push(element);
  inputContainers.splice(index, 1);
  console.log(inputContainers);
  element.remove();
}

function setNumber(element) {
  var len = element.childNodes[0].value.length;
  element.childNodes[2].innerHTML = len;
}

function sort() {
  // insertion sort
  for (var i = 1; i < inputContainers.length; i++) {
    var j = i;
    while (j > 0 && parseInt(inputContainers[j-1].childNodes[2].innerHTML) > parseInt(inputContainers[j].childNodes[2].innerHTML)) {
      var temp = inputContainers[j-1];
      inputContainers[j-1] = inputContainers[j];
      inputContainers[j] = temp;
      j--;
    }
  }
  // now remove elements from the container div and readd them
  var div = document.getElementById('container');
  while (div.firstChild) {
    div.removeChild(div.firstChild);
  }
  for (var i = 0; i < inputContainers.length; i++) {
    div.appendChild(inputContainers[i]);
  }
}

function generateInput() {
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
  div.appendChild(generateInput());
  div.appendChild(generateButton());
  div.appendChild(generateLabel());
  return div;
}
