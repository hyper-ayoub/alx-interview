#!/usr/bin/node

const request = require('request');

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) {
  console.error('Please provide a Movie ID as the first positional argument');
  process.exit(1);
}

// Construct the API URL for the specified movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the response status code is 200 (OK)
  if (response.statusCode !== 200) {
    console.error('Failed to retrieve the movie:', response.statusCode);
    return;
  }

  // Parse the JSON response body
  const filmData = JSON.parse(body);

  // Get the list of character URLs
  const characters = filmData.characters;

  // Fetch and print each character's name
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Check if the response status code is 200 (OK)
      if (response.statusCode !== 200) {
        console.error('Failed to retrieve the character:', response.statusCode);
        return;
      }

      // Parse the JSON response body
      const characterData = JSON.parse(body);

      // Print the character's name
      console.log(characterData.name);
    });
  });
});

