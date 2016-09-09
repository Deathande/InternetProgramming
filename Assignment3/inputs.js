function add() {
  document.getElementById('container').appendChild(generateDiv());
}

function subtract(element) {
  element.remove();
}

function generateInput() {
  var input = document.createElement('input');
  //var att = document.createAttribute('type');
  //att.type = 'text';
  input.setAttribute('type', 'text');
  //input.setAttributeNode(att);
  return input;
}

function generateButton() {
  var button = document.createElement('button');
  //var att = document.createAttribute('onClick');
  button.appendChild(document.createTextNode('-'));
  button.setAttribute('onClick', 'subtract(this.parentElement)');
  //att.onClick = 'subtract()';
  //button.setAttributeNode(att);
  return button;
}

function generateDiv() {
  var div = document.createElement('div');
  div.appendChild(generateInput());
  div.appendChild(generateButton());
  return div;
}
