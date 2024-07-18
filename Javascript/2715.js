/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */


// Motive : Return a function after a specifc time only if you didn't call other function , if we called the other function then the first function shouldn't be called at all !!


var cancellable = function(fn, args, t) {

    const timer = setTimeout((cancelFn, cancelTimeMs) => {
        return (fn(...args))
    }, t)
    return (cancelTimeMs) => {
        clearTimeout(timer, cancelTimeMs)
    }
};



/**
 *  const result = [];
 *
 *  const fn = (x) => x * 5;
 *  const args = [2], t = 20, cancelTimeMs = 50;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *       
 *  const cancel = cancellable(log, args, t);
 *
 *  const maxT = Math.max(t, cancelTimeMs);
 *           
 *  setTimeout(cancel, cancelTimeMs);
 *
 *  setTimeout(() => {
 *      console.log(result); // [{"time":20,"returned":10}]
 *  }, maxT + 15)
 */