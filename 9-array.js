'use strict';

const phonebook = [
  { name: 'Marcus Aurelius', phone: '+380445554433' },
  { name: 'Іван Петренко', phone: '+380501234567' },
  { name: 'Марія Іваненко', phone: '+380679876543' }
];

const findPhoneByName = (name) => {
  for (let i = 0; i < phonebook.length; i++) {
    if (phonebook[i].name === name) {
      return phonebook[i].phone;
    }
  }
  return undefined;
};

module.exports = { phonebook, findPhoneByName };
