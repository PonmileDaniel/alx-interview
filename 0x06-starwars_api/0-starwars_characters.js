#!/usr/bin/node

const request = require('request');

// Retrieve the movie ID from command line argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Construct the API URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a Get request to fetch the film details
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body
  const film = JSON.parse(body);
  if (!film.characters) {
    console.error('No characters found');
    return;
  }

  const characters = film.characters;
  const fetchCharName = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (charErr, charRes, charBody) => {
      if (charErr) {
        console.error(charErr);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
      fetchCharName(index + 1);
    });
  };

  fetchCharName(0);
});
