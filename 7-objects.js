'use strict';

const fn = () => {
  const obj1 = { name: 'Іван' };
  let obj2 = { name: 'Петро' };
  
  obj1.name = 'Микола';
  obj2.name = 'Сергій';
  
  obj2 = { name: 'Андрій' };
  
  return { obj1, obj2 };
};

module.exports = { fn };
