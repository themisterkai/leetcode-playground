// const bills = [5, 5, 5, 10, 20];
// const bills = [5, 5, 10, 10, 20];
// const bills = [5, 5, 5, 5, 20, 20, 5, 5, 20, 5];
const bills = [5, 5, 20, 5, 5, 10, 5, 10, 5, 20];

/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function (bills) {
  const total = {
    5: 0,
    10: 0,
    20: 0,
  };
  for (let i = 0; i < bills.length; i++) {
    total[bills[i]] += 1;
    if (bills[i] === 10) {
      if (total[5] > 0) {
        total[5] = total[5] - 1;
      } else {
        return false;
      }
    } else if (bills[i] === 20) {
      if (total[10] > 0 && total[5] > 0) {
        total[10] = total[10] - 1;
        total[5] = total[5] - 1;
      } else if (total[5] > 2) {
        total[5] = total[5] - 3;
      } else {
        return false;
      }
    }
  }
  return true;
};

console.log(lemonadeChange(bills));
