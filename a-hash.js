'use strict';

const phonebook = {
  'Marcus Aurelius': '+380445554433',
  'Іван Петренко': '+380501234567',
  'Марія Іваненко': '+380679876543'
};

const findPhoneByName = (name) => {
  return phonebook[name];
};

module.exports = { phonebook, findPhoneByName };
