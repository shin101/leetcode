/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
  for(let i=0; i<this.length; i++){
      if(i===this.length-1){
          return this[i]
      }
  }
  return -1
};

/**
* const arr = [1, 2, 3];
* arr.last(); // 3
*/