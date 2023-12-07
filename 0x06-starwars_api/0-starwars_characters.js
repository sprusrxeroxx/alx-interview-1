#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printOrderly(characters, 0);
  }
});

const printOrderly = (characters, index) => {
  request(characters[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printOrderly(characters, index + 1);
      }
    }
  });
};


// const { argv } = require('process');
// const request = require('axios');
// const num = argv[2]
// const baseUrl = `https://swapi-api.alx-tools.com/api/films/${num}`

// const fetchFilmCharacters = (url, attributes) => {
//   return new Promise((resolve, reject) => {
//     request(url, (error, response, body) => {
//       if (!error && response.statusCode == 200) {
//         let charactersArr = JSON.parse(body);
//         resolve(`${charactersArr}.${attributes}`);
//       } else {
//         reject(error);
//       }
//     })
//   })
// }

// const printCharacters = async () => {
//   try {
//     const characters = await fetchFilmCharacters(baseUrl, 'characters');
//     characters.forEach(async url => {
//       const characterName = await fetchFilmCharacters(url, 'name');
//       console.log(characterName);
//     });
//   } catch (error) {
//     console.log(error);
//   }
  
// }
// printCharacters();
