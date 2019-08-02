var request = new XMLHttpRequest();

request.open('GET', 'https://api.exchangeratesapi.io/latest HTTP/1.1');

request.onreadystatechange = function () {
  if (this.readyState === 4) {
    console.log('Status:', this.status);
    console.log('Headers:', this.getAllResponseHeaders());
    console.log('Body:', this.responseText);
  }
};
