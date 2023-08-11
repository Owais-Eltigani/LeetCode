class MinStack {
  constructor(stack = [], min = Number.MAX_SAFE_INTEGER) {
    this.stack = stack;
    this.min = min;
  }

  push(num) {
    this.min = num < this.min ? num : this.min;

    this.stack.push(num);
  }

  pop() {
    let popped = -1;

    if (this.stack.length > 0) {
      popped = this.stack.pop();

      if (popped === this.min) {
        this.min = Math.min(...this.stack);
      }
    }
    return popped;
  }

  top() {
    const top = this.stack.pop();

    this.stack.push(top);

    return top;
  }

  getMin() {
    return this.min;
  }
}

// ------------ *** ------------

const stack = new MinStack();

stack.push(-2);
stack.push(0);
stack.push(-3);
console.log(stack.getMin());
console.log(stack.pop());
console.log(stack.top());
console.log(stack.getMin());
