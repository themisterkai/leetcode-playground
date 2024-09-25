const prices = [7, 1, 5, 3, 6, 4];

const maxProfit = prices => {
  // const findMinimum = priceArray => {
  //   let min = Number.MAX_VALUE;
  //   for (let i = 0; i < priceArray.length; i++) {
  //     if (priceArray[i] < min) {
  //       min = priceArray[i];
  //     }
  //   }
  //   return min;
  // };

  // let maxProfit = 0;
  // for (let i = 0; i < prices.length; i++) {
  //   const min = findMinimum(prices.slice(0, i));
  //   if (prices[i] - min > maxProfit) {
  //     maxProfit = prices[i] - min;
  //   }
  // }

  let min = Number.MAX_VALUE;
  let maxProfit = 0;

  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < min) {
      min = prices[i];
    }
    if (prices[i] - min > maxProfit) {
      maxProfit = prices[i] - min;
    }
  }
  return maxProfit;
};

console.log(maxProfit(prices));
