#!/usr/bin/node
const callMeMoby = function (x, theFunction) {
  do {
    theFunction();
  } while (x-- > 0);
};
module.exports.callMeMoby = callMeMoby;
