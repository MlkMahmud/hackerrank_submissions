function processData(input) {
  //Enter your code here
  const data = input.replace(/\s/g, '\n').split('\n'), queue = [];
  data.shift();
  for (let i = 0, len = data.length; i < len; i++) {
    if (data[i] === '1') {
      queue.push(data[i + 1]);
      i++;
    }
    else if (data[i] === '2') {
      queue.shift();
    }
    else {
      console.log(queue[0]);
    }
  }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});

